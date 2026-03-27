from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"status": "success", "message": "Experiment 6: Backend is LIVE"}

if __name__ == "__main__":
    # host='0.0.0.0' is REQUIRED for Docker to talk to your Windows host
    app.run(host='0.0.0.0', port=8000)
