from nosqlclass import NosqlClass


class KpUserTopic(NosqlClass):
    id: str = ''
    status: str = ''
    notice_at: str = ''
    created_at: str = ''
    updated_at: str = ''
    created_by: str = ''
    updated_by: str = ''

    @classmethod
    @property
    def prefix(cls) -> str:
        return 'usertopic@'
