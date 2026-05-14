HRmanagement_Automation

Automated testing framework for HR Management applications using Python, Pytest, Selenium WebDriver, and Allure Reports.


---

Project Overview

This project is designed to automate end-to-end testing of HR management functionalities such as:

Employee Login

Dashboard Validation

Forgot Password

My Info Module

Leave Management

Claim Requests

UI Validation

Navigation Testing


The framework follows the Page Object Model (POM) design pattern for better scalability, maintainability, and reusability.


---

Tech Stack        

Technology                                            Purpose
Python                                                Programming Language
Selenium WebDriver                                    Browser Automation
Pytest                                                Test Execution Framework
Allure Reports                                        Reporting & Visualization
PyCharm                                               IDE
Git & GitHub                                          Version Control



---

Project Structure

HRmanagement_Automation/
│
├── allure-report/
├── allure-results/
├── reports/
├── venv/
│
├── config.py
├── conftest.py
├── csv_reader.py
├── dashboard_page.py
├── logger.py
├── login_page.py
├── login_data.csv
├── main.py
├── pytest.ini
├── requirements.txt
│
├── test_claim_request.py
├── test_forgot_password.py
├── test_myinfo_menu.py
├── test_assign_leave.py
│
└── README.md


---

Features

Page Object Model (POM) architecture

Reusable utility functions

CSV-based test data handling

Logging support

Pytest fixtures and configuration

Allure HTML reporting

Cross-browser support ready

Easy maintenance and scalability



---

Installation

Clone Repository

git clone https://github.com/sundharam-19/HRmanagement_Automation.git

Navigate to Project

cd HRmanagement_Automation

Create Virtual Environment

python -m venv venv

Activate Virtual Environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

Install Dependencies

pip install -r requirements.txt


---

Running Test Cases

Run All Tests

pytest

Run Specific Test File

pytest test_claim_request.py

Run Tests with Detailed Output

pytest -v


---

Generate Allure Report

Run Tests with Allure Results

pytest --alluredir=allure-results

Generate Allure Report

allure serve allure-results


---

Sample Test Scenarios

Login Validation

Verify valid login functionality

Verify invalid login handling

Verify dashboard visibility after login


Forgot Password

Validate forgot password workflow

Verify reset confirmation message


Claim Request

Validate claim request submission

Verify successful claim processing


My Info Module

Validate employee profile access

Verify personal details visibility



---

Reporting

The framework generates:

Pytest execution reports

Allure interactive reports

Console logs

Execution status tracking



---

Best Practices Used

Page Object Model (POM)

Reusable methods

Explicit waits

Centralized configuration

Modular framework structure

Data-driven testing



---

Future Enhancements

Jenkins CI/CD integration

Docker support

Parallel test execution

Cross-browser execution

Screenshot capture on failure

Email report integration



---

Author

S Sundharam

GitHub: https://github.com/sundharam-19


---

Repository Link

https://github.com/sundharam-19/HRmanagement_Automation


---

License

This project is created for educational and automation practice purposes.
