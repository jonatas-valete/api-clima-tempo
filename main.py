from api_2_7_dias import *

""""
    Bem-Vindos ao API de clima e tempo.
    Para consumir este API é necessário criar uma conta no site 'https://openweathermap.org/'
    será necessário criar também uma chave de acesso para usa-la
"""

if __name__ == '__main__':
    while True:
        mostrar_menu()
        opcao = input('Digite uma opção: ')
        if opcao == '1':
            clima_tempo_hoje = weather_today()
            print(clima_tempo_hoje)
        elif opcao == '2':
            consultar = input('Digite uma data para consulta, Exemplo; 2020-07-05 15:00:00'
                              ' (ano, mês e dia, hora padrão sempre 15:00:00): ')
            days = date_7_days()
            dates = data(days)
            if consultar == dates[0]:
                ver_temperature(0)
            elif consultar == dates[1]:
                ver_temperature(1)
            elif consultar == dates[2]:
                ver_temperature(2)
            elif consultar == dates[3]:
                ver_temperature(3)
            elif consultar == dates[4]:
                ver_temperature(4)
            elif consultar == dates[5]:
                ver_temperature(5)
            elif consultar == dates[6]:
                ver_temperature(6)
            elif consultar == dates[7]:
                ver_temperature(7)
        elif opcao == '3':
            print('Bye')
            break

