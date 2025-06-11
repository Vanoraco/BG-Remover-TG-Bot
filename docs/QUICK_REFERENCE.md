# 📋 Quick Reference Guide

## 🚀 Getting Started

### 1. Clone and Setup
```bash
git clone https://github.com/Vanoraco/BG-Remover-TG-Bot.git
cd BG-Remover-TG-Bot
python setup.py
```

### 2. Configure Bot Token
```bash
cp .env.example .env
# Edit .env and add: BOT_TOKEN=your_token_here
```

### 3. Run the Bot
```bash
python bot.py
```

## 🎨 Transparency Modes

| Command | Effect | Description |
|---------|--------|-------------|
| `mode:full` | ![Full](https://img.shields.io/badge/Full-Complete%20Removal-green) | Complete background removal (default) |
| `mode:semi` | ![Semi](https://img.shields.io/badge/Semi-50%25%20Transparent-orange) | Semi-transparent background |
| `mode:soft` | ![Soft](https://img.shields.io/badge/Soft-Feathered%20Edges-blue) | Soft edge transparency |
| `mode:subject` | ![Subject](https://img.shields.io/badge/Subject-Translucent-purple) | Make subject semi-transparent |
| `opacity:75` | ![Custom](https://img.shields.io/badge/Custom-75%25%20Opacity-red) | Custom opacity level |

## 🤖 Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message and transparency options |
| `/help` | Detailed help and usage information |
| `/modes` | See all available transparency modes |
| `/settings` | View and adjust your preferences |

## 🔧 Common Tasks

### Test Installation
```bash
python test_setup.py
```

### Test Transparency Features
```bash
python test_transparency.py
```

### Process Image Directly
```bash
python example_usage.py path/to/image.jpg
```

### Deploy to Railway
```bash
railway login
railway init
railway up
```

### Deploy to DigitalOcean
```bash
curl -sSL https://raw.githubusercontent.com/Vanoraco/BG-Remover-TG-Bot/main/deploy-digitalocean.sh | bash -s server
```

## 🐳 Docker Commands

### Build and Run
```bash
docker-compose up -d
```

### View Logs
```bash
docker-compose logs -f
```

### Stop
```bash
docker-compose down
```

## 🔍 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Bot token error | Check `.env` file has correct `BOT_TOKEN` |
| Model download slow | First run downloads 367MB model |
| Memory issues | Ensure 2GB+ RAM available |
| Import errors | Run `pip install -r requirements.txt` |

### Check Bot Status
```bash
# View logs
tail -f bot.log

# Check process
ps aux | grep python

# Test connection
curl -s https://api.telegram.org/bot$BOT_TOKEN/getMe
```

## 📊 System Requirements

### Minimum
- Python 3.8+
- 2GB RAM
- 5GB storage
- Stable internet

### Recommended
- Python 3.9+
- 4GB RAM
- 10GB storage
- SSD storage
- GPU (optional)

## 🌐 Hosting Options

| Platform | Cost | Difficulty | Best For |
|----------|------|------------|----------|
| Railway | Free-$5/mo | ⭐ Easy | Testing |
| Render | Free-$7/mo | ⭐ Easy | Development |
| DigitalOcean | $6/mo | ⭐⭐ Medium | Production |
| AWS EC2 | $5-10/mo | ⭐⭐⭐ Hard | Enterprise |

## 📁 Important Files

| File | Purpose |
|------|---------|
| `bot.py` | Main bot application |
| `image_processor.py` | AI transparency processing |
| `config.py` | Configuration settings |
| `.env` | Environment variables (BOT_TOKEN) |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Container configuration |

## 🔗 Useful Links

- **Repository**: https://github.com/Vanoraco/BG-Remover-TG-Bot
- **Issues**: https://github.com/Vanoraco/BG-Remover-TG-Bot/issues
- **Telegram Bot API**: https://core.telegram.org/bots/api
- **InSPyReNet Paper**: https://arxiv.org/abs/2209.09475
- **Railway**: https://railway.app
- **DigitalOcean**: https://digitalocean.com

## 📞 Getting Help

1. **Check Documentation**:
   - [How It Works](HOW_IT_WORKS.md)
   - [Flow Diagrams](FLOW_DIAGRAMS.md)
   - [Contributing Guide](../CONTRIBUTING.md)

2. **Common Solutions**:
   - Restart the bot: `Ctrl+C` then `python bot.py`
   - Clear model cache: `rm -rf ~/.transparent-background/`
   - Update dependencies: `pip install -r requirements.txt --upgrade`

3. **Get Support**:
   - Open an issue on GitHub
   - Check existing issues and discussions
   - Review troubleshooting section in README

## 🎯 Quick Commands Cheat Sheet

```bash
# Setup
git clone https://github.com/Vanoraco/BG-Remover-TG-Bot.git
cd BG-Remover-TG-Bot
python setup.py

# Run
python bot.py

# Test
python test_setup.py

# Deploy
railway deploy
# OR
docker-compose up -d

# Monitor
docker-compose logs -f
```

---

**Need more help?** Check the full documentation or open an issue! 🚀
