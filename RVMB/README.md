# RVMB 🎥

RVMB (Reddit Video Maker Bot) is an automated tool that turns Reddit threads into short-form videos no video editing or manual asset compiling required. It handles everything from scraping the thread to producing a finished MP4 file ready for upload.

---

## What It Does

Short-form Reddit content performs extremely well on platforms like TikTok, YouTube Shorts and Instagram Reels. Creating it manually means finding a thread, screenshotting comments, recording a voiceover, and editing everything together which takes time and effort every single time.

RVMB automates the entire process. You point it at a subreddit, it picks a thread, captures screenshots of the post and comments, generates a text-to-speech voiceover, and assembles it all over a background video into a finished MP4. The result is a complete video ready for you to upload wherever you want.

> **Note:** RVMB produces the video file only. Uploading to any platform is done manually by you, keeping full control over what gets posted and when.

---

## Requirements

- **Python 3.11** other versions may cause dependency issues
- **FFmpeg** required for video encoding
- **Playwright** installed automatically during setup, used for browser-based screenshots

---

## Installation

**Step 1 Install Python 3.11**

Download the Python 3.11 installer for Windows and run it. During installation, make sure to tick **"Add Python to PATH"** before clicking Install.

**Step 2 Install FFmpeg**

Download FFmpeg from the official site and add the `ffmpeg/bin` folder to your system PATH. This is required for the final video encoding step.

**Step 3 Install dependencies**

Open the project folder, then double-click **`install.bat`**.

This will install all required Python packages and download the Playwright browser automatically. Wait for it to finish before moving on.

Alternatively, run the following in PowerShell from inside the project folder:

```sh
py -3.11 -m pip install -r requirements.txt --timeout 120
py -3.11 -m playwright install chromium
```

---

## Running the GUI

The GUI is a browser-based control panel that lets you manage settings, browse generated videos, and manage background videos.

Double-click **`start.bat`** to launch it.

Or run manually:

```sh
cd path\to\RVMB
py -3.11 GUI.py
```

Then open your browser and go to:

```
http://localhost:4000
```

---

## Configuration

Before generating any videos, go to the **Settings** page in the GUI and fill in the following:

**Reddit Credentials**
- Go to `reddit.com/prefs/apps` and create a new app of type **script**
- Copy the **Client ID** and **Client Secret** into the Settings page
- Enter your Reddit username and password

**Content Settings**
- Choose which subreddit to pull posts from (e.g. `AskReddit`)
- Set minimum comment count, max comment length, and whether to allow NSFW posts

**Voice Settings**
- Choose a TTS platform (TikTok, Google Translate, AWS Polly, ElevenLabs, etc.)
- Select a specific voice and preview it with the play button

**Background Video**
- Choose from the available background videos or add your own on the Backgrounds page

Click **Save Changes** when done. All settings are stored in `config.toml`.

---

## Generating a Video

Once settings are configured, double-click **`run_bot.bat`** to generate a video.

Or run manually:

```sh
py -3.11 main.py
```

The bot will fetch a thread, capture screenshots, generate audio, and assemble the final MP4. Progress is shown in the terminal window. The finished video is saved to the `results/` folder and will appear in the GUI under **Videos**.

---

## Reconfiguring

To change any setting, use the **Settings** page in the GUI and save again. Alternatively, open `config.toml` directly in a text editor delete the lines you want to reset and they will be prompted again on the next run.

---

## What Has Been Implemented

- Automated Reddit thread scraping via the official Reddit API
- Browser-based screenshot capture of posts and comments
- Multiple TTS voice platforms: TikTok, Google Translate, AWS Polly, Streamlabs Polly, ElevenLabs, OpenAI, and system voices
- Randomised or manually specified thread selection
- Choice of background video and background audio
- Light, dark and transparent Reddit screenshot themes
- NSFW post filtering
- Duplicate video detection skips threads that have already been processed
- Story mode for narrative-style subreddits
- Thumbnail generation
- AI-based thread similarity ranking
- Configurable video resolution, zoom level, opacity and transitions
- Full browser-based GUI for configuration and video management

---

## Troubleshooting

**`ModuleNotFoundError`** Run `install.bat` again. A package did not install correctly.

**`TemplateNotFound: index.html`** You ran `GUI.py` from the wrong directory. Always use `start.bat`, or `cd` into the project folder before running `py -3.11 GUI.py`.

**pip timeouts during install** Your network is blocking the package server. Switch to a mobile hotspot and run `install.bat` again.

**`spacy` or `torch` install errors** These packages are only needed for the optional AI similarity feature and are not included in `requirements.txt`. The bot works fully without them.

**Videos not appearing in the GUI** Make sure `main.py` completed without errors. Check the `results/` folder directly to confirm the MP4 was created.

---

## License

The Roboto fonts included in the `fonts/` folder are licensed under the Apache License 2.0.
