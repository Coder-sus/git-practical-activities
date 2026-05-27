class Task:
    def __init__(self, title, status="ToDo"):
        """Initialize a Task with a title and optional status (default: 'ToDo')."""
        self.title = title
        self.completed = False
        self.status = status

    def mark_completed(self):
        """Mark the task as completed and update its status to 'Done'."""
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        """Return a concise representation like 'Task Title - ToDo'."""
        return f"{self.title} - {self.status}"

    def __str__(self):
        """Return a user-friendly string like 'Task: Task Title, Status: ToDo'."""
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        """Initialize an empty TaskPool."""
        self.tasks = []

    def populate(self):
        """Create six sample tasks and mark the first three as completed."""
        t1 = Task("Design database schema")
        t2 = Task("Set up CI/CD pipeline")
        t3 = Task("Write unit tests")
        t4 = Task("Implement login feature")
        t5 = Task("Deploy to staging")
        t6 = Task("Code review")

        t1.mark_completed()
        t2.mark_completed()
        t3.mark_completed()

        self.tasks = [t1, t2, t3, t4, t5, t6]

    def add_task(self, task):
        """Add a Task object to the pool."""
        self.tasks.append(task)

    def get_open_tasks(self):
        """Return a list of tasks with status 'ToDo'."""
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        """Return a list of tasks with status 'Done'."""
        return [task for task in self.tasks if task.status == "Done"]


def main():
    pool = TaskPool()
    pool.populate()

    todo_titles = [task.title for task in pool.get_open_tasks()]
    print("ToDo Tasks:")
    for title in todo_titles:
        print(title)

    done_titles = [task.title for task in pool.get_done_tasks()]
    print("Done Tasks:")
    for title in done_titles:
        print(title)


if __name__ == "__main__":
    main()
