from flask import Flask, render_template, send_from_directory, jsonify
import subprocess
import shutil
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-tests', methods=['POST'])
def run_tests():
    try:
        # Paths to directories
        allure_results_dir = 'allure-results'
        allure_report_dir = 'allure-report'
        test_file_path = r"D:\playwright_automation\Test check\test_mfs_admin_portal.py"

        # Remove old Allure results and report if they exist
        if os.path.exists(allure_results_dir):
            shutil.rmtree(allure_results_dir)
        if os.path.exists(allure_report_dir):
            shutil.rmtree(allure_report_dir)
        
        # Run the specific test file and generate Allure results
        subprocess.run(["pytest", test_file_path, "--alluredir=allure-results"], check=True)
        
        # Generate the Allure report
        allure_cmd_path = r'C:\Users\khaled.showkot\AppData\Roaming\npm\allure.cmd'
        subprocess.run([allure_cmd_path, "generate", "allure-results", "--clean", "-o", "allure-report"], check=True)
        
        # Return the path to the generated report
        return jsonify({'message': 'Tests completed successfully', 'report': '/allure-report/index.html'})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'Error running tests or generating report'}), 500

@app.route('/allure-report/<path:filename>')
def serve_report(filename):
    return send_from_directory('allure-report', filename)


if __name__ == '__main__':
    app.run(debug=True)
