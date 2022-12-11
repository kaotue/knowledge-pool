import uuid
import dataclasses


@dataclasses.dataclass
class NosqlClass:

    def __new__(cls, *args, **kwargs):
        dataclasses.dataclass(cls)
        return super().__new__(cls)

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
                'id': self.prefix + self.id,
                'attr': self.prefix + k,
                'data': v
            })
        return ary

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
