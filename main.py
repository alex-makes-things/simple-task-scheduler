from scheduler import Scheduler

def sayHello():
    print("Hello")

def sayGoodbye():
    print("Goodbye")

sch = Scheduler()
sch.addTask(sayHello, 0)
sch.addTask(sayGoodbye, 1)
sch.runTasks()
