# Payroll calculation module - Enhanced version

def calculate_salary(basic, allowance, deduction):
    gross = basic + allowance
    net = gross - deduction
    tax = net * 0.10
    final = net - tax
    return {
        "gross_salary": gross,
        "tax": tax,
        "net_salary": final
    }

def calculate_hra(basic_salary):
    hra = basic_salary * 0.20
    return {"hra": hra}

def calculate_pf(basic_salary):
    pf = basic_salary * 0.12
    return {"pf_deduction": pf}

def calculate_bonus(basic_salary):
    bonus = basic_salary * 0.05
    return {"bonus": bonus}

def calculate_total_salary(basic, allowance, deduction):
    bonus = basic * 0.05
    hra = basic * 0.20
    pf = basic * 0.12
    gross = basic + allowance + bonus + hra
    net_before_tax = gross - deduction - pf
    tax = net_before_tax * 0.10
    final = net_before_tax - tax

    return {
        "gross_salary": gross,
        "bonus": bonus,
        "hra": hra,
        "pf_deduction": pf,
        "tax": tax,
        "net_salary": final
    }

def generate_payslip(emp_id, month, net_salary):
    return {
        "employee_id": emp_id,
        "month": month,
        "net_salary": net_salary,
        "status": "Generated"
    }
