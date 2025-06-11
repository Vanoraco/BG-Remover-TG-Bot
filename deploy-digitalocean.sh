#!/bin/bash
# DigitalOcean Deployment Script

echo "🌊 DigitalOcean Deployment Setup"
echo "This script helps you deploy to a DigitalOcean droplet"

# Check if we're on the server
if [ "$1" = "server" ]; then
    echo "Setting up on DigitalOcean server..."
    
    # Update system
    apt update && apt upgrade -y
    
    # Install Docker
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    
    # Install Docker Compose
    apt install docker-compose git nano -y
    
    # Clone repository (you'll need to replace with your repo)
    echo "Enter your GitHub repository URL:"
    read REPO_URL
    git clone $REPO_URL BGTGBot
    cd BGTGBot
    
    # Setup environment
    echo "Enter your bot token:"
    read -s BOT_TOKEN
    echo "BOT_TOKEN=$BOT_TOKEN" > .env
    
    # Build and run
    docker-compose up -d
    
    # Setup auto-restart service
    cat > /etc/systemd/system/transparency-bot.service << EOF
[Unit]
Description=Transparency Bot
After=docker.service
Requires=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=$(pwd)
ExecStart=/usr/bin/docker-compose up -d
ExecStop=/usr/bin/docker-compose down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
EOF
    
    systemctl enable transparency-bot
    systemctl start transparency-bot
    
    echo "✅ Bot deployed and running!"
    echo "Check status with: docker-compose logs -f"
    
else
    echo "Instructions for DigitalOcean deployment:"
    echo ""
    echo "1. Create a DigitalOcean droplet (Ubuntu 22.04, $6/month)"
    echo "2. Copy this script to your server:"
    echo "   scp deploy-digitalocean.sh root@your-server-ip:~/"
    echo "3. SSH to your server:"
    echo "   ssh root@your-server-ip"
    echo "4. Run the script:"
    echo "   chmod +x deploy-digitalocean.sh"
    echo "   ./deploy-digitalocean.sh server"
    echo ""
    echo "Or run this one-liner on your server:"
    echo "curl -sSL https://raw.githubusercontent.com/yourusername/BGTGBot/main/deploy-digitalocean.sh | bash -s server"
fi
