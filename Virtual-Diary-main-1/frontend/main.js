const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow () {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true, // only if needed
      contextIsolation: false
    }
  });

  win.loadFile(path.join(__dirname, 'index.html')); // Adjust path if necessary
  // win.webContents.openDevTools(); // Commented out to prevent dev tools from opening
}

app.whenReady().then(() => {
  createWindow();
});