import inspect

class Registry:
    def __init__(self, name):
        self._name = name
        self._registry = {}

    def register(self, cls):
        if not inspect.isclass(cls):
            raise ValueError("Registry can only register classes")
        if cls.__name__ in self._registry:
            raise ValueError("Cannot register duplicate class: {}".format(cls.__name__))
        self._registry[cls.__name__] = cls

    def get(self, name):
        return self._registry.get(name)

    def __str__(self):
        return str(self._registry)

    def __repr__(self):
        return self.__class__.__name__ + "(name={}, items={})".format(self._name, self._registry)

