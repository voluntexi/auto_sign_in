
import requests
def recognize(url):

    '''
    通用文字识别
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    img = url
    params = {"image":img}
    #token 输入token
    access_token = '输入获取的token'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())
    response = response.json()
    return response
def json1(data):
    import json
    s = json.dumps(data)
    s1 = json.loads(s)
    s2 = str(s1["words_result"])
    s3 = s2.replace(' ', '')
    return s3[11:15]

def recognize2(url):
    import requests
    import base64

    '''
    通用文字识别（高精度版）
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    img = url.split(',')[1]
    params = {"image": img}
     #token 输入token
    access_token = '输入获取的token'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
    response = response.json()
    return response

