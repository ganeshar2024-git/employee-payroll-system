# Main application entry point
from flask import Flask
from employee import get_employee
from payroll import calculate_salary

app = Flask(__name__)

@app.route('/')
def home():
    return "Employee Payroll Management System"

@app.route('/employee/<int:id>')
def employee(id):
    return get_employee(id)

if __name__ == '__main__':
    app.run(debug=True)
