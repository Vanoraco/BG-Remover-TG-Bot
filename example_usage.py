"""
Example usage of the background removal functionality
This script demonstrates how to use the image processor directly
"""
import asyncio
import sys
from pathlib import Path
from PIL import Image
from image_processor import background_remover

async def process_image_example(input_path: str, output_path: str = None):
    """
    Example function to process a single image
    
    Args:
        input_path: Path to input image
        output_path: Path for output image (optional)
    """
    try:
        # Check if input file exists
        if not Path(input_path).exists():
            print(f"❌ Input file not found: {input_path}")
            return False
        
        # Read image file
        with open(input_path, 'rb') as f:
            image_bytes = f.read()
        
        print(f"📁 Processing image: {input_path}")
        print(f"📊 File size: {len(image_bytes) / 1024:.1f} KB")
        
        # Validate image
        is_valid, error_msg = background_remover.validate_image(image_bytes)
        if not is_valid:
            print(f"❌ Validation failed: {error_msg}")
            return False
        
        print("✅ Image validation passed")
        print("🔄 Processing image (this may take 10-60 seconds)...")
        
        # Process image
        result_bytes = await background_remover.process_image(image_bytes)
        
        if result_bytes is None:
            print("❌ Processing failed")
            return False
        
        # Save result
        if output_path is None:
            input_file = Path(input_path)
            output_path = input_file.parent / f"{input_file.stem}_no_bg.png"
        
        with open(output_path, 'wb') as f:
            f.write(result_bytes)
        
        print(f"✅ Processing completed successfully!")
        print(f"💾 Output saved to: {output_path}")
        print(f"📊 Output size: {len(result_bytes) / 1024:.1f} KB")
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing image: {e}")
        return False

async def main():
    """Main function for example usage"""
    print("🎨 Background Removal Example\n")
    
    if len(sys.argv) < 2:
        print("Usage: python example_usage.py <input_image_path> [output_image_path]")
        print("\nExample:")
        print("  python example_usage.py test_image.jpg")
        print("  python example_usage.py test_image.jpg output_no_bg.png")
        return 1
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = await process_image_example(input_path, output_path)
    
    if success:
        print("\n🎉 Example completed successfully!")
        return 0
    else:
        print("\n❌ Example failed!")
        return 1

if __name__ == '__main__':
    asyncio.run(main())
