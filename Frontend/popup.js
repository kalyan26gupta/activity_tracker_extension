document.getElementById("bookmark").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: "bookmark", url: tabs[0].url });
  });
});

document.getElementById("reminder").addEventListener("click", () => {
  chrome.notifications.create({
    type: "basic",
    iconUrl: "icon.png",
    title: "Reminder",
    message: "This is your reminder!"
  }, (notificationId) => {
    if (chrome.runtime.lastError) {
      console.error(chrome.runtime.lastError);
    } else {
      console.log("Manual reminder notification created with ID:", notificationId);
    }
  });
});

function displayActivityLog() {
  chrome.storage.sync.get(null, (items) => {
    const logContainer = document.getElementById("activity-log");
    logContainer.innerHTML = '<h3>Activity Log</h3>';
    for (let [key, value] of Object.entries(items)) {
      logContainer.innerHTML += `<p>Tab ${key}: ${value / 1000} seconds</p>`;
    }
  });
}

displayActivityLog();
