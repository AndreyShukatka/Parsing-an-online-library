import requests

book_id = 10
url = "https://tululu.org/txt.php"

def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError
    return


def downloads_books():
    for book in range(book_id):
        params = {'id': book + 1}
        response = requests.get(url, params=params)
        response.raise_for_status()
        filename = f'books/id {book + 1}.txt'
        try:
            check_for_redirect(response)
        except requests.HTTPError:
            continue
        with open(filename, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    downloads_books()
