#!/bin/bash
# Git Setup Script for BG-Remover-TG-Bot

echo "🚀 Setting up Git repository for BG-Remover-TG-Bot"
echo "=================================================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Initialize git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
else
    echo "✅ Git repository already initialized"
fi

# Add remote origin
echo "🔗 Adding remote origin..."
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/Vanoraco/BG-Remover-TG-Bot.git

# Verify remote
echo "🔍 Verifying remote..."
git remote -v

# Create .gitignore if it doesn't exist
if [ ! -f ".gitignore" ]; then
    echo "📝 Creating .gitignore..."
    cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Environment variables
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
*.log
logs/

# Model checkpoints and cache
*.pth
*.pt
*.ckpt
.transparent-background/

# Temporary files
temp/
tmp/
*.tmp

# Test files
test_images/
output/
test_input.png
test_output_*.png
EOF
fi

# Stage all files
echo "📦 Staging files..."
git add .

# Check git status
echo "📊 Git status:"
git status

# Commit files
echo "💾 Creating initial commit..."
read -p "Enter commit message (or press Enter for default): " commit_msg
if [ -z "$commit_msg" ]; then
    commit_msg="Initial commit: Telegram Transparency Master Bot

Features:
- Multiple transparency effects (full, semi, soft, subject, custom)
- AI-powered background removal using InSPyReNet
- User-friendly Telegram bot interface
- Docker deployment support
- Comprehensive documentation and setup scripts"
fi

git commit -m "$commit_msg"

# Set up branch
echo "🌿 Setting up main branch..."
git branch -M main

# Push to GitHub
echo "🚀 Pushing to GitHub..."
echo "Note: You may need to authenticate with GitHub"
git push -u origin main

echo ""
echo "✅ Git setup completed successfully!"
echo ""
echo "🎉 Your repository is now available at:"
echo "   https://github.com/Vanoraco/BG-Remover-TG-Bot"
echo ""
echo "📋 Next steps:"
echo "1. Go to GitHub and verify your repository"
echo "2. Add repository description and topics"
echo "3. Enable GitHub Pages if desired"
echo "4. Set up branch protection rules"
echo "5. Configure deployment secrets for CI/CD"
echo ""
echo "🔧 Useful Git commands:"
echo "   git status          - Check repository status"
echo "   git add .           - Stage all changes"
echo "   git commit -m 'msg' - Commit changes"
echo "   git push            - Push to GitHub"
echo "   git pull            - Pull latest changes"
