import requests
from pathlib import Path
from PIL import Image
import time

LOOP_ACTIVE = True
id = 0
clientId = "V5zJ1IQ1QL5FpklEW4ra" #zE0lkJXP3Hzc_iobeTFx"
clientSecret = "nrDY4PduHo" #"EHGLQ8DSF5"
url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

data = 0
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

    fileName = str(id) + ".jpg"

    image = Image.init()

    while(1):
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
            global data, done
            data = response.json()
            if(data['info']['faceCount'] == 1):
                print("%d번째 얼굴은 %s을(를) %.1lf%c 닮았습니다." % (id, data['faces'][0]['celebrity']['value'], data['faces'][0]['celebrity']['confidence'] * 100.0, '%'))
            else:
                print("얼굴이 없습니다.")
        else:
            print("Error Code:", rescode)

        id += 1
        done = True

        break

