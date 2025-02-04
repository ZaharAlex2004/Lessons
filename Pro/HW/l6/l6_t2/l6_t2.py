import requests


def page(url, filename):
    try:
        response = requests.get(url)

        response.raise_for_status()

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"Site saved in {filename}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"RequestException: {err}")


# Пример использования
site = "https://gortransport.kharkov.ua"
file = "page_content.txt"

page(site, file)