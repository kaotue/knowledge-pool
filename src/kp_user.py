import dataclasses
import uuid


@dataclasses.dataclass
class KpUser:
    id: str = ''
    name: str = ''
    created_at: str = ''
    updated_at: str = ''
    created_by: str = ''
    updated_by: str = ''

    @classmethod
    @property
    def prefix(cls) -> str:
        return 'user@'

    @classmethod
    def create_new_id(cls) -> str:
        return uuid.uuid4().hex

    @classmethod
    def create_by_items(cls, items: list[dict]):
        d = {x['attr'].removeprefix(cls.prefix): x['data'] for x in items}
        return cls(**d)

    def to_items(self) -> list[dict]:
        ary = []
        for k, v in self.__dict__.items():
            ary.append({
                'id': KpUser.prefix + self.id,
                'attr': KpUser.prefix + k,
                'data': v
            })
        return ary

    def to_dict(self):
        return dataclasses.asdict(self)

