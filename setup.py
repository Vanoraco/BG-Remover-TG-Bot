"""
Setup script for the Telegram Background Removal Bot
"""
import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible")
        print("Please use Python 3.8 or higher")
        return False

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    
    # Check if we're in a virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment detected")
    else:
        print("⚠️  No virtual environment detected. Consider using one for better isolation.")
    
    # Install requirements
    return run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Installing Python packages"
    )

def setup_environment():
    """Set up environment file"""
    print("\n🔧 Setting up environment...")
    
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    if env_example.exists():
        # Copy example to .env
        with open(env_example, 'r') as src, open(env_file, 'w') as dst:
            dst.write(src.read())
        print("✅ Created .env file from template")
        print("⚠️  Please edit .env file and add your BOT_TOKEN")
        return True
    else:
        print("❌ .env.example file not found")
        return False

def test_installation():
    """Test if everything is installed correctly"""
    print("\n🧪 Testing installation...")
    
    try:
        # Test imports
        import telegram
        import transparent_background
        from PIL import Image
        import cv2
        
        print("✅ All required packages imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Telegram Background Removal Bot Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Failed to install dependencies")
        return 1
    
    # Setup environment
    if not setup_environment():
        print("\n❌ Failed to setup environment")
        return 1
    
    # Test installation
    if not test_installation():
        print("\n❌ Installation test failed")
        return 1
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Get a bot token from @BotFather on Telegram")
    print("2. Edit .env file and add your BOT_TOKEN")
    print("3. Run: python test_setup.py (to verify everything works)")
    print("4. Run: python bot.py (to start the bot)")
    print("\nFor testing image processing:")
    print("5. Run: python example_usage.py <image_path>")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
