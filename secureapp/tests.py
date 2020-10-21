from django.test import TestCase

# Create your tests here.
import requests
import json


TOKEN_URI = 'http://127.0.0.1:8000/token/'
EMP_BASE_URL='http://127.0.0.1:8000/employee/employee/api/v1/'
STUD_BASE_URL='http://127.0.0.1:8000/employee/student/api/v2/'

APP_TOKEN_STAFF= 'Token 46f38f06a731a72ea78ea3c0e79ab31d763be583'
APP_TOKEN_ADMIN= 'Token 0a40ca8d0e22affa60549c07639a84e0349886c0'


dict_token_staff= {'Authorization': APP_TOKEN_STAFF}
dict_token_Admin= {'Authorization': APP_TOKEN_ADMIN}


def get_token_for_user(user,pwd):
    response =requests.post(TOKEN_URI,json={"username":user,"password":pwd})
    print(response.status_code)
    # print(response.json())
    return response.json()

def get_all_emps_without_token():
    response = requests.get(EMP_BASE_URL)
    print('status code-->',response.status_code)
    print(response.json())


def get_all_studs_without_token():
    response = requests.get(STUD_BASE_URL)
    print('status code-->',response.status_code)
    print(response.json())

#
# def get_all_emps(token):
#     response = requests.get(EMP_BASE_URL,headers=token)
#     print('status code-->',response.status_code)
#     print(response.json())

def get_all_emps(token):
    employees={
              "name": "Praful",
              "age": 29,
              "salary": 70000,
              "desig": "Manager"
            }
    response = requests.post(EMP_BASE_URL,headers=token,json=employees)
    print('status code-->',response.status_code)
    print(response.json())


def get_all_students(token):
    response = requests.get(STUD_BASE_URL,headers=token)
    print('status code-->',response.status_code)
    print(response.json())


if __name__ == '__main__':
    response = get_token_for_user('mitentallewar','miten')
    print(response)
    app_token='Token {}'.format(response.get('token'))
    dict_token_val = {'Authorization': app_token}
    # # print("dict token value-->",dict_token_val)
    # get_all_emps_without_token()
    # print('---------------')
    # get_all_studs_without_token()

    # print('employees')
    get_all_emps(dict_token_val)
    # print("sudents")
    # get_all_students(dict_token_val)
