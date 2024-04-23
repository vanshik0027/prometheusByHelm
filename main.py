from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics 
app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = request.form['data']
        # Process data as needed
        return f'Received data via POST: {data}'

@app.route('/data/<data>', methods=['GET'])
def get_data(data):
    return f'Received data via GET: {data}'

if __name__ == '__main__':
    app.run(debug=True, port=7000)
