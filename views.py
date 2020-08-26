from config import app, db, group_config
#from models import Person
from flask import request
import json
from vk_api import vk

@app.route('/bot', methods=['POST'])
def bot():
    # Распаковка данных
    data = json.loads(request.data)
    # Проверка на наличие поля 'type'
    if 'type' not in data.keys():
        return 'not \'type\' in keys'
    # Проверка группы
    if data['group_id'] == group_config['id']:
        # Проверка секретного ключа
        if data['secret'] == group_config['secret']:
            session = vk(group_config['token'])
            # Возвращение confirmationToken на сервер
            if data['type'] == 'confirmation':
                return group_config['confirm']
            # Если пришло сообщение
            if data['type'] == 'message_new':
                message = data['object']['message'] # Объект сообщения
                text = message['text'] # Текст сообщения
                payload = json.dumps(message['payload']) # Полезная нагрузка 
                peer_id = message['peer_id'] # Откудо пришло
                from_id = message['from_id'] # Кто прислал

                # Только в личных сообщениях
                if peer_id == from_id:
                    if(text.lower() == 'привет' or payload['button'] == '2'):
                        session.send_message(peer_id, text="ну хай.")
                # Только в беседах
                elif peer_id != from_id:
                    pass

                return 'ok'