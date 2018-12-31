Class intSet(object):
    def __init__(self):
        # create empty set of integers
        self.vals = []

    def  insert(self,e):
        """ Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)


    def member(self,e):
        """Assumes e is an integer. Returns true if e is in self, else False"""
        return e.self.vals

    def remove(self,e):
        """ Assumes e is an integer and removes e from self,
            rasies value error if e is not in self"""

        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + "Not Found")

    def __str__self(self):
        """ Returns a self representation of self"""
        self.vals.sort()
        result = ""
        for e in self.vals:
            result = result + str(e) + ","
        return '{' + result[:1] + '}'
        

            
            
        
