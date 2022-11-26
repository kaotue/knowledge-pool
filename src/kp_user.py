import uuid
import dataclasses


@dataclasses.dataclass
class KpUser:
    id: str = ''
    created_at: str = ''
    updated_at: str = ''

    @classmethod
    @property
    def prefix(cls) -> str:
        return 'user@'

    @classmethod
    def create_new_id(cls) -> str:
        return cls.prefix + uuid.uuid4().hex

    @classmethod
    def create_by_items(cls, items: list[dict]):
        d = {x['attr'].removeprefix(cls.prefix): x['data'] for x in items}
        return cls(**d)

    def to_table_items(self):
        return [
            {'id': self.id, 'attr': KpUser.prefix + 'created_at', 'data': self.created_at},
            {'id': self.id, 'attr': KpUser.prefix + 'updated_at', 'data': self.updated_at}
        ]

    def to_dict(self):
        return dataclasses.asdict(self)

