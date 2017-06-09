import requests
from pathlib import Path
from PIL import Image
import time
import urllib.request
import json

LOOP_ACTIVE = True
id = 0
clientId = "zE0lkJXP3Hzc_iobeTFx" #"V5zJ1IQ1QL5FpklEW4ra"
clientSecret = "EHGLQ8DSF5" #"nrDY4PduHo"
url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

data = 0
searchData = 0
done = False

def CFR_Process():
    global id, clientId, clientSecret, url
    while(1):
            fileName = str(id) + ".jpg"
            file = Path(fileName)
            if file.is_file():
                id += 1
                continue
            else:
                break

    while(1):
        fileName = str(id) + ".jpg"
        image = Image.init()

        while(1):
            try:
                image = Image.open(fileName)
                break
            except:
                continue

        time.sleep(1)
        rotatedImage = image.rotate(-90, expand = 1)
        rotatedImage.save(fileName)

        files = {'image': open(fileName, 'rb')}
        headers = {'X-Naver-Client-Id': clientId, 'X-Naver-Client-Secret': clientSecret }
        response = requests.post(url,  files=files, headers=headers)
        rescode = response.status_code
        if(rescode == 200):
            global data, searchData, done
            data = response.json()
            if(data['info']['faceCount'] == 1):
                print("%d번째 얼굴은 %s을(를) %.1lf%c 닮았습니다." % (id, data['faces'][0]['celebrity']['value'], data['faces'][0]['celebrity']['confidence'] * 100.0, '%'))

                encText = urllib.parse.quote(data['faces'][0]['celebrity']['value'])
                searchUrl = "https://openapi.naver.com/v1/search/image?query=" + encText  # json 결과
                request = urllib.request.Request(searchUrl)
                request.add_header("X-Naver-Client-Id", clientId)
                request.add_header("X-Naver-Client-Secret", clientSecret)
                searchResponse = urllib.request.urlopen(request)
                searchRescode = searchResponse.getcode()
                if (searchRescode == 200):
                    responseBody = searchResponse.read()
                    searchData =  json.loads(responseBody.decode('utf-8'))
                    print(searchData['items'][0]['link'])
                else:
                    print("Error Code:" + searchRescode)
            else:
                print("얼굴이 없습니다.")
        else:
            print("Error Code:", rescode)

        id += 1

