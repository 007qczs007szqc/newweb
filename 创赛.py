'''我的主页'''
import streamlit as st
from PIL import Image
import base64
import time
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的游戏作品推荐', '我的科普视频推荐','我的飞花令','我的计算器','我的留言区'])

def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

bar_bg('mybg1.jpg')

def qu(q,t1,t2,t3,t4,s,n,m = -1):
    st.write(q)
    c1,c2 = st.columns([1,1])
    with c1:
        cb1 = st.checkbox(t1)
    with c2:
        cb2 = st.checkbox(t2)
    c1,c2 = st.columns([1,1])
    with c1:
        cb3 = st.checkbox(t3)
    with c2:
        cb4 = st.checkbox(t4)
    l = [cb1, cb2, cb3, cb4]
    if st.button(f'第{n}章确认答案'):
        if l[s] == True:
            if(m>=0 and l[m] == True):
                a = l[m]
                l.pop(s)
                l.remove(a)
                if True not in l:
                    st.write('回答正确')
                else:
                    st.write('你快给我好好想想吧!')
            else:
                l.pop(s)
                if True not in l and m == -1:
                    st.write('回答正确')
                else:
                    st.write('你快给我好好想想吧!')
        else:
            st.write('你快给我好好想想吧!')
    st.write("")
    st.write("")

def img_cg(img1,r_,g_,b_):
    w,h = img1.size
    imga = img1.load()
    for x in range(w):
        for y in range(h):
            r = imga[x,y][r_]
            g = imga[x,y][g_]
            b = imga[x,y][b_]
            imga[x,y] = (r,g,b)
            
    return img1

def img_rm(img):
    w,h = img.size
    img.save("tp.png")
    img = Image.open("tp.png")
    imga = img.load()
    for x in range(w):
        for y in range(h):
            r = imga[x,y][0]
            g = imga[x,y][1]
            b = imga[x,y][2]
            if(r >= 230 and g >= 230 and b >= 230):
                imga[x,y] = (0,0,0,255)
            
    return img

def img_rt(img):
    r = st.slider('旋转角度:', 0, 360, 180)
    img = img.rotate(r,expand = True)
    return img

def img_rs(img):
    h = st.number_input("图片高度:",min_value = 1)
    w = st.number_input("图片宽度:",min_value = 1)
    img = img.resize((w,h))
    return img

def img_cp(img):
    ex = st.number_input("裁剪终点X坐标:",min_value = 1)
    ey = st.number_input("裁剪终点Y坐标:",min_value = 1)
    sx = st.number_input("裁剪起点X坐标:",min_value = 0,max_value = ex-1)
    sy = st.number_input("裁剪起点Y坐标:",min_value = 0,max_value = ey-1)
    img = img.crop((sx,sy,ex,ey))
    return img

def img_cc(img1):
    w,h = img1.size
    imga = img1.load()
    for x in range(w):
        for y in range(h):
            r = imga[x,y][0]
            g = imga[x,y][1]
            b = imga[x,y][2]
            imga[x,y] = (255-r,255-g,255-b)
            
    return img1

def img_a(img):
    w,h = img.size
    a = st.slider('透明度:', 1, 255, 100)
    img = img.convert("RGBA")
    imga = img.load()
    for x in range(w):
        for y in range(h):
            r = imga[x,y][0]
            g = imga[x,y][1]
            b = imga[x,y][2]
            imga[x,y] = (r,g,b,a)
            
    return img

def show_vedio(v):
    if v != "":
        with open(f"{v}.mp4","rb") as f:
            mymp4 = f.read()
        st.video(mymp4)

def audio():
    with open("bgm.mp3","rb") as f:
        mymp3 = f.read()
    st.audio(mymp3,format = "audio/mp3",start_time = 0)

def temp(word):
    with open("temp.txt","r",encoding="utf-8") as f:
        words_list = f.read().split("\n")
    words_list = set(words_list)
    words_list = list(words_list)
    if(" " not in word and word != ""):
        roading = st.progress(0, '开始加载')
        for i in range(1, 101, 1):
            time.sleep(0.02)
            roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
        for i in words_list:
            if word in i:
                st.write(i)

