import pytest
from observer_pattern.observer import ObserverImpl, Observable

def test_observer_pattern():
    observable = Observable()
    observer = ObserverImpl()

    observable.register(observer)
    observable.update_observers("test message")
    assert observer.messages == ["test message"]

    observable.unregister(observer)
    observable.update_observers("second message")
    assert observer.messages == ["test message"]  # observer has been unregistered, so it should not receive "second message"
