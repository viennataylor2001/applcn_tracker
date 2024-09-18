document.getElementById("download").addEventListener("click", function() {
    chrome.storage.local.get(["websiteUsage"], function(result) {
      let usageData = result.websiteUsage || {};
  
      // Convert data to JSON string
      let dataStr = JSON.stringify(usageData);
      
      // Create a downloadable link
      let blob = new Blob([dataStr], { type: "application/json" });
      let url = URL.createObjectURL(blob);
  
      // Trigger download
      let downloadLink = document.createElement("a");
      downloadLink.href = url;
      downloadLink.download = "website_usage.json";
      downloadLink.click();
    });
  });
  