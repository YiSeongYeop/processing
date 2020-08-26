
#libraries
import random
from unicode import join_jamos

#global variables
mouseClick = False
s1 = -100
input_str = ""
answer_str = ""
kor_input_str = []
eng_kor = {'q':u'ㅂ','w':u'ㅈ','e':u'ㄷ','r':u'ㄱ','t':u'ㅅ','y':u'ㅛ','u':u'ㅕ',
           'i':u'ㅑ','o':u'ㅐ','p':u'ㅔ','a':u'ㅁ','s':u'ㄴ','d':u'ㅇ','f':u'ㄹ',
           'g':u'ㅎ','h':u'ㅗ','j':u'ㅓ','k':u'ㅏ','l':u'ㅣ','z':u'ㅋ','x':u'ㅌ',
           'c':u'ㅊ','v':u'ㅍ','b':u'ㅠ','n':u'ㅜ','m':u'ㅡ'}
  #game pages
Main = True
Lang = False
Kor = False
Eng = False
  #game characteristic
Dif = 0 #Easy, Normal, Hard, Extreme
Life = 3 #3
Score = 0 #over 10000, game win
  #word list
Eng_list1 = ["cat","apple","banana","monkey"]
Eng_list2 = ["cat","apple","banana","monkey"]
Eng_list3 = ["cat","apple","banana","monkey"]
Eng_list4 = ["cat","apple","banana","monkey"]
Kor_list1 = [u"고양이",u"사과",u"바나나",u"원숭이"]
Kor_list2 = [u"고양이",u"사과",u"바나나",u"원숭이"]
Kor_list3 = [u"고양이",u"사과",u"바나나",u"원숭이"]
Kor_list4 = [u"고양이",u"사과",u"바나나",u"원숭이"]
Total_list = []

#word class
class words(object):
    def __init__ (self, x, y, word):
        self.x = x
        self.y = y
        self.word = word
        self.indisplay = True
        
    def update(self):
        self.y += 1
        
    def display(self):
        text(self.word, self.x, self.y)

#setup page
def setup():
    size(1200,800)
    textAlign(CENTER, CENTER)
    background(77,169,225)
    font = createFont("DotumChe",32)
    textFont(font)
    #NotoSansCJKkr-Regular
