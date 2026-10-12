from abc import ABC,abstractmethod
class Abscls(ABC):
    def print(self,x):
        print("the value is:",x)
    @abstractmethod
    def tsk(self):
        print("we are inside abstact class!")
class testcls (Abscls):
    def tsk(self):
        print("now we are inside testcls!")
tstobj=testcls()
tstobj.tsk()
tstobj.print(67)
