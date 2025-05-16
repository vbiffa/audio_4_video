import moviepy
def vid_aud(video):
    audio = moviepy.VideoFileClip(video)
    audio.audio.write_audiofile('audio.wav')
