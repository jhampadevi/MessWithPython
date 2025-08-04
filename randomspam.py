import os
import time
import random
import pyautogui
import string

# Enable fail-safe mode
# stop the script by moving the mouse to the top-left corner of the screen
pyautogui.FAILSAFE = True

# Uncomment this to enable fail-safe mode Custom one
# # get screen shit
# w, h = pyautogui.size()
# stop_x = 0  
# stop_y = h - 1  
# zone = 50  # whatever

# def mouse_check():
#     # see if mouse in corner or whatever
#     x, y = pyautogui.position()
#     # just check if mouse is in bottom-left area (make it bigger zone)
#     if x <= 100 and y >= (h - 100):  # bigger zone so easier to trigger
#         print(f"STOP! mouse at {x},{y}")
#         raise pyautogui.FailSafeException("stopped cause mouse moved to the corner and shi")

stuff = [
    "Yo!",
    "checking in!",
    "spam spam spam!",
    "como estas bitch?",
    "dih",
    "fuck you",
    "bitchass",
    "bombaclaat",
    "dumbahh",
    "WASSSSSSUPPPPP",
    "no cap fr fr",
    "sheeeesh",
    "that's sus ngl",
    "touch grass",
    "ratio + L + you fell off",
    "certified hood classic",
    "based and redpilled"
]

# some faces idk
weird_faces = [
    "( ͡° ͜ʖ ͡°)",
    "¯\\_(ツ)_/¯",
    "(╯°□°）╯︵ ┻━┻",
    "ಠ_ಠ",
    "( ͡~ ͜ʖ ͡°)",
    "┬─┬ノ( º _ ºノ)",
    "◉_◉",
    "(☞ﾟヮﾟ)☞",
    "ᕕ( ᐛ )ᕗ"
]

# emojis n shit
emoji_crap = ["😂", "💀", "🔥", "👀", "😭", "🤡", "💯", "🗿", "🤮", "😈", "🥵", "🤯", "👺", "🤠"]

def make_gibberish():
    # just random letters lol
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 15)))

def emoji_vomit():
    # puke emojis everywhere
    return ''.join(random.choices(emoji_crap, k=random.randint(3, 8)))

def caps_madness():
    # make caps go crazy
    txt = random.choice(stuff)
    return ''.join(random.choice([c.upper(), c.lower()]) for c in txt)

def slow_type(txt):
    # type slow like human
    for c in txt:
        pyautogui.typewrite(c)
        time.sleep(random.uniform(0.01, 0.1))

print("chaos bot tye xii")
print("wait 10 sec...")
print(f"put mouse top left to stop")
print("ctrl c also works")

# wait some time
for i in range(5, 0, -1):
    print(f"go in {i}...")
    time.sleep(1)

try:
    count = 0
    while True:
        # pyautogui default failsafe handles mouse check
        
        count += 1
        
        # pick random shit to do
        mode = random.randint(1, 8)
        
        if mode == 1:
            # normal msg
            msg = random.choice(stuff)
            print(f"[{count}] normal: {msg}")
            pyautogui.typewrite(msg)
            
        elif mode == 2:
            # face thing
            msg = random.choice(weird_faces)
            print(f"[{count}] face: {msg}")
            pyautogui.typewrite(msg)
            
        elif mode == 3:
            # emoji dump
            msg = emoji_vomit()
            print(f"[{count}] emoji: {msg}")
            pyautogui.typewrite(msg)
            
        elif mode == 4:
            # random letters
            msg = make_gibberish()
            print(f"[{count}] gibberish: {msg}")
            slow_type(msg)
            
        elif mode == 5:
            # caps mess
            msg = caps_madness()
            print(f"[{count}] caps: {msg}")
            pyautogui.typewrite(msg)
            
        elif mode == 6:
            # spam multiple
            for _ in range(random.randint(2, 4)):
                quick = random.choice(stuff[:5])
                pyautogui.typewrite(quick)
                pyautogui.press('enter')
                time.sleep(0.1)
            print(f"[{count}] rapid fire")
            continue
            
        elif mode == 7:
            # type then delete lol
            fake = random.choice(stuff)
            print(f"[{count}] fake delete: {fake}")
            slow_type(fake)
            time.sleep(0.5)
            # delete it
            for _ in range(len(fake)):
                pyautogui.press('backspace')
                time.sleep(0.02)
            # type real one
            real = random.choice(stuff)
            pyautogui.typewrite(real)
            
        elif mode == 8:
            # mix emojis in text
            msg = random.choice(stuff)
            mixed = ""
            for c in msg:
                mixed += c
                if random.random() < 0.3:
                    mixed += random.choice(emoji_crap)
            print(f"[{count}] mixed: {mixed}")
            pyautogui.typewrite(mixed)
        
        pyautogui.press('enter')
        
        # random wait
        wait = random.uniform(0.5, 3.0)
        time.sleep(wait)

except KeyboardInterrupt:
    print(f"\nstopped, sent {count} msgs")
except pyautogui.FailSafeException as e:
    print(f"\nemergency stop - sent {count}")
