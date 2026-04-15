@echo off
title RedditVideoMakerBot - Generate Video
cd /d "%~dp0"
echo Generating Reddit video...
echo.
py -3.11 main.py
pause
