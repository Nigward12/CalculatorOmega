class SingletonMeta(type):
    # this class's purpose is to set the meta behavior of the operator classes
    # so that each class could only ever have one instance (singleton)
    # the class inherits from type which is the base metaclass in Python
    # the class overrides the call method of type metaclass , the method is called when an instance of a class
    # that uses this class as its metaclass is being "created"
    # the class stores the instances of the operator classes in a dictionary in which each key
    # is an operator class and each corresponding value is the instance of the class
    # (this dictionary can be accessed from all classes using SingletonMeta as their metaclass)

    # * this metaclass and the way it works in creating objects as "singletons" is not thread safe
    # as it is , I added it with the thought that if a program like this was used it would have been locally
    # in an actual calculator or an offline app for phone or computer so that there is only one thread
    # entering the __call__ method each time at all times
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
