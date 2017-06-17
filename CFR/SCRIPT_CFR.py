############################### GMAIL ###############################
# -*- coding: cp949 -*-
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#######################################################################
from GlobalVriables import *
from tkinter import *
from tkinter import font
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
import DoubleH
from PIL import ImageGrab


class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        global is_QUIT
        is_QUIT = True
        self.g_Tk.quit()

    # Mouse Event
    def mouse(self, event):
        global scene
        # Quit
        if event.x > 640 and event.x < 850 and event.y < 780 and event.y > 730 and scene == "MainMenu":
            self.callback()
        # Rank
        elif event.x > 45 and event.x < 280 and event.y < 780 and event.y > 730 and scene == "MainMenu":
            RenderRank()

        # Gmail
        if event.x > 610 and event.x < 850 and event.y < 600 and event.y > 570 and scene == "ShowResult":
            snapshot = ImageGrab.grab(bbox=(450 ,80, 1400 ,680))
            snapshot.save('Captures/im.gif')
            self.Render_Email()

        # Rank
        elif event.x > 630 and event.x < 825 and event.y < 690 and event.y > 650 and scene == "ShowResult":
            RenderRank()
    # Email UI
    def Render_Email(self):
        global EmailImageLabel, SendToBox, MailTitleBox, SendButton
        im = Image.open("Email.gif")
        im = im.resize((800, 700), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(im)

        EmailImageLabel = Label(self.g_Tk, image=img, height=700, width=800)
        EmailImageLabel.configure(image = img)
        EmailImageLabel.image = img
        EmailImageLabel.pack()
        EmailImageLabel.place(x=50,y=65)

        TempFont = font.Font(self.g_Tk,size = 13,weight ='bold', family = 'Consolas')
        SendToBox = Entry(self.g_Tk, font = TempFont, width = 35, borderwidth =12,
                           relief = 'ridge')
        SendToBox.pack()
        SendToBox.place(x=440, y=405)

        MailTitleBox = Entry(self.g_Tk, font = TempFont, width = 35, borderwidth =12,
                           relief = 'ridge')
        MailTitleBox.pack()
        MailTitleBox.place(x=440, y=455)

        SendButton = Button(self.g_Tk,text = "전송", command =self.sendGmail)
        SendButton.pack()
        SendButton.place (x= 445, y=530)

    def sendGmail(self):
        global EmailImageLabel
        global SendToBox,MailTitleBox, SendButton
        # global value
        host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
        port = "587"
        htmlFileName = "Captures/im.gif"

        senderAddr = "khs500kr@gmail.com"  # 보내는 사람 email 주소.
        recipientAddr = SendToBox.get()  # 받는 사람 email 주소.

        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = MailTitleBox.get()
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        # MIME 문서를 생성합니다.
        htmlFD = open(htmlFileName,'rb')

        HtmlPart = MIMEImage(htmlFD.read())
        htmlFD.close()

        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        msg.attach(HtmlPart)

        # 메일을 발송한다.
        s = mysmtplib.MySMTP(host, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("khs500kr@gmail.com", "script123")
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()

        if EmailImageLabel != 0:
            EmailImageLabel.destroy()
        if SendToBox != 0:
            SendToBox.destroy()
        if MailTitleBox != 0:
            MailTitleBox.destroy()
        if SendButton != 0:
            SendButton.destroy()


    # Rank UI
    def Render_Rank(self):
        global Rank1, Rank2, Rank3
        global Conf1, Conf2, Conf3
        global Rankim1, Rankim2, Rankim3
        global RankImageLabel1, RankImageLabel2, RankImageLabel3
        global RankLabel1, RankLabel2, RankLabel3


        if RankImageLabel1 != 0:
            RankImageLabel1.destroy()
        if RankImageLabel2 != 0:
            RankImageLabel2.destroy()
        if RankImageLabel3 != 0:
            RankImageLabel3.destroy()

            # Rank Text
        if RankLabel1 != 0:
            RankLabel1.destroy()
        if RankLabel2 != 0:
            RankLabel2.destroy()
        if RankLabel3 != 0:
            RankLabel3.destroy()


        if Rank1 != 0:
            Rankim1 = Image.open("Pictures/" +Rank1)
            RankLabel1 = Label(self.g_Tk, text=str(Conf1) + "%   ", bg="black", fg="white", font="Consolas")
            RankLabel1.pack()
            RankLabel1.place(x=190, y=710)
        else:
            Rankim1 = Image.open("NoImage.gif")

        Rankim1 = Rankim1.resize((240, 300), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(Rankim1)

        RankImageLabel1 = Label(self.g_Tk, image=img1, height=300, width=240)
        RankImageLabel1.configure(image=img1)
        RankImageLabel1.image = img1
        RankImageLabel1.pack()
        RankImageLabel1.place(x=40, y=386)
        Rank1 = 0

        if Rank2 != 0:
            Rankim2 = Image.open("Pictures/" +Rank2)
            RankLabel2 = Label(self.g_Tk, text=str(Conf2) + "%  ", bg="black", fg="white", font="Consolas")
            RankLabel2.pack()
            RankLabel2.place(x=480, y=710)
        else:
            Rankim2 = Image.open("NoImage.gif")

        Rankim2 = Rankim2.resize((240, 300), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(Rankim2)

        RankImageLabel2 = Label(self.g_Tk, image=img2, height=300, width=240)
        RankImageLabel2.configure(image=img2)
        RankImageLabel2.image = img2
        RankImageLabel2.pack()
        RankImageLabel2.place(x=330, y=386)
        Rank2 = 0

        if Rank3 != 0:
            Rankim3 = Image.open("Pictures/" +Rank3)
            RankLabel3 = Label(self.g_Tk, text=str(Conf3) + "%  ", bg="black", fg="white", font="Consolas")
            RankLabel3.pack()
            RankLabel3.place(x=770, y=710)
        else:
            Rankim3 = Image.open("NoImage.gif")

        Rankim3 = Rankim3.resize((240, 300), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(Rankim3)

        RankImageLabel3 = Label(self.g_Tk, image=img3, height=300, width=240)
        RankImageLabel3.configure(image=img3)
        RankImageLabel3.image = img3
        RankImageLabel3.pack()
        RankImageLabel3.place(x=620, y=386)
        Rank3 = 0

    def Input_Label(self):
        global SearchLabel
        if SearchLabel != 0:
            SearchLabel.destroy()

        TempFont = font.Font(self.g_Tk,size = 15,weight ='bold', family = 'Consolas')
        SearchLabel = Entry(self.g_Tk, font = TempFont, width = 35, borderwidth =12,
                           relief = 'ridge')
        SearchLabel.pack()
        SearchLabel.place(x=220, y=220)

    def search_button(self):
        TempFont = font.Font(self.g_Tk,size = 15,weight ='bold', family = 'Consolas')
        SearchButton = Button(self.g_Tk, font=TempFont, text="검색",
                              command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=650, y=225)

    def SearchButtonAction(self):
        global Rank1, Rank2, Rank3
        global Conf1, Conf2, Conf3
        global NoResultLabel

        name = SearchLabel.get()

        with open('./FaceJSONData.json', 'r') as f:
            dict = json.load(f)

        if name in dict:
            if NoResultLabel != 0:
                NoResultLabel.destroy()
            print(dict[name]['first']['confidence'])
            print(dict[name]['first']['file'])
            Rank1 = dict[name]['first']['file']
            Conf1 = round(dict[name]['first']['confidence'])
            if 'second' in dict[name]:
                print(dict[name]['second']['confidence'])
                print(dict[name]['second']['file'])
                Rank2 = dict[name]['second']['file']
                Conf2 = round(dict[name]['second']['confidence'])

                if 'third' in dict[name]:
                    print(dict[name]['third']['confidence'])
                    print(dict[name]['third']['file'])
                    Rank3 = dict[name]['third']['file']
                    Conf3 = round(dict[name]['third']['confidence'])

                else:
                    print("third가 없습니다.")
            else:
                print("second가 없습니다.")
        else:
            print("검색 결과가 존재하지 않습니다.")
            NoResultLabel = Label(self.g_Tk, text="검색 결과가 존재하지 않습니다.", bg = "black", fg= "white", font ="Consolas")
            NoResultLabel.pack()
            NoResultLabel.place(x=290,y=300)

        self.Render_Rank()

    # To change scene
    def change_scene(self, path):
        global ImageLabel
        img = PhotoImage(file=path)
        ImageLabel.configure(image=img)
        ImageLabel.image = img

    # Result
    def Render_celebrity(self,url):
        if scene == "ShowResult" :
            global CelebrityLabel, my_celeb, my_confidence
            global CelebLabel,ConfiLabel
            if CelebrityLabel != 0:
                CelebrityLabel.destroy()
                # Result Text
            if CelebLabel != 0:
                CelebLabel.destroy()
            if ConfiLabel != 0:
                ConfiLabel.destroy()

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

            # Text
            CelebLabel = Label(self.g_Tk, text = my_celeb + "  ",bg = "black", fg = "white", font = "Consolas")
            CelebLabel.pack()
            CelebLabel.place(x = 225, y = 485)

            ConfiLabel = Label(self.g_Tk, text = str(my_confidence) + "%    ",bg = "black", fg = "white", font = "Consolas")
            ConfiLabel.pack()
            ConfiLabel.place(x = 295 , y = 485)


    def Render_myface(self):
        global id, MyImageLabel
        path = "Pictures/" + str(id) + ".jpg"
        if MyImageLabel != 0:
            MyImageLabel.destroy()

        im = Image.open(path)
        im = im.resize((235, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(im)

        MyImageLabel = Label(self.g_Tk, image=img, height=300, width=235)
        MyImageLabel.configure(image = img)
        MyImageLabel.image = img
        MyImageLabel.pack()
        MyImageLabel.place(x=530,y=130)


    def Render_rankfaces(self):
        global ResultRank1, ResultRank2, ResultRank3
        global im1,im2,im3
        global ResultConf1, ResultConf2, ResultConf3
        global ImageLabel1,ImageLabel2,ImageLabel3
        global RankLabel1,RankLabel2,RankLabel3

        if ImageLabel1 != 0:
            ImageLabel1.destroy()
        if ImageLabel2 != 0:
            ImageLabel2.destroy()
        if ImageLabel3 != 0:
            ImageLabel3.destroy()
            # Rank Text
        if RankLabel1 != 0:
            RankLabel1.destroy()
        if RankLabel2 != 0:
            RankLabel2.destroy()
        if RankLabel3 != 0:
            RankLabel3.destroy()


        if ResultRank1 != 0:
            im1 = Image.open("Pictures/" +ResultRank1)
            RankLabel1 = Label(self.g_Tk, text=str(ResultConf1) + "%   ", bg="black", fg="white", font="Consolas")
            RankLabel1.place(x=150, y=740)
        else:
            im1 = Image.open("NoImage.gif")

        im1 = im1.resize((160, 200), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(im1)

        ImageLabel1 = Label(self.g_Tk, image=img1, height=200, width=160)
        ImageLabel1.configure(image=img1)
        ImageLabel1.image = img1
        ImageLabel1.pack()
        ImageLabel1.place(x=40, y=520)
        ResultRank1 = 0

        if ResultRank2 != 0:
            im2 = Image.open("Pictures/" +ResultRank2)
            RankLabel2 = Label(self.g_Tk, text=str(ResultConf2) + "%  ", bg="black", fg="white", font="Consolas")
            RankLabel2.place(x=320, y=740)
        else:
            im2 = Image.open("NoImage.gif")

        im2 = im2.resize((160, 200), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(im2)

        ImageLabel2 = Label(self.g_Tk, image=img2, height=200, width=160)
        ImageLabel2.configure(image=img2)
        ImageLabel2.image = img2
        ImageLabel2.pack()
        ImageLabel2.place(x=210, y=520)
        ResultRank2 = 0

        if ResultRank3 != 0:
            im3 = Image.open("Pictures/" +ResultRank3)
            RankLabel3 = Label(self.g_Tk, text=str(ResultConf3) + "%  ", bg="black", fg="white", font="Consolas")
            RankLabel3.place(x=490, y=740)
        else:
            im3 = Image.open("NoImage.gif")

        im3 = im3.resize((160, 200), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(im3)

        ImageLabel3 = Label(self.g_Tk, image=img3, height=200, width=160)
        ImageLabel3.configure(image=img3)
        ImageLabel3.image = img3
        ImageLabel3.pack()
        ImageLabel3.place(x=380, y=520)
        ResultRank3 = 0

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
    global id, clientId, clientSecret, url, is_QUIT, my_celeb, my_confidence

    # File Search
    id = DoubleH.CountCurrentFile(PicPath)

    # After Search
    while(1):
        fileName = str(id) + ".jpg"
        image = Image.init()

        while(1):
            if is_QUIT == True:
                return False
            try:
                image = Image.open("Pictures/" +fileName)
                break
            except:
                continue

        time.sleep(1)
        rotatedImage = image.rotate(-90, expand = 1)
        rotatedImage.save("Pictures/" +fileName)

        files = {'image': open("Pictures/" +fileName, 'rb')}
        headers = {'X-Naver-Client-Id': clientId, 'X-Naver-Client-Secret': clientSecret }
        response = requests.post(url,  files=files, headers=headers)
        rescode = response.status_code
        if(rescode == 200):
            global data, searchData, done
            data = response.json()
            if(data['info']['faceCount'] == 1):
                name = data['faces'][0]['celebrity']['value']
                confidence = round(data['faces'][0]['celebrity']['confidence'] * 100.0 )

                my_celeb = name
                my_confidence = confidence

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
                                        tempDict[name].update({'third': {'confidence': confidence, 'file': fileName}})
                            else:
                                tempDict[name].update({'second': {'confidence': confidence, 'file': fileName}})
                    else:
                        tempDict[name] = {'first': {'confidence': confidence, 'file': fileName}}

                    print(json.dumps(tempDict, ensure_ascii=False))

                    with open('./FaceJSONData.json', 'w') as f:
                        json.dump(tempDict, f, ensure_ascii=False)

                    ############################################################
                    with open('./FaceJSONData.json', 'r') as f:
                        dict = json.load(f)

                    # 검색
                    global ResultRank1, ResultRank2, ResultRank3
                    global ResultConf1, ResultConf2, ResultConf3

                    if name in dict:
                        print(dict[name]['first']['confidence'])
                        print(dict[name]['first']['file'])
                        ResultRank1 = dict[name]['first']['file']
                        ResultConf1 = round(dict[name]['first']['confidence'])
                        if 'second' in dict[name]:
                            print(dict[name]['second']['confidence'])
                            print(dict[name]['second']['file'])
                            ResultRank2 = dict[name]['second']['file']
                            ResultConf2 = round(dict[name]['second']['confidence'])

                            if 'third' in dict[name]:
                                print(dict[name]['third']['confidence'])
                                print(dict[name]['third']['file'])
                                ResultRank3 = dict[name]['third']['file']
                                ResultConf3 = round(dict[name]['third']['confidence'])

                            else:
                                print("third가 없습니다.")
                        else:
                            print("second가 없습니다.")
                    else:
                        print("검색 결과가 존재하지 않습니다.")
                    RenderResult(searchData['items'][0]['link'])

                        ############################################################
                else:
                    print("Error Code:" + searchRescode)
            else:
                print("얼굴이 없습니다.")
        else:
            print("Error Code:", rescode)
        id += 1


def RenderResult(searchUrl):
    global app, scene
    global RankImageLabel1, RankImageLabel2, RankImageLabel3
    global RankLabel1, RankLabel2, RankLabel3
    global SearchLabel
    global NoResultLabel

    if NoResultLabel != 0:
        NoResultLabel.destroy()
    if SearchLabel != 0:
        SearchLabel.destroy()
    if RankImageLabel1 != 0:
        RankImageLabel1.destroy()
    if RankImageLabel2 != 0:
        RankImageLabel2.destroy()
    if RankImageLabel3 != 0:
        RankImageLabel3.destroy()
        # Rank Text
    if RankLabel1 !=0:
        RankLabel1.destroy()
    if RankLabel2 !=0:
        RankLabel2.destroy()
    if RankLabel3 !=0:
        RankLabel3.destroy()

    scene = "ShowResult"
    if scene == "ShowResult":
        app.change_scene("ShowResult.gif")
        app.Render_celebrity(searchUrl)
        app.Render_myface()
        app.Render_rankfaces()

def RenderRank():
    global app,scene
    global CelebrityLabel
    global ImageLabel1, ImageLabel2, ImageLabel3
    global MyImageLabel
    global CelebLabel, ConfiLabel
    global RankLabel1, RankLabel2, RankLabel3

    if CelebrityLabel !=0:
        CelebrityLabel.destroy()
    if ImageLabel1 !=0:
        ImageLabel1.destroy()
    if ImageLabel2 !=0:
        ImageLabel2.destroy()
    if ImageLabel3 !=0:
        ImageLabel3.destroy()
    if MyImageLabel !=0:
        MyImageLabel.destroy()

        # Result Text
    if CelebLabel !=0:
        CelebLabel.destroy()
    if ConfiLabel !=0:
        ConfiLabel.destroy()
        # Rank Text
    if RankLabel1 !=0:
        RankLabel1.destroy()
    if RankLabel2 !=0:
        RankLabel2.destroy()
    if RankLabel3 !=0:
        RankLabel3.destroy()


    scene = "Rank"
    if scene == "Rank":
        app.change_scene(scene + ".gif")
        app.Input_Label()
        app.search_button()


def main():
    global app
    app = App()
    CFR_Process()


if __name__ == '__main__':
    main()
