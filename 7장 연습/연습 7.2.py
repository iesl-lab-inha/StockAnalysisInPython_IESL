import requests
import json

def post_message(token, channel, text, attachments):
    attachments = json.dumps(attachments)
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text, "attachments": attachments}
    )

markdown_text = '''
This message is plain.
*This message is bold.*
`This message is code.`
_This message is italic._
~This message is strike.~
'''

attach_dict = {
    "color"      :'#ff0000',
    "author_name":'INVESTMENT',
    "title"      :'오늘의 증시 KOSPI',
    "title_link" :'http://finance.naver.com/sise/sise_index.nhn?code=KOSPI',
    "text"       :'2,326.13 △11.89 (+0.51%)',
    "image_url"  :'https://ssl.pstatic.net/imgstock/chart3/day/KOSPI.png'
}
attach_list = [attach_dict]

post_message('xoxb-3865209074087-3882244789620-xI1s77B392q0TB5zZaAKY5lY', '#일반', markdown_text, attach_list)