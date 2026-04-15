import json
import webbrowser
from pathlib import Path

# Used "tomlkit" instead of "toml" because it doesn't change formatting on "dump"
import tomlkit
from flask import (
    Flask,
    Response,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

import utils.gui_utils as gui

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #
HOST = "localhost"
PORT = 4000

app = Flask(__name__, template_folder="GUI")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# --------------------------------------------------------------------------- #
# Cache-control — keep UI fresh on every load
# --------------------------------------------------------------------------- #
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# --------------------------------------------------------------------------- #
# Pages
# --------------------------------------------------------------------------- #
@app.route("/")
def index():
    return render_template("index.html", file="videos.json")


@app.route("/backgrounds", methods=["GET"])
def backgrounds():
    return render_template("backgrounds.html", file="backgrounds.json")


@app.route("/settings", methods=["GET", "POST"])
def settings():
    config_path = Path("config.toml")

    # Gracefully handle missing config
    if not config_path.exists():
        config_load = tomlkit.loads("")
        config = {}
    else:
        config_load = tomlkit.loads(config_path.read_text())
        config = gui.get_config(config_load)

    checks = gui.get_checks()

    if request.method == "POST":
        data = request.form.to_dict()
        config = gui.modify_settings(data, config_load, checks)

    return render_template(
        "settings.html", file="config.toml", data=config, checks=checks
    )


# --------------------------------------------------------------------------- #
# Background actions
# --------------------------------------------------------------------------- #
@app.route("/background/add", methods=["POST"])
def background_add():
    youtube_uri = (request.form.get("youtube_uri") or "").strip()
    filename = (request.form.get("filename") or "").strip()
    citation = (request.form.get("citation") or "").strip()
    position = (request.form.get("position") or "").strip()

    gui.add_background(youtube_uri, filename, citation, position)
    return redirect(url_for("backgrounds"))


@app.route("/background/delete", methods=["POST"])
def background_delete():
    key = request.form.get("background-key") or ""
    gui.delete_background(key)
    return redirect(url_for("backgrounds"))


# --------------------------------------------------------------------------- #
# JSON data endpoints
# --------------------------------------------------------------------------- #
@app.route("/videos.json")
def videos_json():
    """Serve videos.json; return empty list if file doesn't exist yet."""
    videos_path = Path("video_creation/data/videos.json")
    if not videos_path.exists():
        return Response(
            json.dumps([]),
            status=200,
            mimetype="application/json",
        )
    return send_from_directory("video_creation/data", "videos.json")


@app.route("/backgrounds.json")
def backgrounds_json():
    """Serve backgrounds.json; return empty object if missing."""
    bg_path = Path("utils/backgrounds.json")
    if not bg_path.exists():
        return Response(
            json.dumps({}),
            status=200,
            mimetype="application/json",
        )
    return send_from_directory("utils", "backgrounds.json")


# --------------------------------------------------------------------------- #
# Static assets
# --------------------------------------------------------------------------- #
@app.route("/results/<path:name>")
def results(name):
    return send_from_directory("results", name, as_attachment=True)


@app.route("/voices/<path:name>")
def voices(name):
    return send_from_directory("GUI/voices", name, as_attachment=True)


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    webbrowser.open(f"http://{HOST}:{PORT}", new=2)
    print(f"RedditVideoMakerBot GUI running at http://{HOST}:{PORT}")
    print("Press Ctrl+C to quit.")
    app.run(host=HOST, port=PORT, debug=False)
