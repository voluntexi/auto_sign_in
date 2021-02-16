
import requests
def recognize(url):

    '''
    通用文字识别
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    img = url
    params = {"image":img}
    #tocken 由上面的touken()生成
    access_token = '24.44ba2a866c651be8fa8fb066a532331c.2592000.1614014544.282335-23581523'
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
    access_token = '24.44ba2a866c651be8fa8fb066a532331c.2592000.1614014544.282335-23581523'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
    response = response.json()
    return response

