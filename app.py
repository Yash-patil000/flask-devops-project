from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "    <h1>🚀 Flask CI/CD Pipeline Successful!</h1>
    <h2>Application Deployed on Amazon EKS</h2>
    <p>Version: v2</p>
    <p>Built and Deployed using Jenkins Pipeline</p>
    """

@app.route("/health")
def health():
    return "Application is Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
