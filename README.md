# fuckAround

## what's included

### 1. randomspam.py - spam bot
spam bot for whatsapp/discord/whatever. types random messages and chaos into any app.


**how to use:**
1. `python randomspam.py`
2. switch to target app during 5sec countdown
3. click in text box
4. watch

### 2. soundboard.py - soundboard
hotkey soundboard that plays random sound effects globally.

**how to use:**
1. put sound files in sounds/ folders (memes/, fx/, music/, misc/)
2. `python soundboard.py`
3. press hotkeys to make noise

## installation

```bash
git clone <this-repo>
cd fuckAround
pip install pyautogui pygame pynput
```

## customization

wanna change messages in spam bot? edit the `stuff` list in randomspam.py.

wanna add more sound categories? add folders and update the `folders` dict in soundboard.py.

wanna change hotkeys? edit the `keys` dict.

## warnings

- these will type/play sounds into whatever window is active
- some apps might detect spam and rate limit you
- dont blame me if you get in trouble for being an idiot with these
- be steady with it

