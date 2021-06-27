import moviepy.editor

video=moviepy.editor.VideoFileClip('v1.mp4')

audio=video.audio

audio.write_audiofile('a1.mp3')
