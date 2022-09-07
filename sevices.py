import httpx
import os
import secrets

from settings import settings


def get_response(urls: tuple) -> None:
    data = zip(urls, [url.split('/')[-1] for url in urls])

    if not os.path.exists(settings.static_path):
        os.mkdir(settings.static_path)

    for url, file_name in data:

        print(f'Отправка запроса на {url}')

        response = httpx.get(url, timeout=None)

        file_to_save = settings.static_path + f'{file_name}.json'
        if os.path.exists(file_to_save):
            print('A file with this name already exists')
            default = secrets.token_hex(6)
            file_to_save = settings.static_path + f'{file_name}_{default}.json'

        try:
            with open(f'{file_to_save}', 'w') as file:
                file.write(str(response.json()))
        except Exception as e:
            raise e

        print(f'Ответ сервера {response.status_code}')
