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
        global is_QUIT
        is_QUIT = True
        self.g_Tk.quit()

    def mouse(self, event):
        # Quit
        if event.x > 640 and event.x < 850 and event.y < 780 and event.y > 730:
            self.callback()
        # Rank
        elif event.x > 45 and event.x < 280 and event.y < 780 and event.y > 730:
            pass

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

    def Rendner_myface(self):
        global id
        path = str(id) + ".jpg"

        im = Image.open(path)
        im = im.resize((235, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(im)

        ImageLabel = Label(self.g_Tk, image=img, height=300, width=235)
        ImageLabel.configure(image = img)
        ImageLabel.image = img
        ImageLabel.pack()
        ImageLabel.place(x=530,y=130)

    def Redner_rankfaces(self):
        global id
        path = str(id) + ".jpg"

        im1 = Image.open(path)
        im1 = im1.resize((160, 200), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(im1)

        ImageLabel1 = Label(self.g_Tk, image=img1, height=200, width=160)
        ImageLabel1.configure(image=img1)
        ImageLabel1.image = img1
        ImageLabel1.pack()
        ImageLabel1.place(x=40, y=520)

        im2 = Image.open(path)
        im2 = im2.resize((160, 200), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(im2)

        ImageLabel2 = Label(self.g_Tk, image=img2, height=200, width=160)
        ImageLabel2.configure(image=img2)
        ImageLabel2.image = img2
        ImageLabel2.pack()
        ImageLabel2.place(x=210, y=520)

        im3 = Image.open(path)
        im3 = im3.resize((160, 200), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(im3)

        ImageLabel3 = Label(self.g_Tk, image=img3, height=200, width=160)
        ImageLabel3.configure(image=img3)
        ImageLabel3.image = img3
        ImageLabel3.pack()
        ImageLabel3.place(x=380, y=520)

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
    global id, clientId, clientSecret, url, is_QUIT

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
            if is_QUIT == True:
                return False
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
                name = data['faces'][0]['celebrity']['value']
                confidence = data['faces'][0]['celebrity']['confidence'] * 100.0

                print("%d번째 얼굴은 %s을(를) %.1lf%c 닮았습니다." % (id, name, confidence, '%'))

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

                    with open('./FaceJSONData.json', 'r') as f:
                        tempDict = json.load(f)

                    if (name in tempDict):
                        if (tempDict[name]['first']['confidence'] < confidence):
                            if ('third' in tempDict[name]):
                                tempDict[name]['third'] = tempDict[name]['second']
                                tempDict[name]['second'] = tempDict[name]['first']
                                tempDict[name]['first'] = {'confidence': confidence, 'file': fileName}
                            else:
                                if ('second' in tempDict[name]):
                                    tempDict[name].update({'third': tempDict[name]['second']})
                                    tempDict[name]['second'] = tempDict[name]['first']
                                    tempDict[name]['first'] = {'confidence': confidence, 'file': fileName}
                                else:
                                    tempDict[name].update({'second': tempDict[name]['first']})
                                    tempDict[name]['first'] = {'confidence': confidence, 'file': fileName}
                        else:
                            if ('second' in tempDict[name]):
                                if (tempDict[name]['second']['confidence'] < confidence):
                                    if ('third' in tempDict[name]):
                                        tempDict[name]['third'] = tempDict[name]['second']
                                        tempDict[name]['second'] = {'confidence': confidence, 'file': fileName}
                                    else:
                                        tempDict[name].update({'third': tempDict[name]['second']})
                                        tempDict[name]['second'] = {'confidence': confidence, 'file': fileName}
                                else:
                                    if ('third' in tempDict[name]):
                                        if (tempDict[name]['third']['confidence'] < confidence):
                                            tempDict[name]['third'] = {'confidence': confidence, 'file': fileName}
                                    else:
                                        if (tempDict[name]['third']['confidence'] < confidence):
                                            tempDict[name].update({'third': {'confidence': confidence, 'file': fileName}})
                            else:
                                tempDict[name].update({'second': {'confidence': confidence, 'file': fileName}})
                    else:
                        tempDict[name] = {'first': {'confidence': confidence, 'file': fileName}}

                    print(json.dumps(tempDict, ensure_ascii=False))

                    with open('./FaceJSONData.json', 'w') as f:
                        json.dump(tempDict, f, ensure_ascii=False)
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
    if scene == "ShowResult":
        app.change_scene("ShowResult.gif")
        app.Render_celebrity(searchUrl)
        app.Rendner_myface()
        app.Redner_rankfaces()

def main():
    global app
    app = App()
    CFR_Process()


if __name__ == '__main__':
    main()
