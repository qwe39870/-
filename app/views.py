from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.conf import settings

from linebot import WebhookHandler, LineBotApi
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, URITemplateAction, CarouselTemplate, MessageTemplateAction, CarouselColumn

from function import function_list,dinner,medicine_list

line_bot_api = LineBotApi('OFYecLIa0Jf/oG3DarhVPnhHG0wOvWl8LVnuAsLiIsA4+uvlKQ1h4dHOWVJiMSUNvdJcQoV6cxfah7id2GGnx+fbIp7bAxyJtSL/YP3t7s1T5uLXMotcEIPwFhAwNfCK2cN8be+Rkt8x2G0xsHtALwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d600365b0debbc75ad76959dc1245df7')

@method_decorator(csrf_exempt, name='dispatch')
class CallbackView(View):
    def post(self, request, *args, **kwargs):
        signature = request.META.get('HTTP_X_LINE_SIGNATURE', '')
        body = request.body.decode('utf-8')
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponse(status=400)
        return HttpResponse(status=200)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    
    if '測試' in msg:
        message = function_list()

    elif '晚餐' in msg:
        message = dinner()

    elif '藥' in msg:
        message = medicine_list

    else:
        message = TextSendMessage(text="測試不成功")

    line_bot_api.reply_message(event.reply_token,message)

    # TemplateSendMessage(
    #         alt_text='功能列表',
    #         template=CarouselTemplate(
    #             columns=[
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkl5qgGtBxZbBu921rynn7HN7C7JaD_Hbi5cMMV5gEgQu2mE-rIw',
    #                     title='Maso萬事屋百貨',
    #                     text='百萬種商品一站購足',
    #                     actions=[
    #                         MessageTemplateAction(
    #                             label='關於Maso百貨',
    #                             text='Maso萬事屋百貨是什麼呢？'
    #                         ),
    #                         URITemplateAction(
    #                             label='點我逛百貨',
    #                             uri='https://tw.shop.com/maso0310'
    #                         )
    #                     ]
    #                 ),
    #             ]
    #         )
    #     )

    # message = TextSendMessage(text="測試"+event.message.text)
    # line_bot_api.reply_message(event.reply_token,message)
