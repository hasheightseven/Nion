# welcome to the NION
# build.py
import os

# Example: Create a simple static HTML file
os.makedirs("build", exist_ok=True)
with open("build/index.html", "w") as f:
    f.write("<html><body id='n-ion-body'>NION</h1></body></html>")
