# Flask Automation Test Dashboard

A Flask web application that provides an interactive interface to run automated tests using Playwright and display Allure reports in real-time. The application allows users to execute tests with a click of a button and view the results instantly.

## Features

- **Automated Test Execution:** Run Playwright tests directly from the web interface with a single click.
- **Real-time Test Reports:** View detailed Allure test reports right after the test execution.
- **User-friendly Interface:** Simple and intuitive design for easy navigation and test management.

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python** (version 3.8 or higher)
- **Flask**
- **Playwright** and **pytest**
- **Allure** for generating test reports

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name

2. **Set up a virtual environment:**
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. **Install the required packages:**
    pip install -r requirements.txt

4. **Install Playwright and Allure:**
    playwright install
    npm install -g allure-commandline --save-dev


## Running the Application

1. **Start the Flask server:**
    python app.py

2. **Access the application:**
    Open your browser and go to `http://127.0.0.1:5000/`.

3. **Run Tests:**
    - Click the "Run Tests" button to execute the Playwright tests.
    - View the Allure report directly within the interface.

## File Structure
- **app.py**: The main Flask application file.
- **templates/**: Contains the HTML files for the user interface.
- **static/**: Contains CSS and JavaScript files.
- **allure-results/**: Directory where Allure test results are stored.
- **allure-report/**: Generated Allure report files.

## How to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.


## Contact
For any questions or suggestions, please contact khaledtanim@gmail.com

