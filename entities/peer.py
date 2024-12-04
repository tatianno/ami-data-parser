from dataclasses import dataclass
from entities.core import BaseEntitie


@dataclass
class Peer(BaseEntitie):
    exten: str
    peername: str
    state: str
    presence: str
    watchers: int 

    def get_key(self) -> str:
        return self.peername
    
    def __eq__(self, value: object) -> bool:

        if type(self) != type(value):
            return False
        
        return bool(self.state == value.state and
            self.get_key() == value.get_key()    
        )
    
    def __post_init__(self) -> None:
        self.type = 'peer'