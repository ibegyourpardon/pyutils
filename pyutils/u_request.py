import requests


class RequestHandler:

    def __init__(self, method, url, payload):
        self.method = method
        self.url = url
        self.payload = payload

    def get(self, url, **kwargs):
        params = kwargs.get("params")
        headers = kwargs.get("headers")
        try:
            result = requests.get(url=url,params=params, headers=headers)
            return result
        except Exception as e:
            print("post请求错误: %s" % e)