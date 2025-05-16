from audio_detect_voice import detect_voice as d_v
from video_audio import vid_aud as v_a
from smaller_text import summarization as sumn
v_a('./uploads/12.mp4')
a = sumn(d_v('ru-RU' ,'audio.wav'), 1, 'russian')
print(a)