#draw page
def draw():
    global input_str, answer_str, s1, Main, Lang, Eng, Kor, Dif, Life, Score, mouseClick, Eng_list1, Kor_list1, Eng_list2, Kor_list2, Eng_list3, Kor_list3, Eng_list4, Kor_list4,Total_list
    #palette init
    background(77,169,225)
    #ground and cloud
    fill(0,200,0)
    stroke(0,200,0)
    rect(0,720,1200,80)
    
    fill(240,248,255)
    stroke(240,248,255)
    ellipse(150,100,70,50)
    ellipse(850,100,70,50)
    
    fill(240,248,255)
    stroke(240,248,255)
    ellipse(350,100,70,50)
    ellipse(385,80,70,50)
    ellipse(385,120,70,50)
    ellipse(420,100,70,50)
    
    #main display
    if Main:
        textSize(80)
        stroke(255)
        text("Word Rain Game", width/2, height/2.5)
        
        #language and difficulty
        fill(255)
        rect(400,400,120,50)
        rect(700,400,120,50)
        fill(0)
        textSize(32)
        text("English", 460, 420)
        text(u"한글", 760, 420)
                
        if mouseClick:
            if mouseX > 400 and mouseX < 520 and mouseY > 400 and mouseY < 450:
                print("English choosed")
                Main = False
                Lang = True
                Eng = True
            elif mouseX > 700 and mouseX < 820 and mouseY > 400 and mouseY < 450:
                print("Korean choosed")
                Main = False
                Lang = True
                Kor = True
            else:
                pass
            mouseClick = False
    #after choosing lang, choosing difficulty display
    if Lang:
        if Eng:
            fill(255)
            rect(240,400,120,50)
            rect(440,400,120,50)
            rect(640,400,120,50)
            rect(840,400,120,50)
            fill(0)
            textSize(32)
            text("Easy", 300, 420)
            text("Normal", 500, 420)
            text("Hard", 700, 420)
            text("Extreme", 900, 420)
            
            if mouseClick:
                if mouseX > 300 and mouseX < 420 and mouseY > 400 and mouseY < 450:
                    print("Easy choosed")
                    Dif = 1200
                    Lang = False
                elif mouseX > 500 and mouseX < 620 and mouseY > 400 and mouseY < 450:
                    print("Normal choosed")
                    Dif = 1100
                    Lang = False
                elif mouseX > 700 and mouseX < 820 and mouseY > 400 and mouseY < 450:
                    print("Hard choosed")
                    Dif = 1000
                    Lang = False
                elif mouseX > 900 and mouseX < 1020 and mouseY > 400 and mouseY < 450:
                    print("Extreme choosed")
                    Dif = 900
                    Lang = False
                else:
                    pass
                mouseClick = False
        elif Kor:
            fill(255)
            rect(240,400,120,50)
            rect(440,400,120,50)
            rect(640,400,120,50)
            rect(840,400,120,50)
            fill(0)
            textSize(32)
            text(u"쉬움", 300, 420)
            text(u"보통", 500, 420)
            text(u"어려움", 700, 420)
            text(u"극악", 900, 420)
            if mouseClick:
                if mouseX > 300 and mouseX < 420 and mouseY > 400 and mouseY < 450:
                    print("Easy choosed")
                    Dif = 1000
                    Lang = False
                elif mouseX > 500 and mouseX < 620 and mouseY > 400 and mouseY < 450:
                    print("Normal choosed")
                    Dif = 900
                    Lang = False
                elif mouseX > 700 and mouseX < 820 and mouseY > 400 and mouseY < 450:
                    print("Hard choosed")
                    Dif = 800
                    Lang = False
                elif mouseX > 900 and mouseX < 1020 and mouseY > 400 and mouseY < 450:
                    print("Extreme choosed")
                    Dif = 700
                    Lang = False
                else:
                    pass
                mouseClick = False
        else:
            pass
    
    #real game display
    if Main == False and Lang == False:
        #lang and difficulty know
        if Eng:
            if Dif == 1200:
                word_list = Eng_list1
            elif Dif == 1100:
                word_list = Eng_list2
            elif Dif == 1000:
                word_list = Eng_list3
            elif Dif == 900:
                word_list = Eng_list4
        if Kor:
            if Dif == 1000:
                word_list = Kor_list1
            elif Dif == 900:
                word_list = Kor_list2
            elif Dif == 800:
                word_list = Kor_list3
            elif Dif == 700:
                word_list = Kor_list4
        text(input_str, 600, 760)
        s2 = millis()
        if s2-s1 >= Dif:
            word = words(random.randrange(100,1100), 50, random.choice(word_list))
            Total_list.append(word)
            s1 = millis()
        for i in range(len(Total_list)):
            if Total_list[i].indisplay:
                if answer_str == Total_list[i].word:
                    Score += 100
                    Total_list[i].indisplay = False
                    if Score >= 10000:
                        text("Game Win", width/2, height/2)
                        noLoop()
                    answer_str = ""
                    continue
                Total_list[i].update()
                if Total_list[i].y > 750:
                    Total_list[i].indisplay = False
                    Life -= 1
                    if Life == 0:
                        text("Game Over", width/2, height/2)
                        noLoop()
                Total_list[i].display()
        answer_str = ""
        
        #score display
        fill(255)
        textSize(32)
        text(Score, 1100, 760)
        #life display
        img = loadImage("heart.png")
        for i in range(Life):
            image(img,20+i*55,745,50,50)
        
            
def mouseClicked():
    global mouseClick
    mouseClick = True
    
def keyPressed():
    global input_str, answer_str, kor_input_str
    if Eng:
        if (key == ENTER):
            answer_str = input_str
            input_str = ""
            return
        input_str += key
    if Kor:
        if (key == ENTER):
            answer_str = join_jamos(kor_input_str)
            kor_input_str = []
            return
        kor_input_str.append(eng_kor[key])
        print(kor_input_str)