def page_1():
    '我的主页'
    st.image("mw.gif")
    audio()
    t1,t2,t3,t4 = st.tabs(["首页","科普视频","游戏作品","飞花令"])
    with t1:
        st.write("<span style='font-size:30px; color:blue'>:sunglasses:---------------我的图片处理工具----------------:sunglasses:</span>", unsafe_allow_html=True)
        st.write("可以对图片进行改色、抠图、旋转、缩放、裁剪、反色和更改透明度操作")
        st.write("")
        st.image("hp_or.png")
        st.write("")
        st.write("<span style='font-size:30px; color:blue'>:sunglasses:---------------我的游戏作品推荐----------------:sunglasses:</span>", unsafe_allow_html=True)
        st.write("用python制作的坦克征战、元素拼拼乐、我的世界、淘金者等游戏")
        st.write("")
        st.image("hp_or.png")
        st.write("")
        st.write("<span style='font-size:30px; color:blue'>:sunglasses:---------------我的科普视频推荐----------------:sunglasses:</span>", unsafe_allow_html=True)
        st.write("讲解夸克、引力红移、光速不变、三体水滴、链式反应等")
        st.write("")
        st.image("hp_or.png")
        st.write("")
        st.write("<span style='font-size:30px; color:blue'>:sunglasses:---------------我的飞花令----------------:sunglasses:</span>", unsafe_allow_html=True)
        st.write("腹有诗书气自华，诗书不尽待飞花！")
        st.write("")
        st.image("hp_or.png")
        st.write("")
        st.write("<span style='font-size:30px; color:blue'>:sunglasses:---------------我的计算器----------------:sunglasses:</span>", unsafe_allow_html=True)
        st.write("在这里计算，功能可不少嘞！")
        st.write("")
        st.image("hp_or.png")
        st.write("<span style='font-size:30px; color:blue'>:sunglasses:---------------我的留言区----------------:sunglasses:</span>", unsafe_allow_html=True)
        st.write("在这里尽情发言吧！")
        st.write("")
    with t2:
        st.image("sci.gif")
        st.write("<span style='font-size:30px; color:blue'>:sunglasses:---------------三体水滴----------------:sunglasses:</span>", unsafe_allow_html=True)
        st.image("tbc.jpg")
        show_vedio("tb")
    with t3:
        st.image("code.gif")
        st.write("<span style='font-size:30px; color:blue'>:sunglasses:---------------坦克征战----------------:sunglasses:</span>", unsafe_allow_html=True)
        st.image("tankc.png")
        show_vedio("tank")
    with t4:
        a1,a2,a3 = False, False, False
        q1,q2,q3 = False, False, False
        st.image("flour.gif")
        c0,c1,c2,c3,c4 = st.columns([0.8,1,1,1,2.2])
        with c1:
            a1 = st.button("花")
        with c2:
            a2 = st.button("月")
        with c3:
            a3 = st.button("春")
        if(q1 != a1):
            q1 = a1
            a2,a3 = False, False
            q2,q3 = False, False
        if(q2 != a2):
            q2 = a2
            a1,a3 = False, False
            q1,q3 = False, False
        if(q3 != a3):
            q3 = a3
            a2,a1 = False, False
            q2,q1 = False, False
        if a1:
            st.write("")
            st.write("飞花之字:花")
            st.write("")
            temp("花")
            st.snow()
        if a2:
            st.write("")
            st.write("飞花之字:月")
            st.write("")
            temp("月")
            st.balloons()
        if a3:
            st.write("")
            st.write("飞花之字:春")
            st.write("")
            temp("春")

