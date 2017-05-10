class Controller:
    """Class responsible for managing task invokes and returning results"""

    def __init__(self, task, timeout=30):
        self.task = task
        self.timeout = timeout

    def get_data(self):
        """Function, which invokes timeit, collects data and sends to solver"""

        import signal
        import cmptcomplexity.scripts.exceptions as excp
        from cmptcomplexity.scripts.decorators import timeout

        @timeout()
        def avrg_measure(task, N, repeat, n):
            import timeit
            msrs = timeit.repeat(task.stringify_example_invoke(N),
                                 task.stringify_init(N), repeat=repeat,
                                 number=n)
            return (sum(msrs) / len(msrs)) / n

        if self.timeout < 0.5:
            raise excp.WrongTimeoutCCException('Timeout must be > 0.5')
        timeout = self.timeout
        signal.setitimer(signal.ITIMER_REAL, timeout)
        import logging
        logging.info('Started receiving data.')
        can = True
        import random
        MIN = 10
        MAX = 100
        x = []
        y = []
        r = 5
        n = 10
        to_alarm = self.timeout - 0.00001
        while can:
            if to_alarm == 0:
                to_alarm = 0.00001  # prevents from /0
            i = random.randint(MIN, MAX)
            logging.info('\t(%f %%)\tMeasuring time for N=%s range (0, %s).',
                         (100 - to_alarm * 100.0 / self.timeout),
                         str(i), str(MAX))
            timeout = to_alarm

            c_y, to_alarm = avrg_measure(self.task, i, r, n)
            if to_alarm == 'except':
                can = False
            else:

                if to_alarm > 0.5:
                    if (timeout - to_alarm) / float(to_alarm) < 0.1:
                        MAX = i + MAX
                        n += 1
                    else:
                        if n > 10:
                            n -= 1
                        if MAX > 100:
                            MAX //= 1.25

                    x.append(i)

                    y.append(c_y * 1000)
                else:
                    can = False

        to_alarm, _ = signal.setitimer(signal.ITIMER_REAL, 0)
        logging.info('\t(%f %%)\tMeasuring times finished.', 100.0)
        logging.info('Started approximate received data.')
        import cmptcomplexity.scripts.solver as solver
        slvr = solver.Solver(x, y)
        results = slvr.solve()
        logging.info('Finished!')
        return results
