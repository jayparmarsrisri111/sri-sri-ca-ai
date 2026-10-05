"""
Sri Sri CA AI -- Go LIVE Script
================================
Creates a public HTTPS tunnel so anyone can access the web app.
Usage: python go_live.py
"""

import sys
import os
import time

# Fix Windows console encoding
os.environ["PYTHONIOENCODING"] = "utf-8"
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

def main():
    print("=" * 65)
    print("  Sri Sri CA AI - GLOBAL LIVE DEPLOYMENT")
    print("  Making your CA Web App accessible worldwide...")
    print("=" * 65)
    print()

    try:
        from pyngrok import ngrok, conf

        conf.get_default().region = "in"

        print("[*] Starting ngrok tunnel to http://127.0.0.1:8000 ...")
        print()

        public_url = ngrok.connect(8000, "http")

        print("=" * 65)
        print("  [SUCCESS] WEB APP IS NOW LIVE!")
        print("=" * 65)
        print()
        print(f"  PUBLIC URL : {public_url}")
        print(f"  Mobile     : Open the URL above on any phone")
        print(f"  Laptop     : Open the URL above on any computer")
        print(f"  2FA PIN    : 7788")
        print()
        print("=" * 65)
        print("  SHARE THIS URL WITH ANYONE:")
        print(f"  >>> {public_url}")
        print("=" * 65)
        print()
        print("  WARNING: Keep this window open while the app is live.")
        print("  Press Ctrl+C to stop the live server.")
        print()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[*] Shutting down live tunnel...")
            ngrok.kill()
            print("[OK] Tunnel closed.")

    except ImportError:
        print("[ERROR] pyngrok not found. Run: pip install pyngrok")
        sys.exit(1)
    except Exception as e:
        error_msg = str(e)
        if "authtoken" in error_msg.lower() or "ERR_NGROK" in error_msg or "authentication" in error_msg.lower():
            print()
            print("=" * 65)
            print("  ngrok FREE ACCOUNT REQUIRED (1 minute setup)")
            print("=" * 65)
            print()
            print("  ngrok needs a free auth token. Follow these steps:")
            print()
            print("  Step 1: Go to https://dashboard.ngrok.com/signup")
            print("          (Free sign up with Google/GitHub)")
            print()
            print("  Step 2: Copy your Authtoken from Dashboard:")
            print("          https://dashboard.ngrok.com/get-started/your-authtoken")
            print()
            print("  Step 3: Run this command:")
            print("          ngrok config add-authtoken YOUR_TOKEN_HERE")
            print("     OR:")
            print("          python -c \"from pyngrok import ngrok; ngrok.set_auth_token('YOUR_TOKEN_HERE')\"")
            print()
            print("  Step 4: Run again:")
            print("          python go_live.py")
            print()
            print("=" * 65)
        else:
            print(f"[ERROR] {error_msg}")
            sys.exit(1)


if __name__ == "__main__":
    main()
