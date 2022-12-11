from nosqlclass import NosqlClass


class KpTopic(NosqlClass):
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
