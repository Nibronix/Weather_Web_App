from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import generate_csrf
import requests
import secret_key

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'my-secret-key'
csrf = CSRFProtect(app)
API_KEY = secret_key.API_KEY


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        city = request.form['city']
        url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&days=1"
        response = requests.get(url).json()

        weather_data = {
            'city': response['location']['name'],
            'temperature': response['current']['temp_f'],
            'description': response['current']['condition']['text'],
            'icon': response['current']['condition']['icon']
        }

        return render_template('index.html', weather_data=weather_data, csrf_token=request.form['csrf_token'])
    else:
        print("Weather data is not available.")
        csrf_token = generate_csrf()
        return render_template('index.html', csrf_token=csrf_token)


if __name__ == '__main__':
    app.run(debug=True)
