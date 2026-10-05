"""
Sri Sri ❤️ AI CA & Global Tax Intelligence
Autonomous Double-Entry Accounting Engine
"""

import json
import os
import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "ledger_db.json")

DEFAULT_ACCOUNTS = {
    # Assets
    "Cash on Hand": "Asset",
    "Bank / Checking Account": "Asset",
    "Bank Account (HDFC/Chase/Barclays)": "Asset",
    "Accounts Receivable (Debtors)": "Asset",
    "Accounts Receivable (Sundry Debtors)": "Asset",
    "Inventory": "Asset",
    "Office Equipment & Computers": "Asset",
    "Input Tax Credit / Tax Receivable": "Asset",
    # Liabilities
    "Accounts Payable (Creditors)": "Liability",
    "Accounts Payable (Sundry Creditors)": "Liability",
    "Duties & Taxes Payable (GST/VAT/TDS)": "Liability",
    "Bank Loan": "Liability",
    # Equity
    "Owner's Capital": "Equity",
    "Retained Earnings": "Equity",
    # Revenue
    "Sales Revenue": "Revenue",
    "Sales Revenue (GST Invoice)": "Revenue",
    "Service & Consulting Income": "Revenue",
    "Other Operating Income": "Revenue",
    # Expenses
    "Cost of Goods Sold (Purchases)": "Expense",
    "Rent Expense": "Expense",
    "Salaries & Wages": "Expense",
    "Salaries & Employee Benefits Expense": "Expense",
    "Office Expense": "Expense",
    "Software & Technology Tools": "Expense",
    "Marketing & Advertising": "Expense",
    "Office & Electricity Expense": "Expense",
    "Professional & Legal Fees": "Expense"
}

