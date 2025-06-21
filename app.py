from flask import Flask, render_template, request, send_file
import json
import csv

app = Flask(__name__)

# Load airdrop data from file
with open("airdrop_results.json") as f:
    data = json.load(f)

@app.route("/", methods=["GET"])
def dashboard():
    query = request.args.get("search")
    results = data

    if query:
        query = query.strip().lower()
        results = [row for row in data if query in row["wallet"].lower()]

    return render_template("dashboard.html", results=results)

@app.route("/download")
def download():
    # Write filtered or full data to CSV for download
    with open("airdrop_data.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["wallet", "index", "status"])
        writer.writeheader()
        writer.writerows(data)

    return send_file("airdrop_data.csv", as_attachment=True)
