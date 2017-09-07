import physycs as phy

class Object:
    '''
        Class for an object.
        name    type:char   desc:name of the object
        id      type:int    desc:unique id of the object
    '''
    def __init__(self, n, i):
        self.name = n
        self.id = i
        self.forces = []
        self.actions = []
        