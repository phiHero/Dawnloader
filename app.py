import json
from io import BytesIO
from os import environ

import youtube_dl
import yt_dlp
from flask import Flask, redirect, render_template, request, send_file, session, url_for
from pytube import YouTube

app = Flask(__name__)
app.config["SECRET_KEY"] = environ.get("FLASK_SECRET_KEY") or "test"


"""YTDLP"""


@app.route("/download", methods=["GET", "POST"])
def allPlatform():
    if request.method == "POST":
        try:
            session["link"] = request.form.get("url")
            ydl_opts = {
                "format_sort": ["hasvid", "hasaud", "quality"],
                "skip_download": True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.sanitize_info(
                    ydl.extract_info(session["link"], download=False)
                )
                formats = []
                for format in info["formats"]:
                    if format["ext"] == "mhtml" or "manifest_url" in format:
                        continue
                    format["tbr"] = round(format["tbr"])
                    formats.append(format)
                info["formats"] = formats
                return render_template("all-platform-dl.html", info=info)
        except Exception as e:
            print(e.args)
            return render_template("error.html")
    return render_template("index.html")


"""YT"""


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            session["link"] = request.form.get("url")
            url = YouTube(session["link"])
            url.check_availability()
        except:
            return render_template("error.html")
        return render_template("ytdownload.html", url=url)
    return render_template("index.html")


@app.route("/ytdownload", methods=["GET", "POST"])
def download_video():
    if request.method == "POST":
        try:
            buffer = BytesIO()
            url = YouTube(session["link"])
            itag = request.form.get("itag")
            if itag == "139" or itag == "140":
                audio = url.streams.get_by_itag(itag)
                audio.stream_to_buffer(buffer)
                buffer.seek(0)
                return send_file(
                    buffer,
                    as_attachment=True,
                    download_name=url.title + "-" + audio.abr + ".mp3",
                    mimetype="audio/mp4",
                )
            elif itag == "249" or itag == "250" or itag == "251":
                audio = url.streams.get_by_itag(itag)
                audio.stream_to_buffer(buffer)
                buffer.seek(0)
                return send_file(
                    buffer,
                    as_attachment=True,
                    download_name=url.title + "-" + audio.abr + ".webm",
                    mimetype="audio/webm",
                )
            elif itag == "137":
                h_video = url.streams.get_by_itag(itag)
                h_video.stream_to_buffer(buffer)
                ##h_audio = url.streams.filter(abr="160kbps",progressive=False, mime_type="audio/webm", type="audio")
                return send_file(
                    buffer,
                    as_attachment=True,
                    download_name=url.title + "-1080p(No-audio).mp4",
                    mimetype="video/mp4",
                )
            else:
                video = url.streams.get_by_itag(itag)
                video.stream_to_buffer(buffer)
                buffer.seek(0)
                return send_file(
                    buffer,
                    as_attachment=True,
                    download_name=url.title + "-" + video.resolution + ".mp4",
                    mimetype="video/mp4",
                )
        except:
            return render_template("error.html")
    return redirect(url_for("home"))


@app.route("/indexing")
def back():
    return redirect(url_for("home"))


"""FB"""


@app.route("/fb", methods=["POST", "GET"])
def download():
    if request.method == "POST":
        session["link2"] = request.form.get("url1")
        url1 = session["link2"]
        if "http" and "f" and "b" not in url1:
            return render_template("error.html")
        else:
            return render_template("fbdl.html", url1=url1)


@app.route("/configure", methods=["POST", "GET"])
def configure():
    url1 = session["link2"]
    try:
        with youtube_dl.YoutubeDL() as ydl:
            url1 = ydl.extract_info(url1, download=False)
            configure = request.form.get("vid_type")
            if configure == "sd":
                try:
                    download_link = url1["entries"][-1]["formats"][-2]["url"]
                except:
                    download_link = url1["formats"][-2]["url"]
            elif configure == "hd":
                try:
                    download_link = url1["entries"][-1]["formats"][-1]["url"]
                except:
                    download_link = url1["formats"][-1]["url"]
            else:
                try:
                    download_link = url1["entries"][-1]["formats"][0]["url"]
                except:
                    download_link = url1["formats"][0]["url"]
            return redirect(download_link + "&dl=1")
    except:
        return render_template("error.html")


@app.route("/terms-conditions")
def terms():
    return render_template("terms-conditions.html")


if __name__ == "__main__":
    app.run(debug=False, port=3000, host="192.168.1.6")
    # app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
