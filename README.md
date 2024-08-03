To start Chrome with remote debugging enabled, follow these steps:
Step 1: Close All Running Instances of Chrome
Make sure all instances of Chrome are closed before proceeding.

Step 2: Create a New User Data Directory
This will allow Chrome to run with a fresh profile, which is necessary for debugging.

Create a New Directory:
Open File Explorer and create a new folder on your computer, e.g., C:\selenum\ChromeProfile.
Step 3: Open Command Prompt
Press Win + R, type cmd, and hit Enter to open the Command Prompfwddwwt.
Step 4: Start Chrom

e with Remote Debugging
In the Command Prompt, type the following command to start Chrome with remote debugging enabled:
bash
Copy code
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Selenum\ChromeProfile"
Make sure to adjust the path to chrome.exe if Chrome is installed in a different directory.
Step 5: Verify Remote Debugging is Active
Open a web browser and go to http://localhost:9222.
You should see a page listing all open tabs in Chrome, indicating that remote debugging is enabled.
Step 6: Run Your Python Script
Now, you can run your Python script (the activity tracker) in a separate terminal or command prompt:
bash
Copy code
python tracker.py
Summary
This setup will allow your Python script to connect to the Chrome instance running with remote debugging, enabling you to track the active tab's URL. Make sure to keep both Chrome and your script running to track your activities properly. If you encounter any issues, feel free to ask for further assistance!






