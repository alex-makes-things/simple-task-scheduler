from scheduler import Scheduler

#DEMO CODE

def sayHello():
    print("Hello")

def sayGoodbye():
    print("Goodbye")

sch = Scheduler()
sch.addTask(sayHello, 1)
sch.addTask(sayGoodbye, 0)
sch.runTasks()
