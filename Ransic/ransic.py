import requests
import glob
import asyncio
from playsound import playsound
import os

async def ran_num(min: int, max: int):
    number = requests.get(f"https://www.random.org/integers/?num=1&min={min}&max={max}&col=1&base=10&format=plain&rnd=new")
    number = int(number.text)
    return number

async def sound_files():
    mp3_list = []
    mp3_files = glob.iglob('sound-files/*.mp3', recursive=True)
    for mp3 in mp3_files:
        root_dir = os.path.abspath(os.path.dirname(__file__))
        bg_path = os.path.join(root_dir, mp3)
        mp3_list.append(bg_path)
    
    wav_list = []
    wav_files = glob.iglob('sound-files/*.wav', recursive=True)
    for wav in wav_files:
        root_dir = os.path.abspath(os.path.dirname(__file__))
        bg_path = os.path.join(root_dir, wav)
        wav_list.append(bg_path)
    
    return mp3_list, wav_list;

async def main():
    mp3_list, wav_list = await sound_files()
    while True:
        num1 = await ran_num(min=0, max=1)
        if num1 == 0:
            if (int(len(mp3_list))-1) == 0:
                playsound(mp3_list[0])
            elif (int(len(mp3_list))-1) > 0:
                num2 = await ran_num(min=0, max=(int(len(mp3_list))-1))
                playsound(mp3_list[num2])
        elif num1 == 1:
            if (int(len(wav_list))-1) == 0:
                playsound(wav_list[0])
            elif (int(len(wav_list))-1) > 0:
                num2 = await ran_num(min=0, max=(int(len(wav_list))-1))
                playsound(wav_list[num2])

asyncio.run(main())