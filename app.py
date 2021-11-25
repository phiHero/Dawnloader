from flask import Flask, render_template, request, url_for, redirect, send_file, session
import youtube_dl
from pytube import YouTube
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"


@app.route('/terms-conditions')
def terms():
	return render_template('terms-conditions.html')

"""YT"""
@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except:
            return render_template("error.html")
        return render_template("ytdownload.html", url = url)
    return render_template("ytDl.html")

@app.route("/ytdownload", methods = ["GET", "POST"])
def download_video():
    if request.method == "POST":
        buffer = BytesIO()
        url = YouTube(session['link'])
        itag = request.form.get("itag")
        if itag =="139" or itag =="140":
            audio = url.streams.get_by_itag(itag)
            audio.stream_to_buffer(buffer)
            buffer.seek(0)
            return send_file(buffer, as_attachment=True, download_name=url.title +".mp3",  mimetype="audio/mp4")
        else:
            video = url.streams.get_by_itag(itag)
            video.stream_to_buffer(buffer)
            buffer.seek(0)
            return send_file(buffer, as_attachment=True, download_name=url.title +".mp4", mimetype="video/mp4")
    return redirect(url_for("home"))




"""FB"""
@app.route("/fb", methods=["GET", "POST"])
def facebook_downloader():
    if request.method == "GET":
        return render_template("fbDl.html")
    else:
        if not request.form["url1"]:
            return redirect("/fb")
								
@app.route('/download', methods=["POST", "GET"])
def download():
	if request.method == "POST":
			if not request.form["url1"]:
				return redirect("/fb")
			url1 = request.form["url1"]
			if "http" and "f" and "b" not in url1:
				return render_template("error.html")
			else:
				with youtube_dl.YoutubeDL() as ydl:
					url1 = ydl.extract_info(url1, download=False)
					try:
						download_link = url1["entries"][-1]["formats"][-1]["url"]
					except:
						download_link = url1["formats"][-1]["url"]
					return redirect(download_link+"&dl=1")


if __name__ == "__main__":
    app.run(debug=False)