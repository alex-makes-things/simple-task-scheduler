class Scheduler:
    def __init__(self):
        self.tasklist = []
        self.tasks = {}

    def addTask(self, task, priority=0):
        self.tasklist.append(Task(task, priority))
        self.tasks = {t.func.__name__: t for t in self.tasklist}    #Adds task to dictionary from the tasklist
    
    def removeTask(self, task):
        self.tasklist.remove(task)
        self.tasks = {t.func.__name__: t for t in self.tasklist}

    def clearTaskTree(self):
        self.tasks = {}

    def runTasks(self):
        for task in sorted(self.tasks.values(), key=lambda x: x.priority):
            task.run()

class Task:
    def __init__(self, func, priority):
        self.priority = priority
        self.func = func

    def run(self):
        self.func()