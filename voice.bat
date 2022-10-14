mkdir wav
for /r %%a in (*.ogg) do ffmpeg -i "%%~fa" -ar 22050 "wav/%%~na.wav"