########################## UI VARIABLES ##########################
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 800
scene = "MainMenu"
photo = 0
ImageLabel = 0
CelebrityLabel = 0
app = 0

is_QUIT = False

# Result
ResultRank1 = 0
ResultRank2 = 0
ResultRank3 = 0
ResultConf1 = 0
ResultConf2 = 0
ResultConf3 = 0
im1 = 0
im2 = 0
im3 = 0

# Rank
Rank1 = 0
Rank2 = 0
Rank3 = 0
Conf1 = 0
Conf2 = 0
Conf3 = 0
Rankim1 = 0
Rankim2 = 0
Rankim3 = 0

my_confidence = 0
my_celeb = 0

SearchLabel = 0

# Image ( Result )
MyImageLabel = 0
ImageLabel1 = 0
ImageLabel2 = 0
ImageLabel3 = 0
# Text ( Reuslt)
CelebLabel = 0
ConfiLabel = 0
RankLabel1 = 0
RankLabel2 = 0
RankLabel3 = 0

# Image (Rank)
RankImageLabel1 = 0
RankImageLabel2 = 0
RankImageLabel3 = 0

# Text(Can't Search)
NoResultLabel = 0

# Image (Mail)
EmailImageLabel = 0
SendToBox = 0
MailTitleBox = 0
SendButton = 0

########################## CFR VARIABLES ##########################
LOOP_ACTIVE = True
id = 0
clientId = "zE0lkJXP3Hzc_iobeTFx" #"V5zJ1IQ1QL5FpklEW4ra"
clientSecret = "EHGLQ8DSF5" #"nrDY4PduHo"
url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

data = 0
searchData = 0
done = False

######################################################################
# 사진 파일 경로
PicPath = "D:\Class\Senior\Script\Script_TermProject\CFR\Pictures"