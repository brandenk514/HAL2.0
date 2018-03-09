from wit import Wit
import wave
import pyaudio
import os
from array import array


class Witai:
    def __init__(self):
        client = Wit(access_token=os.environ.get('wit_token'))

        resp = client.message('what is the weather in London?')
        print('Yay, got Wit.ai response: ' + str(resp))

        self.create_audio_file()

        res = None
        with open('resources/audio.wav', 'rb') as f:
            res = client.speech(f, None, {'Content-Type': 'audio/wav'})
        print('Yay, got Wit.ai response: ' + str(res))

    def create_audio_file(self):

        audio_format = pyaudio.paInt16
        channels = 2
        sample_rate = 44100
        chunk = 1024
        recording_seconds = 5
        file_name = "resources/audio.wav"

        audio = pyaudio.PyAudio()  # instantiate the pyaudio

        # recording prerequisites
        stream = audio.open(format=audio_format, channels=channels,
                            rate=sample_rate,
                            input=True,
                            frames_per_buffer=chunk)

        # starting recording
        frames = []

        for i in range(0, int(sample_rate / chunk * recording_seconds)):
            data = stream.read(chunk)
            data_chunk = array('h', data)
            vol = max(data_chunk)
            if vol >= 500:
                frames.append(data)

        # end of recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # writing to file
        wave_file = wave.open(file_name, 'wb')
        wave_file.setnchannels(channels)
        wave_file.setsampwidth(audio.get_sample_size(audio_format))
        wave_file.setframerate(sample_rate)
        wave_file.writeframes(b''.join(frames))  # append frames recorded to file
        wave_file.close()


if __name__ == '__main__':
    w = Witai()
