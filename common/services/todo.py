from typing import List, Optional
from common.repositories.factory import RepositoryFactory, RepoType
from common.models.todo import Todo

class TodoService:
    def __init__(self, config):
        self.config = config
        self.repository_factory = RepositoryFactory(config)
        self.todo_repo = self.repository_factory.get_repository(RepoType.TODO)

    def save_todo(self, todo: Todo) -> Todo:
        return self.todo_repo.save(todo)

    def get_todo_by_id(self, entity_id: str) -> Optional[Todo]:
        return self.todo_repo.get_one({"entity_id": entity_id})
    
    def get_todos_by_person(self, person_id: str, filter_status: Optional[str] = None) -> List[Todo]:

        query = {"person_id": person_id}
        
        if filter_status == "completed":
            query["is_completed"] = True
        elif filter_status == "incomplete":
            query["is_completed"] = False
        
        todos = self.todo_repo.get_many(query)
        return todos if todos else []

    def delete_todo(self, todo: Todo):
        self.todo_repo.delete(todo)
