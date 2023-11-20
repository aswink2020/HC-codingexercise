from task import Task

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class ToDoListManager:
    def __init__(self):
        self.tasks = []
        self.mementos = []

    def add_task(self, task):
        self.tasks.append(task)
        self.save_memento()

    def mark_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.mark_completed()
                self.save_memento()
                return True
        return False

    def delete_task(self, task_description):
        self.tasks = [task for task in self.tasks if task.description != task_description]
        self.save_memento()

    def view_tasks(self, status=None):
        if status == "completed":
            return [str(task) for task in self.tasks if task.completed]
        elif status == "pending":
            return [str(task) for task in self.tasks if not task.completed]
        else:
            return [str(task) for task in self.tasks]

    def save_memento(self):
        current_state = [task.__dict__.copy() for task in self.tasks]
        self.mementos.append(Memento(current_state))

    def undo(self):
        if len(self.mementos) > 1:
            self.mementos.pop()
            previous_state = self.mementos[-1].get_state()
            self.tasks = [Task(task['description'], task['due_date'], task['tags']) for task in previous_state]
