import logging
import signal
from functools import wraps

import cmptcomplexity.scripts.exceptions as exceptions


def log_it(func):
    def wrap(*args, **kwargs):
        logging.info('invoked function %s (%s)', func.__name__, str(args) + str(kwargs))
        result = func(*args, **kwargs)
        return result

    return wrap


def timeout():
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise exceptions.TimeoutCCException('ops')

        def wrapper(*args, **kwargs):
            to_alarm, _ = signal.setitimer(signal.ITIMER_REAL, 0)
            signal.setitimer(signal.ITIMER_REAL, to_alarm)
            signal.signal(signal.SIGALRM, _handle_timeout)

            try:
                result = func(*args, **kwargs)
            except exceptions.TimeoutCCException:
                return 0, 'except'

            finally:
                to_alarm, _ = signal.setitimer(signal.ITIMER_REAL, 0)
                signal.setitimer(signal.ITIMER_REAL, to_alarm)

            return result, to_alarm

        return wraps(func)(wrapper)

    return decorator
