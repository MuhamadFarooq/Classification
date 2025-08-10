import os, sys, subprocess

# Make dataset dir
os.makedirs("dataset", exist_ok=True)

# Install gdown if needed
try:
    import gdown  # noqa
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown"])

# Public Google Drive folder ID
FOLDER_ID = "1dZvL1gi5QLwOGrfdn9XEsi4EnXx535bD"
url = f"https://drive.google.com/drive/folders/{FOLDER_ID}"

# Download entire folder into dataset/
exit_code = subprocess.call(["gdown", "--folder", url, "-O", "dataset"])
if exit_code != 0:
    print("\n Download failed. If you're in an environment without pip/system access, "
          "run this in Colab or locally.\n")
else:
    print("\n Dataset downloaded into dataset/\n")
