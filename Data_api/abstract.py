from abc import ABC,abstractmethod

@abstractmethod
class base_account(ABC):
    def get_account(self,*args,**kwargs):
        pass

    def login(self,*args,**kwargs):
        pass

    def logout(self,*args,**kwargs):
        pass