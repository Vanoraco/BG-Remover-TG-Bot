# PowerShell Git Setup Script for BG-Remover-TG-Bot

Write-Host "🚀 Setting up Git repository for BG-Remover-TG-Bot" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green

# Check if git is installed
try {
    git --version | Out-Null
    Write-Host "✅ Git is installed" -ForegroundColor Green
} catch {
    Write-Host "❌ Git is not installed. Please install Git first." -ForegroundColor Red
    exit 1
}

# Initialize git repository if not already initialized
if (-not (Test-Path ".git")) {
    Write-Host "📁 Initializing Git repository..." -ForegroundColor Yellow
    git init
} else {
    Write-Host "✅ Git repository already initialized" -ForegroundColor Green
}

# Add remote origin
Write-Host "🔗 Adding remote origin..." -ForegroundColor Yellow
git remote remove origin 2>$null
git remote add origin https://github.com/Vanoraco/BG-Remover-TG-Bot.git

# Verify remote
Write-Host "🔍 Verifying remote..." -ForegroundColor Yellow
git remote -v

# Stage all files
Write-Host "📦 Staging files..." -ForegroundColor Yellow
git add .

# Check git status
Write-Host "📊 Git status:" -ForegroundColor Yellow
git status

# Commit files
Write-Host "💾 Creating initial commit..." -ForegroundColor Yellow
$commitMsg = Read-Host "Enter commit message (or press Enter for default)"
if ([string]::IsNullOrWhiteSpace($commitMsg)) {
    $commitMsg = @"
Initial commit: Telegram Transparency Master Bot

Features:
- Multiple transparency effects (full, semi, soft, subject, custom)
- AI-powered background removal using InSPyReNet
- User-friendly Telegram bot interface
- Docker deployment support
- Comprehensive documentation and setup scripts
"@
}

git commit -m $commitMsg

# Set up branch
Write-Host "🌿 Setting up main branch..." -ForegroundColor Yellow
git branch -M main

# Push to GitHub
Write-Host "🚀 Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "Note: You may need to authenticate with GitHub" -ForegroundColor Cyan
git push -u origin main

Write-Host ""
Write-Host "✅ Git setup completed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "🎉 Your repository is now available at:" -ForegroundColor Green
Write-Host "   https://github.com/Vanoraco/BG-Remover-TG-Bot" -ForegroundColor Cyan
Write-Host ""
Write-Host "📋 Next steps:" -ForegroundColor Yellow
Write-Host "1. Go to GitHub and verify your repository"
Write-Host "2. Add repository description and topics"
Write-Host "3. Enable GitHub Pages if desired"
Write-Host "4. Set up branch protection rules"
Write-Host "5. Configure deployment secrets for CI/CD"
Write-Host ""
Write-Host "🔧 Useful Git commands:" -ForegroundColor Yellow
Write-Host "   git status          - Check repository status"
Write-Host "   git add .           - Stage all changes"
Write-Host "   git commit -m 'msg' - Commit changes"
Write-Host "   git push            - Push to GitHub"
Write-Host "   git pull            - Pull latest changes"
