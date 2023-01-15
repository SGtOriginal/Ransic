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

def ogg_conv(file):
    return f"{file.rsplit('.', 1)[0]}.ogg"

def fixer():
    files = os.listdir(os.path.join(os.getcwd(), 'sound-files'))
    for file in files:
        # print(f"ffmpeg.exe -y -loglevel quiet -i '{os.path.join(os.path.join(os.getcwd(), 'sound-files'), file)}' '{os.path.join(os.path.join(os.getcwd(), 'sound-files'), ogg_conv(file))}'")
        os.system(f"powershell -c ./ffmpeg.exe -y -loglevel quiet -i '{os.path.join(os.path.join(os.getcwd(), 'sound-files'), file)}' '{os.path.join(os.path.join(os.getcwd(), 'sound-files'), ogg_conv(file))}'")
        if file.rsplit('.', 1)[1] != "ogg":
            os.remove(f"sound-files/{file}")

def sound_files():
    audio_list = []
    
    fixer()
    
    files = os.listdir(os.path.join(os.getcwd(), 'sound-files'))
    for file in files:
        path = os.path.join(os.path.join(os.getcwd(), 'sound-files'), file)
        audio_list.append(path)
    
    return audio_list

def main():
    mixer.init()
    
    audio_list = sound_files()
    
    while True:
        song_num = rand_num(min=0, max=(len(audio_list)-1))
        
        song_path = audio_list[song_num]
        
        print(song_path)
        
        if round(audioread.audio_open(song_path).duration) <= 2:
            mixer.music.load(song_path)
            
            mixer.music.play()
            
            time.sleep(audioread.audio_open(song_path).duration)
        
        else:
            song_start_pos = rand_num(min=2, max=(round(audioread.audio_open(song_path).duration)))

            #Monkey Fix
            if song_start_pos == 2:
                song_start_pos = 3

            song_end_pos = rand_num(min=1, max=((song_start_pos)-1))
            
            mixer.music.load(song_path)

            monkey_fix = True

            while monkey_fix:
                try:
                    mixer.music.play(start=song_start_pos)
                except Exception as e:
                    song_start_pos = rand_num(min=2, max=(round(audioread.audio_open(song_path).duration)))

                    if song_start_pos == 2:
                        song_start_pos = 3

                    song_end_pos = rand_num(min=1, max=((song_start_pos) - 1))

                    mixer.music.load(song_path)
                else:
                    monkey_fix = False

            time.sleep(song_end_pos)
        
        mixer.music.stop()

main()