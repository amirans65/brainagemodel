import copy as copylib
class Config():
    def __init__(self, **kwargs):
        self.assign(**kwargs)

    def assign(self, **kwargs):
        for k,v in kwargs.items():
            self.__dict__[k] = v

    def join(self, obj, key_prefix:str=None):
        '''
        This function takes two objects (or self, obj) and join the parameters into the first one (self). 
        It raises an error if there is a conflict in the keys.
        key_prefix: if is not none, it will be added to the keys of the obj.
            e.g. obj.p (given key_prefix='blabla_') -> self.blabla_p = obj.p
        '''
        if(key_prefix is None):
            key_prefix = ''
        for objk in obj.keys():
            k = key_prefix + objk
            if(k in self.keys()):
                raise ValueError(f"Conflict in the keys: '{k}' exists in both Configs!")
            self[k] = obj[objk]
            
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def keys(self):
        return list(self.__dict__.keys())

    def items(self):
        return self.__dict__

    def copy(self, deep:bool=True):
        '''copy the item, deep or shallow'''
        if(deep):
            return copylib.deepcopy(self)
        else:
            return copylib.copy(self)
