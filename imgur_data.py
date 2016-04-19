from imgurpython import ImgurClient

from client_data import get_id, get_secret

client_id = get_id()
client_secret = get_secret()

client = ImgurClient(client_id, client_secret)

# Example request
items = client.gallery()
for item in items:
    #print(item.link)
    pass

def test_test(number):
    return number + 10