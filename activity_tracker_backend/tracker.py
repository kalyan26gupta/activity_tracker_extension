import time
import sqlite3
import logging
import psutil
import re
import json
from datetime import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import sqlite3

# Create the directory if it does not exist
os.makedirs('activity_tracker', exist_ok=True)

# Connect to the SQLite database
conn = sqlite3.connect('activity_tracker/activity_tracker.db')

# Setup logging
logging.basicConfig(filename='activity_tracker.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Connect to SQLite database
conn = sqlite3.connect('activity_tracker/activity_tracker.db')
c = conn.cursor()

# Create table to store activity logs
c.execute('''
CREATE TABLE IF NOT EXISTS activity_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    title TEXT,
    url TEXT,
    category TEXT,
    details TEXT
)
''')
conn.commit()

# Define categories and reminders
categories = {
    "video": ["youtube.com", "vimeo.com", "netflix.com", "hulu.com"],
    "comics": ["examplecomic.com", "webtoon.com", "mangadex.org"],
    "music": ["spotify.com", "soundcloud.com", "apple.com/music"],
    "news": ["news.com", "cnn.com", "bbc.com"],
}

# Gmail API setup
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def get_gmail_reminders(service):
    reminders = []
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
    messages = results.get('messages', [])

    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        snippet = msg['snippet']
        reminders.append(snippet)
    
    return reminders

# Function to categorize URLs based on defined categories
def categorize_url(url):
    for category, sites in categories.items():
        if any(site in url for site in sites):
            return category
    return "other"

# Function to extract relevant details from specific URLs
def extract_details(url):
    if "youtube.com" in url:
        # Extract channel and playlist from YouTube URLs
        channel_pattern = r"(?:youtube\.com\/(?:channel|user)\/|youtu\.be\/)([a-zA-Z0-9_-]+)"
        playlist_pattern = r"(?:list=)([a-zA-Z0-9_-]+)"
        channel = re.search(channel_pattern, url)
        playlist = re.search(playlist_pattern, url)

        details = {
            "channel": channel.group(1) if channel else None,
            "playlist": playlist.group(1) if playlist else None
        }
        return json.dumps(details)

    return None

# Function to log activity to the database
def log_activity(title, url):
    category = categorize_url(url)
    details = extract_details(url)
    timestamp = datetime.now().isoformat()
    c.execute("INSERT INTO activity_logs (timestamp, title, url, category, details) VALUES (?, ?, ?, ?, ?)", 
              (timestamp, title, url, category, details))
    conn.commit()

# Function to get active window title and URL
def get_active_window_info():
    active_window = None
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'chrome.exe':
            try:
                # Get window title
                win32gui = __import__('win32gui')
                hwnd = win32gui.GetForegroundWindow()
                title = win32gui.GetWindowText(hwnd)
                
                # Here we mock the URL retrieval. Replace this with actual Chrome remote debugging calls.
                url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLfW2sYtX6U5D8YbLXYvDBW4k4Rr8a3xD3"  # Mock URL

                active_window = (title, url)
                break
            except Exception as e:
                logging.error(f"Error: {e}")
                continue
    return active_window

# Main tracking loop
if __name__ == '__main__':
    logging.info("Starting activity tracking.")
    
    # Authenticate Gmail
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)

    while True:
        active_window_info = get_active_window_info()
        
        if active_window_info:
            title, url = active_window_info
            logging.info(f"Active window: {title}, URL: {url}")
            log_activity(title, url)

            # Get Gmail reminders
            reminders = get_gmail_reminders(service)
            if reminders:
                for reminder in reminders:
                    logging.info(f"Gmail Reminder: {reminder}")
        
        time.sleep(5)  # Adjust the sleep time as needed

# Close the database connection on exit
conn.close()
