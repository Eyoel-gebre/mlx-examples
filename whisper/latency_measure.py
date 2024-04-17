import whisper
import time

start = time.time()
result = whisper.transcribe('interior_soundclip.mp3')
print(f'sample 1 finished in {time.time() - start} ms\n result: \n{result}')

start = time.time()
result = whisper.transcribe('long_speech.mp3')
print(f'sample 2 finished in {time.time() - start} ms\n result: \n{result}')