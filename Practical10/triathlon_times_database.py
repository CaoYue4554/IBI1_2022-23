class triathlon(object):
    def __init__(self,firstname,lastname,location,swim,cycle,run):
        triathlon.firstname = firstname
        triathlon.lastname = lastname
        triathlon.location = location
        triathlon.swim = swim
        triathlon.cycle = cycle
        triathlon.run = run
        triathlon.totaltime = swim + cycle + run
    def speak(self):
        print(triathlon.firstname,triathlon.lastname,triathlon.location,triathlon.swim,triathlon.cycle,triathlon.run,triathlon.totaltime)
someone= triathlon("Yue","Cao","Haining",1,1,1)
someone.speak()
