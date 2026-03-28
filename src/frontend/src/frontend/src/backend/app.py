# Main application entry point
from flask import Flask
from payroll import calculate_total_salary

app = Flask(__name__)

@app.route('/')
def home():
    return "Employee Payroll Management System Backend Running"

@app.route('/salary/<int:basic>/<int:allowance>/<int:deduction>')
def salary(basic, allowance, deduction):
    return calculate_total_salary(basic, allowance, deduction)

if __name__ == '__main__':
    app.run(debug=True)
# CR-010 backend route enhancement completed
