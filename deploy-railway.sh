#!/bin/bash
# Railway Deployment Script

echo "🚀 Deploying to Railway..."

# Check if railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "Installing Railway CLI..."
    npm install -g @railway/cli
fi

# Login to Railway
echo "Please login to Railway..."
railway login

# Initialize project
railway init

# Set environment variables
echo "Setting environment variables..."
echo "Please enter your bot token:"
read -s BOT_TOKEN
railway variables set BOT_TOKEN="$BOT_TOKEN"

# Deploy
echo "Deploying..."
railway up

echo "✅ Deployment complete!"
echo "Check your Railway dashboard for the deployment status."
