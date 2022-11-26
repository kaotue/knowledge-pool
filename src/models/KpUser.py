import datetime
import dataclasses


@dataclasses.dataclass
class KpUser:
    id: str = ''
    created_at: datetime.datetime = None
    updated_at: datetime.datetime = None

    @classmethod
    @property
    def prefix(cls) -> str:
        return 'user@'

    def __post_init__(self):
        pass
        # self.id = 'user-' + uuid.uuid4().hex

    def to_table_items(self):
        return [
            {'id': self.id, 'attr': KpUser.prefix + 'created_at', 'data': self.created_at},
            {'id': self.id, 'attr': KpUser.prefix + 'updated_at', 'data': self.updated_at}
        ]

    def to_dict(self):
        return dataclasses.asdict(self)

