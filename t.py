import requests
# try:
#     token = requests.get("http://127.0.0.1:5000/api/token", auth=('sam', 'pytho')).json()['token']
# except:
#     print(requests.get("http://127.0.0.1:5000/api/token", auth=('sam', 'python')).text)
# print(token)
# 
# print(requests.get("http://127.0.0.1:5000/api/resource", auth=('eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzNzU5NjM2MSwiZXhwIjoxNjM3NTk2OTYxfQ.eyJpZCI6MX0.nBRX_fLJYn7hQ8ihb8MgLQj406ReRa_RYd7MtrNEODrO8RWAGGAKMB-HeBt2sWKfxcV6PbKoiE0B00xt4YHziw', 'unused')).text)



# requests.post("http://127.0.0.1:5000/api/users", json={"username":"sam","password":"python"})
#print(requests.get("http://127.0.0.1:5000/api/token", auth=('sam', 'python')).text)
# print(requests.get("http://127.0.0.1:5000/api/resource", auth=('eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzNzY5MTQ5MiwiZXhwIjoxNjM3NjkyMDkyfQ.eyJpZCI6MX0.0EAud2hPeyGYGyDe4d5zGHG-JKhv9ksIcw5utfogk7ENrmZwaJUycIN3IaLgiQWbGauWKiNRliNJgUMizLmyOQ', 'unused')).text)
#print(requests.post("http://127.0.0.1:5000/api/post_task", json={"task":"poyti bebru poyti nazad i ponuhat", "username":"sam"}).text)
print(requests.get("http://127.0.0.1:5000/api/get_task", json={"username":"sam"}, auth=('eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzNzY5MjY2NCwiZXhwIjoxNjM3NjkzMjY0fQ.eyJpZCI6MX0.8Qv8mCQc7HGLrTNOkdHfhs6VnvRo-NxVYMBhRzdN9mzRhuCSsZ4qcPMO0MKw88Yj2lTKDT0f19suNIPUawGh3w','unused')).text)