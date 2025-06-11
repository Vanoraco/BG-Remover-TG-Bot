"""
Test script to verify the bot setup and dependencies
"""
import sys
import os
from pathlib import Path

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing imports...")
    
    try:
        import telegram
        print("✅ python-telegram-bot imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import telegram: {e}")
        return False
    
    try:
        import transparent_background
        print("✅ transparent-background imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import transparent_background: {e}")
        return False
    
    try:
        from PIL import Image
        print("✅ Pillow imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Pillow: {e}")
        return False
    
    try:
        import cv2
        print("✅ OpenCV imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import OpenCV: {e}")
        return False
    
    try:
        import numpy
        print("✅ NumPy imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import NumPy: {e}")
        return False
    
    return True

def test_config():
    """Test configuration loading"""
    print("\nTesting configuration...")
    
    try:
        from config import Config, validate_config
        print("✅ Config module imported successfully")
        
        # Check if .env file exists
        if Path('.env').exists():
            print("✅ .env file found")
            if Config.BOT_TOKEN:
                print("✅ BOT_TOKEN is set")
            else:
                print("⚠️  BOT_TOKEN is not set in .env file")
        else:
            print("⚠️  .env file not found. Copy .env.example to .env and set BOT_TOKEN")
        
        return True
    except Exception as e:
        print(f"❌ Config test failed: {e}")
        return False

def test_image_processor():
    """Test image processor initialization"""
    print("\nTesting image processor...")
    
    try:
        from image_processor import BackgroundRemover
        print("✅ BackgroundRemover imported successfully")
        
        # Try to initialize (this will download the model if needed)
        print("Initializing model (this may take a while on first run)...")
        remover = BackgroundRemover()
        print("✅ Model initialized successfully")
        
        return True
    except Exception as e:
        print(f"❌ Image processor test failed: {e}")
        return False

def test_bot_module():
    """Test bot module loading"""
    print("\nTesting bot module...")
    
    try:
        from bot import BackgroundRemovalBot
        print("✅ Bot module imported successfully")
        return True
    except Exception as e:
        print(f"❌ Bot module test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Background Removal Bot Setup\n")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_config,
        test_image_processor,
        test_bot_module
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! Your bot is ready to run.")
        print("\nTo start the bot:")
        print("1. Make sure BOT_TOKEN is set in .env file")
        print("2. Run: python bot.py")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
