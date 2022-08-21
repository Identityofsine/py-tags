from ast import parse

from __service__ import Service


class HashTag():
    def __init__(self, tag, service : Service) -> None:
        self.hashtag = self.parseHashTag()
        self.service = service
        pass
    def parseHashTag(self, tag):
        pass