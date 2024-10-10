
class TaskManager:

    def __init__(self, filepath):
        self.filepath = filepath
        self.tasks = []

    def addTasks(self,task):
        self.tasks.append(task)

    def listTasks(self):
        return self.tasks

    def loadTasks(self):
        try:
            lines = []
            f = open(self.filepath)
            for line in f:
                lines.append(line)
            return lines
        except FileNotFoundError as e:
            raise e

    def addTasksToFile(self):
        try:
            f = open(self.filepath, "w")
            for task in self.tasks:
                f.write(task)
            f.close()
        except FileNotFoundError as e:
            raise e

    def markByIndex(self, index):
        self.tasks[index].markAsCompleted()