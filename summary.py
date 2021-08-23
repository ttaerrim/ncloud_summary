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
                "summaryCount": 3,
                "tone": 3
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
    contents = ""
    WORDS = 1999
    summary = ""

    for i in range((len(contents)//WORDS)+1):
        print(i,"번째***********")
        res = ClovaSummary().req(contents[WORDS*i:WORDS*(i+1)])
        rescode = res.status_code
        if(rescode == 200):
            print(res.text)
            summary += json.loads(res.text)["summary"]
        else:
            print("Error : " + res.text)
    if (len(contents)//WORDS) > 0:
        res = ClovaSummary().req(summary)
        rescode = res.status_code
        if(rescode == 200):
            summary = json.loads(res.text)["summary"]
        else:
            print("Error : " + res.text)
    
    # print("최종 summary")        
    print(summary)

    ## 2000자 넘는 문장 2000자씩 나눠서 요약