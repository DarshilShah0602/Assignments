# fees.py
"""
Fee Management Module
Handles student fee-related operations
"""

from datetime import datetime

fee_records = {}

def set_fee_structure(student_id, total_fee, installments=1):
    """Set fee structure for a student"""
    fee_records[student_id] = {
        'total_fee': total_fee,
        'paid': 0,
        'balance': total_fee,
        'installments': installments,
        'payment_history': []
    }
    return True, "Fee structure set successfully"

def make_payment(student_id, amount):
    """Record a fee payment"""
    if student_id not in fee_records:
        return False, "Fee record not found"
    
    record = fee_records[student_id]
    if amount > record['balance']:
        return False, "Amount exceeds balance"
    
    record['paid'] += amount
    record['balance'] -= amount
    record['payment_history'].append({
        'amount': amount,
        'date': datetime.now().strftime("%Y-%m-%d"),
        'time': datetime.now().strftime("%H:%M:%S")
    })
    
    return True, f"Payment of {amount} received. Balance: {record['balance']}"

def get_fee_status(student_id):
    """Get fee status for a student"""
    return fee_records.get(student_id, None)

def get_all_fees():
    """Get all fee records"""
    return fee_records