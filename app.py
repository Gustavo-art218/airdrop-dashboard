from flask import Flask, render_template, request, send_file
import csv
import os
from io import StringIO
import json

app = Flask(__name__)

# Load results from JSON
with open('airdrop_results.json', 'r') as f:
    results = json.load(f)

@app.route('/', methods=['GET'])
def dashboard():
    query = request.args.get('query', '').lower()
    status_filter = request.args.get('status', '')

    filtered = []
    for row in results:
        wallet = row['wallet'].lower()
        status = row['status'].lower()
        if query in wallet or query in status:
            if status_filter == '' or status_filter.lower() == status:
                filtered.append(row)

    return render_template('dashboard.html', results=filtered)

@app.route('/download')
def download_csv():
    si = StringIO()
    writer = csv.DictWriter(si, fieldnames=["wallet", "index", "status"])
    writer.writeheader()
    writer.writerows(results)
    output = si.getvalue()
    si.close()

    return send_file(
        StringIO(output),
        mimetype='text/csv',
        as_attachment=True,
        download_name='airdrop_results.csv'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
