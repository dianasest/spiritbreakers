from django.shortcuts import render
from .models import Data
import folium
from folium import plugins
# Create your views here.


def Map(request):
    data = Data.objects.all()
    data_list = Data.objects.values_list('latitude', 'longitude')
    adress_list = Data.objects.values_list('country')
    map1 = folium.Map(location=[42.8746, 74.5698], zoom_start=13)
    icon = plugins.BeautifyIcon(icon="marker")
    for i in range(0,len(data_list)):
        folium.Marker(
            location=[data_list[i][0], data_list[i][1]],
            popup=f"<p>АДРЕС:{adress_list[i]}</p><p>наличие денег:10000</p><p>РЕЖИМ РАБОТЫ: 9.00 до 17.30</p><button style='background-color:green;color:white;outline:none;'>ОТПРАВИТЬ ЗАЯВКУ</button>").add_to(map1)

    map1 = map1._repr_html_()
    context = {
        'map1': map1,
    }
    return render(request, 'map.html', context)

def Table(request):
    atms = Data.objects.all() 
    context = {
    'atms':atms,
    }
    return render(request, "table.html", context)

def Home(request):
    return render(request,"home.html")