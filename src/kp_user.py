import uuid
import dataclasses


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

    def to_items(self):
        return [
            {'id': KpUser.prefix + self.id, 'attr': KpUser.prefix + 'id', 'data': self.id},
            {'id': KpUser.prefix + self.id, 'attr': KpUser.prefix + 'name', 'data': self.name},
            {'id': KpUser.prefix + self.id, 'attr': KpUser.prefix + 'created_at', 'data': self.created_at},
            {'id': KpUser.prefix + self.id, 'attr': KpUser.prefix + 'updated_at', 'data': self.updated_at},
            {'id': KpUser.prefix + self.id, 'attr': KpUser.prefix + 'created_by', 'data': self.created_by},
            {'id': KpUser.prefix + self.id, 'attr': KpUser.prefix + 'updated_by', 'data': self.updated_by}
        ]

    def to_dict(self):
        return dataclasses.asdict(self)

