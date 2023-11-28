#這個檔案的作用是：建立功能列表

#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import TemplateSendMessage, URITemplateAction, CarouselTemplate, MessageTemplateAction, CarouselColumn, TextSendMessage
import random
import db
#===============LINEAPI=============================================

#以下是本檔案的內容本文

#1.建立旋轉木馬訊息，名為function_list(未來可以叫出此函數來使用)
#function_list的括號內是設定此函數呼叫時需要給函數的參數有哪些

def function_list():
    message = TemplateSendMessage(
        alt_text='功能列表',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/MMn2vqZ.png',
                    title='作品集',
                    text='各種網頁作品',
                    actions=[
                        MessageTemplateAction(
                            label='關於作品集',
                            text='好棒哦？'
                        ),
                        URITemplateAction(
                            label='點我看作品',
                            uri='https://eudemon.pythonanywhere.com/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/MMn2vqZ.png',
                    title='森森鈴蘭',
                    text='喜歡的vtuber',
                    actions=[
                        MessageTemplateAction(
                            label='vtuber介紹',
                            text='vtuber是什麼'
                        ),
                        URITemplateAction(
                            label='YT直播網址',
                            uri='https://www.youtube.com/@lilylinglan'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/MMn2vqZ.png',
                    title='喜歡的歌',
                    text='最喜歡有趣的歌',
                    actions=[
                        MessageTemplateAction(
                            label='瞭解更多',
                            text='這是誰唱的'
                        ),
                        URITemplateAction(
                            label='小嫦娥',
                            uri='https://www.youtube.com/watch?v=H_aer3jC0jE&list=RDH_aer3jC0jE&start_radio=1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/MMn2vqZ.png',
                    title='聯繫Eudemon本人',
                    text='直接聯繫Eudemon',
                    actions=[
                        MessageTemplateAction(
                            label='誰是Eudemon?',
                            text='Eudemon是誰？想認識'
                        ),
                        URITemplateAction(
                            label='加我的LINE',
                            uri='https://line.me/ti/p/kiGy4Pw7ib'
                        )
                    ]
                )
            ]
        )
    )
    return message

def dinner():
    id = random.randint(1,10)

    if id == 1:
        message = TextSendMessage(text="吃土啦")
    elif id == 2:
        message = TextSendMessage(text="喝飲料LA")
    else:
        message = TextSendMessage(text="自己想")

    return message

def medicine_list():
    id = random.randint(1,20)
    sql="SELECT * FROM newtest_test WHERE id='"+str(id)+"'"
    medicines = db.querydata(sql)
    message = TemplateSendMessage(
        alt_text='藥物',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=medicines["img"],
                    title=medicines["name"],
                    text='各種網頁作品',
                    actions=[
                        MessageTemplateAction(
                            label='關於作品集',
                            text='好棒哦？'
                        ),
                        URITemplateAction(
                            label='點我看作品',
                            uri="https://eudemon.pythonanywhere.com/detail/"+id+""
                        )
                    ]
                ),     
            ]
        )
    )
    return message