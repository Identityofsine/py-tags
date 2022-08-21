from nis import match
from unittest import case


class Service():
    def __init__(self,service) -> None:
        self.service = service
        pass
    def getHashTagStats(self):
        pass


class Youtube(Service):
    def __init__(self, service) -> None:
        super().__init__(service)
        pass
    def getHashTagStats(self):
        return super().getHashTagStats()

class TikTok(Service):
    def __init__(self, service) -> None:
        super().__init__(service)
        pass

class Instagram(Service):
    def __init__(self, service) -> None:
        super().__init__(service)
        pass