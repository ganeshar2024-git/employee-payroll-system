# Main Application - Employee Payroll Management System v2.0
from flask import Flask, request, jsonify, render_template
from payroll import generate_payslip, EMPLOYEES

app = Flask(__name__)

# Simulated user login credentials
USERS = {
    "admin": "admin123",
    "hr":    "hr@2026",
}

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login():
    data     = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')

    if USERS.get(username) == password:
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"})

@app.route('/employee/<emp_id>', methods=['GET'])
def get_employee_details(emp_id):
    payslip = generate_payslip(emp_id)
    if payslip:
        return jsonify({"success": True, "data": payslip})
    else:
        return jsonify({"success": False, "message": f"Employee {emp_id} not found"})

@app.route('/employees', methods=['GET'])
def list_employees():
    return jsonify({"success": True, "employees": list(EMPLOYEES.keys())})

if __name__ == '__main__':
    app.run(debug=True)
