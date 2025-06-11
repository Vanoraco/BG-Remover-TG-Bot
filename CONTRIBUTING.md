# Contributing to Telegram Transparency Master Bot

Thank you for your interest in contributing to this project! We welcome contributions from everyone.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git
- Basic knowledge of Python and Telegram bots

### Setting Up Development Environment

1. **Fork the repository**
   ```bash
   # Click the "Fork" button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/BG-Remover-TG-Bot.git
   cd BG-Remover-TG-Bot
   ```

3. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Add your test bot token to .env
   ```

## 🛠️ Development Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused

### Testing

- Write tests for new features
- Ensure all existing tests pass
- Test with different image formats and sizes
- Verify transparency effects work correctly

### Commit Messages

Use clear and descriptive commit messages:
```
feat: add new transparency mode
fix: resolve memory leak in image processing
docs: update installation instructions
test: add unit tests for transparency effects
```

## 🎯 How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported
2. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version)
   - Error logs if applicable

### Suggesting Features

1. Check if the feature has been suggested before
2. Create a new issue with:
   - Clear description of the feature
   - Use cases and benefits
   - Possible implementation approach

### Submitting Code Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, well-documented code
   - Add tests for new functionality
   - Update documentation if needed

3. **Test your changes**
   ```bash
   python test_setup.py
   python test_transparency.py
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Provide a clear description of your changes

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No merge conflicts

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Tested locally
- [ ] Added new tests
- [ ] All existing tests pass

## Screenshots (if applicable)
Add screenshots of new features or UI changes
```

## 🎨 Areas for Contribution

### High Priority
- Performance optimizations
- New transparency effects
- Better error handling
- Documentation improvements

### Medium Priority
- Additional image formats support
- Batch processing features
- User interface improvements
- Deployment automation

### Low Priority
- Code refactoring
- Additional tests
- Example scripts
- Tutorials

## 🔧 Development Tips

### Local Testing
```bash
# Test with sample images
python example_usage.py test_image.jpg

# Run transparency tests
python test_transparency.py

# Check bot functionality
python bot.py
```

### Debugging
- Use logging for debugging: `logger.info("Debug message")`
- Test with different image sizes and formats
- Monitor memory usage during processing
- Check error handling with invalid inputs

### Performance Considerations
- Profile code for bottlenecks
- Optimize image processing pipeline
- Consider memory usage with large images
- Test concurrent user scenarios

## 📚 Resources

- [Python-telegram-bot documentation](https://python-telegram-bot.readthedocs.io/)
- [InSPyReNet paper](https://arxiv.org/abs/2209.09475)
- [PIL/Pillow documentation](https://pillow.readthedocs.io/)
- [Docker documentation](https://docs.docker.com/)

## 🤝 Community

- Be respectful and inclusive
- Help others learn and grow
- Share knowledge and best practices
- Provide constructive feedback

## 📞 Getting Help

If you need help:
1. Check existing issues and discussions
2. Read the documentation
3. Ask questions in GitHub Discussions
4. Contact maintainers if needed

Thank you for contributing! 🎉
