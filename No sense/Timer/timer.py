
from threading import Thread
from time import sleep
from random import randint


class EventError(Exception):
    pass


class Timer:
    __slots__ = ('__timeout__', '_functions', 'events')

    def __init__(self, timeout: int=30):
        self.__timeout__ = timeout

        self._functions = {
            'on_timeout': [],
            'on_decrease': []
        }

        self.events = (
            'on_timeout', 'on_decrease'
        )

    @property
    def value(self):
        return self.__timeout__

    @value.setter
    def value(self, new_value):
        return self.__timeout__

    def _decrease(self):
        self.__timeout__ -= 1
        self._call_event('on_decrease')

    def start(self):
        'Da inicio ao Timer'
        def _run():
            while self.__timeout__ > 0:
                self._decrease()
                sleep(1)
            self._call_event('on_timeout')

        _thread = Thread(target=_run)
        _thread.start()

    def wait_timeout(self):
        'Espera o tempo do timer acabar para prosseguir'
        while self.__timeout__ > 0:
            pass

    def _call_event(self, name: str):
        if name in self.events:
            for function in self._functions[name]:
                function()
        else:
            raise EventError(f'{name} not found')

    def event(self, function):
        '''
        Decorador
        '''
        if function.__name__ not in self.events:
            raise EventError(f'{function.__name__} is not a event')
        else:
            self._functions[function.__name__].append(function)

        return function
