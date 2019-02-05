from bps import app

@app.route('/')
def index():
    return 'Hello World!'