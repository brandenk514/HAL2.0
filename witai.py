from wit import Wit
import wave
import pyaudio
import os
from array import array
import logging


class Witai:
    def __init__(self):
        self.client = Wit(access_token=os.environ.get('wit_token'))

    def create_audio_file(self):

        audio_format = pyaudio.paInt16
        channels = 2
        sample_rate = 44100
        chunk = 1024
        recording_seconds = 5
        file_name = "resources/audio.wav"

        audio = pyaudio.PyAudio()  # instantiate the pyAudio

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

    def create_message_request(self, text):
        try:
            resp = self.client.message(text)
            print('Yay, got Wit.ai response: ' + str(resp))
        except Exception:
            self.client.logger.setLevel(logging.WARNING)
            print('Something went wrong with the message request')

    def create_speech_request(self):
        self.create_audio_file()
        try:
            with open('resources/audio.wav', 'rb') as f:
                res = self.client.speech(f, None, {'Content-Type': 'audio/wav'})
                print('Yay, got Wit.ai response: ' + str(res))
        except Exception:
            self.client.logger.setLevel(logging.WARNING)
            print("Something went wrong with the speech request")


if __name__ == '__main__':
    w = Witai()
    w.create_speech_request()
