from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect, generate_csrf
import requests
import secret_key

app = Flask(__name__, static_url_path='/static')  # Create an instance of the Flask app
app.config['SECRET_KEY'] = 'my-secret-key'  # Set a secret key for the app
csrf = CSRFProtect(app)  # Add CSRF protection to the app using Flask-WTF
API_KEY = secret_key.API_KEY  # Import API key from secret_key.py

# Create a route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # If the user submits a form
        city = request.form['city']  # Get the city name from the form
        url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&days=1"  # Create API URL with city name and API key
        response = requests.get(url).json()  # Get the JSON response from the API

        # Store relevant data from the API response in a dictionary
        weather_data = {
            'city': response['location']['name'],
            'temperature': response['current']['temp_f'],
            'description': response['current']['condition']['text'],
            'icon': response['current']['condition']['icon']
        }

        # Render the index.html template with the weather data and the CSRF token
        return render_template('index.html', weather_data=weather_data, csrf_token=request.form['csrf_token'])

    # If the user accesses the homepage without submitting a form
    else:
        print("Weather data is not available.")

        # Generate a new CSRF token
        csrf_token = generate_csrf()
        # Render the index.html template with the CSRF token
        return render_template('index.html', csrf_token=csrf_token)

# Start the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
