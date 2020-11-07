__author__ = 'Tomasz Rybotycki'

"""
This PennyLane plugin is basically the same thing as default_qubit device, with only one difference - it logs every
method call. 
"""

import inspect
from datetime import datetime

from pennylane.devices.default_qubit import DefaultQubit


def log(func):
    should_print = False

    def wrapped(*args, **kwargs):
        entry = {}
        try:
            # https://stackoverflow.com/questions/218616/how-to-get-method-parameter-names
            # updated with
            # https://stackoverflow.com/questions/32659552/importing-izip-from-itertools-module-gives-nameerror-in-python-3-x
            # and modified by me, so it works...
            if should_print:
                print(f"Entering: [{func.__name__}] with {len(args)} arguments.")

            args_name = inspect.getfullargspec(func)[0]

            if args_name[0] == 'cls':
                if should_print:
                    print(f'Removing {args_name[0]} from arguments list')
                args_name.pop(0)
                args_list = list(args)
                args_list.pop(0)
                args = tuple(args_list)

            if should_print:
                args_dict = dict(zip(args_name, args))

                i = 1
                for x in args_dict:
                    print(f'\t{i}. {x} = {args_dict[x]}')
                    i += 1

            entry = {
                'time': datetime.now(),
                'name': func.__name__,
                'args': args,
                'kwargs': kwargs
            }

            try:
                return func(*args, **kwargs)
            except Exception as e:
                if should_print:
                    print('Exception in %s : %s' % (func.__name__, e))
                entry['exception'] = e
        finally:
            if should_print:
                print("Exiting: [%s]" % func.__name__)
            if args_name.__contains__('self'):
                args[0].device_log.append(entry)
            if should_print:
                print(f'Log length: {len(args[0].device_log)}')

    return wrapped


def trace(cls):
    # https://stackoverflow.com/a/17019983/190597 (jamylak)
    # Modified by me for this case.
    for name, m in inspect.getmembers(cls, lambda x: inspect.isfunction(x) or inspect.ismethod(x)):
        if {'__repr__', '__init__', '__str__'}.__contains__(name):  # These three methods are not important.
            continue  # Also they cause problem with recursions.
        if isinstance(inspect.getattr_static(cls, name), staticmethod):
            continue
            # Static methods were called with self as an argument and it caused a lot of problems for the logger.
            # Most of them are just staticmethod(numpy.function) therefore are more of tools than instructions,
            # so I decided to omit them during logging.
        setattr(cls, name, log(m))
    return cls


@trace
class LoggingQubit(DefaultQubit):
    name = "Logging qubit PennyLane plugin"
    short_name = "logging.qubit"
    author = "Tomasz Rybotycki"

    def __init__(self, wires, *, shots=1000, analytic=True):
        self.device_log = list()
        super().__init__(wires, shots=shots, analytic=analytic)
