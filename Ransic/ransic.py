import glob
import time
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from pygame import mixer
import audioread
import secrets as sc

def rand_num(min: int, max: int):
    secretsGenerator = sc.SystemRandom()
    number = secretsGenerator.randint(min, max)
    return number

def sound_files():
    audio_list = []
    
    mp3_files = glob.iglob('sound-files/*.mp3', recursive=True)
    for mp3 in mp3_files:
        root_dir = os.path.abspath(os.path.dirname(__file__))
        bg_path = os.path.join(root_dir, mp3)
        audio_list.append(bg_path)
    
    wav_files = glob.iglob('sound-files/*.wav', recursive=True)
    for wav in wav_files:
        root_dir = os.path.abspath(os.path.dirname(__file__))
        bg_path = os.path.join(root_dir, wav)
        audio_list.append(bg_path)
    
    return audio_list

def main():
    mixer.init()
    
    audio_list = sound_files()
    
    while True:
        song_num = rand_num(min=0, max=(len(audio_list)-1))
        
        song_path = audio_list[song_num]
        
        song_start_pos = rand_num(min=0, max=(int((audioread.audio_open(song_path).duration))))
        
        song_end_pos = rand_num(min=0, max=song_start_pos)
        
        mixer.music.load(song_path)
        
        mixer.music.play(start=song_start_pos)
        
        time.sleep(song_end_pos)
        
        mixer.music.stop()

main()