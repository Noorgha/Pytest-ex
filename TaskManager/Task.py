class Task:
    def __init__(self, description):
        self.description = description
        self.status = False

    def markTaskAsCompleted(self):
        self.status = True

    def taskStatus(self):
        if self.status:
            return "completed"
        else:
            return  "uncomplete"


