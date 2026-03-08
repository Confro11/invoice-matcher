"""
Invoice Matcher - Launcher
Entry point pro PyInstaller .exe
"""
import sys
import os
import multiprocessing
import threading
import time
import webbrowser

# Nutné pro PyInstaller na Windows
multiprocessing.freeze_support()

# PyInstaller path fix
if getattr(sys, "frozen", False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

os.environ["INVOICE_MATCHER_BASE_DIR"] = BASE_DIR

PORT = 8080
URL = f"http://localhost:{PORT}"


def open_browser():
    time.sleep(2.0)
    webbrowser.open(URL)


if __name__ == "__main__":
    try:
        import uvicorn
        from main import app  # přímý import místo stringu — funguje v .exe

        print(f"Invoice Matcher běží na {URL}")
        threading.Thread(target=open_browser, daemon=True).start()
        uvicorn.run(app, host="127.0.0.1", port=PORT, log_level="info")
    except Exception:
        import traceback
        traceback.print_exc()
        input("\nStiskni Enter pro zavření...")
