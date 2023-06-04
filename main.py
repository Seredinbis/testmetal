from flask import Flask, request

app = Flask(__name__)

webh_data = Noneq

@app.route('/', methods=['POST', 'GET', 'PUT'])
def webhook():
    # data = request.get_json()  # получаем данные из запроса в формате JSON
    global webh_data
    webh_data = request.json
    print(webh_data)  # выводим полученные данные в консоль
    print()
    print(webh_data['object']['source'])
    print(webh_data['object']['source']['pay'])
    print(webh_data['object']['source']['pay']['first'])
    return '200'  # отправляем ответ серверу, чтобы он знал, что запрос успешно обработан


app.run(host='0.0.0.0', debug=True, port=5000)  # запускаем приложение в режиме отладки