chrome.runtime.onInstalled.addListener(() => {
  console.log("Activity Tracker installed.");
});

chrome.tabs.onActivated.addListener((activeInfo) => {
  chrome.tabs.get(activeInfo.tabId, (tab) => {
      console.log(`Active tab: ${tab.title}, URL: ${tab.url}`);
  });
});
