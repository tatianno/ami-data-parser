from entities.member import Member
from repositories.core import BaseRepository


class MemberRepository(BaseRepository):
    _entitie = Member  

    def get(self, name) -> Member:
        return super().get(name)

    def get_dict(self) -> dict:
        return [
            vars(self._objects[key])
            for key in self._objects
        ]

    def __eq__(self, value: object) -> bool:
       
        if self.count() != value.count():
            return False
        
        for member in value.all():
            if not self.exists(member.get_key()):
                return False
            
            if member != self.get(member.get_key()):
                return False
        
        return True