class triathlon(object):
    def __init__(self,firstname,lastname,location,swim,cycle,run):
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.swim = swim
        self.cycle = cycle
        self.run = run
        self.totaltime = swim + cycle + run
    def speak(self):
        print(triathlon.firstname,triathlon.lastname,triathlon.location,triathlon.swim,triathlon.cycle,triathlon.run,triathlon.totaltime)
someone= triathlon("Steve","Rogers","New York",1,1,1)
someone.speak()
