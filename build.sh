#!/usr/bin/env bash
set -e
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Training MedBot chatbot model..."
python train.py
echo "Build complete!"
