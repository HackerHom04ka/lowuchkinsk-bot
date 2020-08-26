import requests
import json

class vk(object):
    """
    :param token: access_token группы или пользователя
    :type token: str
    :param v: Версия API
    :type v: str
    """
    
    def __init__(self, token, v='5.122'):
        self.token = token
        self.v = v

    def send_message(self, peer_id, text=None, attachment=None, keyboard=None):
        """
        :type keyboard: str or dict
        """

        if isinstance(keyboard, (dict, list)):
            keyboard = json.dumps(keyboard)

        requests.post('https://api.vk.com/method/messages.send', params={'access_token': self.token, 'v': self.v, 'random_id': 0, 'peer_id': peer_id, 'message': text, 'attachment': attachment, 'keyboard': keyboard})
        return 'ok'
    
    def inputIMG(self, photo, peer_id):
        res1 = requests.post('https://api.vk.com/method/photos.getMessagesUploadServer', params={'access_token': self.token, 'v': self.v, 'random_id': 0, 'peer_id': peer_id}).json()
        res2 = requests.post(res1['upload_url'], files={'photo': photo}).json()
        res3 = requests.post('https://api.vk.com/method/photos.saveMessagesPhoto', params={'access_token': self.token, 'v': self.v, 'photo': res2['photo'], 'server': res2['server'], 'hash': res2['hash']}).json()

        return 'photo' + res3['owner_id'] + '_' + res3['id']