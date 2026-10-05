"""
Sri Sri ❤️ AI CA & Global Tax Intelligence
One-Click Launch Script
"""

import sys
import uvicorn

# Ensure utf-8 encoding for Windows terminals
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

if __name__ == "__main__":
    print("\n" + "="*65)
    print("   [+] Sri Sri ❤️ AI CA & Global Tax Intelligence System")
    print("   [+] Autonomous Accounting, Multi-Country Tax & Legal Copilot")
    print("="*65)
    print("\nStarting Web Server on http://127.0.0.1:8000 ...")
    print("Open your browser at: http://127.0.0.1:8000")
    print("="*65 + "\n")
    
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=False)
