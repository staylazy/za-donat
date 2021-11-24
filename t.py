import requests

# requests.post("http://127.0.0.1:5000/api/users", json={"username":"sam","password":"python"})
token = requests.get("http://127.0.0.1:5000/api/token", auth=('sam', 'python')).json()["token"]

print(requests.post(
    "http://127.0.0.1:5000/api/del_task", 
    json={"task":"poyt poyti ponuhat"}, 
    auth=(token,'unused')
    ).text)


# print(requests.post(
#     "http://127.0.0.1:5000/api/post_task", 
#     json={"task":"poyt poyti ponuhat", "username":"sam"}, 
#     auth=(token,'unused')
#     ).text)

# print(requests.get(
#     "http://127.0.0.1:5000/api/get_task", 
#     json={"username":"sam"}, 
#     auth=(token,'unused')
#     ).text)