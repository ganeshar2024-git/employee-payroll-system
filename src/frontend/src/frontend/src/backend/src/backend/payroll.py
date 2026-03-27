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
  
