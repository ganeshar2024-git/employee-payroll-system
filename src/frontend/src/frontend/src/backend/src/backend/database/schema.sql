-- Employee Payroll Management System Database Schema

CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department VARCHAR(50),
    designation VARCHAR(50),
    email VARCHAR(100),
    organization VARCHAR(100),
    basic_salary DECIMAL(10,2),
    joining_date DATE
);

CREATE TABLE payroll (
    payroll_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    month VARCHAR(20),
    allowance DECIMAL(10,2),
    deduction DECIMAL(10,2),
    bonus DECIMAL(10,2),
    hra DECIMAL(10,2),
    pf_deduction DECIMAL(10,2),
    tax DECIMAL(10,2),
    net_salary DECIMAL(10,2),
    payment_status VARCHAR(20),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);
-- CR-003 database schema enhanced with additional payroll fields
