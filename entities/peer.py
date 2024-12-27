from entities.core import BaseEntitie


class Peer(BaseEntitie):

    def __init__(
        self,
        exten: str,
        peername: str,
        state: str,
        presence: str,
        watchers: int
    ):
        self.exten = exten
        self.peername = peername
        self.state = state
        self.presence = presence
        self.watchers = watchers
        self.type = 'peer'

    def get_key(self) -> str:
        return self.peername
    
    def __eq__(self, value: object) -> bool:

        if type(self) != type(value):
            return False
        
        return bool(self.state == value.state and
            self.get_key() == value.get_key()    
        )