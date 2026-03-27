# Payroll calculation module
def calculate_salary(basic, allowance, deduction):
    gross = basic + allowance
    net = gross - deduction
    tax = net * 0.10  # 10% tax
    final = net - tax
    return {
        "gross_salary": gross,
        "tax": tax,
        "net_salary": final
    }

# Added in development branch
def generate_payslip(emp_id, month, net_salary):
    return {
        "employee_id": emp_id,
        "month": month,
        "net_salary": net_salary,
        "status": "Generated"
    }
  