class AccountingEngine:
    def __init__(self):
        self._ensure_storage()

    def _ensure_storage(self):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        if not os.path.exists(DATA_FILE):
            # Seed with realistic transactions for immediate demonstration
            sample_entries = [
                {
                    "id": "JE-1001",
                    "date": "2026-09-01",
                    "reference_no": "INV-2026-01",
                    "description": "Software Consulting Service to TechCorp",
                    "debit_account": "Bank Account (HDFC/Chase/Barclays)",
                    "credit_account": "Service & Consulting Income",
                    "amount": 150000.0,
                    "tax_account": "Duties & Taxes Payable (GST/VAT/TDS)",
                    "tax_amount": 27000.0,
                    "category": "Sales",
                    "country": "IN"
                },
                {
                    "id": "JE-1002",
                    "date": "2026-09-05",
                    "reference_no": "OFF-RENT-SEP",
                    "description": "Monthly Office Space Rent",
                    "debit_account": "Rent Expense",
                    "credit_account": "Bank Account (HDFC/Chase/Barclays)",
                    "amount": 35000.0,
                    "tax_account": "Input Tax Credit / Tax Receivable",
                    "tax_amount": 6300.0,
                    "category": "Office",
                    "country": "IN"
                },
                {
                    "id": "JE-1003",
                    "date": "2026-09-12",
                    "reference_no": "PO-DELL-992",
                    "description": "Dell High-End Workstation Laptop for AI Dev",
                    "debit_account": "Office Equipment & Computers",
                    "credit_account": "Bank Account (HDFC/Chase/Barclays)",
                    "amount": 85000.0,
                    "tax_account": "Input Tax Credit / Tax Receivable",
                    "tax_amount": 15300.0,
                    "category": "Asset Purchase",
                    "country": "IN"
                },
                {
                    "id": "JE-1004",
                    "date": "2026-09-18",
                    "reference_no": "SALES-882",
                    "description": "Export Web Development Project to US Client",
                    "debit_account": "Accounts Receivable (Debtors)",
                    "credit_account": "Sales Revenue",
                    "amount": 220000.0,
                    "tax_account": None,
                    "tax_amount": 0.0,
                    "category": "Export Sales",
                    "country": "IN"
                },
                {
                    "id": "JE-1005",
                    "date": "2026-09-25",
                    "reference_no": "SAL-SEP-26",
                    "description": "Staff Salary & Developer Remuneration",
                    "debit_account": "Salaries & Wages",
                    "credit_account": "Bank Account (HDFC/Chase/Barclays)",
                    "amount": 65000.0,
                    "tax_account": None,
                    "tax_amount": 0.0,
                    "category": "Payroll",
                    "country": "IN"
                }
            ]
            self._save(sample_entries)

    def _load(self) -> List[Dict[str, Any]]:
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _save(self, entries: List[Dict[str, Any]]):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(entries, f, indent=2, ensure_ascii=False)

    def get_entries(self, country: Optional[str] = None) -> List[Dict[str, Any]]:
        entries = self._load()
        if country and country != "GLOBAL":
            # return all or filtered
            return [e for e in entries if e.get("country", "IN") == country or e.get("country") == "IN"]
        return entries

    def add_entry(self, entry_dict: Dict[str, Any]) -> Dict[str, Any]:
        entries = self._load()
        if "id" not in entry_dict or not entry_dict["id"]:
            entry_dict["id"] = f"JE-{len(entries) + 1001}"
        if "date" not in entry_dict or not entry_dict["date"]:
            entry_dict["date"] = datetime.now().strftime("%Y-%m-%d")
        
        # Ensure amounts are floats
        entry_dict["amount"] = float(entry_dict.get("amount", 0.0))
        entry_dict["tax_amount"] = float(entry_dict.get("tax_amount", 0.0))

        entries.append(entry_dict)
        self._save(entries)
        return entry_dict

    def delete_entry(self, entry_id: str) -> bool:
        entries = self._load()
        new_entries = [e for e in entries if e["id"] != entry_id]
        if len(new_entries) != len(entries):
            self._save(new_entries)
            return True
        return False

    def get_ledger(self, country: Optional[str] = None) -> Dict[str, Any]:
        entries = self.get_entries(country)
        ledger: Dict[str, Dict[str, Any]] = {}

        # Initialize all known accounts
        for acc, acc_type in DEFAULT_ACCOUNTS.items():
            ledger[acc] = {
                "type": acc_type,
                "debit_total": 0.0,
                "credit_total": 0.0,
                "balance": 0.0,
                "transactions": []
            }

        # Process entries
        for e in entries:
            amt = float(e.get("amount", 0.0))
            tax = float(e.get("tax_amount", 0.0))
            dr = e.get("debit_account")
            cr = e.get("credit_account")
            tax_acc = e.get("tax_account")

            if dr not in ledger:
                ledger[dr] = {"type": "Expense", "debit_total": 0.0, "credit_total": 0.0, "balance": 0.0, "transactions": []}
            if cr not in ledger:
                ledger[cr] = {"type": "Liability", "debit_total": 0.0, "credit_total": 0.0, "balance": 0.0, "transactions": []}

            # Check if entry includes tax routing
            if tax_acc and tax > 0:
                if tax_acc not in ledger:
                    ledger[tax_acc] = {
                        "type": "Asset" if ("Input" in tax_acc or "Receivable" in tax_acc) else "Liability",
                        "debit_total": 0.0,
                        "credit_total": 0.0,
                        "balance": 0.0,
                        "transactions": []
                    }
                
                if "Input" in tax_acc or "Receivable" in tax_acc:
                    # Purchase/Expense with Input Tax:
                    # Debit Expense: amt
                    # Debit Input Tax Credit: tax
                    # Credit Bank/Payable: amt + tax
                    ledger[dr]["debit_total"] += amt
                    ledger[dr]["transactions"].append({
                        "id": e["id"], "date": e["date"], "ref": e["reference_no"],
                        "particulars": f"To {cr}", "debit": amt, "credit": 0.0
                    })
                    
                    ledger[tax_acc]["debit_total"] += tax
                    ledger[tax_acc]["transactions"].append({
                        "id": e["id"], "date": e["date"], "ref": e["reference_no"],
                        "particulars": f"Tax on {dr}", "debit": tax, "credit": 0.0
                    })
                    
                    total_gross = amt + tax
                    ledger[cr]["credit_total"] += total_gross
                    ledger[cr]["transactions"].append({
                        "id": e["id"], "date": e["date"], "ref": e["reference_no"],
                        "particulars": f"By {dr} & {tax_acc}", "debit": 0.0, "credit": total_gross
                    })
                else:
                    # Sale/Revenue with Output Tax:
                    # Debit Bank/Receivable: amt + tax
                    # Credit Sales Revenue: amt
                    # Credit Output Tax Payable: tax
                    total_gross = amt + tax
                    ledger[dr]["debit_total"] += total_gross
                    ledger[dr]["transactions"].append({
                        "id": e["id"], "date": e["date"], "ref": e["reference_no"],
                        "particulars": f"To {cr} & {tax_acc}", "debit": total_gross, "credit": 0.0
                    })
                    
                    ledger[cr]["credit_total"] += amt
                    ledger[cr]["transactions"].append({
                        "id": e["id"], "date": e["date"], "ref": e["reference_no"],
                        "particulars": f"By {dr}", "debit": 0.0, "credit": amt
                    })
                    
                    ledger[tax_acc]["credit_total"] += tax
                    ledger[tax_acc]["transactions"].append({
                        "id": e["id"], "date": e["date"], "ref": e["reference_no"],
                        "particulars": f"Tax on {cr}", "debit": 0.0, "credit": tax
                    })
            else:
                # Standard Simple Double-Entry without separate tax split:
                # Debit dr: amt
                # Credit cr: amt
                ledger[dr]["debit_total"] += amt
                ledger[dr]["transactions"].append({
                    "id": e["id"], "date": e["date"], "ref": e["reference_no"],
                    "particulars": f"To {cr}", "debit": amt, "credit": 0.0
                })
                ledger[cr]["credit_total"] += amt
                ledger[cr]["transactions"].append({
                    "id": e["id"], "date": e["date"], "ref": e["reference_no"],
                    "particulars": f"By {dr}", "debit": 0.0, "credit": amt
                })

        # Calculate closing balances based on account normal balances
        for acc, data in ledger.items():
            acc_type = data["type"]
            if acc_type in ["Asset", "Expense"]:
                data["balance"] = data["debit_total"] - data["credit_total"]
            else:  # Liability, Equity, Revenue
                data["balance"] = data["credit_total"] - data["debit_total"]

        return ledger

    def get_financial_statements(self, country: Optional[str] = None) -> Dict[str, Any]:
        ledger = self.get_ledger(country)

        # 1. Trial Balance
        trial_balance = []
        total_dr = 0.0
        total_cr = 0.0

        for acc, data in ledger.items():
            if data["debit_total"] > 0 or data["credit_total"] > 0:
                net_dr = data["balance"] if data["type"] in ["Asset", "Expense"] and data["balance"] > 0 else 0.0
                net_cr = data["balance"] if data["type"] in ["Liability", "Equity", "Revenue"] and data["balance"] > 0 else 0.0
                
                # handle reverse balances
                if data["type"] in ["Asset", "Expense"] and data["balance"] < 0:
                    net_cr = abs(data["balance"])
                elif data["type"] in ["Liability", "Equity", "Revenue"] and data["balance"] < 0:
                    net_dr = abs(data["balance"])

                trial_balance.append({
                    "account": acc,
                    "type": data["type"],
                    "debit": round(net_dr, 2),
                    "credit": round(net_cr, 2)
                })
                total_dr += net_dr
                total_cr += net_cr

        # 2. Profit & Loss Statement
        revenue_items = []
        expense_items = []
        total_revenue = 0.0
        total_expenses = 0.0

        for acc, data in ledger.items():
            if data["type"] == "Revenue" and data["balance"] != 0:
                revenue_items.append({"name": acc, "amount": round(data["balance"], 2)})
                total_revenue += data["balance"]
            elif data["type"] == "Expense" and data["balance"] != 0:
                expense_items.append({"name": acc, "amount": round(data["balance"], 2)})
                total_expenses += data["balance"]

        net_profit = total_revenue - total_expenses

        # 3. Balance Sheet
        asset_items = []
        liability_items = []
        equity_items = []
        total_assets = 0.0
        total_liabilities = 0.0
        total_equity = 0.0

        for acc, data in ledger.items():
            if data["type"] == "Asset" and data["balance"] != 0:
                asset_items.append({"name": acc, "amount": round(data["balance"], 2)})
                total_assets += data["balance"]
            elif data["type"] == "Liability" and data["balance"] != 0:
                liability_items.append({"name": acc, "amount": round(data["balance"], 2)})
                total_liabilities += data["balance"]
            elif data["type"] == "Equity":
                equity_items.append({"name": acc, "amount": round(data["balance"], 2)})
                total_equity += data["balance"]

        # Add Net Profit to Owner's Equity (Current Period Retained Earnings)
        equity_items.append({"name": "Net Profit / Current Period Earnings", "amount": round(net_profit, 2)})
        total_equity += net_profit

        return {
            "trial_balance": {
                "rows": trial_balance,
                "total_debit": round(total_dr, 2),
                "total_credit": round(total_cr, 2),
                "is_balanced": abs(total_dr - total_cr) < 1.0
            },
            "profit_and_loss": {
                "revenue": revenue_items,
                "total_revenue": round(total_revenue, 2),
                "expenses": expense_items,
                "total_expenses": round(total_expenses, 2),
                "net_profit": round(net_profit, 2),
                "net_profit_margin_percent": round((net_profit / total_revenue * 100), 2) if total_revenue > 0 else 0.0
            },
            "balance_sheet": {
                "assets": asset_items,
                "total_assets": round(total_assets, 2),
                "liabilities": liability_items,
                "total_liabilities": round(total_liabilities, 2),
                "equity": equity_items,
                "total_equity": round(total_equity, 2),
                "total_liabilities_and_equity": round(total_liabilities + total_equity, 2),
                "is_balanced": abs(total_assets - (total_liabilities + total_equity)) < 5.0
            }
        }
