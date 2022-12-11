from nosqlclass import NosqlClass


class KpUser(NosqlClass):
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
