import requests

class FreeDictionary:
    def __init__(self):
        self.api_root = 'https://api.dictionaryapi.dev/api/v2/entries/en'

    def api_call(self, endpoint):
        url = '/'.join([self.api_root, endpoint])
        response = requests.get(url)
        return response.json()

    def get_definitions(self, word):
        return self.api_call(word)
