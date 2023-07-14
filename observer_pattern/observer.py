class Observer:
    def update(self, message):
        raise NotImplementedError

class Observable:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def update_observers(self, message):
        for observer in self.observers:
            observer.update(message)


class ObserverImpl(Observer):
    def __init__(self):
        self.messages = []

    def update(self, message):
        self.messages.append(message)
