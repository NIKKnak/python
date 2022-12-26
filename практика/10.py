import json
import requests



response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
result = json.loads(response.text)
result = dict(result)

with open('USD.json', 'w' , encoding="UTF-8") as file:
    for i in result['Valute'].items():
        file.write(f"{i}\n")
        print(i)



print(result['Valute']['USD']['Value'])
print(result['Valute']['EUR']['Value'])


