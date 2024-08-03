chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "getURL") {
    chrome.runtime.sendMessage({ action: "getURL" }, (response) => {
      sendResponse(response);
    });
    return true; // Keep the message channel open for sendResponse
  }
});
