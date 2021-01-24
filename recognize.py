import requests
def recognize2(url):
    import requests
    import base64
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    img = url.split(',')[1]
    params = {"image": img}
    access_token = '获取的access_token'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
    response = response.json()
    return response
