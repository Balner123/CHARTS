from flask import Flask, render_template
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    data = fetch_weather_data()
    hourly_data = get_hourly_data(data)
    return render_template('index.html', hourly_data=hourly_data)

if __name__ == '__main__':
    app.run(debug=True)