def page_2():
    st.image("pil.gif")
    audio()
    st.write("<span style='font-size:30px; color:blue'>:smile:图片处理小程序:smile:</span>", unsafe_allow_html=True)
    up_file = st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if up_file:
        fn = up_file.name
        ft = up_file.type
        img = Image.open(up_file)
        fs = img.size
        st.write(f"图片宽度：{fs[0]}")
        st.write(f"图片高度：{fs[1]}")
        t1,t2,t3,t4,t5,t6,t7,t8 = st.tabs(["原图","改色","抠图","旋转","缩放","裁剪","反色","透明度"])
        si = 0
        with t1:
            st.image(img)
            si = img
        with t2:
            img1 = img
            new_img = img_cg(img1,1,2,0)
            si = new_img
            st.image(new_img)
        img = Image.open(up_file)
        with t3:
            new_img = img_rm(img)
            si = new_img
            st.image(new_img)
        img = Image.open(up_file)
        with t4:
            new_img = img_rt(img)
            si = new_img
            st.image(new_img)
        img = Image.open(up_file)
        with t5:
            new_img = img_rs(img)
            si = new_img
            st.image(new_img)
        img = Image.open(up_file)
        with t6:
            new_img = img_cp(img)
            si = new_img
            st.image(new_img)
        img = Image.open(up_file)
        with t7:
            new_img = img_cc(img)
            si = new_img
            st.image(new_img)
        img = Image.open(up_file)
        with t8:
            new_img = img_a(img)
            si = new_img
            st.image(new_img)
            
def page_3():
    st.image("code.gif")
    audio()
    t1,t2,t3,t4,t5,t6 = st.tabs(["我的世界","母亲节快乐","元素拼拼乐","淘金者","火星探索","其他作品"])
    with t1:
        st.write("<span style='font-size:20px; color:red'>:coffee:我的世界:coffee:</span>", unsafe_allow_html=True)
        st.image("mcc.png")
        show_vedio("exni")
    with t2:
        st.write("<span style='font-size:20px; color:red'>:coffee:母亲节快乐:coffee:</span>", unsafe_allow_html=True)
        st.image("smoc.png")
        show_vedio("smo")
    with t3:
        st.write("<span style='font-size:20px; color:red'>:coffee:元素拼拼乐:coffee:</span>", unsafe_allow_html=True)
        st.image("enc.png")
        show_vedio("en")
    with t4:
        st.write("<span style='font-size:20px; color:red'>:coffee:淘金者:coffee:</span>", unsafe_allow_html=True)
        st.image("goc.png")
        show_vedio("go")
    with t5:
        st.write("<span style='font-size:20px; color:red'>:coffee:坦克征战:coffee:</span>", unsafe_allow_html=True)
        st.image("marsc.png")
        show_vedio("Mars")
    with t6:
        st.link_button('我的Kitten作品主页', 'https://shequ.codemao.cn/user/6452625/')
        wos = ['1.  智子蚀刻','2.  计算器',"3.  文字游戏","4.  星际大战",
               "5.  星际迷航","6.  密室逃脱-校园篇","7.  抽奖游戏","8.  星光璀璨",
               "9.  小鸟觅食","10.  水滴消灭人类舰队","11.  水滴摧毁引力波发射场","12.  被掏空的水滴",
               "13.  射箭","14.  向日葵","15.  风扇转转转","16.  没有后羿的射日",
               "17.  彩色圆盘","18.  红心跳跳跳","19.  抢元宝","20.  日历时钟",
               "21.  引力弹弓","22.  硅犁","23.  音乐宝典","24.  外星探秘",
               "25.  大黄鸡","26.  傅里叶残影(后面有彩蛋)","27.  密室逃脱-普通篇","28.  捉住一个小兔崽"
              ]
        wo = ["https://lunar-turtle.codemao.cn/?entry=share&action=view_work&work_id=167432615",
              "https://tanyue-h5.codemao.cn/preview-player/2/233811024",
              "https://tanyue-h5.codemao.cn/preview-player/2/233812080",
              "https://tanyue-h5.codemao.cn/preview-player/2/233812173",
              "https://tanyue-h5.codemao.cn/preview-player/2/233812305",
              "https://tanyue-h5.codemao.cn/preview-player/2/233812393",
              "https://tanyue-h5.codemao.cn/preview-player/2/233812544",
              "https://tanyue-h5.codemao.cn/preview-player/2/233812714",
              "https://tanyue-h5.codemao.cn/preview-player/2/233812807",
              "https://tanyue-h5.codemao.cn/preview-player/2/233812933",
              "https://tanyue-h5.codemao.cn/preview-player/2/233813063",
              "https://tanyue-h5.codemao.cn/preview-player/2/233813107",
              "https://tanyue-h5.codemao.cn/preview-player/2/233813186",
              "https://tanyue-h5.codemao.cn/preview-player/2/233813293",
              "https://tanyue-h5.codemao.cn/preview-player/2/233813430",
              "https://tanyue-h5.codemao.cn/preview-player/2/233813469",
              "https://tanyue-h5.codemao.cn/preview-player/2/233813698",
              "https://tanyue-h5.codemao.cn/preview-player/2/233813765",
              "https://lunar-turtle.codemao.cn/?entry=share&action=view_work&work_id=174690816",
              "https://lunar-turtle.codemao.cn/?entry=share&action=view_work&work_id=161269516",
              "https://lunar-turtle.codemao.cn/?entry=share&action=view_work&work_id=171011961",
              "https://lunar-turtle.codemao.cn/?entry=share&action=view_work&work_id=171012204",
              "https://lunar-turtle.codemao.cn/?entry=share&action=view_work&work_id=145995810",
              "https://tanyue-h5.codemao.cn/preview-player/2/233815735",
              "https://lunar-turtle.codemao.cn/?entry=share&action=view_work&work_id=147063845",
              "https://tanyue-h5.codemao.cn/preview-player/2/233816692",
              "https://tanyue-h5.codemao.cn/preview-player/2/233817005",
              "https://tanyue-h5.codemao.cn/preview-player/2/233816350"
             ]
        go = int(st.selectbox('我的python作品', wos).split(".")[0]) - 1
        st.link_button('打开作品', wo[go])
        st.write("tips:有时你会打开前一个作品，你只需在选择后点击空白处，让红框消失就行")

