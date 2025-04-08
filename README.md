# Secure Medical Data Project

## Project Overview
This project simulates a secure medical data handling system with a focus on protecting against membership inference attacks (MIA). It incorporates various security techniques, including differential privacy, PII redaction, access control, and file encryption, to ensure data confidentiality and user privacy.

## Modules Breakdown
- `data/`: Contains raw and processed datasets.
- `scripts/`: Contains core functionality and modules.
    - `attacks/`: Contains scripts to simulate various attacks on medical data.
    - `defenses/`: Contains scripts implementing various defenses against attacks on medical data.
    - `core/`: Contains core modules and functionalities for the project.
    - `utils/`: Contains utility scripts and helper functions.
    - `main.py`: Entry point for the project.
    - `evaluate.py`: Evaluation logic for the project.
- `logs/`: Contains access logs and audit trails.
- `models/`: Contains model files or placeholders.
- `results/`: Contains attack results and graphs.
- `tests/`: Contains unit tests for the project.

## How to Run
1. Ensure you have Python 3 installed.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the main script using `python secure-medical-data-project/scripts/main.py`.

## Security Techniques Used
- **PII Redaction**: Uses regular expressions to detect and redact personally identifiable information (PII) from medical records.
- **Differential Privacy**: Implements DP-SGD to train models with differential privacy, protecting against membership inference attacks.
- **Access Control**: Simulates role-based access control to restrict access to sensitive data.
- **File Encryption**: Encrypts sensitive files using Fernet encryption to ensure data confidentiality.

## Results Summary
The project simulates a membership inference attack and evaluates the effectiveness of the implemented security techniques. The results are logged to the console and can be visualized using matplotlib.
