import requests


response = requests.get("https://api.github.com/repos/hapifhir/hapi-fhir/pulls")
response_dict = response.json()
for i in range(len(response_dict)):
    print(response_dict[i]["user"]["login"])
    print(response_dict[i]["title"])