def page_4():
    st.image("sci.gif")
    audio()
    t1,t2,t3,t4,t5,t6,t7,t8 = st.tabs(["夸克的秘密","引力红移","光速不变","链式反应","肥皂去污","古代高考","《红楼梦》与和珅","科普小问答"])
    with t1:
        st.write("<span style='font-size:30px; color:red'>:sun_with_face:夸克的秘密:sun_with_face:</span>", unsafe_allow_html=True)
        st.image("kkc.jpg")
        show_vedio("kk")
    with t2:
        st.write("<span style='font-size:30px; color:orange'>:sun_with_face:引力红移:sun_with_face:</span>", unsafe_allow_html=True)
        st.image("lwc.jpg")
        show_vedio("lw")
    with t3:
        st.write("<span style='font-size:30px; color:yellowgreen'>:sun_with_face:光速不变:sun_with_face:</span>", unsafe_allow_html=True)
        st.image("lic.jpg")
        show_vedio("li")
    with t4:
        st.write("<span style='font-size:30px; color:green'>:sun_with_face:链式反应:sun_with_face:</span>", unsafe_allow_html=True)
        st.image("hc.png")
        show_vedio("h")
    with t5:
        st.write("<span style='font-size:30px; color:cyan'>:sun_with_face:肥皂去污:sun_with_face:</span>", unsafe_allow_html=True)
        st.image("soapc.png")
        show_vedio("soap")
    with t6:
        st.write("<span style='font-size:30px; color:blue'>:sun_with_face:古代高考:sun_with_face:</span>", unsafe_allow_html=True)
        st.image("gkc.jpg")
        show_vedio("gk")
    with t7:
        st.write("<span style='font-size:30px; color:purple'>:sun_with_face:《红楼梦》与和珅:sun_with_face:</span>", unsafe_allow_html=True)
        st.image("rc.jpg")
        show_vedio("r")
    with t8:
        qu("第一章科普小问答:质子为什么带正电?","因为里面有1个上夸克和1个下夸克","因为里面有1个上夸克","因为里面有2个上夸克和1个下夸克","里面有1个上夸克和2个下夸克",2,1)
        qu("第二章科普小问答:在可见光中，下列说法正确的有?","红光的波长最长","紫光的波长最长","红光的频率最低","紫光的能量最低",0,2,2)
        qu("第三章科普小问答:如果一列火车以光速前进，打开车上的一盏灯，灯光也以光速前进，那么相对于地面，灯光的速度是每秒多少万千米?","每秒0万千米","每分30万千米","每秒60万千米","每秒30万千米",3,3)
        qu("第四章科普小问答:链式反应是用高速运动的（    ）去轰击原子核?","质子","中子","电子","中微子",1,4)
        qu("第五章科普小问答:下列说法正确的有?","肥皂分子的\"长尾巴\"喜欢油","肥皂分子的\"圆脑袋\"喜欢油","肥皂分子的\"长尾巴\"喜欢水","肥皂分子的\"圆脑袋\"喜欢水",0,5,3)
        qu("第六章科普小问答:下列说法正确的有?","乾隆年间连中三元的考生钱棨是杭州人","张謇原本考了第一名","张謇原本考了第六十名","温八叉是温庭筠的外号",3,6,2)
        qu("第七章科普小问答:和珅给谁讲《红楼梦》，使其得以流传?","皇后","皇帝","纪晓岚","太后",3,7)

