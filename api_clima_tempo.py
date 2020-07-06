import requests
import json

key = 'your-token-key'

def weather_today():
    cidade = input('Digite a cidade: ')
    DOMINIO = ('http://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&appid=your-token-key')
    r = requests.get(DOMINIO)
    parse_json = json.loads(r.text)

    temperatura = parse_json['main']['temp']
    temperatura_min = parse_json['main']['temp_min']
    temperatura_max = parse_json['main']['temp_max']

    tempo = parse_json['weather'][0]['main']
    tempo_desc = parse_json['weather'][0]['description']

    TEMPERATURAS = [
        temperatura,
        temperatura_min,
        temperatura_max,
    ]

    VER_TEMPERATURAS = []

    for temperatura in TEMPERATURAS:
        t = temperatura
        temp = (int(t) - 273.15)
        r = round(temp, 0)
        VER_TEMPERATURAS.append(r)

    consulta1 = VER_TEMPERATURAS[0]
    consulta2 = VER_TEMPERATURAS[1]
    consulta3 = VER_TEMPERATURAS[2]
    print('------------------------------------------')
    print('\nTemperatura agora {}ªC'.format(consulta1))
    print('Temperatura minima {}ªC'.format(consulta2))
    print('Temperatura Máxima {}ªC'.format(consulta3))
    print('Main {}'.format(tempo))
    print('description {}'.format(tempo_desc))
    print('------------------------------------------')