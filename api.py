from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/date', methods=['GET'])
def get_current_date():
    result = subprocess.check_output(['date']).decode('utf-8').strip()
    return jsonify({'date': result})

@app.route('/cal', methods=['GET'])
def get_calendar():
    result = subprocess.check_output(['cal']).decode('utf-8').strip()
    return jsonify({'calendar': result})

@app.route('/docker', methods=['GET'])
def get_docker_info():
    result = subprocess.check_output(['docker', 'info']).decode('utf-8').strip()
    return jsonify({'docker_info': result})

if __name__ == '__main__':
    app.run()
