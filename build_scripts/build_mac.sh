#!/bin/bash

# Build script for macOS
# ==============================================================================
#
# Description:
#   - This script builds the mBank to HomeBank converter application for macOS 
#       using PyInstaller.
#   - It checks for PyInstaller, installs it if necessary, and then builds the
#       application.
#   - It also moves the Info.plist file into the application bundle.
#
# Requirements:
#   - Python 3.x installed.
#   - PyInstaller must be installed.
#      - If not, the script will attempt to install it.
#   - The script should be run from the build_script directory. It will
#       navigate to the project root directory automatically.
#
# Note:
#   - This script is intended for macOS systems.
#   - Ensure you have the necessary permissions to run scripts and install 
#       packages.
#   - chmod +x build_mac.sh to make the script executable.
#
# Usage: 
#   ./build_mac.sh
#
# Exit codes:
#   0 - Success
#   1 - Failure (e.g., PyInstaller not installed, build failed, etc.)
#
# ==============================================================================

echo "### Starting build process for macOS..."

# Ensure the script is run from the project root directory
cd "$(dirname "$0")/.."

# Check if PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "### PyInstaller is not installed. Try to install it using 'pip install pyinstaller'."
    # Attempt to install PyInstaller
    pip install pyinstaller
    if [ $? -ne 0 ]; then
        echo "### Failed to install PyInstaller. Please check your Python environment."
        exit 1
    else
        echo "### PyInstaller installed successfully. Proceeding with the build..."
    fi
else
    echo "### PyInstaller is installed. Proceeding with the build..."
fi

# Run PyInstaller to create the macOS application
# --noconfirm: Overwrite existing files without confirmation
# --onedir: Create a directory with the application files
# --windowed: Suppress the terminal window for GUI applications
# --icon: Specify the application icon
# --version-file: Include version information from a file
# scr/mbank-to-homebank.py: The main script to build

pyinstaller --noconfirm --onedir --windowed --icon=resources/icon.icns --version-file=resources/mbank-to-homebank.version scr/mbank-to-homebank.py

# Check if the build was successful
if [ $? -ne 0 ]; then
    echo "### PyInstaller build failed. Please check the output for errors."
    exit 1
else
    echo "### PyInstaller build completed successfully."
fi

# Move Info.plist to the application bundle
if [ ! -d "dist/mbank-to-homebank.app/Contents" ]; then
    echo "### Application bundle not found. Please check the build output."
    exit 1
else
    echo "### Moving Info.plist to the application bundle..."
    cp resources/Info.plist dist/mbank-to-homebank.app/Contents/Info.plist
fi

# Check if the Info.plist was copied successfully
if [ $? -ne 0 ]; then
    echo "### Copying Info.plist failed. Please check the output for errors."
    exit 1
else
    echo "### Info.plist copied successfully."
fi

# Final check
if [ $? -eq 0 ]; then
    echo "### Build completed successfully."
else
    echo "### Build failed. Please check the output for errors."
    exit 1
fi