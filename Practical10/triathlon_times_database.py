class triathlon(object):
    def __init__(self, firstname, lastname, location, swim, cycle, run):
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.swim = swim
        self.cycle = cycle
        self.run = run
        self.totaltime = swim + cycle + run

    def speak(self):
        print("name: {} {}, location: {}, swim: {}s, cycle: {}s, run: {}s, total time: {}s".format(self.firstname, self.lastname, self.location, self.swim, self.cycle,
              self.run, self.totaltime))


someone = triathlon("Steve", "Rogers", "New York", 1, 1, 1)
someone.speak()
