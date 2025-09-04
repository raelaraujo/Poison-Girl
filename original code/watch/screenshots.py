from mss import mss
import datetime, os, time

def capture_screenshots():
    interval_seconds = 10
    total_screenshots = 100
    folder_name = datetime.datetime.now().strftime("%Y-%m-%d_screenshots")
    os.makedirs(folder_name, exist_ok=True)

    with mss() as sct:
        for _ in range(total_screenshots):
            timestamp = datetime.datetime.now().strftime("%H%M%S")
            filename = os.path.join(folder_name, f"screenshot_{timestamp}.jpg")
            sct.shot(output=filename)
            time.sleep(interval_seconds)
