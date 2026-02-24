# Password-Security-Assessment-and-Resilience-Analyzer
A real-time web application that helps users assess the strength of their passwords, understand security weaknesses, and generate strong, secure passwords. This interactive dashboard provides entropy calculation, crack time estimation ,AI pattern detection, and attack simulation and a criteria checklist .

Password Security Assessment and Resilience Analyzer By Digital Vault

A real-time web application to evaluate the strength of your passwords, detect security weaknesses, and generate strong, resilient passwords. This interactive dashboard integrates entropy calculation, crack time estimation, AI pattern detection, attack simulation, and security criteria validation in one professional interface.

Project Overview Digital Vault’s Password Security and Resilience Analyzer is designed to help users understand why some passwords are weak and how to create stronger ones. The tool provides: Real-time password strength scoring Entropy calculation for security assessment Crack time estimation for different attack scenarios AI-based pattern detection (common passwords, sequences, repeated chars, low diversity, weak substrings, year patterns) Criteria checklist validation Attack simulation: brute-force, dictionary, and AI pattern attacks Secure password generation

This project combines frontend interactivity with a Python Flask backend, delivering a responsive and professional cybersecurity dashboard.

Key Features

Real-Time Password Strength Analysis
Entropy-Based Security Scoring
Crack Time Visualization
Criteria Validation: Minimum 8 characters Recommended 12+ characters Lowercase, Uppercase, Numbers, Special symbols AI Pattern Detection compliance
Advanced AI Pattern Detection: Common passwords (password, 123456, qwerty, etc.) Sequential letters and numbers Repeated characters or pattern blocks Weak substrings (pass, login, admin) Low character diversity Year patterns (1900–2099)
Attack Simulation: Brute-force Dictionary attack AI Pattern attack vulnerability
Cryptographically Secure Password Generation
Modern, Interactive Dashboard UI
Technologies Used Frontend: HTML, CSS, JavaScript Backend: Python, Flask Data Communication: JSON

Project Structure

Password Security Analyzer/ ├── app.py # Flask backend ├── templates/ │ └── index.html # Frontend UI ├── static/ │ ├── style.css # Styling │ └── script.js # Frontend logic ├── requirements.txt # Python dependencies └── README.md # Project documentation

Installation & Usage

Install Python 3.8+
Install dependencies pip install -r requirements.txt
Run the Flask application python app.py
Open your browser http://127.0.0.1:5000/
Start testing passwords Type your password Click Generate for a strong random password Toggle visibility with the eye icon
How It Works

User enters a password in the input field.
Frontend JavaScript captures the input and sends it to the Flask backend via POST request.
Backend processes the password: Calculates entropy Estimates crack time Validates security criteria Runs AI pattern detection Simulates attacks (brute-force, dictionary, AI-based)
Frontend updates dynamically with: Strength bar and text Criteria checklist with ✅/❌ Attack simulation results AI pattern warnings
AI Pattern Detection Details The system checks for: Common passwords Sequential characters (letters/numbers) Repeated characters or pattern blocks Weak substrings Low character diversity Year patterns (1900–2099) Detected patterns reduce the password strength score and are highlighted in the dashboard.

Security Concepts Used Entropy calculation Character pool analysis Brute-force and dictionary attack modeling AI-based pattern detection for modern password attacks

Future Improvements Deploy to cloud platforms (Render/Heroku) Add user authentication module Integrate database for password history tracking AI-based password scoring with machine learning Admin dashboard for enterprise password security monitoring

Developed By Ameesha Kumari & Digital Vault Team

