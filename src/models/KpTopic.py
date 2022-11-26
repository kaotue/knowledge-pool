import datetime
import dataclasses


@dataclasses.dataclass
class KpTopic:
    id: str = ''
    type: str = ''
    q: str = ''
    a: str = ''
    is_public: str = ''
    tags: list[str] = dataclasses.field(default_factory=list)
    created_at: datetime.datetime = None
    updated_at: datetime.datetime = None
    created_by: str = ''
    updated_by: str = ''

    @classmethod
    @property
    def prefix(cls) -> str:
        return 'topic@'

    def __post_init__(self):
        pass
        # self.id = 'item-' + uuid.uuid4().hex

    def to_items(self):
        return [
            {'id': self.id, 'attr': KpTopic.prefix + 'type', 'data': self.type},
            {'id': self.id, 'attr': KpTopic.prefix + 'q', 'data': self.q},
            {'id': self.id, 'attr': KpTopic.prefix + 'a', 'data': self.a},
            {'id': self.id, 'attr': KpTopic.prefix + 'tags', 'data': self.tags},
            {'id': self.id, 'attr': KpTopic.prefix + 'created_at', 'data': self.created_at},
            {'id': self.id, 'attr': KpTopic.prefix + 'updated_at', 'data': self.updated_at},
            {'id': self.id, 'attr': KpTopic.prefix + 'created_by', 'data': self.created_by},
            {'id': self.id, 'attr': KpTopic.prefix + 'updated_by', 'data': self.updated_by}
        ]

    @classmethod
    def create_by_items(cls, items: list[dict]):
        d = {x['attr'].removeprefix(cls.prefix): x['data'] for x in items}
        return cls(**d)
