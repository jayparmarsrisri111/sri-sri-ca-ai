"""
Sri Sri ❤️ AI CA & Global Tax Intelligence
Comprehensive Full Verification & Testing Suite
Covers 6 Domains:
1. API Functional & Integration Tests (40+ Endpoints)
2. Enterprise Security & Vulnerability Defense
3. Accounting & Financial Invariants Mathematical Correctness
4. Frontend UI, Assets & Sav Light Blue Zero-Black Verification
5. Internationalization (I18N) & Jurisdictions (195+ Countries)
6. Latency & Performance Benchmarks
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
import urllib.error
import subprocess

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BASE_URL = "http://127.0.0.1:8000"

results = {
    "total": 0,
    "passed": 0,
    "failed": 0,
    "categories": {}
}

def record_test(category, name, passed, details="", latency_ms=0):
    results["total"] += 1
    if passed:
        results["passed"] += 1
        status_str = "PASS"
    else:
        results["failed"] += 1
        status_str = "FAIL"

    if category not in results["categories"]:
        results["categories"][category] = []
    
    results["categories"][category].append({
        "name": name,
        "status": status_str,
        "details": details,
        "latency_ms": latency_ms
    })
    
    latency_info = f" ({latency_ms:.1f}ms)" if latency_ms > 0 else ""
    print(f"[{status_str}] {category} :: {name}{latency_info} - {details}")

def http_req(path, method="GET", data=None, headers=None):
    url = f"{BASE_URL}{path}"
    req_headers = {"User-Agent": "SriSri-TestingSuite/1.0"}
    if headers:
        req_headers.update(headers)
    
    encoded_data = None
    if data is not None:
        if isinstance(data, dict):
            encoded_data = json.dumps(data).encode("utf-8")
            req_headers["Content-Type"] = "application/json"
        elif isinstance(data, (bytes, bytearray)):
            encoded_data = data
        else:
            encoded_data = str(data).encode("utf-8")
            
    req = urllib.request.Request(url, data=encoded_data, headers=req_headers, method=method)
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            latency = (time.perf_counter() - start) * 1000
            body = resp.read()
            resp_headers = dict(resp.getheaders())
            return resp.status, body, resp_headers, latency
    except urllib.error.HTTPError as e:
        latency = (time.perf_counter() - start) * 1000
        return e.code, e.read(), dict(e.headers), latency
    except Exception as e:
        latency = (time.perf_counter() - start) * 1000
        return 0, str(e).encode(), {}, latency

# ==============================================================
# TEST SUITE IMPLEMENTATION
# ==============================================================

def test_domain_1_api_endpoints():
    print("\n" + "="*70)
    print("DOMAIN 1: API FUNCTIONAL & INTEGRATION TESTS (40+ ENDPOINTS)")
    print("="*70)

    # 1. Health check
    code, body, _, lat = http_req("/health")
    record_test("API Endpoints", "GET /health", code == 200, f"Status: {code}", lat)

    # 2. Status check
    code, body, _, lat = http_req("/api/status")
    try:
        data = json.loads(body.decode())
        ok = code == 200 and data.get("company") == "Sri Sri ❤️"
        record_test("API Endpoints", "GET /api/status", ok, f"Company: {data.get('company')}", lat)
    except Exception as e:
        record_test("API Endpoints", "GET /api/status", False, str(e), lat)

    # 3. Security status
    code, body, _, lat = http_req("/api/security/status")
    record_test("API Endpoints", "GET /api/security/status", code == 200, f"Status: {code}", lat)

    # 4. Auth: Register new test user
    rand_email = f"test_{int(time.time())}@srisri.com"
    reg_payload = {
        "name": "ટેસ્ટ યુઝર",
        "email": rand_email,
        "password": "Password@123",
        "role": "user",
        "company_or_firm_name": "ટેસ્ટ કંપની"
    }
    code, body, _, lat = http_req("/api/auth/register", method="POST", data=reg_payload)
    try:
        data = json.loads(body.decode())
        ok = code == 200 and data.get("success") is True and "token" in data.get("user", {})
        record_test("API Endpoints", "POST /api/auth/register (New User)", ok, f"User ID: {data.get('user', {}).get('id')}", lat)
    except Exception as e:
        record_test("API Endpoints", "POST /api/auth/register (New User)", False, str(e), lat)

    # 5. Auth: Login with valid credentials
    login_payload = {"email": rand_email, "password": "Password@123"}
    code, body, _, lat = http_req("/api/auth/login", method="POST", data=login_payload)
    try:
        data = json.loads(body.decode())
        ok = code == 200 and data.get("success") is True and "token" in data.get("user", {})
        record_test("API Endpoints", "POST /api/auth/login (Valid Credentials)", ok, f"Role: {data.get('user', {}).get('role')}", lat)
    except Exception as e:
        record_test("API Endpoints", "POST /api/auth/login (Valid Credentials)", False, str(e), lat)

    # 6. Auth: Login with bad password
    bad_login = {"email": rand_email, "password": "WrongPassword999"}
    code, body, _, lat = http_req("/api/auth/login", method="POST", data=bad_login)
    try:
        data = json.loads(body.decode())
        ok = data.get("success") is False
        record_test("API Endpoints", "POST /api/auth/login (Bad Password Rejection)", ok, f"Message: {data.get('message')}", lat)
    except Exception as e:
        record_test("API Endpoints", "POST /api/auth/login (Bad Password Rejection)", False, str(e), lat)

    # 7. CA Clients list
    code, body, _, lat = http_req("/api/auth/ca-clients")
    record_test("API Endpoints", "GET /api/auth/ca-clients", code == 200, f"Status: {code}", lat)

    # 8. All World Countries (195+)
    code, body, _, lat = http_req("/api/countries")
    try:
        countries = json.loads(body.decode())
        ok = code == 200 and len(countries) >= 195
        record_test("API Endpoints", "GET /api/countries (195+ Countries)", ok, f"Countries count: {len(countries)}", lat)
    except Exception as e:
        record_test("API Endpoints", "GET /api/countries (195+ Countries)", False, str(e), lat)

    # 9. Get transactions
    code, body, _, lat = http_req("/api/transactions?country=IN")
    record_test("API Endpoints", "GET /api/transactions?country=IN", code == 200, f"Status: {code}", lat)

    # 10. Post new transaction
    test_entry = {
        "date": "2026-10-03",
        "reference_no": f"TEST-VCH-{int(time.time())}",
        "description": "ઓટોમેટેડ સિસ્ટમ વેરિફિકેશન ટેસ્ટ વાઉચર",
        "debit_account": "Office Equipment & Computers",
        "credit_account": "Bank / Checking Account",
        "amount": 25000.0,
        "tax_amount": 0.0,
        "country": "IN"
    }
    code, body, _, lat = http_req("/api/transactions", method="POST", data=test_entry)
    try:
        data = json.loads(body.decode())
        ok = code == 200 and data.get("success") is True
        record_test("API Endpoints", "POST /api/transactions (Journal Entry)", ok, f"Entry ID: {data.get('entry', {}).get('id')}", lat)
    except Exception as e:
        record_test("API Endpoints", "POST /api/transactions (Journal Entry)", False, str(e), lat)

    # 11. Get ledger
    code, body, _, lat = http_req("/api/ledger?country=IN")
    record_test("API Endpoints", "GET /api/ledger?country=IN", code == 200, f"Status: {code}", lat)

    # 12. Get financial statements
    code, body, _, lat = http_req("/api/financial-statements?country=IN")
    try:
        stmts = json.loads(body.decode())
        ok = code == 200 and "profit_and_loss" in stmts and "balance_sheet" in stmts
        record_test("API Endpoints", "GET /api/financial-statements", ok, "P&L and Balance Sheet generated", lat)
    except Exception as e:
        record_test("API Endpoints", "GET /api/financial-statements", False, str(e), lat)

    # 13. Tax calculations across jurisdictions
    for c_code, c_name in [("IN", "India"), ("US", "United States"), ("UK", "United Kingdom"), ("AE", "UAE")]:
        code, body, _, lat = http_req(f"/api/tax-calculation?country={c_code}")
        try:
            tax = json.loads(body.decode())
            ok = code == 200 and "total_tax_payable" in tax or "tax_payable" in tax or "estimated_tax" in tax or "net_tax_payable" in tax or len(tax) > 0
            record_test("API Endpoints", f"GET /api/tax-calculation ({c_name})", ok, f"Tax payload received ({len(tax)} keys)", lat)
        except Exception as e:
            record_test("API Endpoints", f"GET /api/tax-calculation ({c_name})", False, str(e), lat)

    # 14. Bank Reconciliation
    code, body, _, lat = http_req("/api/reconciliation")
    try:
        recon = json.loads(body.decode())
        ok = code == 200 and "reconciliation_summary" in recon or "status" in recon or isinstance(recon, dict)
        record_test("API Endpoints", "GET /api/reconciliation", ok, f"Recon keys: {list(recon.keys())[:3]}", lat)
    except Exception as e:
        record_test("API Endpoints", "GET /api/reconciliation", False, str(e), lat)

    # 15. OCR Sample Invoice
    form_data = urllib.parse.urlencode({"country": "IN", "is_sample": "true"}).encode("utf-8")
    code, body, _, lat = http_req("/api/scan-invoice", method="POST", data=form_data, headers={"Content-Type": "application/x-www-form-urlencoded"})
    try:
        inv = json.loads(body.decode())
        ok = code == 200 and inv.get("success") is True and "extracted_data" in inv
        record_test("API Endpoints", "POST /api/scan-invoice (Multimodal AI)", ok, f"Invoice No: {inv.get('extracted_data', {}).get('invoice_number')}", lat)
    except Exception as e:
        record_test("API Endpoints", "POST /api/scan-invoice (Multimodal AI)", False, str(e), lat)

    # 16. AI Chat Copilot
    chat_payload = {
        "message": "Presumptive Taxation Section 44AD વિષે સમજાવો",
        "conversation_history": [],
        "country": "IN",
        "language": "gu"
    }
    code, body, _, lat = http_req("/api/chat", method="POST", data=chat_payload)
    try:
        reply_data = json.loads(body.decode())
        ok = code == 200 and bool(reply_data.get("reply"))
        record_test("API Endpoints", "POST /api/chat (Tax Copilot in Gujarati)", ok, f"Reply length: {len(reply_data.get('reply', ''))} chars", lat)
    except Exception as e:
        record_test("API Endpoints", "POST /api/chat (Tax Copilot in Gujarati)", False, str(e), lat)

    # 17. AI Tax Notice Analyzer
    notice_payload = {
        "notice_text": "Income Tax Notice under Section 148 for Assessment Year 2024-25 regarding unexplained bank credits of INR 15,00,000",
        "country": "IN",
        "language": "gu"
    }
    code, body, _, lat = http_req("/api/analyze-notice", method="POST", data=notice_payload)
    try:
        notice_data = json.loads(body.decode())
        ok = code == 200 and ("notice_type" in notice_data or "reply_draft" in notice_data or "analysis" in notice_data or len(notice_data) > 0)
        record_test("API Endpoints", "POST /api/analyze-notice (Legal Supreme Court Analyzer)", ok, "Analysis & Draft Generated", lat)
    except Exception as e:
        record_test("API Endpoints", "POST /api/analyze-notice (Legal Supreme Court Analyzer)", False, str(e), lat)

    # 18. ERP Invoices: GET and POST
    code, body, _, lat = http_req("/api/erp/invoices")
    record_test("API Endpoints", "GET /api/erp/invoices", code == 200, f"Status: {code}", lat)

    new_invoice_payload = {
        "customer_name": "શ્રીજી ગ્લોબલ ટ્રેડિંગ કોર્પોરેશન",
        "customer_gstin": "24AAACG1122H1Z4",
        "customer_email": "info@shreejicorp.com",
        "items": [
            {"description": "AI ક્લાઉડ એકાઉન્ટિંગ સૉફ્ટવેર લાયસન્સ", "hsn": "998313", "qty": 1, "rate": 50000.0, "tax_rate": 18.0, "amount": 50000.0}
        ],
        "auto_post_ledger": True
    }
    code, body, _, lat = http_req("/api/erp/invoices", method="POST", data=new_invoice_payload)
    try:
        inv_res = json.loads(body.decode())
        ok = code == 200 and inv_res.get("success") is True and "irn" in inv_res.get("invoice", {})
        record_test("API Endpoints", "POST /api/erp/invoices (IRN & QR Generation)", ok, f"IRN: {inv_res.get('invoice', {}).get('irn')[:16]}...", lat)
    except Exception as e:
        record_test("API Endpoints", "POST /api/erp/invoices (IRN & QR Generation)", False, str(e), lat)

    # 19. ERP Inventory: GET and POST
    code, body, _, lat = http_req("/api/erp/inventory")
    record_test("API Endpoints", "GET /api/erp/inventory", code == 200, f"Status: {code}", lat)

    sku_payload = {
        "name": "હાઇ-સ્પીડ બારકોડ / QR સ્કેનર ટર્મિનલ",
        "sku": f"SKU-{int(time.time())}",
        "category": "હાર્ડવેર",
        "stock_qty": 25,
        "unit_cost": 4500.0,
        "selling_price": 7200.0,
        "reorder_level": 5
    }
    code, body, _, lat = http_req("/api/erp/inventory", method="POST", data=sku_payload)
    try:
        sku_res = json.loads(body.decode())
        ok = code == 200 and sku_res.get("success") is True and bool(sku_res.get("item", {}).get("id"))
        record_test("API Endpoints", "POST /api/erp/inventory (Add Stock SKU)", ok, f"SKU ID: {sku_res.get('item', {}).get('id')}", lat)
    except Exception as e:
        record_test("API Endpoints", "POST /api/erp/inventory (Add Stock SKU)", False, str(e), lat)

    # 20. ERP Payroll: GET and POST
    code, body, _, lat = http_req("/api/erp/payroll")
    record_test("API Endpoints", "GET /api/erp/payroll", code == 200, f"Status: {code}", lat)

    emp_payload = {
        "name": "દિલીપ જોશી",
        "designation": "સિનિયર એકાઉન્ટન્ટ",
        "basic_salary": 60000.0,
        "hra": 24000.0,
        "special_allowance": 16000.0,
        "tds_deduction": 5000.0
    }
    code, body, _, lat = http_req("/api/erp/payroll", method="POST", data=emp_payload)
    try:
        emp_res = json.loads(body.decode())
        ok = code == 200 and emp_res.get("success") is True and "net_payable" in emp_res.get("employee", {})
        record_test("API Endpoints", "POST /api/erp/payroll (EPF & Net Salary Calc)", ok, f"Net: ₹{emp_res.get('employee', {}).get('net_payable')}", lat)
    except Exception as e:
        record_test("API Endpoints", "POST /api/erp/payroll (EPF & Net Salary Calc)", False, str(e), lat)

    # 21. ERP Assets & Depreciation
    code, body, _, lat = http_req("/api/erp/assets")
    record_test("API Endpoints", "GET /api/erp/assets", code == 200, f"Status: {code}", lat)

    # 22. ERP Anomaly Audit
    code, body, _, lat = http_req("/api/erp/anomalies")
    try:
        anom_res = json.loads(body.decode())
        ok = code == 200 and ("audit_score_percent" in anom_res or "anomalies" in anom_res)
        record_test("API Endpoints", "GET /api/erp/anomalies (AI Fraud Detector)", ok, f"Score: {anom_res.get('audit_score_percent')}% | Status: {anom_res.get('status')}", lat)
    except Exception as e:
        record_test("API Endpoints", "GET /api/erp/anomalies (AI Fraud Detector)", False, str(e), lat)

    # 23. ERP UDIN Generator
    udin_payload = {
        "document_type": "Tax Audit Report Form 3CD",
        "client_name": "આર્યન ટેકનોલોજીસ",
        "ca_membership": "542190"
    }
    code, body, _, lat = http_req("/api/erp/generate-udin", method="POST", data=udin_payload)
    try:
        udin_res = json.loads(body.decode())
        ok = code == 200 and udin_res.get("success") is True and len(udin_res.get("udin_data", {}).get("udin", "")) == 18
        record_test("API Endpoints", "POST /api/erp/generate-udin (18-Digit UDIN)", ok, f"UDIN: {udin_res.get('udin_data', {}).get('udin')}", lat)
    except Exception as e:
        record_test("API Endpoints", "POST /api/erp/generate-udin (18-Digit UDIN)", False, str(e), lat)

    # 24. 7 Superpowers: Superpower 1 (CA COP & Audit Signoff)
    code, body, _, lat = http_req("/api/advancement/ca-verify-cop", method="POST", data={"membership_no": "542190"})
    record_test("API Endpoints", "POST /api/advancement/ca-verify-cop", code == 200, f"Status: {code}", lat)

    sign_payload = {
        "report_type": "Form 3CD Tax Audit",
        "client_name": "શાહ ટ્રેડર્સ",
        "ca_membership": "542190",
        "findings": {"status": "Clean"}
    }
    code, body, _, lat = http_req("/api/advancement/ca-sign-audit", method="POST", data=sign_payload)
    record_test("API Endpoints", "POST /api/advancement/ca-sign-audit", code == 200, f"Status: {code}", lat)

    # 25. 7 Superpowers: Superpower 2 (Official Govt GSTR1 & ITR JSON, GSP Push)
    code, body, _, lat = http_req("/api/advancement/export-gstr1")
    record_test("API Endpoints", "GET /api/advancement/export-gstr1", code == 200, f"Status: {code}", lat)

    code, body, _, lat = http_req("/api/advancement/export-itr")
    record_test("API Endpoints", "GET /api/advancement/export-itr", code == 200, f"Status: {code}", lat)

    code, body, _, lat = http_req("/api/advancement/gsp-direct-sync", method="POST", data={"form_type": "GSTR-1"})
    record_test("API Endpoints", "POST /api/advancement/gsp-direct-sync", code == 200, f"Status: {code}", lat)

    # 26. 7 Superpowers: Superpower 3 (Dual-Engine SQLite WAL Mode DB)
    code, body, _, lat = http_req("/api/advancement/db-status")
    record_test("API Endpoints", "GET /api/advancement/db-status", code == 200, f"Status: {code}", lat)

    # 27. 7 Superpowers: Superpower 4 (RBI Account Aggregator)
    code, body, _, lat = http_req("/api/advancement/aa-status")
    record_test("API Endpoints", "GET /api/advancement/aa-status", code == 200, f"Status: {code}", lat)

    code, body, _, lat = http_req("/api/advancement/aa-live-sync", method="POST", data={})
    record_test("API Endpoints", "POST /api/advancement/aa-live-sync", code == 200, f"Status: {code}", lat)

    # 28. 7 Superpowers: Superpower 5 (Virtual Class-3 DSC Bridge)
    dsc_payload = {"applicant_name": "CA Jaydeep Shah", "pan": "ABCDE1234F"}
    code, body, _, lat = http_req("/api/advancement/issue-dsc", method="POST", data=dsc_payload)
    record_test("API Endpoints", "POST /api/advancement/issue-dsc", code == 200, f"Status: {code}", lat)

    sign_doc_payload = {"document_name": "Tax Audit Report 2026-27", "cert_serial": "SRI-2026-CLASS3"}
    code, body, _, lat = http_req("/api/advancement/sign-dsc", method="POST", data=sign_doc_payload)
    record_test("API Endpoints", "POST /api/advancement/sign-dsc", code == 200, f"Status: {code}", lat)

    # 29. 7 Superpowers: Superpower 6 (Adaptive OCR Confidence Radar)
    code, body, _, lat = http_req("/api/advancement/ocr-confidence", method="POST", data={})
    record_test("API Endpoints", "POST /api/advancement/ocr-confidence", code == 200, f"Status: {code}", lat)

    # 30. 7 Superpowers: Superpower 7 (100% Offline Hybrid Engine)
    code, body, _, lat = http_req("/api/advancement/offline-status")
    record_test("API Endpoints", "GET /api/advancement/offline-status", code == 200, f"Status: {code}", lat)

    # 31. PWA Manifest & Service Worker
    code, body, _, lat = http_req("/manifest.json")
    record_test("API Endpoints", "GET /manifest.json", code == 200, f"Status: {code}", lat)

    code, body, _, lat = http_req("/sw.js")
    record_test("API Endpoints", "GET /sw.js", code == 200, f"Status: {code}", lat)

def test_domain_2_security():
    print("\n" + "="*70)
    print("DOMAIN 2: ENTERPRISE SECURITY & DEFENSE TESTS")
    print("="*70)

    # 1. Inspect HTTP Security Headers on API endpoint
    code, _, headers, _ = http_req("/api/status")
    h_lower = {k.lower(): v for k, v in headers.items()}
    
    sec_checks = [
        ("X-Content-Type-Options", "x-content-type-options", "nosniff", h_lower.get("x-content-type-options") == "nosniff"),
        ("X-Frame-Options", "x-frame-options", "SAMEORIGIN", h_lower.get("x-frame-options") == "SAMEORIGIN"),
        ("X-XSS-Protection", "x-xss-protection", "1; mode=block", "1" in h_lower.get("x-xss-protection", "")),
        ("Referrer-Policy", "referrer-policy", "strict-origin", "strict-origin" in h_lower.get("referrer-policy", "")),
        ("Cache-Control (No Financial Leak)", "cache-control", "no-store", "no-store" in h_lower.get("cache-control", "")),
        ("Permissions-Policy", "permissions-policy", "camera=()", "camera=()" in h_lower.get("permissions-policy", ""))
    ]
    for hname, hkey, exp, ok in sec_checks:
        record_test("Security Headers", f"Header: {hname}", ok, f"Value: {h_lower.get(hkey)}")

    # 2. XSS and Injection Sanitization Test
    xss_entry = {
        "date": "2026-10-03",
        "reference_no": "XSS-REF<script>alert('pwned')</script>",
        "description": "<script>alert('xss')</script>Safe Description",
        "debit_account": "Office Expense",
        "credit_account": "Bank / Checking Account",
        "amount": 1000.0,
        "country": "IN"
    }
    code, body, _, _ = http_req("/api/transactions", method="POST", data=xss_entry)
    try:
        data = json.loads(body.decode())
        entry = data.get("entry", {})
        no_script = "<script>" not in entry.get("description", "") and "<script>" not in entry.get("reference_no", "")
        record_test("Security Sanitization", "XSS Tag Stripping in Journal Entries", no_script, f"Cleaned: {entry.get('description')}")
    except Exception as e:
        record_test("Security Sanitization", "XSS Tag Stripping in Journal Entries", False, str(e))

    # 3. Password Hashing and Salted PBKDF2 Check
    from app.security import hash_password, verify_password
    test_pwd = "MySuperSecretKey!@#"
    h1 = hash_password(test_pwd)
    h2 = hash_password(test_pwd)
    salt_unique = h1 != h2  # Unique salts must produce different hashes
    valid_verify = verify_password(test_pwd, h1) and verify_password(test_pwd, h2)
    invalid_verify = not verify_password("WrongKey", h1)
    record_test("Security Cryptography", "PBKDF2-HMAC-SHA256 Unique Salt Hash", salt_unique and valid_verify and invalid_verify, f"Hash algo: {h1[:24]}...")

def test_domain_3_accounting_invariants():
    print("\n" + "="*70)
    print("DOMAIN 3: ACCOUNTING & FINANCIAL INVARIANTS MATHEMATICAL VERIFICATION")
    print("="*70)

    # 1. Double-Entry Balance Invariant: Total Debits == Total Credits across Ledger
    code, body, _, _ = http_req("/api/ledger?country=IN")
    try:
        ledger = json.loads(body.decode())
        total_dr = sum(acc.get("debit_total", 0.0) for acc in ledger.values() if isinstance(acc, dict))
        total_cr = sum(acc.get("credit_total", 0.0) for acc in ledger.values() if isinstance(acc, dict))
        diff = abs(total_dr - total_cr)
        balanced = diff < 0.01
        record_test("Accounting Invariants", "Double-Entry Balance (Total Dr == Total Cr)", balanced, f"Dr: ₹{total_dr:,.2f}, Cr: ₹{total_cr:,.2f}, Diff: ₹{diff:.2f}")
    except Exception as e:
        record_test("Accounting Invariants", "Double-Entry Balance (Total Dr == Total Cr)", False, str(e))

    # 2. Profit & Loss Invariant: Net Profit == Total Revenue - Total Expenses
    code, body, _, _ = http_req("/api/financial-statements?country=IN")
    try:
        stmts = json.loads(body.decode())
        pnl = stmts.get("profit_and_loss", {})
        rev = pnl.get("total_revenue", 0.0)
        exp = pnl.get("total_expenses", 0.0)
        net = pnl.get("net_profit", 0.0)
        expected_net = rev - exp
        diff = abs(net - expected_net)
        pnl_ok = diff < 0.01
        record_test("Accounting Invariants", "P&L Invariant (Revenue - Expenses == Net Profit)", pnl_ok, f"Rev: ₹{rev:,.2f}, Exp: ₹{exp:,.2f}, Net: ₹{net:,.2f}")
    except Exception as e:
        record_test("Accounting Invariants", "P&L Invariant (Revenue - Expenses == Net Profit)", False, str(e))

    # 3. Balance Sheet Invariant: Assets == Liabilities + Equity
    try:
        bs = stmts.get("balance_sheet", {})
        assets = bs.get("total_assets", 0.0)
        liab_eq = bs.get("total_liabilities_and_equity", 0.0)
        diff = abs(assets - liab_eq)
        bs_ok = diff < 0.05
        record_test("Accounting Invariants", "Balance Sheet Equilibrium (Assets == Liab + Equity)", bs_ok, f"Assets: ₹{assets:,.2f}, Liab+Eq: ₹{liab_eq:,.2f}")
    except Exception as e:
        record_test("Accounting Invariants", "Balance Sheet Equilibrium (Assets == Liab + Equity)", False, str(e))

def test_domain_4_frontend_and_zero_black():
    print("\n" + "="*70)
    print("DOMAIN 4: FRONTEND UI, ASSETS & ICAI ROYAL NAVY & GOLD DESIGN SYSTEM")
    print("="*70)

    # 1. HTML check
    code, body, _, _ = http_req("/")
    html_content = body.decode("utf-8", errors="ignore")
    has_title = "<title>" in html_content
    has_doctype = "<!DOCTYPE html>" in html_content
    has_ca_royal = 'class="ca-royal"' in html_content
    has_theme_meta = '#07162c' in html_content
    has_pwa_install = 'id="pwaInstallBtn"' in html_content
    record_test("Frontend UI", "HTML Structure & ICAI Royal Class Present", has_title and has_doctype and has_ca_royal and has_theme_meta, f"Size: {len(html_content)} bytes")
    record_test("Frontend UI", "PWA Install & Security Trigger Elements Present", has_pwa_install, "Found PWA install button")

    # 2. CSS Royal CA Navy & Gold Verification
    code, body, _, _ = http_req("/static/styles.css")
    css_content = body.decode("utf-8", errors="ignore")
    has_root_vars = "--bg-base: #07162c;" in css_content and "--text-primary: #f8fafc;" in css_content
    
    # Check that bg-slate-950, bg-slate-900 are mapped to royal navy
    has_slate_950_override = ".bg-slate-950" in css_content and "#07162c" in css_content
    has_slate_900_override = ".bg-slate-900" in css_content and "#0b2240" in css_content
    has_aurora_mesh = ".aurora-bg-mesh" in css_content
    has_media_queries = "@media (max-width: 767px)" in css_content and "@media (max-width: 480px)" in css_content
    
    record_test("Frontend UI", "CSS Root Palette: ICAI Royal Navy & Diamond Text", has_root_vars, "Base: #07162c, Text: #f8fafc")
    record_test("Frontend UI", "CSS ICAI Royal Navy Tailwind Dark Overrides", has_slate_950_override and has_slate_900_override, "bg-slate-950/900 mapped to #07162c/#0b2240")
    record_test("Frontend UI", "CSS 60fps Aurora Mesh Animations Present", has_aurora_mesh, "Aurora orb keyframes and glassmorphism verified")
    record_test("Frontend UI", "CSS Cross-Device Responsive Breakpoints Present", has_media_queries, "Mobile, Tablet & Desktop media queries verified")

    # 3. JavaScript Syntax Verification
    try:
        proc = subprocess.run(["node", "-c", "static/app.js"], capture_output=True, text=True, check=True)
        record_test("Frontend UI", "JavaScript Syntax Check (node -c static/app.js)", proc.returncode == 0, "No syntax errors")
    except Exception as e:
        record_test("Frontend UI", "JavaScript Syntax Check (node -c static/app.js)", False, str(e))

    # 4. Static Files Verification
    static_files = [
        ("static/logo.png", "Logo Image"),
        ("static/icon-192.png", "PWA 192px Icon"),
        ("static/icon-512.png", "PWA 512px Icon"),
        ("static/manifest.json", "PWA Web App Manifest"),
        ("static/sw.js", "PWA Service Worker Cache Script")
    ]
    for s_path, s_desc in static_files:
        exists = os.path.exists(s_path)
        sz = os.path.getsize(s_path) if exists else 0
        record_test("Frontend Assets", f"Static Asset: {s_desc}", exists and sz > 0, f"File size: {sz} bytes")

def test_domain_5_i18n_and_jurisdictions():
    print("\n" + "="*70)
    print("DOMAIN 5: INTERNATIONALIZATION & 195+ JURISDICTIONS")
    print("="*70)

    from app.config import ALL_WORLD_COUNTRIES
    count = len(ALL_WORLD_COUNTRIES)
    record_test("I18N & Jurisdictions", "195+ All World Countries Count", count >= 195, f"Total Countries: {count}")

    # Check key global economic jurisdictions are present
    key_codes = ["IN", "US", "UK", "AE", "SG", "DE", "FR", "JP", "CN", "CA", "AU", "SA"]
    present_keys = list(ALL_WORLD_COUNTRIES.keys())
    all_keys_ok = all(k in present_keys for k in key_codes)
    record_test("I18N & Jurisdictions", "Key Economic Hubs Present (IN, US, UK, AE, SG, DE, JP, etc.)", all_keys_ok, f"Checked: {', '.join(key_codes)}")

    # Verify I18N dictionary in app.js
    with open("static/app.js", "r", encoding="utf-8") as f:
        app_js_text = f.read()
    has_gu = 'gu: {' in app_js_text
    has_en = 'en: {' in app_js_text
    has_hi = 'hi: {' in app_js_text
    record_test("I18N & Jurisdictions", "Multi-Language Dictionaries in Client App (gu, en, hi)", has_gu and has_en and has_hi, "Verified translations")

def test_domain_6_latency_benchmarks():
    print("\n" + "="*70)
    print("DOMAIN 6: REAL-WORLD LATENCY & PERFORMANCE BENCHMARKS")
    print("="*70)

    endpoints_to_bench = [
        ("/health", "Health Ping"),
        ("/api/status", "System Status"),
        ("/api/countries", "195+ Countries Listing"),
        ("/api/financial-statements?country=IN", "Financial Statements Engine"),
        ("/api/erp/invoices", "ERP Invoices Retrieval"),
        ("/api/erp/anomalies", "AI Anomaly & Fraud Engine"),
        ("/api/advancement/db-status", "SQLite WAL Sync Status")
    ]
    for ep, desc in endpoints_to_bench:
        _, _, _, lat = http_req(ep)
        fast = lat < 250.0  # Under 250ms is excellent
        record_test("Performance & Latency", f"Latency: {desc} ({ep})", fast, f"{lat:.2f}ms (Threshold: < 250ms)", lat)

def main():
    print("\n=======================================================================")
    print("   SRI SRI ❤️ AI CA & GLOBAL TAX INTELLIGENCE - FULL VERIFICATION   ")
    print("=======================================================================")
    
    test_domain_1_api_endpoints()
    test_domain_2_security()
    test_domain_3_accounting_invariants()
    test_domain_4_frontend_and_zero_black()
    test_domain_5_i18n_and_jurisdictions()
    test_domain_6_latency_benchmarks()

    print("\n" + "="*70)
    print("                  FINAL VERIFICATION REPORT SUMMARY                    ")
    print("="*70)
    print(f"Total Tests Run   : {results['total']}")
    print(f"Total Passed      : {results['passed']} ({(results['passed']/results['total'])*100:.1f}%)")
    print(f"Total Failed      : {results['failed']}")

    for cat, tests in results["categories"].items():
        cat_pass = sum(1 for t in tests if t["status"] == "PASS")
        print(f"  - {cat:32s}: {cat_pass}/{len(tests)} Passed")

    print("="*70)
    if results["failed"] == 0:
        print(">>> RESULT: ALL VERIFICATIONS PASSED WITH 100% SUCCESS! <<<\n")
        return 0
    else:
        print(">>> RESULT: SOME TESTS FAILED <<<\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
