from dataclasses import dataclass
from rococo.models import VersionedModel

@dataclass
class Todo(VersionedModel):

    person_id: str = None
    title: str = None
    is_completed: bool = False