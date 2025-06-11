"""
Configuration settings for the Telegram Background Removal Bot
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for bot settings"""
    
    # Bot Configuration
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    
    # File Processing Settings
    MAX_FILE_SIZE_MB = 20  # Maximum file size in MB
    MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
    
    # Supported image formats
    SUPPORTED_FORMATS = ['.jpg', '.jpeg', '.png', '.webp']
    
    # InSPyReNet Model Settings
    MODEL_MODE = 'base'  # Options: 'base', 'fast', 'base-nightly'
    USE_JIT = True  # Enable TorchScript for better performance
    RESIZE_MODE = 'static'  # Options: 'static', 'dynamic'

    # Transparency Options
    TRANSPARENCY_MODES = {
        'full': 'Complete background removal (transparent)',
        'semi': 'Semi-transparent background (50% opacity)',
        'soft': 'Soft edge transparency (feathered)',
        'subject': 'Make subject semi-transparent',
        'custom': 'Custom opacity level'
    }
    
    # Rate Limiting Settings
    MAX_REQUESTS_PER_USER_PER_MINUTE = 5
    
    # Processing Settings
    PROCESSING_TIMEOUT_SECONDS = 60
    
    # Messages
    WELCOME_MESSAGE = """
🎨 **Welcome to Transparency Master Bot!**

I can create amazing transparency effects with your images using advanced AI technology.

**✨ Transparency Options:**
• **Full** - Complete background removal (default)
• **Semi** - Semi-transparent background
• **Soft** - Soft edge transparency
• **Subject** - Make subject translucent
• **Custom** - Choose opacity level

**How to use:**
1. Send me an image (JPEG, PNG, or WebP)
2. Choose transparency mode (or use default)
3. Get your transparent masterpiece!

**Supported formats:** JPG, JPEG, PNG, WebP
**Maximum file size:** {max_size}MB

Type /help for more options and /modes to see all transparency effects.
    """.format(max_size=MAX_FILE_SIZE_MB)
    
    HELP_MESSAGE = """
🔧 **Help & Instructions**

**Commands:**
• /start - Start the bot and see welcome message
• /help - Show this help message
• /modes - See all transparency modes
• /settings - Adjust your preferences

**🎨 Transparency Modes:**
• **Default:** Send image → get transparent background
• **Mode Selection:** Send "mode:semi" before image for semi-transparent
• **Custom Opacity:** Send "opacity:75" for 75% transparency
• **Soft Edges:** Send "mode:soft" for feathered edges

**📱 How to use:**
1. Send image directly (uses full transparency)
2. OR send "mode:semi" then your image
3. OR send "opacity:50" then your image
4. Get your transparent result!

**Supported formats:**
• JPEG (.jpg, .jpeg) • PNG (.png) • WebP (.webp)

**Limitations:**
• Maximum file size: {max_size}MB
• Processing time: 10-60 seconds
• Rate limit: {rate_limit} images per minute

**✨ Pro Tips:**
• High-quality images = better results
• Good subject/background contrast helps
• Try different modes for creative effects

**Powered by InSPyReNet AI Model**
    """.format(max_size=MAX_FILE_SIZE_MB, rate_limit=MAX_REQUESTS_PER_USER_PER_MINUTE)
    
    MODES_MESSAGE = """
🎨 **Transparency Modes Available:**

🔹 **Full** (default)
   Complete background removal - fully transparent
   Usage: Just send your image

🔹 **Semi**
   Semi-transparent background (50% opacity)
   Usage: Send "mode:semi" then your image

🔹 **Soft**
   Soft edge transparency with feathered borders
   Usage: Send "mode:soft" then your image

🔹 **Subject**
   Make the main subject semi-transparent
   Usage: Send "mode:subject" then your image

🔹 **Custom Opacity**
   Choose your own transparency level (1-99%)
   Usage: Send "opacity:75" then your image

**Examples:**
• "mode:semi" → semi-transparent background
• "opacity:30" → 30% opacity background
• "mode:soft" → feathered edge effect

**Tips:**
• Send mode command first, then your image
• Default mode is full transparency
• Try different modes for creative effects!
    """

    PROCESSING_MESSAGE = "🔄 Processing your image... This may take 10-60 seconds depending on image size."
    
    ERROR_MESSAGES = {
        'no_token': '❌ Bot token not found. Please set BOT_TOKEN environment variable.',
        'file_too_large': f'❌ File too large! Maximum size is {MAX_FILE_SIZE_MB}MB.',
        'unsupported_format': f'❌ Unsupported format! Please send: {", ".join(SUPPORTED_FORMATS)}',
        'processing_error': '❌ Error processing image. Please try again with a different image.',
        'rate_limit': f'❌ Too many requests! Please wait before sending another image. Limit: {MAX_REQUESTS_PER_USER_PER_MINUTE} per minute.',
        'timeout': '❌ Processing timeout. Please try with a smaller image.',
        'download_error': '❌ Failed to download image. Please try again.',
        'general_error': '❌ An unexpected error occurred. Please try again later.'
    }

# Validate configuration
def validate_config():
    """Validate that all required configuration is present"""
    if not Config.BOT_TOKEN:
        raise ValueError(Config.ERROR_MESSAGES['no_token'])
    
    return True
