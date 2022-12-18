from nosqlclass import NosqlClass


class KpTopic(NosqlClass):
    id: str = ''
    type: str = ''
    q: str = ''
    a: str = ''
    is_public: str = ''
    tag_1: str = ''
    tag_2: str = ''
    tag_3: str = ''
    created_at: str = ''
    updated_at: str = ''
    created_by: str = ''
    updated_by: str = ''

    @classmethod
    @property
    def prefix(cls) -> str:
        return 'topic@'
