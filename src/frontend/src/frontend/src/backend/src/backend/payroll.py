# Payroll Module v2.0 - Real-Time Salary, Deductions & Allowances

# Salary structure based on Department and Experience
SALARY_STRUCTURE = {
    "IT":         {"0-2": 35000, "2-5": 55000, "5+": 85000},
    "HR":         {"0-2": 25000, "2-5": 40000, "5+": 60000},
    "Finance":    {"0-2": 30000, "2-5": 50000, "5+": 75000},
    "Operations": {"0-2": 20000, "2-5": 35000, "5+": 55000},
}

# Employee Database (simulated)
EMPLOYEES = {
    "EMP001": {"name": "Ganesh R",    "department": "IT",         "experience": 3},
    "EMP002": {"name": "Priya S",     "department": "HR",         "experience": 6},
    "EMP003": {"name": "Arjun M",     "department": "Finance",    "experience": 1},
    "EMP004": {"name": "Deepa K",     "department": "Operations", "experience": 4},
    "EMP005": {"name": "Vikram T",    "department": "IT",         "experience": 7},
}

def get_experience_slab(years):
    if years < 2:
        return "0-2"
    elif years < 5:
        return "2-5"
    else:
        return "5+"

def get_basic_salary(department, experience):
    slab = get_experience_slab(experience)
    return SALARY_STRUCTURE.get(department, {}).get(slab, 0)

def calculate_allowances(basic):
    hra       = round(basic * 0.40)   # 40% of basic
    da        = round(basic * 0.10)   # 10% of basic
    medical   = 1500                  # Fixed
    travel    = 1000                  # Fixed
    return {
        "hra": hra,
        "da": da,
        "medical_allowance": medical,
        "travel_allowance": travel,
        "total_allowances": hra + da + medical + travel
    }

def calculate_deductions(basic, gross):
    pf   = round(basic * 0.12)        # 12% of basic
    esi  = round(gross * 0.0075) if gross < 21000 else 0   # 0.75% if gross < 21000
    pt   = 200 if gross > 15000 else 0                     # Professional Tax
    tds  = round(gross * 0.10) if gross > 50000 else 0     # TDS 10% if gross > 50000
    return {
        "pf": pf,
        "esi": esi,
        "professional_tax": pt,
        "tds": tds,
        "total_deductions": pf + esi + pt + tds
    }

def get_employee(emp_id):
    return EMPLOYEES.get(emp_id.upper(), None)

def generate_payslip(emp_id):
    emp = get_employee(emp_id)
    if not emp:
        return None

    basic       = get_basic_salary(emp["department"], emp["experience"])
    allowances  = calculate_allowances(basic)
    gross       = basic + allowances["total_allowances"]
    deductions  = calculate_deductions(basic, gross)
    net_salary  = gross - deductions["total_deductions"]
    slab        = get_experience_slab(emp["experience"])

    return {
        "emp_id":           emp_id.upper(),
        "name":             emp["name"],
        "department":       emp["department"],
        "experience":       emp["experience"],
        "experience_slab":  slab,
        "basic_salary":     basic,
        "allowances":       allowances,
        "gross_salary":     gross,
        "deductions":       deductions,
        "net_salary":       net_salary
    }
