# Payroll calculation module - Updated with HRA and PF
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

def calculate_hra(basic_salary):
    hra = basic_salary * 0.20  # 20% of basic
    return {"hra": hra}

def calculate_pf(basic_salary):
    pf = basic_salary * 0.12  # 12% PF deduction
    return {"pf_deduction": pf}

def generate_payslip(emp_id, month, net_salary):
    return {
        "employee_id": emp_id,
        "month": month,
        "net_salary": net_salary,
        "status": "Generated"
    }
