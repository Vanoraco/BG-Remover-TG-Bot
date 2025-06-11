# Makefile for Telegram Background Removal Bot

.PHONY: help setup install test run clean

help:
	@echo "Available commands:"
	@echo "  setup     - Run complete setup (install dependencies, create .env)"
	@echo "  install   - Install dependencies only"
	@echo "  test      - Test the setup and configuration"
	@echo "  run       - Start the bot"
	@echo "  clean     - Clean up temporary files"
	@echo "  help      - Show this help message"

setup:
	@echo "🚀 Running complete setup..."
	python setup.py

install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt

test:
	@echo "🧪 Testing setup..."
	python test_setup.py

run:
	@echo "🤖 Starting the bot..."
	python bot.py

clean:
	@echo "🧹 Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete
