"""
Sri Sri ❤️ AI CA & Global Tax Intelligence
Standalone Autonomous SEO Scheduler & Background Liveness Keeper
Target Launch Window: 11-10-2026 between 10:51:00 and 11:30:00 IST
================================================================
This script can be executed as a background process or scheduled via
Windows Task Scheduler / cron. It continuously ensures that when 11-10-2026
between 10:51 and 11:30 arrives, the search engine pings (Google & Bing IndexNow)
are executed, and the state is permanently recorded.
"""

import os
import sys
import time
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from app.seo_auto_launcher import (
    seo_auto_launcher,
    TARGET_LAUNCH_DATETIME,
    TARGET_LAUNCH_END_DATETIME,
    TARGET_LAUNCH_FULL_LABEL
)

def run_scheduler_daemon(poll_seconds=20):
    print("=" * 75)
    print("  🚀 SRI SRI ❤️ AI CA - SEO AUTONOMOUS LAUNCH SCHEDULER")
    print(f"  Target Window : {TARGET_LAUNCH_FULL_LABEL}")
    print(f"  Poll Rate     : Every {poll_seconds} seconds")
    print("=" * 75)


    while True:
        status = seo_auto_launcher.check_and_update()
        now = datetime.now()
        
        if status.get("is_live"):
            print(f"[{now.strftime('%H:%M:%S')}] 🟢 SEO IS 100% LIVE! Auto-activated at {status.get('auto_activated_at')}")
            print(f"                     All Search Engines (Google, Bing) notified.")
            break
        else:
            cd = status.get("countdown", {}).get("formatted", "")
            print(f"[{now.strftime('%H:%M:%S')}] ⏳ Countdown active: {cd} remaining until 11-10-2026 auto-launch.")
        
        time.sleep(poll_seconds)

if __name__ == "__main__":
    poll = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    run_scheduler_daemon(poll)
