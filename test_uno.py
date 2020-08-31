import pytest
import requests
# for each test we wright this first two parametrs
import config

def test_u():
    # every time when we wright new FUNCTIONS we put after DEF -> test and _word()
    # we dont need to call exzact function at the end!!!
    # import requests
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

    respon = requests.post(config.diction["second"], json=config.body)
    print(respon)
    respon.status_code
    print(respon.status_code)
    respon.json
    print(respon.json())
    print(respon.cookies)
    print(respon.headers)

    # vsegda spashivaut REQUEST: get,delete; post and put we check body,
    # but at the begining i tested in postman and python

    assert respon.status_code == 200
    # assert respon.status_code == 404
    assert respon.json()["success"] == True

def test_two():
    # this is Python library
    requests.get(config.diction["first"])
    # go to postman and take URL from GET requests
    # combane REQUEST into VARIABLE
    # now we check our RESPONSE (this is class)
    response=requests.get(config.diction["first"])
    print(response)
    response.status_code
    # this is first mehond
    print(response.status_code)
    response.json
    # this is second method
    print(response.json())
    print(response.cookies)
    print(response.headers)
    assert response.status_code == 200
    assert response.json()["success"] == True


