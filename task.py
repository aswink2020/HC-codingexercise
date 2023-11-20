class Task:
    def __init__(self, description, due_date=None, tags=None):
        self.description = description
        self.completed = False
        self.due_date = due_date
        self.tags = tags if tags else []

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        due_date_str = f", Due: {self.due_date}" if self.due_date else ""
        return f"{self.description} - {status}{due_date_str}"

class TaskBuilder:
    def __init__(self, description):
        self.task = Task(description)

    def set_due_date(self, due_date):
        self.task.due_date = due_date
        return self

    def add_tags(self, tags):
        self.task.tags.extend(tags)
        return self

    def build(self):
        return self.task
