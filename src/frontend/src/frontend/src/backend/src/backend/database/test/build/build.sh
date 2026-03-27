#!/bin/bash
# Build script for Employee Payroll Management System

echo "Starting build process..."
pip install flask
echo "Dependencies installed."
python app.py &
echo "Application started successfully."
echo "Build complete!"
