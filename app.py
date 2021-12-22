from flask import Flask, render_template, request, url_for, redirect, send_file, session
import youtube_dl
from pytube import YouTube
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "b'\x9d\x8a\x0fD\x04\x02\xda\xc7\xff\x9e\x0e\x9a\x15\xe0\x81\x87]\x06j\xab\x86\x99 G'"


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
    return render_template("index.html")

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


@app.route('/indexing')
def back():
	return redirect(url_for("home"))

"""FB"""
								
@app.route('/download', methods=["POST", "GET"])
def download():
	if request.method == "POST":
                session['link2'] = request.form.get('url1')
                url1 = session['link2']
                if "http" and "f" and "b" not in url1:
                    return render_template("error.html")
                else:
                                return render_template("fbdl.html",url1=url1)

@app.route('/configure', methods=["POST", "GET"])
def configure():
    url1 = session['link2']
    with youtube_dl.YoutubeDL() as ydl:
        url1 = ydl.extract_info(url1, download=False)
        configure = request.form.get("vid_type")
        if configure =='sd':
            try:
                download_link = url1["entries"][-1]["formats"][-2]["url"]
            except:
                download_link = url1["formats"][-2]["url"]
        elif configure =='hd':
            try:
                download_link = url1["entries"][-1]["formats"][-1]["url"]
            except:
                download_link = url1["formats"][-1]["url"]
        else:
            try:
                download_link = url1["entries"][-1]["formats"][0]["url"]
            except:
                download_link = url1["formats"][0]["url"]
        return redirect(download_link+"&dl=1")


if __name__ == "__main__":
    app.run(debug=True)