import requests
import json
import pickle

url = 'http://api.data.go.kr/openapi/tn_pubr_public_cctv_api'
api_key = "gqfjsOnOZ6t4U6Z7tOHkD9gYAguMqI42doHU0UubyUPkJJROUQEOF5lLQfuaHuZTC7Hm8J05HdDOhN7Tq2vjeA=="


def get_cctv_list(pageNo, size):
    ret = requests.get(url, params={
        'ServiceKey': api_key,
        'pageNo': pageNo,
        'numOfRows': size,
        'type': 'json'
    })
    return json.loads(ret.text, strict=False)['response']


if __name__ == '__main__':
    cctv_list = []
    i = 0
    while True:
        res = get_cctv_list(i, 1000)
        if res['header']['resultMsg'] == 'NODATA_ERROR':
            break
        else:
            print(i, ":", len(res['body']['items']))
            for item in res['body']['items']:
                cctv_list.append(item)
        i += 1
    print(len(cctv_list))
    with open('cctv_list.p', 'wb') as f:
        pickle.dump(cctv_list, f)