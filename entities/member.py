from dataclasses import dataclass
from entities.core import BaseEntitie


@dataclass
class Member(BaseEntitie):
    name: str
    has_paused: bool
    paused_time: int
    logged_time: int
    total_calls: int
    last_call_time: int

    class DoesExists(Exception):
        ...

    def get_key(self) -> str:
        return self.name
    
    def __eq__(self, value: object) -> bool:

        if type(self) != type(value):
            return False
        
        return bool(self.has_paused == value.has_paused and
            self.get_key() == value.get_key() 
        )

    def __post_init__(self) -> None:
        self.type = 'member'