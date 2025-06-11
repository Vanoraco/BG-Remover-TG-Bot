"""
Image processing module for background removal using InSPyReNet
"""
import io
import logging
import asyncio
from typing import Optional, Tuple
from PIL import Image

from transparent_background import Remover
from config import Config

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BackgroundRemover:
    """
    Background removal processor using InSPyReNet model
    """
    
    def __init__(self):
        """Initialize the background remover with InSPyReNet model"""
        self.remover = None
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize the InSPyReNet model with tracer_b7 configuration"""
        try:
            logger.info("Initializing InSPyReNet model...")
            self.remover = Remover(
                mode=Config.MODEL_MODE,  # 'base' uses tracer_b7 variant
                jit=Config.USE_JIT,
                resize=Config.RESIZE_MODE
            )
            logger.info("Model initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize model: {e}")
            raise
    
    async def process_image(self, image_bytes: bytes, mode: str = 'full', opacity: int = 100) -> Optional[bytes]:
        """
        Process image with transparency effects

        Args:
            image_bytes: Raw image bytes
            mode: Transparency mode ('full', 'semi', 'soft', 'subject', 'custom')
            opacity: Opacity level for custom mode (1-100)

        Returns:
            Processed image bytes with transparency effects, or None if failed
        """
        try:
            # Convert bytes to PIL Image
            image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            logger.info(f"Processing image of size: {image.size}")
            
            # Process in thread pool to avoid blocking
            loop = asyncio.get_event_loop()
            processed_image = await loop.run_in_executor(
                None,
                self._apply_transparency_effect,
                image, mode, opacity
            )
            
            if processed_image is None:
                return None
            
            # Convert back to bytes
            output_buffer = io.BytesIO()
            processed_image.save(output_buffer, format='PNG')
            output_bytes = output_buffer.getvalue()
            
            logger.info(f"Successfully processed image. Output size: {len(output_bytes)} bytes")
            return output_bytes
            
        except Exception as e:
            logger.error(f"Error processing image: {e}")
            return None
    
    def _apply_transparency_effect(self, image: Image.Image, mode: str = 'full', opacity: int = 100) -> Optional[Image.Image]:
        """
        Apply transparency effects to PIL Image using InSPyReNet

        Args:
            image: PIL Image object
            mode: Transparency mode
            opacity: Opacity level (1-100)

        Returns:
            Processed PIL Image with transparency effects
        """
        try:
            if self.remover is None:
                logger.error("Model not initialized")
                return None

            # Get the mask first
            mask = self.remover.process(image, type='map')

            # Apply different transparency effects based on mode
            if mode == 'full':
                # Standard transparent background
                result = self.remover.process(image, type='rgba')

            elif mode == 'semi':
                # Semi-transparent background
                result = self._create_semi_transparent(image, mask, 0.5)

            elif mode == 'soft':
                # Soft edge transparency
                result = self._create_soft_edges(image, mask)

            elif mode == 'subject':
                # Semi-transparent subject
                result = self._create_transparent_subject(image, mask, 0.7)

            elif mode == 'custom':
                # Custom opacity
                alpha_value = opacity / 100.0
                result = self._create_semi_transparent(image, mask, 1.0 - alpha_value)

            else:
                # Default to full transparency
                result = self.remover.process(image, type='rgba')

            return result

        except Exception as e:
            logger.error(f"Error in transparency processing: {e}")
            return None

    def _create_semi_transparent(self, image: Image.Image, mask: Image.Image, bg_alpha: float) -> Image.Image:
        """Create semi-transparent background effect"""
        # Convert to RGBA
        image_rgba = image.convert('RGBA')
        mask_gray = mask.convert('L')

        # Create alpha channel
        alpha = Image.new('L', image.size, 255)

        # Apply transparency to background areas
        for x in range(image.width):
            for y in range(image.height):
                mask_val = mask_gray.getpixel((x, y))
                if mask_val < 128:  # Background area
                    alpha.putpixel((x, y), int(255 * bg_alpha))

        # Apply alpha channel
        image_rgba.putalpha(alpha)
        return image_rgba

    def _create_soft_edges(self, image: Image.Image, mask: Image.Image) -> Image.Image:
        """Create soft edge transparency with feathering"""
        from PIL import ImageFilter

        # Convert to RGBA
        image_rgba = image.convert('RGBA')
        mask_gray = mask.convert('L')

        # Apply gaussian blur to mask for soft edges
        soft_mask = mask_gray.filter(ImageFilter.GaussianBlur(radius=3))

        # Use the blurred mask as alpha channel
        image_rgba.putalpha(soft_mask)
        return image_rgba

    def _create_transparent_subject(self, image: Image.Image, mask: Image.Image, subject_alpha: float) -> Image.Image:
        """Make the subject semi-transparent instead of background"""
        # Convert to RGBA
        image_rgba = image.convert('RGBA')
        mask_gray = mask.convert('L')

        # Create alpha channel
        alpha = Image.new('L', image.size, 255)

        # Apply transparency to subject areas
        for x in range(image.width):
            for y in range(image.height):
                mask_val = mask_gray.getpixel((x, y))
                if mask_val >= 128:  # Subject area
                    alpha.putpixel((x, y), int(255 * subject_alpha))
                else:  # Background - make fully transparent
                    alpha.putpixel((x, y), 0)

        # Apply alpha channel
        image_rgba.putalpha(alpha)
        return image_rgba
    
    def validate_image(self, image_bytes: bytes) -> Tuple[bool, str]:
        """
        Validate image format and size
        
        Args:
            image_bytes: Raw image bytes
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            # Check file size
            if len(image_bytes) > Config.MAX_FILE_SIZE_BYTES:
                return False, Config.ERROR_MESSAGES['file_too_large']
            
            # Try to open image to validate format
            image = Image.open(io.BytesIO(image_bytes))
            
            # Check if it's a valid image format
            if image.format.lower() not in ['jpeg', 'png', 'webp']:
                return False, Config.ERROR_MESSAGES['unsupported_format']
            
            # Additional validation - check if image can be processed
            if image.size[0] < 10 or image.size[1] < 10:
                return False, "❌ Image too small. Minimum size is 10x10 pixels."
            
            if image.size[0] > 4096 or image.size[1] > 4096:
                return False, "❌ Image too large. Maximum size is 4096x4096 pixels."
            
            return True, ""
            
        except Exception as e:
            logger.error(f"Error validating image: {e}")
            return False, "❌ Invalid image file. Please send a valid image."

# Global instance
background_remover = BackgroundRemover()
