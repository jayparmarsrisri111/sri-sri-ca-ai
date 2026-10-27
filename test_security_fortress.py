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

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from app.security import mca_audit_trail, ca_partner_guard, pii_shield, db_snapshot_manager
from app.auth import auth_manager
from app.main import (
    get_mca_audit_trail,
    verify_mca_chain,
    verify_partner_pin,
    get_clients_list,
    add_new_client,
    get_client_overview,
    generate_encrypted_backup
)

class MockClientRequest:
    def __init__(self, host="127.0.0.1"):
        class ClientObj:
            def __init__(self, h):
                self.host = h
        self.client = ClientObj(host)

class TestSecurityFortress(unittest.TestCase):
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
        self.assertIn("attempts", res["message"].lower())

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
            "name": "Mahindra & Mahindra Testing Pvt. Ltd.",
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
        data = get_mca_audit_trail()
        self.assertEqual(data["status"], "active")
        self.assertTrue(data["integrity"]["valid"])

    def test_09_api_security_verify_chain(self):
        data = verify_mca_chain()
        self.assertTrue(data["valid"])

    def test_10_api_security_partner_pin(self):
        data = verify_partner_pin({"pin": "7788"})
        self.assertTrue(data["success"])

    def test_11_api_clients_list_and_create(self):
        # 1. Get clients
        clients = get_clients_list()
        self.assertIsInstance(clients, list)

        # 2. Add client via API handler
        payload = {
            "name": "Infosys Limited Branch",
            "gstin": "24AAACI1234F1Z1",
            "pan": "AAACI1234F",
            "turnover": "₹12,00,00,000",
            "bank_account": "SBI-1122334455",
            "contact_email": "tax@infosys.com"
        }
        req = MockClientRequest("127.0.0.1")
        create_res = add_new_client(payload, req)
        self.assertTrue(create_res["success"])
        new_id = create_res["client"]["client_id"]

        # 3. Verify client overview endpoint
        overview_data = get_client_overview(new_id)
        self.assertEqual(overview_data["client"]["name"], payload["name"])

    def test_12_api_security_backup(self):
        data = generate_encrypted_backup()
        self.assertIn("master_integrity_hash", data)

if __name__ == "__main__":
    unittest.main()
