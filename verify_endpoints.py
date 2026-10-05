import urllib.request

endpoints = [
    '/health',
    '/api/status',
    '/api/transactions',
    '/api/ledger',
    '/api/financial-statements',
    '/api/countries',
    '/api/reconciliation',
    '/api/erp/invoices',
    '/api/erp/inventory',
    '/api/erp/payroll',
    '/api/erp/assets',
    '/api/erp/anomalies',
    '/api/advancement/db-status',
    '/api/advancement/aa-status',
    '/api/advancement/offline-status',
    '/manifest.json',
    '/sw.js'
]

all_ok = True
for ep in endpoints:
    url = f"http://127.0.0.1:8000{ep}"
    try:
        resp = urllib.request.urlopen(url)
        print(f"PASS: {ep} -> {resp.status}")
    except Exception as e:
        print(f"FAIL: {ep} -> {e}")
        all_ok = False

if all_ok:
    print("\n>>> ALL 17 ENDPOINTS TESTED AND 100% OPERATIONAL! <<<")
else:
    print("\n>>> SOME ENDPOINTS FAILED <<<")
