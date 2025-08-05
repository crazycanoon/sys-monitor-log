import cv2
import datetime
import requests

# === CONFIG ===
BOT_TOKEN = "7668396361:AAG0F-SjQFXr9gdJp9nYhiIjfVMjCUZldic"   # from BotFather
CHAT_ID = "7045963417"       # your Telegram chat ID

def capture_and_send():
    # Open webcam
    cap = cv2.VideoCapture(0)
    status, photo = cap.read()
    
    if status:
        filename = f"photo_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, photo)
        print(f"[INFO] Saved photo: {filename}")
        
        # Upload to Telegram
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        with open(filename, "rb") as img:
            files = {"photo": img}
            data = {"chat_id": CHAT_ID, "caption": "📸 Laptop login capture"}
            response = requests.post(url, data=data, files=files)
        
        if response.status_code == 200:
            print("[INFO] Photo sent successfully to Telegram!")
        else:
            print(f"[ERROR] Failed to send photo: {response.text}")
    else:
        print("[ERROR] Failed to capture photo")

    cap.release()

if __name__ == "__main__":
    capture_and_send()
