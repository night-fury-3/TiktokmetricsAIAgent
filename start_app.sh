#!/bin/bash

# TikTok Metrics AI Agent - Startup Script

echo "🚀 Starting TikTok Metrics AI Agent..."

# Set Python path
export PYTHONPATH="/home/ubuntu/Documents/Dev/AlgoTest/TikTokMetricsAIAgent"

# Check if port 8000 is already in use
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  Port 8000 is already in use. Stopping existing process..."
    pkill -f "python3 app.py"
    sleep 2
fi

# Start the application
echo "📊 Starting FastAPI application..."
python3 app.py
