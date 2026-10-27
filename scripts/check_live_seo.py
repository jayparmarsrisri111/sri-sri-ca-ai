import urllib.request
import re

url = "https://srisricaai.netlify.app/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"})

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode("utf-8", errors="replace")
        print("HTTP Status:", resp.status)
        print("HTML Byte Count:", len(html))
        
        # Check SEO signals
        meta_desc = bool(re.search(r'name=["\']description["\']', html))
        canonical = bool(re.search(r'rel=["\']canonical["\']', html))
        og_title = bool(re.search(r'property=["\']og:title["\']', html))
        json_ld = bool(re.search(r'application/ld\+json', html))
        
        print("Meta Description Present:", meta_desc)
        print("Canonical Link Present:", canonical)
        print("Open Graph Title Present:", og_title)
        print("JSON-LD Schema Present:", json_ld)

        # Print the head portion
        head_match = re.search(r'<head>(.*?)</head>', html, re.DOTALL)
        if head_match:
            head_content = head_match.group(1).strip()
            print("\n--- FIRST 800 CHARS OF HEAD ---")
            print(head_content[:800])
except Exception as e:
    print("Error:", e)
