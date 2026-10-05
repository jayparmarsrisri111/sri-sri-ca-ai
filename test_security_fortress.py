"""
Sri Sri ❤️ AI CA Project - Security Fortress & Dynamic Clients Test Suite
Verifies:
1. MCA Rule 11(g) Cryptographic Hash-Chained Blockchain Audit Trail
2. CA Partner Step-Up 2FA Guard with Brute-Force Lockout
3. DPDP Act 2023 & ICAI PII Privacy Shield
4. SHA-256 Disaster Recovery Encrypted Backup Manager
5. Dynamic Multi-Client Vault Architecture
6. Security REST API Integration
"""

import os
import sys
import json
import unittest
from fastapi.testclient import TestClient

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from app.main import app
from app.security import mca_audit_trail, ca_partner_guard, pii_shield, db_snapshot_manager
from app.auth import auth_manager

class TestSecurityFortress(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    # 1. MCA Audit Trail Blockchain Tests
    def test_01_mca_audit_chain_integrity(self):
        result = mca_audit_trail.verify_integrity()
        self.assertTrue(result["valid"], "MCA Audit trail should be cryptographically valid")
        self.assertFalse(result.get("tamper_detected", True))
        self.assertGreaterEqual(result["total_blocks"], 1)
        self.assertEqual(len(result["last_block_hash"]), 64)

    def test_02_mca_record_and_hash_chaining(self):
        initial_blocks = mca_audit_trail.verify_integrity()["total_blocks"]
        new_block = mca_audit_trail.record_event(
            user_id="CA_TEST_PARTNER",
            action="STATUTORY_AUDIT_SIGN",
            entity_type="TAX_AUDIT",
            entity_id="FORM_3CD_TEST",
            details="Form 3CD signed with UDIN verification under Section 44AB",
            client_ip="127.0.0.1"
        )
        self.assertEqual(new_block["block_index"], initial_blocks)
        self.assertEqual(len(new_block["hash"]), 64)
        
        # Verify chain validity after recording
        integrity = mca_audit_trail.verify_integrity()
        self.assertTrue(integrity["valid"])
        self.assertEqual(integrity["total_blocks"], initial_blocks + 1)

    # 2. CA Partner Step-Up 2FA Guard Tests
    def test_03_partner_guard_verification(self):
        # Default pin 7788
        res = ca_partner_guard.verify_pin("7788")
        self.assertTrue(res["success"])
        self.assertIn("grant_token", res)

    def test_04_partner_guard_wrong_pin(self):
        res = ca_partner_guard.verify_pin("9999")
        self.assertFalse(res["success"])
        self.assertIn("પ્રયાસો", res["message"])

    # 3. PII Privacy Shield Tests
    def test_05_pii_shield_masking(self):
        raw_pan = "ABCDE1234F"
        masked_pan = pii_shield.mask_pan(raw_pan)
        self.assertEqual(masked_pan, "ABCDE****F")

        raw_bank = "HDFC0012345678"
        masked_bank = pii_shield.mask_bank_acc(raw_bank)
        self.assertTrue(masked_bank.endswith("5678"))
        self.assertTrue(masked_bank.startswith("******"))

        raw_aadhaar = "123456789012"
        masked_aadhaar = pii_shield.mask_aadhaar(raw_aadhaar)
        self.assertEqual(masked_aadhaar, "XXXX-XXXX-9012")

    # 4. Disaster Recovery Encrypted Backup Tests
    def test_06_database_backup_generation(self):
        backup_pkg = db_snapshot_manager.create_snapshot()
        self.assertIn("master_integrity_hash", backup_pkg)
        self.assertEqual(len(backup_pkg["master_integrity_hash"]), 64)
        self.assertIn("integrity_manifest", backup_pkg)

    # 5. Dynamic Client Vault Architecture Tests
    def test_07_dynamic_client_enrollment(self):
        client_data = {
            "name": "મહિન્દ્રા એન્ડ મહિન્દ્રા ટેસ્ટિંગ પ્રા. લી.",
            "gstin": "24AAACM9999M1Z3",
            "pan": "AAACM9999M",
            "turnover": "₹8,50,00,000",
            "bank_account": "AXIS-1234567890",
            "contact_email": "accounts@mahindra-test.com"
        }
        saved = auth_manager.add_ca_client(client_data)
        self.assertIn("client_id", saved)
        self.assertEqual(saved["name"], client_data["name"])

        # Check client appears in listing
        all_clients = auth_manager.get_ca_clients()
        matching = [c for c in all_clients if c["client_id"] == saved["client_id"]]
        self.assertEqual(len(matching), 1)

    # 6. REST API Endpoints Integration Tests
    def test_08_api_security_audit_trail(self):
        response = self.client.get("/api/security/audit-trail")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "active")
        self.assertTrue(data["integrity"]["valid"])

    def test_09_api_security_verify_chain(self):
        response = self.client.post("/api/security/verify-chain")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["valid"])

    def test_10_api_security_partner_pin(self):
        response = self.client.post("/api/security/partner-pin", json={"pin": "7788"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])

    def test_11_api_clients_list_and_create(self):
        # 1. Get clients
        res = self.client.get("/api/clients")
        self.assertEqual(res.status_code, 200)
        initial_count = len(res.json())

        # 2. Add client via API
        payload = {
            "name": "ઇન્ફોસિસ લિમિટેડ શાખા",
            "gstin": "24AAACI1234F1Z1",
            "pan": "AAACI1234F",
            "turnover": "₹12,00,00,000",
            "bank_account": "SBI-1122334455",
            "contact_email": "tax@infosys.com"
        }
        create_res = self.client.post("/api/clients", json=payload)
        self.assertEqual(create_res.status_code, 200)
        create_data = create_res.json()
        self.assertTrue(create_data["success"])
        new_id = create_data["client"]["client_id"]

        # 3. Verify client overview endpoint
        overview_res = self.client.get(f"/api/clients/{new_id}/overview")
        self.assertEqual(overview_res.status_code, 200)
        overview_data = overview_res.json()
        self.assertEqual(overview_data["client"]["name"], payload["name"])

    def test_12_api_security_backup(self):
        res = self.client.post("/api/security/backup")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn("master_integrity_hash", data)

if __name__ == "__main__":
    unittest.main()
