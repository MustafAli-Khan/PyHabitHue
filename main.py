from datetime import datetime
import requests

USERNAME = "mustafali"
TOKEN = "dfhed34cd43dfh34hr4"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "gc01",
    "name": "CodeGrid",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now().strftime("%Y%m%d")


pixel_data = {
    "date": today,
    "quantity": input("How many minutes do you code?\n"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)



update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today}"

new_pixel_data = {
    "quantity": "5"
}


# response = requests.put(url=update_endpoint,  json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today}"

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
