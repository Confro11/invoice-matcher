"""
Invoice Matcher - Launcher
Spustí server a otevře prohlížeč. Entry point pro PyInstaller .exe
"""
import sys
import os
import threading
import time
import webbrowser

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
        print(f"Spouštím Invoice Matcher na {URL} ...")
        print(f"BASE_DIR: {BASE_DIR}")
        threading.Thread(target=open_browser, daemon=True).start()
        uvicorn.run("main:app", host="127.0.0.1", port=PORT, log_level="info")
    except Exception as e:
        import traceback
        print("CHYBA PRI SPUSTENI:")
        traceback.print_exc()
        input("Stiskni Enter pro zavření...")
