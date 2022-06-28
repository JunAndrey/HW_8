import requests
import json
from pprint import pprint



response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
all_json = json.loads(response.text)

def super_hero_compare(super_hero):
    sup_her = {}
    for line in all_json:
         if line['name'] in super_hero:
            sup_her[line['name']] = line['powerstats']['intelligence']
            sorted_dict = {}
    sorted_keys = sorted(sup_her, key=sup_her.get)
    for id in sorted_keys:
        sorted_dict[id] = sup_her[id]
        print(f'Интеллект супергероя {id} составляет {sorted_dict[id]}')

super_hero = ['Hulk', 'Captain America', 'Thanos']
super_hero_compare(super_hero)

"""Прога для загрузки файлов на ЯндексДиск"""
TOKEN = 'AQAAAABieK6SAADLW2JFXvAatUqGgJ6-cz9hs_w'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
class YandexDisk:
    def __init__(self, token):
        self.token = token
    def get_headers(self):
        return {'Content-Type': 'application/json',
        'Authorization': f'OAuth {TOKEN}'}
    def get_my_files_name(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response2 = requests.get(files_url, headers=headers)
        return response2.json()
    def get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {"path": disk_file_path, "overwrite": "true"}
        res = requests.get(upload_url, headers=headers, params=params)
        return res.json()

    def upload_files(self, disk_file_path, filename):
        response_href = self.get_upload_link(disk_file_path=disk_file_path)
        url = response_href.get("href", "")
        response = requests.put(url, data=open(filename, 'rb'))

if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    pprint(ya.get_my_files_name())
    ya.upload_files(disk_file_path="C\\Users\\Андрей\\PycharmProjects\\new_project\\test.txt", filename="test.txt")

