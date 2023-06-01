import requests
class RestSender:
    @staticmethod
    def sendGetMsg(url,params):
        return requests.get(url=url,params=params)
    @staticmethod
    def sendPostMsg(url,data):
        return requests.post(url=url,json=data)
    @staticmethod
    def sendPutMsg(url,data):
        return requests.put(url=url,json=data)
    @staticmethod
    def sendDeleteMsg(url):
        return requests.delete(url=url)