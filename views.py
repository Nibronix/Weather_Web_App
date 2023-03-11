from django.shortcuts import render
import weather

def index(request):
    return render(request, 'index.html')

def get_weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        weather_data = weather.get_weather_data(city)
        context = {'weather_data': weather_data}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

print(weather_data)

