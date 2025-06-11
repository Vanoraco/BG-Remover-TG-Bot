"""
Test script for transparency features
"""
import asyncio
import sys
from pathlib import Path
from PIL import Image, ImageDraw
from image_processor import background_remover

def create_test_image():
    """Create a simple test image with a clear subject and background"""
    # Create a 300x300 image with white background
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw a blue circle (subject) in the center
    draw.ellipse([75, 75, 225, 225], fill='blue', outline='darkblue', width=3)
    
    # Add some text
    try:
        draw.text((150, 150), "TEST", fill='white', anchor='mm')
    except:
        # Fallback if font not available
        pass
    
    return img

async def test_transparency_modes():
    """Test different transparency modes"""
    print("🧪 Testing Transparency Modes\n")
    
    # Create test image
    test_img = create_test_image()
    test_img.save('test_input.png')
    print("✅ Created test image: test_input.png")
    
    # Convert to bytes
    import io
    img_buffer = io.BytesIO()
    test_img.save(img_buffer, format='PNG')
    img_bytes = img_buffer.getvalue()
    
    # Test different modes
    modes_to_test = [
        ('full', 100, 'Full transparency (background removal)'),
        ('semi', 100, 'Semi-transparent background'),
        ('soft', 100, 'Soft edge transparency'),
        ('subject', 100, 'Semi-transparent subject'),
        ('custom', 75, 'Custom 75% opacity')
    ]
    
    for mode, opacity, description in modes_to_test:
        print(f"\n🔄 Testing {mode} mode: {description}")
        
        try:
            result_bytes = await background_remover.process_image(
                img_bytes, 
                mode=mode, 
                opacity=opacity
            )
            
            if result_bytes:
                output_path = f'test_output_{mode}.png'
                with open(output_path, 'wb') as f:
                    f.write(result_bytes)
                print(f"✅ Success! Saved: {output_path}")
            else:
                print(f"❌ Failed to process {mode} mode")
                
        except Exception as e:
            print(f"❌ Error in {mode} mode: {e}")
    
    print(f"\n🎉 Transparency testing completed!")
    print("Check the generated test_output_*.png files to see the results.")

async def main():
    """Main test function"""
    print("🎨 Transparency Features Test\n")
    
    try:
        await test_transparency_modes()
        return 0
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return 1

if __name__ == '__main__':
    asyncio.run(main())
