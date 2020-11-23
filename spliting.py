
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import simpleaudio as sa
import sys
import time

recognizer = sr.Recognizer()

class spliting():
    
    def __init__(self, file_in):
        self.file_in = file_in
    
    def get_duration(self):
        newAudio = AudioSegment.from_wav(self.file_in)
        return len(newAudio)

    def get_text(self, file_ , lang='ar-DZ'):
        with sr.AudioFile(file_) as source:
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio, language=lang)
            except Exception as ex:
                text = ex
        return text

    def split_time(self, time1, time2, file_out):
        # time (millisecond)
        if time1 < time2:
            newAudio = AudioSegment.from_wav(self.file_in)
            if time2 > len(newAudio):
                time2 = len(newAudio)
            newAudio = newAudio[time1:time2]
            newAudio.export(file_out, format="wav")
            return file_out
    


    def playing(self, file_, file_out_name, time1=None, time2=None):
        if (time1!=None) and (time2!= None):
            self.split_time(time1, time2, file_out_name+'.wav')        
        wave_obj = sa.WaveObject.from_wave_file(file_out_name+'.wav')
        play_obj = wave_obj.play()
        play_obj.wait_done()
        
        t0 = time.time() * 1000
        t1 = time.time() * 1000

    def playing2(self, file_, time1, time2):
        self.split_time(time1, time2, 'temp.wav')        
        wave_obj = sa.WaveObject.from_wave_file('temp.wav')
        play_obj = wave_obj.play()
        play_obj.wait_done()

"""
sp = spliting('test.wav')
sp.split_time(1000,6000,'splited.wav')
print(sp.get_text('splited.wav'))
sp.playing('test.wav', 1000,6000)

 def split_threshold(self, filepath , pourcent_thres, min_sile_len):
        sound = AudioSegment.from_wav(filepath)
        dBFS = sound.dBFS
        NEWDBFS = dBFS - (pourcent_thres * dBFS)
        chunks = split_on_silence(sound, 
            min_silence_len = min_sile_len, silence_thresh = NEWDBFS)


        for i, chunk in enumerate(chunks):
            normalized_chunk = match_target_amplitude(chunk, -25.0)
            print("Exporting chunk{0}.wav.".format(i))
            normalized_chunk.export(".//chunk{0}.wav".format(i), bitrate = "256k", format = "wav")

            with sr.AudioFile(".//chunk{0}.wav".format(i)) as source:
                audio = recognizer.listen(source)
                try:
                    text = recognizer.recognize_google(audio, language= 'ar-DZ' )
                    print("Chunk : {}".format(text))
                except Exception as ex:
                    print("Error occured")
                    print(ex)
"""
