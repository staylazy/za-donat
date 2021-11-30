import requests

# requests.post("http://127.0.0.1:5000/api/users", 
#         json={"username":"sam",
#               "password":"python",
#               "role":"parent"})

# requests.post("http://127.0.0.1:5000/api/users", 
#         json={"username":"sam2",
#               "password":"python",
#               "role":"child"})

# print(requests.post(
#     "http://127.0.0.1:5000/api/del_task", 
#     json={"task":"poyt poyti ponuhat", "username":"sam2"}, 
#     auth=('sam','python')
#     ).text)


# print(requests.post(
#     "http://127.0.0.1:5000/api/post_task", 
#     json={"task":"poyt poyti ponuhat", "username":"sam"}, 
#     auth=("sam",'python')
#     ).text)

# print(requests.post(
#     "http://127.0.0.1:5000/api/post_task", 
#     json={"task":"poyt poyti ponuhat", "username":"sam2"}, 
#     auth=('sam2','python')
#     ).text)

# print(requests.get(
#     "http://127.0.0.1:5000/api/get_tasks", 
#     json={"username":"sam"}, 
#     auth=('sam','python')
#     ).text)

# print(requests.get(
#     "http://127.0.0.1:5000/api/get_tasks", 
#     json={"username":"sam2"}, 
#     auth=('sam2','python')
#     ).text)


print(requests.post(
    "http://127.0.0.1:5000/api/add_childs", 
    json={"childs":"sam2"}, 
    auth=("sam",'python')
    ).text)

print(requests.get(
   "http://127.0.0.1:5000/api/users/1"
    ).text)

print(requests.get(
   "http://127.0.0.1:5000/api/users/2"
    ).text)

