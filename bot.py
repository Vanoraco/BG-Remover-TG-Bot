"""
Telegram Bot for Background Removal using InSPyReNet
"""
import asyncio
import logging
import io
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Dict, List

from telegram import Update
from telegram.ext import (
    Application, 
    CommandHandler, 
    MessageHandler, 
    filters, 
    ContextTypes
)

from config import Config, validate_config
from image_processor import background_remover

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Rate limiting storage
user_requests: Dict[int, List[datetime]] = defaultdict(list)

# User settings storage
user_settings: Dict[int, Dict] = defaultdict(lambda: {'mode': 'full', 'opacity': 100})

class BackgroundRemovalBot:
    """Main bot class for handling Telegram interactions"""
    
    def __init__(self):
        """Initialize the bot"""
        validate_config()
        self.application = Application.builder().token(Config.BOT_TOKEN).build()
        self._setup_handlers()
    
    def _setup_handlers(self):
        """Set up command and message handlers"""
        # Command handlers
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("modes", self.modes_command))
        self.application.add_handler(CommandHandler("settings", self.settings_command))
        
        # Message handlers
        self.application.add_handler(
            MessageHandler(filters.PHOTO, self.handle_photo)
        )
        self.application.add_handler(
            MessageHandler(filters.Document.IMAGE, self.handle_document)
        )
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text)
        )
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        await update.message.reply_text(
            Config.WELCOME_MESSAGE,
            parse_mode='Markdown'
        )
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        await update.message.reply_text(
            Config.HELP_MESSAGE,
            parse_mode='Markdown'
        )

    async def modes_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /modes command"""
        await update.message.reply_text(
            Config.MODES_MESSAGE,
            parse_mode='Markdown'
        )

    async def settings_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /settings command"""
        user_id = update.effective_user.id
        current_mode = user_settings[user_id]['mode']
        current_opacity = user_settings[user_id]['opacity']

        settings_text = f"""
⚙️ **Your Current Settings:**

🎨 **Mode:** {current_mode}
🔍 **Opacity:** {current_opacity}%

**To change settings:**
• Send "mode:semi" to change mode
• Send "opacity:75" to set opacity
• Send "reset" to restore defaults

**Available modes:** full, semi, soft, subject, custom
        """

        await update.message.reply_text(settings_text, parse_mode='Markdown')
    
    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle text messages and mode commands"""
        user_id = update.effective_user.id
        text = update.message.text.lower().strip()

        # Handle mode commands
        if text.startswith('mode:'):
            mode = text.split(':', 1)[1].strip()
            if mode in Config.TRANSPARENCY_MODES:
                user_settings[user_id]['mode'] = mode
                mode_desc = Config.TRANSPARENCY_MODES[mode]
                await update.message.reply_text(
                    f"✅ Mode set to **{mode}**\n{mode_desc}\n\nNow send me an image!",
                    parse_mode='Markdown'
                )
            else:
                await update.message.reply_text(
                    f"❌ Unknown mode '{mode}'. Use /modes to see available options."
                )
            return

        # Handle opacity commands
        elif text.startswith('opacity:'):
            try:
                opacity = int(text.split(':', 1)[1].strip())
                if 1 <= opacity <= 99:
                    user_settings[user_id]['opacity'] = opacity
                    user_settings[user_id]['mode'] = 'custom'
                    await update.message.reply_text(
                        f"✅ Opacity set to **{opacity}%**\n\nNow send me an image!",
                        parse_mode='Markdown'
                    )
                else:
                    await update.message.reply_text("❌ Opacity must be between 1-99%")
            except ValueError:
                await update.message.reply_text("❌ Invalid opacity value. Use: opacity:50")
            return

        # Handle reset command
        elif text == 'reset':
            user_settings[user_id] = {'mode': 'full', 'opacity': 100}
            await update.message.reply_text("✅ Settings reset to default (full transparency)")
            return

        # Default response
        current_mode = user_settings[user_id]['mode']
        await update.message.reply_text(
            f"Please send me an image! 📸\n\n"
            f"Current mode: **{current_mode}**\n"
            f"Supported formats: JPG, PNG, WebP\n\n"
            f"💡 Try: mode:semi, opacity:75, or /modes for options",
            parse_mode='Markdown'
        )
    
    async def handle_photo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle photo messages (compressed images)"""
        user_id = update.effective_user.id
        
        # Check rate limiting
        if not self._check_rate_limit(user_id):
            await update.message.reply_text(Config.ERROR_MESSAGES['rate_limit'])
            return
        
        try:
            # Get the largest photo size
            photo = update.message.photo[-1]
            
            # Download photo
            file = await context.bot.get_file(photo.file_id)
            image_bytes = await file.download_as_bytearray()
            
            await self._process_and_send_image(update, bytes(image_bytes))
            
        except Exception as e:
            logger.error(f"Error handling photo: {e}")
            await update.message.reply_text(Config.ERROR_MESSAGES['download_error'])
    
    async def handle_document(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle document messages (uncompressed images)"""
        user_id = update.effective_user.id
        
        # Check rate limiting
        if not self._check_rate_limit(user_id):
            await update.message.reply_text(Config.ERROR_MESSAGES['rate_limit'])
            return
        
        try:
            document = update.message.document
            
            # Check file size
            if document.file_size > Config.MAX_FILE_SIZE_BYTES:
                await update.message.reply_text(Config.ERROR_MESSAGES['file_too_large'])
                return
            
            # Download document
            file = await context.bot.get_file(document.file_id)
            image_bytes = await file.download_as_bytearray()
            
            await self._process_and_send_image(update, bytes(image_bytes))
            
        except Exception as e:
            logger.error(f"Error handling document: {e}")
            await update.message.reply_text(Config.ERROR_MESSAGES['download_error'])
    
    async def _process_and_send_image(self, update: Update, image_bytes: bytes):
        """Process image and send result back to user"""
        try:
            user_id = update.effective_user.id

            # Validate image
            is_valid, error_message = background_remover.validate_image(image_bytes)
            if not is_valid:
                await update.message.reply_text(error_message)
                return

            # Get user settings
            mode = user_settings[user_id]['mode']
            opacity = user_settings[user_id]['opacity']

            # Send processing message with mode info
            processing_text = f"🔄 Processing with **{mode}** mode...\n{Config.PROCESSING_MESSAGE}"
            processing_msg = await update.message.reply_text(processing_text, parse_mode='Markdown')

            # Process image with timeout and user settings
            try:
                processed_bytes = await asyncio.wait_for(
                    background_remover.process_image(image_bytes, mode=mode, opacity=opacity),
                    timeout=Config.PROCESSING_TIMEOUT_SECONDS
                )
            except asyncio.TimeoutError:
                await processing_msg.edit_text(Config.ERROR_MESSAGES['timeout'])
                return

            if processed_bytes is None:
                await processing_msg.edit_text(Config.ERROR_MESSAGES['processing_error'])
                return

            # Create caption with mode info
            caption = f"✅ Transparency applied with **{mode}** mode! 🎨"
            if mode == 'custom':
                caption += f"\nOpacity: {opacity}%"

            # Send processed image
            await update.message.reply_document(
                document=io.BytesIO(processed_bytes),
                filename=f"transparent_{mode}.png",
                caption=caption,
                parse_mode='Markdown'
            )

            # Delete processing message
            await processing_msg.delete()

        except Exception as e:
            logger.error(f"Error processing image: {e}")
            await update.message.reply_text(Config.ERROR_MESSAGES['general_error'])
    
    def _check_rate_limit(self, user_id: int) -> bool:
        """Check if user is within rate limits"""
        now = datetime.now()
        minute_ago = now - timedelta(minutes=1)
        
        # Clean old requests
        user_requests[user_id] = [
            req_time for req_time in user_requests[user_id] 
            if req_time > minute_ago
        ]
        
        # Check if under limit
        if len(user_requests[user_id]) >= Config.MAX_REQUESTS_PER_USER_PER_MINUTE:
            return False
        
        # Add current request
        user_requests[user_id].append(now)
        return True
    
    async def run(self):
        """Start the bot"""
        logger.info("Starting Background Removal Bot...")
        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()
        
        logger.info("Bot is running! Press Ctrl+C to stop.")
        
        # Keep running until interrupted
        try:
            await asyncio.Event().wait()
        except KeyboardInterrupt:
            logger.info("Stopping bot...")
        finally:
            await self.application.updater.stop()
            await self.application.stop()
            await self.application.shutdown()

async def main():
    """Main function to run the bot"""
    bot = BackgroundRemovalBot()
    await bot.run()

if __name__ == '__main__':
    asyncio.run(main())
