def save_img(data):

    import os, stat
    import urllib.request

    img_url = data
    file_path = 'img'
    file_name = "pyt"
    try:
        # 是否有这个路径
        if not os.path.exists(file_path):
            # 创建路径
            os.makedirs(file_path)
            # 获得图片后缀
        # 拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, '.png')
        print(filename)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filename=filename)

    except IOError as e:
        print("IOError")
    except Exception as e:
        print("Exception")

def base64change(url):
    import base64
    img = base64.urlsafe_b64decode(url + '=' * (4 - len(url) % 4))
    fh = open("imageToSave.png", "wb")
    fh.write(img)
    fh.close()
def yanzheng(yanzheng):

    import base64
    import os
    lens = len(yanzheng)
    lenx = lens - (lens % 4 if lens % 4 else 4)
    try:
        result = base64.decodestrings(yanzheng[:lenx])
        print('flase')
    except:
        pass
        print('go')

    imgdata = base64.b64decode(yanzheng, '-_')
    #写文件
    file = open('1.jpg', 'wb')
    file.write(imgdata)
    file.close()

def decode_base64(data):
    import base64
    """Decode base64, padding being optional.
    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.
    """
    missing_padding = len(data) % 4
    data = data.encode('utf-8')
    if missing_padding != 0:
        data += b'=' * (4 - missing_padding)
        print('已装换')
    return base64.decodebytes(data)