def page_5():
    st.image("flour.gif")
    audio()
    st.write("飞花")
    word = st.text_input('请输入要飞花的字')
    temp(word)

def page_6():
    st.image("sa.gif")
    audio()
    num1 = st.number_input("输入第一个数字",value = 0.000)
    num2 = st.number_input("输入第二个数字",value = 0.000)
    f = st.selectbox("运算符", ["+","-","*","/","%"])
    if st.toggle('进制转换'):
        mode = int(st.selectbox("模式选择",["1.  10进制转2进制","2.  10进制转8进制","3.  10进制转16进制"])[0])
        num = st.number_input("输入数字",value = 1)
        if mode == 1:
            st.write(f"{bin(num)[2:]}")
        if mode == 2:
            st.write(f"{oct(num)[2:]}")
        if mode == 3:
            st.write(f"{hex(num)[2:]}")
    if(st.button("运算")):
        if f == "+":
            res = num1+num2
        if f == "-":
            res = num1-num2
        if f == "*":
            res = num1*num2
        if f == "/":
            res = num1/num2
        if f == "%":
            res = num1%num2
        st.write(f"<span style='font-size:30px; color:blue'>{num1}{f}{num2}={res}</span>",unsafe_allow_html=True)

def page_7():
    st.image("ma.gif")
    audio()
    st.write("我的留言区")
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    name = st.selectbox("我是......", ["阿短","编程猫","训练师","自定义"])
    if name == "自定义":
        name = st.text_input("我是......")
    ex = st.selectbox("表情:", ["🌈","❄️","⭐","❤️"])
    new_message = st.text_input("想要说的话......")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message,ex])
        with open("leave_messages.txt","w",encoding='utf-8') as f:
            message = ""
            for i in  messages_list:
                message += i[0] + "#" + i[1] + "#" + i[2] + "#" + i[3] + "\n"
            message = message[:-1]
            f.write(message)
    st.write("")
    st.write("")
    st.write("")
    choice = st.radio(
        '调查:你最喜欢的栏目',
        ['我的编程作品', '我的科普视频', '我的飞花令',"我的图片处理工具","我的计算器"]
    )
    st.write(f"你最喜欢:{choice}")
    if st.button("提交"):
        with open("leave_messages.txt","w",encoding='utf-8') as f:
            message = ""
            messages_list.append([str(int(messages_list[-1][0])+1), name, f"我最喜欢{choice}",ex])
            for i in  messages_list:
                message += i[0] + "#" + i[1] + "#" + i[2] + "#" + i[3] + "\n"
            message = message[:-1]
            f.write(message)
    st.write("")
    st.write("")
    st.write("")
    for i in messages_list:
        with st.chat_message(i[3]):
            st.write(i[1],":",i[2])
        
if (page == '我的兴趣推荐'):
    page_1()
elif (page == '我的图片处理工具') :
    page_2()
elif (page == '我的游戏作品推荐') :
    page_3()
elif (page == '我的科普视频推荐') :
    page_4()
elif (page == '我的飞花令') :
    page_5()
elif(page == '我的计算器') :
    page_6()
elif(page == '我的留言区') :
    page_7()
else :
    pass