import requests

id = 1
url = f"https://tululu.org/txt.php?id={id}"
response = requests.get(url)
response.raise_for_status()


while id != 11:
    filename = f'books/{id}.txt'
    with open(filename, 'wb') as file:
        file.write(response.content)
    id += 1