import base64
import cv2
import requests
import os
from aip import AipOcr

def tailor_video(fname):
    sourceFileName = fname
    video_path = os.path.join(os.getcwd(), sourceFileName + '.mp4')
    times = 0
    # take a snap every 10 frames
    frameFrequency = 10
    outPutDirName = os.getcwd() + '\\video\\' + sourceFileName + '\\'
    if not os.path.exists(outPutDirName):
        os.makedirs(outPutDirName)
    camera = cv2.VideoCapture(video_path)
    while True:
        times += 1
        ret, image = camera.read()
        if not ret:
            print('not ret, not image')
            break
        if times % frameFrequency == 0:
            cv2.imwrite(outPutDirName + str(times) + '.jpg', image)
            print(outPutDirName + str(times) + '.jpg')
    print('end')

def text_create(name, msg):
    path = os.getcwd()
    fullPath = path + '\\' + name + '.txt'
    file = open(fullPath, 'w')
    file.write(msg)
    file.close()

def tailor(path1,path2,begin,end,step_size):  #截取字幕
    for i in range(begin,end,step_size):
        fname1=path1 % str(i)
        print(fname1)
        img = cv2.imread(fname1)
        print(img.shape)
        cropped = img[620:655, 1550:1820]  # 裁剪坐标为[y0:y1, x0:x1]
        imgray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
        thresh = 85
        ret, binary = cv2.threshold(imgray, thresh, 255, cv2.THRESH_BINARY)  # 输入灰度图，输出二值图
        binary1 = cv2.bitwise_not(binary)  # 取反
        cv2.imwrite(path2 % str(i), binary1)


def requestApi(img):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    #request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    params = {"image": img,'language_type':'CHN_ENG'}
    access_token = '24.83c542bf725fa9f946a62e4be476655a.2592000.1597155714.282335-21277708'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    results=response.json()
    return results

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        # 将读取出来的图片转换为b64encode编码格式
        return base64.b64encode(fp.read())
# 定义函数字幕，用来对字幕进行操作
# step_size 步长
def subtitle(fname,begin,end,step_size):
    array =[] #定义一个数组用来存放words
    for i in range(begin,end,step_size):  #begin开始，end结束，循环按照步长step_size遍历，共有419张图片，也就是（1,420,10）
        fname1=fname % str(i)
        print(fname1)
        image = get_file_content(fname1)
        try:
            results=requestApi(image)['words_result']  #调用requestApi函数，获取json字符串中的words_result
            print(results)
            for item in results:
                #if is_Chinese(item['words']):
                array.append(item['words'])

        except Exception as e:
            print(e)

    text=''
    result = list(set(array))  # 将array数组准换为一个无序不重复元素集达到去重的效果，再转为列表
    result.sort(key=array.index) # 利用sort将数组中的元素即字幕重新排序，达到视频播放字幕的顺序
    for item in result:
        print(item)
        text+=item+'\n'
    text_create('test1',text)

if __name__=="__main__":
    path1 = 'C:\\Users\\Oculii_CN\\Desktop\\AUTODETECT\\video\\Video6_1\\%s.jpg'
    path2 = 'C:\\Users\\Oculii_CN\\Desktop\\AUTODETECT\\video\\img\\%s.jpg'
    print("""
    1. pic tailor
    2. text distill
    3. video tailor
    """)
    choose = input()
    begin = 10
    end = 30
    step_size = 10
    if choose == '1':
        tailor(path1, path2, begin, end, step_size)
    if choose == '2':
        subtitle(path2, begin, end, step_size)
    if choose == '3':
        tailor_video()
    #tailor_video('Video6_1')