Got it! Here’s a concise guide on how to set up and run your activity tracker project without including code:

---

# Activity Tracker Project Setup and Run Guide

## Overview
The Activity Tracker is a tool designed to monitor your activities across different platforms, including your browser and Gmail. It categorizes reminders and tracks entertainment content.

## Prerequisites
- Basic knowledge of Git and GitHub
- Python 3.x installed
- Google Chrome installed
- Access to Gmail for reminders

## Step-by-Step Setup

### 1. Clone the Repository
1. Open your terminal or command prompt.
2. Clone the project repository:
   ```bash
   git clone https://github.com/yourusername/activity_tracker.git
   ```
3. Navigate to the project directory:
   ```bash
   cd activity_tracker
   ```

### 2. Create a Virtual Environment
1. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### 3. Install Dependencies
Install the required libraries by running:
```bash
pip install -r requirements.txt
```

### 4. Set Up Gmail API
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the Gmail API for the project.
4. Create credentials (OAuth 2.0 Client IDs) and download the `credentials.json` file.
5. Place the `credentials.json` file in the project directory.

### 5. Configure the Database
1. Ensure the database file path is correctly set in the code (usually in the main Python file).
2. The application will create a database file if it doesn’t already exist.

### 6. Run the Backend
1. Start the backend script:
   ```bash
   python tracker.py
   ```
2. This will initialize the tracking process.

### 7. Load the Chrome Extension
1. Open Google Chrome and navigate to `chrome://extensions`.
2. Enable "Developer mode" in the top right corner.
3. Click "Load unpacked" and select the `frontend` directory from your project.

### 8. Usage
- The tracker will start monitoring your activities.
- For Gmail, it will fetch reminders based on your settings.
- Activities will be logged in the database for reference.

