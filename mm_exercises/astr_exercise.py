#
#
# I realize i did this wrong because i didn't read the instructions all the way
# I'll come back to it later
#
#

class Person:
    """Person class"""
    def __init__(self, name, ismale, birthday, birthplace):
        self.name = name
        self.ismale = None
        self.birthday = birthday
        self.birthplace = birthplace

    def set_ismale (self, maleornot):
        self.ismale = maleornot

class Experience(Person):
    """Person Subclass"""
    def __init__(self, name, ismale, birthday, birthplace, alma_mater, under_major, grad_major, military=None):
        super().__init__(name, ismale, birthday, birthplace)
        self.alma_mater = alma_mater
        self.under_major = under_major
        self.grad_major = grad_major
        if military is None:
            self.military = []
        else:
            self.military = branch
            self.rank = rank
    
    def add_military(self, service):
        if service not in self.military:
            self.military.append(service)
    
    def get_military(self):
        # for service in self.military:
        #     print(service.branch)
        return '{} {}'.format(self.military, self.rank)

class Astronaut(Person):
    def __init__(self, name, ismale, birthday, birthplace, status, year, group, missions = False):
        super().__init__(name, ismale, birthday, birthplace)
        self.status = status
        self.year = year
        self.group = group
        if num_flights == 0 and num_walks ==0:
            missions = False
        else:
            missions = True

    def update_status(self, status):
        pass
