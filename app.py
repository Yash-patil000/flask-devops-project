from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>CI/CD Pipeline Successfully Deployed!</h1>"

@app.route("/health")
def health():
    return "Application is Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
