#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import my_settings

class ClovaSummary:
    # Clova Speech invoke URL
    

    url = 'https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize'
    client_id = my_settings.CLIENT_ID
    client_secret = my_settings.CLIENT_SECRET
    def req(self, content):
        request_body = {
            "document": {
                "content": content
            },
            "option": {
                "language": 'ko',
                "model": "general",
                "summaryCount": 3
            }
        }
        headers = {
            'Accept': 'application/json;UTF-8',
            'Content-Type': 'application/json;UTF-8',
            'X-NCP-APIGW-API-KEY-ID': self.client_id,
            'X-NCP-APIGW-API-KEY': self.client_secret
        }
        return requests.post(headers=headers,
                             url=self.url,
                             data=json.dumps(request_body).encode('UTF-8'))




if __name__ == '__main__':
    res = ClovaSummary().req("걱정이 되니까 묻는 거야. 회의록 대상이 있고 뭐 교수나 전문가 전문가 회의가 아니고 어느 길이. 그냥 소 회의록이 지금. 수업이나 그래서 나 온라인 때문에 많이 들어오고 있잖아. 그렇지. 그리고 이 소 회의록용으로만 우리가 만들 수 있다. 사용자를 좀 국한시켰다 그래서 이거에 대한 내용을 동영상을 쭉 많이 보지 못하니까 이걸 추격하는 방법 이걸로 포크심을 잡았다. 굉장히 협소한 주제야. 이럴 때는 이것만 공부하면 되는 거잖아 그렇지. 그런데 만약에 일반 회의록을 해놨으면 이게 지금. 전문가 활용해서는 벌써 양식이 달라져. 우리 양식대로 양식에 대한 폼. 양식도 넣어. 내가 맞춰놔야 돼. 들어갈 때부터. 오늘 누구. 오늘 시간. 1시간짜리 회의가 우리가 정해져 있어요. 내일 모레 회의를 가. 이메일에 2시간 20분. 그걸 초과하면 돈을 줘야 하거든. 그래서 말도 한 사람당 2분 3분밖에 시간을 안 줘. 시간에 대한 이 회의는 언론에 있어. 누가 얘기를 하잖아. 그런 당시에 2분 초과했습니다 원래 술술. 그런 것까지 다 일일이 만들 것인지 이렇게까지는 안 할 것 같아요. 그러니까 그런 데 용도 누가 사용하느냐에 따라서 이 용도는 굉장히 디테일하다고 그걸 얘기를 한 거예요. 그리고 이 통째로 그냥 굉장히 긴급하게 몇 명이 들어왔다 정도만 할 거면 여기서 또 그거가 안 되고 얘가 얘기한 것처럼 그걸 능력 성능이 좋으니까 통째로 들어와서. 선머리를 할 수 있는 방안 이것만 정리하는 방안만 연구해도 좋다고 화재 분리는 우리는 못하겠습니다 라고 정확하게 얘기하는데 교수들은 너희들한테 수업 시간에 안 되는 걸 하라는 게 아니라 어떻게 대처하면서 갈느냐의 문제 해결 방식을 묻는 거야. 내가 따져서 모르더라도 너희는 당황하지 않고 우리는 이런 문제 때문에 이걸 못하고 이 방법으로 해결할 거고 여기서 문장에 100시간 60분짜리를 우리가 문장 우리가 150 1500자로 줄이는 것도 굉장히 중요하거든요. 이력은 1500자로 줄이는 방안을 하겠다. 요거 하나만 하는데도 상관 안한다고. 그렇게 해결하겠다고 하니까 대신 얘네가 연구 범위를 그렇게 했으면. 그 많은 양을 1500자를 어떻게 줄이느냐. 그러면 의미 분석을 해야 하잖아. 그 그. 양이 어마어마한데. 우리는 회의를 위해 분석하겠다는 거야 그럼 우리는 멤버인 거야. 음이 분석 구글도 못하고 있는데 음 응. 그러니까 너희가 회의를 얘기하면 우리는 루미 본 속으로 가잖아.")
# if __name__ == '__main__':
#     # res = ClovaSpeechClient().req_url(url='http://example.com/media.mp3', completion='sync')
#     # res = ClovaSpeechClient().req_object_storage(data_key='data/media.mp3', completion='sync')
#     res = ClovaSpeechClient().req_upload(file='./rec/file_dialog.wav', completion='sync')
    print(res)
    rescode = res.status_code
    if(rescode == 200):
        print (res.text)
    else:
        print("Error : " + res.text)

    
#     file_path = open('../media/stt/result.json', 'w', encoding="utf-8")
#     file_path.write(res.text)
#     file_path.close()