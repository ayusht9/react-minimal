import os
import subprocess
import json

PROJECT_NAME = input("Enter your project/folder name: ").strip()

if not PROJECT_NAME:
    print("Error: Project name cannot be empty.")
    exit(1)

if os.path.exists(PROJECT_NAME):
    print(f"Error: Folder '{PROJECT_NAME}' already exists.")
    exit(1)

os.makedirs(PROJECT_NAME)
os.chdir(PROJECT_NAME)

subprocess.run(["npm.cmd", "init", "-y"], check=True)
subprocess.run(["npm.cmd", "install", "react", "react-dom"], check=True)
subprocess.run(["npm.cmd", "install", "--save-dev", "vite", "@vitejs/plugin-react"], check=True)

os.makedirs("src", exist_ok=True)

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>React App</title>
</head>
<body>
  <div id="root"></div>
  <script type="module" src="./src/main.jsx"></script>
</body>
</html>
"""
with open("index.html", "w") as f:
    f.write(index_html)

app_jsx = """import React from "react";

function App() {
  return (
    <div>
      <h1>Hello, React!</h1>
    </div>
  );
}

export default App;
"""
with open("src/App.jsx", "w") as f:
    f.write(app_jsx)

main_jsx = """import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
"""
with open("src/main.jsx", "w") as f:
    f.write(main_jsx)

vite_config = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()]
})
"""
with open("vite.config.js", "w") as f:
    f.write(vite_config)

with open("package.json") as f:
    package = json.load(f)

if "scripts" not in package:
    package["scripts"] = {}

package["scripts"]["dev"] = "vite"

with open("package.json", "w") as f:
    json.dump(package, f, indent=2)

print(f"React + Vite setup complete! Folder: '{PROJECT_NAME}'")
print("Run 'npm run dev' inside this folder to start the development server at http://localhost:5173")
