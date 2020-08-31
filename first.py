import requests
# # this is Python library
# requests.get("https://www.qa.saatchiart.com/easel_api/artwork/413499/6858357")
# # go to postman and take URL from GET requests
# # combane REQUEST into VARIABLE
# # now we check our RESPONSE (this is class)
# response=requests.get("https://www.qa.saatchiart.com/easel_api/artwork/413499/6858357")
# print(response)
# response.status_code
# # this is first mehond
# print(response.status_code)
# response.json
# # this is second method
# print(response.json())
# print(response.cookies)
# print(response.headers)
body={ "budget":"1500",
    "email":"coco@gmail.com",
    "firstName":"CoCo",
    "lastName":"Chanel"
       }
respon = requests.post("https://www.qa.saatchiart.com/easel_api/aaquiz",json=body)
print(respon)
respon.status_code
print(respon.status_code)
respon.json
print(respon.json())
print(respon.cookies)
print(respon.headers)

#vsegda spashivaut REQUEST: get,delete; post and put we check body,
# but at the begining i tested in postman and python