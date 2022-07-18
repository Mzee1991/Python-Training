class Codec:
    def __init__(self):
        self.url={}
    def encode(self, longUrl: str) -> str:
        s = longUrl.split("/")
        s = s[len(s)-1][::-1]
        self.url[s] = longUrl
        return s
    def decode(self, shortUrl: str) -> str:
        return self.url[shortUrl]
