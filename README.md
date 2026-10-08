# Sri Sri ❤️ AI CA & Global Tax Intelligence
### Autonomous Chartered Accountant, Double-Entry Bookkeeping & Multi-National Tax Platform

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-8E75C2.svg?logo=google&logoColor=white)](https://ai.google.dev/)
[![OWASP](https://img.shields.io/badge/Security-OWASP%20Top%2010%20Hardened-green.svg)](https://owasp.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 🌟 Overview

**Sri Sri ❤️ AI CA** is a state-of-the-art, autonomous financial and legal artificial intelligence system engineered to eliminate over 95% of manual Chartered Accountant (CA), bookkeeping, and tax compliance workflows.

From automated document ingestion and double-entry ledger posting to complex multi-jurisdiction tax liability calculations and AI-driven tax notice response drafting, the platform delivers enterprise bank-grade accuracy and compliance.

---

## 🚀 Key Features

### 1. 📷 Smart Bill & Invoice Scanner (Multimodal AI Vision & OCR)
- **Instant Optical Extraction:** Upload receipts, bills, and tax invoices in PDF or image format (PNG, JPG, WebP).
- **Automated Metadata Parsing:** Extracts vendor details, GSTIN/Tax ID, invoice date, HSN/SAC codes, taxable amounts, and tax breakdowns (CGST, SGST, IGST, VAT).
- **1-Click Ledger Integration:** Instantly converts scanned documents into balanced double-entry voucher transactions with automated credit/debit assignment.

### 2. 📚 Autonomous Double-Entry Engine & General Ledger
- **Complete Bookkeeping Cycle:** Full support for Cash, Bank, Sales, Purchase, Asset, and Liability ledger accounts.
- **Journal & Voucher Posting:** Validates debit-credit symmetry before recording any financial movement.
- **Balanced Trial Balance:** Generates mathematically verified Trial Balances with real-time discrepancy detection.

### 3. 🌐 Multi-Country & Global Tax Engine
- 🇮🇳 **India:**
  - **GST Compliance:** Automated GSTR-1 sales schedules, GSTR-2B Input Tax Credit (ITC) reconciliation, and monthly GSTR-3B tax liability computation.
  - **Income Tax Computation:** Comparative analysis under Section 115BAC (New Tax Regime vs. Old Tax Regime).
  - **Presumptive Taxation:** Rules engine for Section 44AD (business) and Section 44ADA (professionals).
  - **TDS Compliance:** Automatic identification and calculation of Tax Deducted at Source provisions.
- 🇺🇸 **United States:**
  - IRS Schedule C profit/loss calculations for sole proprietors and LLCs.
  - Self-Employment Tax (15.3% Social Security & Medicare) estimation.
  - Quarterly estimated tax schedule planning.
- 🇬🇧 **United Kingdom:**
  - HMRC VAT Returns (Box 1 through Box 5 calculations).
  - Corporation Tax and allowable business expense evaluation.
- 🇦🇪 **United Arab Emirates:**
  - Corporate Tax calculation (0% on taxable income up to AED 375,000; 9% standard rate).
  - 5% UAE VAT return schedules.
- 🌍 **International Standards:**
  - Compliant with IFRS (International Financial Reporting Standards) and US GAAP.

### 4. 🏦 Automated Bank Statement Reconciliation
- Matches imported bank transactions against internal book vouchers.
- Automatically flags cleared entries, pending items, and ledger differences with precision.

### 5. 📊 Final Accounts & Financial Statements
- **Trading & Profit and Loss Account (P&L):** Calculates Gross Profit, Net Profit, and Operating Margins.
- **Balance Sheet:** Real-time generation of Assets vs. Liabilities statement.
- **Export & Print:** High-resolution print-ready layouts and PDF exports.

### 6. ⚖️ AI CA Copilot & Legal Notice Solver
- **Interactive Advisory:** 24/7 legal and tax consulting powered by Google Gemini AI in multiple languages.
- **Statutory Notice Resolution:** Analyzes complex tax notices (Income Tax Sec 143(1), Sec 148, Sec 139(9); GST DRC-01, ASMT-10).
- **Formal Legal Draft Generation:** Produces submission-ready, structured legal response drafts citing applicable statutory provisions and case references.

### 7. 🛡️ Enterprise "Security Fortress" & Compliance
- **OWASP Top 10 Hardened:** Enforces CSP (Content Security Policy), HSTS, X-Content-Type-Options, X-Frame-Options, and Referrer-Policy.
- **Anti-Brute Force & Rate Limiting:** In-memory request throttler preventing DoS and credential stuffing attacks.
- **Cryptographic Authentication:** Secure password hashing (Argon2 / PBKDF2), role-based access control (Admin, CA Partner, Auditor, Client).
- **PII Shield:** Automatic redaction and masking of sensitive tax identifiers (PAN, Aadhaar, SSN).
- **MCA 2023 Audit Trail Compliance:** Immutable tamper-evident audit logs recording user, timestamp, IP, and changes.
- **Automated Database Backups:** In-memory snapshot manager with rollback support.

### 8. 🌍 20+ Global Languages Offline Deep Translation
- 100% native client-side offline internationalization (i18n) across 20+ world languages (English, Gujarati, Hindi, Spanish, French, German, Arabic, Japanese, and more).
- Zero reliance on external Google Translate scripts — clean UI with zero injected banner bars.

---

## 🏗️ Architecture & Project Structure

```plaintext
SRI SRI ❤️CA AI PROJECT/
├── api/                        # Serverless handler adapters (Vercel / Netlify)
│   └── index.py                # ASGI entrypoint
├── app/                        # Core Application Backend
│   ├── accounting_engine.py    # Double-entry ledger & voucher logic
│   ├── advancement_engine.py   # Advanced forecasting & analytics
│   ├── ai_engine.py            # Multimodal OCR and Gemini AI Copilot
│   ├── auth.py                 # RBAC and session security
│   ├── config.py               # Tax jurisdictions and system constants
│   ├── erp_suite.py            # ERP data management and sync
│   ├── main.py                 # FastAPI application, routes, & middleware
│   ├── models.py               # Pydantic validation schemas
│   ├── reconciliation_engine.py# Bank reconciliation algorithm
│   ├── security.py             # Security Fortress & OWASP middleware
│   └── tax_engine.py           # Multi-country tax calculation rules
├── data/                       # Local storage & snapshots
├── static/                     # Web UI Frontend
│   ├── locales/                # 20+ language translation files (JSON)
│   ├── app.js                  # Frontend controllers & state
│   ├── i18n.js                 # Native translation engine
│   ├── index.html              # Main single-page application
│   └── style.css               # Modern responsive styling
├── scripts/                    # Maintenance & diagnostic utilities
├── .dockerignore               # Docker ignore rules
├── .gitignore                  # Git ignore rules
├── Dockerfile                  # Containerized deployment manifest
├── go_live.py                  # Live deployment validation script
├── netlify.toml                # Netlify deployment configuration
├── Procfile                    # Heroku / PaaS process specification
├── render.yaml                 # Render Blueprint configuration
├── requirements.txt            # Python dependencies
├── run.py                      # Application launch script
├── test_full_suite.py          # Comprehensive test suite
├── test_security_fortress.py   # Security & penetration testing suite
├── vercel.json                 # Vercel deployment configuration
└── verify_endpoints.py         # API endpoint health verification
```

---

## 🛠️ Tech Stack

- **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.11+)
- **Server:** [Uvicorn](https://www.uvicorn.org/) (High-performance ASGI server)
- **AI & Vision:** [Google Gemini API](https://ai.google.dev/) (`google-genai` SDK)
- **Data Validation:** [Pydantic v2](https://docs.pydantic.dev/)
- **Frontend:** Vanilla HTML5, CSS3 (Modern Glassmorphism & Dashboard Layout), JavaScript (ES6+), Native i18n
- **Containerization:** Docker
- **Deployment Targets:** Render, Vercel, Netlify, Docker

---

## 💻 Getting Started

### Prerequisites
- Python 3.11 or higher
- Git
- (Optional) Google Gemini API Key for AI Copilot & Vision OCR

### 1. Clone the Repository
```bash
git clone https://github.com/jayparmarsrisri111/sri-sri-ca-ai.git
cd sri-sri-ca-ai
```

### 2. Set Up a Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
PORT=8000
DEFAULT_COUNTRY=IN
```

### 5. Run the Application
Launch via the runner:
```bash
python run.py
```
Or directly with Uvicorn:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open your browser and navigate to:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🧪 Testing

Run the full end-to-end verification and security audit test suites:

```bash
# Run complete functional & financial test suite
python test_full_suite.py

# Run Security Fortress penetration and OWASP compliance tests
python test_security_fortress.py

# Verify live API health endpoints
python verify_endpoints.py
```

---

## 🚢 Deployment

### 🐳 Docker
```bash
# Build Docker image
docker build -t sri-sri-ca-ai .

# Run Docker container
docker run -p 8000:8000 --env GEMINI_API_KEY=your_key sri-sri-ca-ai
```

### ☁️ Render
The repository includes a ready-to-use [`render.yaml`](render.yaml) blueprint:
1. Connect this GitHub repository on [Render](https://render.com/).
2. Select **Blueprint** deployment.
3. Deploy automatically to the Singapore region with free tier support.

### ▲ Vercel & Netlify
Configuration files [`vercel.json`](vercel.json) and [`netlify.toml`](netlify.toml) are pre-configured to route static assets and serverless Python API requests seamlessly.

---

## 📖 API Documentation

Once the server is running locally, access interactive OpenAPI documentation:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Support & Contribution

For issues, questions, or enhancements, please submit an issue or pull request via the GitHub repository:
👉 **[https://github.com/jayparmarsrisri111/sri-sri-ca-ai](https://github.com/jayparmarsrisri111/sri-sri-ca-ai)**
