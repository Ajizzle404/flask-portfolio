from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    projects = [
        {"name": "DevOps Project-Learning", "desc": "Docker, Kubernetes, Terraform"},
        {"name": "Cloud Automation", "desc": "Infrastructure as Code"},
        {"name": "CI/CD Pipeline", "desc": "Jenkins, GitHub Actions"}
    ]
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
