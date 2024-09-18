console.log("Background script running...");

chrome.tabs.onActivated.addListener(activeInfo => {
  console.log("Tab activated");
  chrome.tabs.get(activeInfo.tabId, tab => {
    if (tab.url) {
      console.log("Tracking website: ", tab.url);
      trackWebsite(tab.url);
    }
  });
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.url) {
    console.log("Tab updated with URL: ", changeInfo.url);
    trackWebsite(changeInfo.url);
  }
});

function trackWebsite(url) {
  chrome.storage.local.get(["websiteUsage"], result => {
    let usageData = result.websiteUsage || {};
    let domain = new URL(url).hostname;

    if (!usageData[domain]) {
      usageData[domain] = { "time_spent": 0 };
    }

    usageData[domain]["time_spent"] += 1;  // Increment time spent

    // Save the updated usage data
    chrome.storage.local.set({ "websiteUsage": usageData });
    console.log("Updated usage for:", domain, "Time spent:", usageData[domain]["time_spent"]);
  });
}
