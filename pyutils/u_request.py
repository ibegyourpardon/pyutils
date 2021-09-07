import requests


class RequestHandler:

    def __init__(self, method, url, payload):
        self.method = method
        self.url = url
        self.payload = payload

    @classmethod
    def get(cls, url, **kwargs):
        params = kwargs.get("params")
        headers = kwargs.get("headers")
        try:
            result = requests.get(url=url,params=params, headers=headers)
            return result
        except Exception as e:
            print("post请求错误: %s" % e)

    @classmethod
    def post(cls, url, **kwargs):
        params = kwargs.get("params")
        data = kwargs.get("data")
        json = kwargs.get("json")
        try:
            result = requests.post(url=url, params=params, data=data, json=json)
            return result
        except Exception as e:
            print("post请求错误: %s" % e)
