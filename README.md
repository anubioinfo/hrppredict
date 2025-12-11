# HRP Predict – High-Risk Pregnancy Classification (PoC)

**HRP Predict** is a demonstration project showcasing how Machine Learning can assist in identifying potential **High-Risk Pregnancy (HRP)** cases using key antenatal care (ANC) parameters.  
This Proof of Concept (PoC) was originally built to demonstrate feasibility for internal stakeholders in a public health program.

> **Note:** This project uses **dummy data only**. It is not intended for real-world clinical use without proper validation.

---

## Features

- Web-based interface built using **Django**
- Simple, interpretable ML classification model
- Accepts key ANC inputs:
  - Weeks of Pregnancy  
  - Age  
  - Hemoglobin (HB) Level  
  - BP Systolic  
  - BP Diastolic  
- Predicts risk category (Low / Medium / High)
- Displays basic suggestions and interpretation

---
## Project Structure

hrppredict/
│
├── hrp/                 # Django application
│   ├── templates/       # HTML templates
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── hrppredict/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md


## How to Run the Project

### Prerequisites
- **Python 3.x**
- **Django** installed  
  ```bash
  pip install django


Setup Instructions

Clone the repository

git clone https://github.com/anubioinfo/hrppredict


Navigate to the project directory

cd hrppredict


Start the Django development server

python3 manage.py runserver


Open the application in your browser

http://127.0.0.1:8000/

How to Use the Tool

This PoC demonstrates how a simple ML model can assist in early identification of high-risk pregnancy based on ANC input parameters.
Once the application is running:
Enter the following ANC inputs:

- Weeks of Pregnancy
- Age
- HB Level
- BP Systolic
- BP Diastolic
Click Submit

The tool will process the inputs through the ML classification model and display:
Predicted HRP risk category

Simple, explanatory suggestions
This project illustrates how AI could support community health workers (e.g., ANMs) in decision support workflows.

Disclaimer
This project uses dummy/generated data and is for demonstration only.
It must not be used for real-world clinical or medical decision-making.

A production-grade solution would require:
Real ANC datasets
Proper ML model development and validation
Clinical expert review
Medical ethics and regulatory compliance
