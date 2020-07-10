from datetime import datetime
from api_clima_tempo import *

one_call_api = 'eda5c12594a03dc52dc2018191872092'
key = 'de5d763fc253d3738b81b7feceff35d0'

API_CALL = ('https://api.openweathermap.org/data/2.5/onecall?'
            'lat=33.441792&lon=-94.037689&exclude=hourly,daily&appid=de5d763fc253d3738b81b7feceff35d0')

def long_lat():
    city = input('Digite a city: ')
    domain = ('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=de5d763fc253d3738b81b7feceff35d0')
    try:
        r = requests.get(domain)
        parse_json = json.loads(r.text)
        lon = parse_json['coord']['lat']
        lat = parse_json['coord']['lon']
        return (lon, lat)
    except Exception as e:
        print('{} fomarto inválido, digite uma cidade válida'.format(city))
        print(e)

def date_7_days():
    try:
        lon_lat = long_lat()
        lati = lon_lat[0]
        longi = lon_lat[1]
        lat = str(lati)
        lon = str(longi)
        api_call = ('https://api.openweathermap.org/data/2.5/onecall?'
                    'lat=' + lat + '&lon=' + lon + '&exclude=hourly&appid=de5d763fc253d3738b81b7feceff35d0')
        r = requests.get(api_call)
        parse_json = json.loads(r.text)
        prev_7_days = parse_json
        hoje = prev_7_days['daily'][0]
        segunda = prev_7_days['daily'][1]
        terca = prev_7_days['daily'][2]
        quarta = prev_7_days['daily'][3]
        quinta = prev_7_days['daily'][4]
        sexta = prev_7_days['daily'][5]
        sabado = prev_7_days['daily'][6]
        domingo = prev_7_days['daily'][7]
        dias = [hoje, segunda, terca, quarta, quinta, sexta, sabado, domingo]
        DIAS = []
        for dia in dias:
            data = dia['dt']
            DIAS.append(data)
        return(DIAS)
    except Exception as e:
        print(e)

def data(ver_forecast):
    data = []
    for i in ver_forecast:
        dia = int(i)
        ts = dia
        dat = (datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        data.append(dat)
    return(data)

def ver_temperature(dia):
    try:
        lon_lat = long_lat()
        lati = lon_lat[0]
        longi = lon_lat[1]
        lat = str(lati)
        lon = str(longi)
        api_call = ('https://api.openweathermap.org/data/2.5/onecall?'
                    'lat=' + lat + '&lon=' + lon + '&exclude=hourly&appid=your-token-key')
        r = requests.get(api_call)
        parse_json = json.loads(r.text)
        prev_7_days = parse_json

        hoje = prev_7_days['daily'][dia]
        data = hoje['dt']
        temp = hoje['temp']
        day = temp['day']
        min = temp['min']
        max = temp['max']
        weather = hoje['weather']
        main = weather[0]['main']
        description = weather[0]['description']
        temp_kelvin = [day, min, max]
        temp_celsius = []
        for i in temp_kelvin:
            t = i
            temp = (int(t) - 273.15)
            r = round(temp)
            temp_celsius.append(r)
        ts = data
        dat = (datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        day = ('day {}ºC'.format(temp_celsius[0]))
        min = ('min {}ºC'.format(temp_celsius[1]))
        max = ('max {}ºC '.format(temp_celsius[2]))
        print('-------------------------------------')
        print('Data e hora {}'.format(dat))
        print(day)
        print(min)
        print(max)
        print('main {}'.format(main))
        print('description {}'.format(description))
        print('-------------------------------------')
    except Exception as e:
        print(e)

def mostrar_menu():
    print('#################################')
    print('Escolha uma opção')
    print('1 - Ver clima e tempo de hoje')
    print('2 - especificar uma data')
    print('3 - Sair')
    print('#################################')
#ver_forecast = forecast_2_7_days()
#ver_data = data(ver_forecast)
#print(ver_data)
# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case





