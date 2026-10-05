"""
Sri Sri ❤️ AI CA & Global Tax Intelligence
Data Models
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class LineItem(BaseModel):
    description: str
    quantity: float = 1.0
    unit_price: float = 0.0
    amount: float = 0.0
    tax_rate: float = 0.0
    tax_amount: float = 0.0
    hsn_sac: Optional[str] = None

class InvoiceParsedData(BaseModel):
    invoice_number: str = ""
    invoice_date: str = ""
    party_name: str = ""
    party_tax_id: str = ""  # GSTIN, EIN, VAT ID
    invoice_type: str = "Purchase"  # Purchase or Sale
    currency: str = "INR"
    subtotal: float = 0.0
    tax_amount: float = 0.0
    cgst: float = 0.0
    sgst: float = 0.0
    igst: float = 0.0
    total_amount: float = 0.0
    items: List[LineItem] = []
    category: str = "General Business Expense"
    suggested_journal_entry: Dict[str, Any] = {}

class JournalEntry(BaseModel):
    id: Optional[str] = None
    date: str
    reference_no: str
    description: str
    debit_account: str
    credit_account: str
    amount: float
    tax_account: Optional[str] = None
    tax_amount: float = 0.0
    category: str = "General"
    country: str = "IN"

class BankTransaction(BaseModel):
    id: str
    date: str
    description: str
    reference_no: Optional[str] = None
    debit: float = 0.0  # Money out
    credit: float = 0.0  # Money in
    balance: float = 0.0
    matched: bool = False
    matched_entry_id: Optional[str] = None

class TaxNoticeRequest(BaseModel):
    notice_text: str
    country: str = "IN"
    authority: str = "Income Tax / GST"
    language: str = "gu"  # gu, en, hi

class AIChatRequest(BaseModel):
    message: str
    conversation_history: List[Dict[str, str]] = []
    country: str = "IN"
    language: str = "gu"  # gu, en, hi
