from GlobalVriables import *
from tkinter import *
import threading
############################### CFR_API ###############################
import requests
from pathlib import Path
import time
import urllib.request
import json
############################### PILLOW ###############################
from io import BytesIO
import urllib
from PIL import Image,ImageTk


class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.g_Tk.quit()

    def mouse(self, event):
        global scene
        if event.x < 300:
            scene = "waiting"
            self.change_scene(scene+".gif");

    def change_scene(self, path):
        global ImageLabel
        img = PhotoImage(file=path)
        ImageLabel.configure(image=img)
        ImageLabel.image = img

    def Render_celebrity(self,url):
        global CelebrityLabel

        with urllib.request.urlopen(url) as u:
            raw_data = u.read()

        im = Image.open(BytesIO(raw_data))
        im = im.resize((320, 400), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(im)

        CelebrityLabel = Label(self.g_Tk, image=img, height=400, width=320)
        CelebrityLabel.configure(image=img)
        CelebrityLabel.image = img

        CelebrityLabel.pack()
        CelebrityLabel.place(x=120, y=80)


    def run(self):
        global scene, photo, ImageLabel

        self.g_Tk = Tk()
        self.g_Tk.wm_title("Project_CFR")
        SetCenter = (self.g_Tk.winfo_screenwidth() // 2) - 450
        self.g_Tk.geometry("{0}x{1}+{2}+0".format(WINDOW_WIDTH, WINDOW_HEIGHT, SetCenter))
        self.g_Tk.protocol("WM_DELETE_WINDOW", self.callback)
        self.g_Tk.bind("<Button-1>", self.mouse)

        # Scene
        photo = PhotoImage(file="MainMenu.gif")
        ImageLabel = Label(self.g_Tk, image=photo)
        ImageLabel.pack()

        self.g_Tk.mainloop()


def CFR_Process():
    global id, clientId, clientSecret, url
    # File Search
    while(1):
            fileName = str(id) + ".jpg"
            file = Path(fileName)
            if file.is_file():
                id += 1
                continue
            else:
                break

    # After Search
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
                    RenderResult(searchData['items'][0]['link'])
                else:
                    print("Error Code:" + searchRescode)
            else:
                print("얼굴이 없습니다.")
        else:
            print("Error Code:", rescode)
        id += 1


def RenderResult(searchUrl):
    global app, scene

    scene = "ShowResult"
    app.change_scene("ShowResult.gif")
    app.Render_celebrity(searchUrl)

def main():
    global app
    app = App()
    CFR_Process()

if __name__ == '__main__':
    main()
