from gtts import gTTS
from tempfile import TemporaryFile
import playsound
tts = gTTS(text='Hello', lang='en')
f = TemporaryFile()
tts.write_to_fp(f)
# Play f
playsound.playsound(f)
f.close()
