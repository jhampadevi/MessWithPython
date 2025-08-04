import pyautogui
import time
import random
import threading
from pynput import keyboard, mouse

# disable failsafe for now
pyautogui.FAILSAFE = False

# click settings
click_active = False
click_pos = None
pattern_mode = 1
click_speed = 1.0

# patterns:
# 1 = single clicks
# 2 = double clicks  
# 3 = rapid fire
# 4 = random pattern
# 5 = position sequence

click_positions = []  # for multi-position clicking

def get_mouse_pos():
    # get current mouse position
    x, y = pyautogui.position()
    return x, y

def single_click():
    # normal single click
    if click_pos:
        pyautogui.click(click_pos[0], click_pos[1])
    else:
        pyautogui.click()

def double_click():
    # double click
    if click_pos:
        pyautogui.doubleClick(click_pos[0], click_pos[1])
    else:
        pyautogui.doubleClick()

def rapid_clicks():
    # 3-5 rapid clicks
    num_clicks = random.randint(3, 5)
    for _ in range(num_clicks):
        if click_pos:
            pyautogui.click(click_pos[0], click_pos[1])
        else:
            pyautogui.click()
        time.sleep(0.05)  # small delay between rapid clicks

def random_pattern():
    # random click pattern
    choice = random.randint(1, 3)
    if choice == 1:
        single_click()
    elif choice == 2:
        double_click()
    else:
        rapid_clicks()

def position_sequence():
    # click through saved positions
    if click_positions:
        for pos in click_positions:
            if not click_active:  # stop if disabled
                break
            pyautogui.click(pos[0], pos[1])
            time.sleep(0.2)  # small delay between positions

def auto_clicker():
    # main clicking loop
    global click_active
    
    patterns = {
        1: single_click,
        2: double_click,
        3: rapid_clicks,
        4: random_pattern,
        5: position_sequence
    }
    
    while click_active:
        if pattern_mode in patterns:
            patterns[pattern_mode]()
        
        # wait based on speed setting
        time.sleep(click_speed)

def start_clicking():
    # start auto clicking
    global click_active
    if not click_active:
        click_active = True
        print(f"started clicking - pattern {pattern_mode}, speed {click_speed}s")
        if click_pos:
            print(f"target position: {click_pos}")
        
        # start in background thread
        t = threading.Thread(target=auto_clicker)
        t.daemon = True
        t.start()

def stop_clicking():
    # stop auto clicking
    global click_active
    click_active = False
    print("stopped clicking")

def set_click_position():
    # set click position to current mouse location
    global click_pos
    click_pos = get_mouse_pos()
    print(f"click position set to: {click_pos}")

def add_position_to_sequence():
    # add current mouse pos to position sequence
    pos = get_mouse_pos()
    click_positions.append(pos)
    print(f"added position {len(click_positions)}: {pos}")

def clear_positions():
    # clear position sequence
    global click_positions
    click_positions = []
    print("cleared position sequence")

def change_pattern(new_pattern):
    # change click pattern
    global pattern_mode
    pattern_mode = new_pattern
    patterns = {
        1: "single clicks",
        2: "double clicks", 
        3: "rapid fire",
        4: "random pattern",
        5: "position sequence"
    }
    print(f"pattern changed to: {patterns.get(new_pattern, 'unknown')}")

def change_speed(new_speed):
    # change click speed
    global click_speed
    click_speed = new_speed
    print(f"click speed changed to: {new_speed}s")

def handle_key(key):
    # handle keyboard shortcuts
    global click_active
    
    try:
        k = key.char.lower()
        
        if k == 's':  # start/stop
            if click_active:
                stop_clicking()
            else:
                start_clicking()
        
        elif k == 'p':  # set position
            set_click_position()
        
        elif k == 'a':  # add to sequence
            add_position_to_sequence()
        
        elif k == 'c':  # clear sequence
            clear_positions()
        
        elif k in '12345':  # change pattern
            change_pattern(int(k))
        
        elif k == 'q':  # faster
            change_speed(max(0.1, click_speed - 0.2))
        
        elif k == 'e':  # slower
            change_speed(click_speed + 0.2)
            
    except AttributeError:
        # special keys
        if key == keyboard.Key.esc:
            stop_clicking()
            print("bye!")
            return False

def show_help():
    print("\n=== AUTO CLICKER ===")
    print("controls:")
    print("s = start/stop clicking")
    print("p = set click position (current mouse location)")
    print("a = add position to sequence")
    print("c = clear position sequence")
    print("1-5 = change pattern:")
    print("  1 = single clicks")
    print("  2 = double clicks")
    print("  3 = rapid fire")
    print("  4 = random pattern")
    print("  5 = position sequence")
    print("q = faster clicking")
    print("e = slower clicking")
    print("esc = quit")
    print("\ncurrent settings:")
    print(f"pattern: {pattern_mode}")
    print(f"speed: {click_speed}s")
    print(f"position: {click_pos}")
    print(f"sequence positions: {len(click_positions)}")

def main():
    print("auto clicker v1.0")
    show_help()
    
    print("\nready! move mouse and press 'p' to set click position")
    print("then press 's' to start clicking")
    
    # listen for keys
    with keyboard.Listener(on_press=handle_key) as listener:
        listener.join()

if __name__ == "__main__":
    main()
