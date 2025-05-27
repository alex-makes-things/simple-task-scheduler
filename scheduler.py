import gc

class Scheduler:
    def __init__(self):
        self.tasks = {}

    def getTaskPriority(self, task):
        return task.priority

    def addTask(self, task, priority=0):
        self.tasks[str(task.__name__)] = Task(task, priority)    #Refresh dictionary from the tasklist
    
    def removeTask(self, task):
        del self.tasks[task.__name__]
        gc.collect()     #Deleting objects from dictionaries (del) leaves the objects in memory, so we garbage collect to avoid leaks

    def clearTaskTree(self):
        self.tasks.clear()
        gc.collect()

    def runTasks(self):
        for task in sorted(self.tasks.values(), key=self.getTaskPriority):    #Iterates over the dictionary, in order with the priorities of each object
            task.run()

class Task:
    def __init__(self, func, priority):
        self.priority = priority
        self.func = func

    def run(self):
        self.func()