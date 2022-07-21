# RIPRODURRE AUDIO

from playsound import playsound

playsound('myfile.wav')


# REGISTRARE AUDIO

import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Frequenza di campionamento
seconds = 3  # Durata della registrazione

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Blocca esecuzione fino a fine registrazione
write('output.wav', fs, myrecording)  # Salva in formato wav




