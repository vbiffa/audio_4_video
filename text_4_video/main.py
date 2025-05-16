from flask import Flask, request, render_template, redirect, url_for
import os
from audio_detect_voice import detect_voice as d_v
from video_audio import vid_aud as v_a
from smaller_text import summarization as sumn
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = 'uploads'
allowed_video = {'mp4', 'mkv', 'mov', 'avi', 'mpg'}
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload_video', methods = ["POST"])
def upload_video():
    if 'video' not in request.files:
        return redirect(request.url)
    vid_file = request.files["video"]
    if vid_file.filename == '':
        return redirect(request.url)
    name_video = '.' in vid_file.filename and vid_file.filename.rsplit('.', 1)[-1].lower() in allowed_video
    if vid_file and name_video:
        name_video = vid_file.filename
        vid_file.save(os.path.join(app.config["UPLOAD_FOLDER"], name_video))
        v_a(f'./uploads/{name_video}')
        text = sumn(d_v('ru-RU' ,'audio.wav'), 1, 'russian')
        os.remove(f'./uploads/{name_video}')
        os.remove('./audio.wav')
    else: 
        text = 'error: неправильный формат файла'
    return render_template('index.html', text = text)
app.run()
