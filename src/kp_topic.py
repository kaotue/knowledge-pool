import dataclasses
import uuid


@dataclasses.dataclass
class KpTopic:
    id: str = ''
    type: str = ''
    q: str = ''
    a: str = ''
    is_public: str = ''
    tags: str = ''
    created_at: str = ''
    updated_at: str = ''
    created_by: str = ''
    updated_by: str = ''

    @classmethod
    @property
    def prefix(cls) -> str:
        return 'topic@'

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
                'id': KpTopic.prefix + self.id,
                'attr': KpTopic.prefix + k,
                'data': v
            })
        return ary

    def to_dict(self):
        return dataclasses.asdict(self)
