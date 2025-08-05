# 🛡️ Laptop Protection Capture

A Python project that captures a photo from your laptop webcam and sends it to your **Telegram** whenever you log in.  
This acts as a personal security/logging tool to keep track of login events.

---

## 🚀 Features
- 📸 Capture a snapshot from your laptop webcam  
- 🕒 Saves the photo with a timestamped filename  
- 📲 Sends the photo directly to your Telegram account  
- ⚡ Runs automatically on Windows login using Task Scheduler  

---

## 📂 Project Structure
capture-project/
├── capture.py # Main script
├── requirements.txt # Python dependencies
└── README.md # Documentation

yaml
Copy
Edit

---

## ⚙️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/capture-project.git
   cd capture-project
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Or manually:

bash
Copy
Edit
pip install opencv-python requests
🔑 Telegram Setup
Open Telegram → search for @BotFather.

Create a new bot → you’ll get a Bot Token.

Start your bot with /start.

Get your Chat ID:

Send any message to your bot.

Open in browser:

bash
Copy
Edit
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
Look for "chat":{"id":123456789} → that’s your Chat ID.

▶️ Usage
Update capture.py with your BOT_TOKEN and CHAT_ID, then run:

bash
Copy
Edit
python capture.py
A photo will be taken from the webcam

Saved locally with a timestamp

Sent to your Telegram instantly

⚡ Auto-Run on Windows Login
Open Task Scheduler (taskschd.msc).

Create a new task → Trigger = At log on.

Action = Start a program.

Program/script = path to your Python executable.

Add arguments = path to capture.py.

Now every time you log in, the script runs automatically.

📜 License
This project is licensed under the MIT License.

✨ Author
Your Name
