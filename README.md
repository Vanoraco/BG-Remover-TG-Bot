# 🎨 Telegram Transparency Master Bot

A powerful Telegram bot that creates amazing transparency effects with images using the state-of-the-art InSPyReNet AI model with tracer_b7 variant configuration.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://telegram.org)
[![AI](https://img.shields.io/badge/AI-InSPyReNet-orange.svg)](https://github.com/plemeri/InSPyReNet)

## ✨ Features

- 🎨 **Multiple Transparency Effects**: Full, semi, soft edges, subject transparency, and custom opacity
- 🤖 **AI-Powered Processing**: Uses InSPyReNet (ACCV 2022) for high-quality results
- 📱 **Easy Mode Selection**: Simple commands to switch between transparency modes
- 🚀 **Fast Processing**: Optimized with TorchScript for quick inference
- 🛡️ **Rate Limiting**: Built-in protection against abuse
- 📊 **Multiple Formats**: Supports JPEG, PNG, and WebP images
- ⚡ **Concurrent Processing**: Handles multiple users simultaneously
- 🔧 **User Settings**: Personalized transparency preferences per user

## 🎯 Transparency Modes

| Mode | Description | Usage |
|------|-------------|-------|
| **Full** | Complete background removal (default) | Just send image |
| **Semi** | Semi-transparent background (50% opacity) | `mode:semi` |
| **Soft** | Soft edge transparency with feathering | `mode:soft` |
| **Subject** | Make the subject semi-transparent | `mode:subject` |
| **Custom** | Choose opacity level (1-99%) | `opacity:75` |

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- WebP (.webp)

## Requirements

- Python 3.8+
- Telegram Bot Token (from @BotFather)
- GPU recommended for faster processing (CPU also supported)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Vanoraco/BG-Remover-TG-Bot.git
cd BG-Remover-TG-Bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Copy the example environment file and configure it:

```bash
cp .env.example .env
```

Edit `.env` and add your bot token:

```env
BOT_TOKEN=your_bot_token_here
```

### 4. Get a Telegram Bot Token

1. Message @BotFather on Telegram
2. Create a new bot with `/newbot`
3. Follow the instructions to get your token
4. Add the token to your `.env` file

## Usage

### Running the Bot

```bash
python bot.py
```

### Bot Commands

- `/start` - Welcome message and transparency options
- `/help` - Detailed help and usage information
- `/modes` - See all available transparency modes
- `/settings` - View and adjust your preferences

### Using the Bot

**Basic Usage:**
1. Start a chat with your bot on Telegram
2. Send `/start` to see the welcome message
3. Send any image → get full transparency (default)

**Advanced Usage:**
1. Send `mode:semi` to switch to semi-transparent mode
2. Send `opacity:75` for 75% transparency
3. Send your image and get custom transparency effects!

**Available Transparency Modes:**
- **Full** - Complete background removal (default)
- **Semi** - Semi-transparent background (50% opacity)
- **Soft** - Soft edge transparency with feathering
- **Subject** - Make the subject semi-transparent
- **Custom** - Choose your own opacity level (1-99%)

## Configuration

The bot can be configured through `config.py`:

- **File Size Limit**: Default 20MB maximum
- **Rate Limiting**: 5 requests per user per minute
- **Model Settings**: InSPyReNet base mode with tracer_b7
- **Processing Timeout**: 60 seconds maximum

## Project Structure

```
BGTGBot/
├── bot.py                 # Main bot application
├── image_processor.py     # Background removal logic
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Technical Details

### InSPyReNet Integration

The bot uses the `transparent-background` library which implements InSPyReNet:

- **Model**: InSPyReNet with tracer_b7 variant
- **Mode**: Base mode for high quality results
- **Output**: RGBA images with transparent backgrounds
- **Optimization**: TorchScript JIT compilation for performance

### Error Handling

- File size validation
- Format verification
- Processing timeout protection
- Rate limiting enforcement
- Comprehensive error messages

### Performance Optimizations

- Asynchronous processing
- Thread pool execution for CPU-intensive tasks
- Model initialization caching
- Memory-efficient image handling

## Deployment

### Local Development

```bash
python bot.py
```

### Production Deployment

For production deployment, consider:

1. **Process Management**: Use systemd, supervisor, or PM2
2. **Environment**: Set up proper Python virtual environment
3. **Logging**: Configure appropriate log levels and rotation
4. **Monitoring**: Set up health checks and monitoring
5. **Resources**: Ensure adequate RAM and GPU memory

### Docker Deployment (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "bot.py"]
```

## Troubleshooting

### Common Issues

1. **Bot Token Error**: Ensure BOT_TOKEN is correctly set in .env
2. **Model Download**: First run may take time to download the model
3. **Memory Issues**: Large images may require more RAM
4. **GPU Issues**: Install CUDA-compatible PyTorch for GPU acceleration

### Logs

The bot provides detailed logging. Check console output for:
- Model initialization status
- Processing progress
- Error details

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [InSPyReNet](https://github.com/plemeri/InSPyReNet) for the background removal model
- [transparent-background](https://github.com/plemeri/transparent-background) for the Python implementation
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for the Telegram integration

## Support

If you encounter any issues or have questions:

1. Check the troubleshooting section
2. Review the logs for error details
3. Open an issue on GitHub with detailed information

---

**Powered by InSPyReNet AI Model** 🤖
