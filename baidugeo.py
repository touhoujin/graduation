import requests
class Geocoder:
    def __init__(self, ak):
        self.ak = ak

    # 给出指定地点返回经纬度 ()
    def encode(self, addr):
        r = requests.get("https://api.map.baidu.com/geocoding/v3/", params={
            "address": addr,
            "output": "json",
            "ak": self.ak
        }).json()
        if r["status"] != 0:
            raise RuntimeError(r)
        result = r["result"]["location"]
        return (result["lng"], result["lat"])
    
    def decode(self, longitude, latitude):
        r = requests.get("https://api.map.baidu.com/reverse_geocoding/v3/", params={
            "location": f"{latitude},{longitude}",
            "output": "json",
            "ak": self.ak
        }).json()
        if r["status"] != 0:
            raise RuntimeError(r)
        result = r["result"]["addressComponent"]
        return result

# g = Geocoder("t2dIEXo5A3at8GSCwLKaEsNVk6rFh3mH")
# longitude, latitude = g.encode("北京大学")

# print(longitude)
# print(latitude)
# r = g.decode(longitude, latitude)
# print(r["province"])