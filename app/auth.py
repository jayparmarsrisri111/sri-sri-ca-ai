"""
Sri Sri ❤️ AI CA & Global Tax Intelligence
Secure Authentication and Role Management
Enterprise Security:
- Salted PBKDF2-HMAC-SHA256 password hashing
- Constant-time verification
- Input sanitization
- 256-bit secure session bearer tokens
"""

import os
import json
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
from app.security import (
    hash_password,
    verify_password,
    generate_session_token,
    sanitize_input,
    security_guard
)

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
USERS_FILE = os.path.join(DATA_DIR, "users_db.json")
CLIENTS_FILE = os.path.join(DATA_DIR, "clients_db.json")

class UserRegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    role: str = "user"  # "ca" or "user"
    company_or_firm_name: str = ""
    membership_or_gstin: str = ""

class UserLoginRequest(BaseModel):
    email: str
    password: str

class AuthManager:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self._ensure_users()

    def _ensure_users(self):
        if not os.path.exists(USERS_FILE):
            default_users = [
                {
                    "id": "CA-001",
                    "name": "CA જયદીપ શાહ (FCA)",
                    "email": "ca@srisri.com",
                    "password": hash_password("ca123"),
                    "role": "ca",
                    "role_title": "Chartered Accountant / Auditor (ICAI / ACCA)",
                    "company_or_firm_name": "શાહ & એસોસિયેટ્સ CA ફર્મ",
                    "membership_or_gstin": "ICAI M.No: 542190",
                    "clients_count": 18
                },
                {
                    "id": "USR-001",
                    "name": "શ્રી શ્રી એન્ટરપ્રાઇઝ (માલિક)",
                    "email": "user@srisri.com",
                    "password": hash_password("user123"),
                    "role": "user",
                    "role_title": "Business Owner / Client",
                    "company_or_firm_name": "Sri Sri ❤️ Global Traders",
                    "membership_or_gstin": "GSTIN: 24AAACS9981M1Z5",
                    "clients_count": 0
                }
            ]
            self._save_users(default_users)
        else:
            # Upgrade existing unhashed passwords to salted pbkdf2
            users = self._load_users()
            changed = False
            for u in users:
                if not u.get("password", "").startswith("pbkdf2:sha256:"):
                    u["password"] = hash_password(u["password"])
                    changed = True
            if changed:
                self._save_users(users)

    def _load_users(self) -> List[Dict[str, Any]]:
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _save_users(self, users: List[Dict[str, Any]]):
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2, ensure_ascii=False)

    def register(self, req: UserRegisterRequest, client_ip: str = "127.0.0.1") -> Dict[str, Any]:
        clean_email = sanitize_input(req.email.strip().lower())
        clean_name = sanitize_input(req.name.strip())
        clean_company = sanitize_input(req.company_or_firm_name.strip())
        clean_reg = sanitize_input(req.membership_or_gstin.strip())
        clean_role = "ca" if req.role == "ca" else "user"

        if not clean_email or not req.password:
            return {"success": False, "message": "ઇમેઇલ અને પાસવર્ડ આવશ્યક છે."}

        users = self._load_users()
        for u in users:
            if u["email"].lower() == clean_email:
                return {"success": False, "message": "આ ઇમેઇલ પહેલેથી રજીસ્ટર થયેલો છે (Email already exists)"}

        prefix = "CA" if clean_role == "ca" else "USR"
        token = generate_session_token()
        new_user = {
            "id": f"{prefix}-{len(users) + 1:03d}",
            "name": clean_name or ("CA Professional" if clean_role == "ca" else "Business Client"),
            "email": clean_email,
            "password": hash_password(req.password),
            "role": clean_role,
            "role_title": "Chartered Accountant / Auditor (ICAI / ACCA)" if clean_role == "ca" else "Business Owner / Client",
            "company_or_firm_name": clean_company,
            "membership_or_gstin": clean_reg,
            "clients_count": 0
        }
        users.append(new_user)
        self._save_users(users)

        security_guard.record_login_success(client_ip, clean_email)

        safe_user = {k: v for k, v in new_user.items() if k != "password"}
        safe_user["token"] = token
        return {"success": True, "user": safe_user}

    def login(self, req: UserLoginRequest, client_ip: str = "127.0.0.1") -> Dict[str, Any]:
        clean_email = sanitize_input(req.email.strip().lower())
        users = self._load_users()

        for u in users:
            if u["email"].lower() == clean_email:
                if verify_password(req.password, u["password"]):
                    security_guard.record_login_success(client_ip, clean_email)
                    safe_user = {k: v for k, v in u.items() if k != "password"}
                    safe_user["token"] = generate_session_token()
                    return {"success": True, "user": safe_user}
                else:
                    security_guard.record_login_failure(client_ip, clean_email)
                    return {"success": False, "message": "ખોટો પાસવર્ડ છે (Invalid password)"}

        security_guard.record_login_failure(client_ip, clean_email)
        return {"success": False, "message": "આ ઇમેઇલ સાથે કોઈ ખાતું મળ્યું નથી (User not found)"}

    def _ensure_clients(self):
        if not os.path.exists(CLIENTS_FILE):
            default_clients = [
                {
                    "client_id": "CL-101",
                    "name": "શ્રી રામ ઇન્ફોટેક પ્રા. લી.",
                    "gstin": "24AAACS9981M1Z5",
                    "pan": "AAACS9981M",
                    "turnover": "₹48,50,000",
                    "gstr_status": "GSTR-3B Filed",
                    "itc_mismatch": "₹0 (100% Matched)",
                    "audit_status": "Verified & Signed",
                    "bank_account": "HDFC-0019283746",
                    "contact_email": "accounts@shreeram.in"
                },
                {
                    "client_id": "CL-102",
                    "name": "શ્રીજી ટેક્સટાઇલ્સ સુરત",
                    "gstin": "24BBCST4412K1Z9",
                    "pan": "BBCST4412K",
                    "turnover": "₹1,24,00,000",
                    "gstr_status": "Pending Verification",
                    "itc_mismatch": "₹14,200 (Action Required)",
                    "audit_status": "Audit in Progress",
                    "bank_account": "SBI-9918273645",
                    "contact_email": "tax@shreejitextiles.com"
                },
                {
                    "client_id": "CL-103",
                    "name": "રાધે કેમિકલ્સ વડોદરા",
                    "gstin": "24CCDTR8891N1Z2",
                    "pan": "CCDTR8891N",
                    "turnover": "₹82,00,000",
                    "gstr_status": "GSTR-3B Filed",
                    "itc_mismatch": "₹0 (100% Matched)",
                    "audit_status": "Verified & Signed",
                    "bank_account": "ICICI-5544332211",
                    "contact_email": "finance@radhechem.com"
                }
            ]
            with open(CLIENTS_FILE, "w", encoding="utf-8") as f:
                json.dump(default_clients, f, indent=2, ensure_ascii=False)

    def get_ca_clients(self) -> List[Dict[str, Any]]:
        """Returns verified clients managed by CA from database"""
        self._ensure_clients()
        try:
            with open(CLIENTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def add_ca_client(self, client_data: Dict[str, Any]) -> Dict[str, Any]:
        """Dynamically adds a new client into the CA portfolio"""
        self._ensure_clients()
        clients = self.get_ca_clients()
        new_id = f"CL-{101 + len(clients)}"
        client_data["client_id"] = new_id
        if "audit_status" not in client_data:
            client_data["audit_status"] = "Newly Enrolled"
        if "gstr_status" not in client_data:
            client_data["gstr_status"] = "Pending Setup"
        if "itc_mismatch" not in client_data:
            client_data["itc_mismatch"] = "₹0"
        
        clients.append(client_data)
        with open(CLIENTS_FILE, "w", encoding="utf-8") as f:
            json.dump(clients, f, indent=2, ensure_ascii=False)
        return client_data

auth_manager = AuthManager()
