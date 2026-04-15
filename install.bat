@echo off
title RedditVideoMakerBot - Install Dependencies
cd /d "%~dp0"
echo Installing dependencies for RedditVideoMakerBot...
echo This may take a few minutes. Do not close this window.
echo.

py -3.11 -m pip install --upgrade pip --timeout 120
py -3.11 -m pip install -r requirements.txt --timeout 120
echo.
echo Installing Playwright browser (needed for screenshots)...
py -3.11 -m playwright install chromium
echo.
echo ============================================
echo  Installation complete!
echo  Double-click start.bat to launch the GUI.
echo ============================================
pause
