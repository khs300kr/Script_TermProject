loopFlag = 11
#from internetbook import *

def PrintMenu():
    print("========Menu==========")
    print("사진 촬영(p/P)")
    print("연예인 랭킹 검색(r/R)")
    print("프로그램 종료(q/Q)")
    print("----------------------------------------")
def launcherFunction(menu):
    if menu == 'p' or menu == 'P':
        pass
    elif menu == 'r' or menu == 'R':
        pass
    elif menu == 'q' or menu == 'Q':
        QuitMenu()

def QuitMenu():
    global loopFlag
    loopFlag = 0
    print("quit")

##### run #####
while(loopFlag > 0):
    PrintMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")