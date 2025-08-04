import pygame
import random
import threading
import time
import os
from pynput import keyboard

# setup sound shit
pygame.mixer.init()

# where to find sounds
folders = {
    'memes': 'sounds/memes/',
    'fx': 'sounds/fx/', 
    'music': 'sounds/music/',
    'misc': 'sounds/misc/'
}

# what keys do what
keys = {
    'q': 'memes',
    'w': 'fx', 
    'e': 'music',
    'r': 'misc'
}

current = None
chaos = False

def get_sounds():
    # find all sound files
    all_sounds = {}
    
    for name, folder in folders.items():
        all_sounds[name] = []
        if os.path.exists(folder):
            for f in os.listdir(folder):
                if f.endswith(('.mp3', '.wav', '.ogg', '.m4a', '.flac')):
                    all_sounds[name].append(os.path.join(folder, f))
                    
    return all_sounds

def play(file):
    # play sound
    global current
    try:
        if current:
            current.stop()
        current = pygame.mixer.Sound(file)
        current.play()
        print(f"playing: {os.path.basename(file)}")
    except:
        print(f"failed to play {file}")

def random_from(category, sounds):
    # play random sound from category
    if category in sounds and sounds[category]:
        file = random.choice(sounds[category])
        play(file)
    else:
        print(f"no sounds in {category}")

def chaos_mode(sounds):
    # continuous random sounds
    global chaos
    chaos = False  # set to true if you want to enable chaos mode
    print("CHAOS MODE! press space to stop")
    
    while chaos:
        # get all sounds
        all_files = []
        for cat in sounds.values():
            all_files.extend(cat)
            
        if all_files:
            file = random.choice(all_files)
            play(file)
            
        # wait random time
        time.sleep(random.uniform(0.3, 2.5))

def stop_chaos():
    global chaos, current
    chaos = False
    if current:
        current.stop()
    print("chaos stopped")

def handle_key(key, sounds):
    global chaos
    
    try:
        k = key.char.lower()
        
        if k in keys:
            if chaos:
                stop_chaos()
            random_from(keys[k], sounds)
                
    except:
        # space key
        if key == keyboard.Key.space:
            if chaos:
                stop_chaos()
            else:
                t = threading.Thread(target=chaos_mode, args=(sounds,))
                t.daemon = True
                t.start()

def setup_folders():
    # make folders if needed
    for folder in folders.values():
        os.makedirs(folder, exist_ok=True)
    
    # make instructions
    txt = """put sound files here:

memes/ - meme sounds (press q)
fx/ - sound effects (press w) 
music/ - music clips (press e)
misc/ - whatever (press r)

space = chaos mode
esc = quit

supports .mp3, .wav, .ogg, .m4a, .flac files
"""
    
    with open('sounds/howto.txt', 'w') as f:
        f.write(txt)

def main():
    print("chaotic soundboard v1.0")
    print("making folders...")
    setup_folders()
    
    print("loading sounds...")
    sounds = get_sounds()
    
    # count sounds
    total = sum(len(cat) for cat in sounds.values())
    print(f"found {total} sounds:")
    for name, files in sounds.items():
        print(f"  {name}: {len(files)}")
    
    if total == 0:
        print("\nno sounds found!")
        print("put some .mp3/.wav files in the sounds/ folders")
        return
    
    print("\ncontrols:")
    print("q=memes, w=fx, e=music, r=misc")
    print("space=chaos mode, esc=quit")
    print("\nready to make noise...")
    
    # listen for keys
    def on_press(key):
        if key == keyboard.Key.esc:
            print("bye!")
            return False
        handle_key(key, sounds)
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
