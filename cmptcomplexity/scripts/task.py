import logging


class Task:
    """Class for representing most of problems in unified way"""

    def __init__(self, init_code, clean_up_code, example_invoke):
        def open_with_logger(filename):
            try:
                f = open(filename, 'r').read()
                logging.info('Read %s', filename)
                return f
            except FileNotFoundError as e:
                logging.error('File %s does not exits or you do not '
                              'have a permision to read!', filename)
                exit(-1)

        if init_code[-3:] == '.py':
            init_code = open_with_logger(init_code)
        if example_invoke[-3:] == '.py':
            example_invoke = open_with_logger(example_invoke)
        if clean_up_code[-3:] == '.py':
            clean_up_code = open_with_logger(clean_up_code)
        if '__N__' not in init_code and '__N__' not in example_invoke:
            from cmptcomplexity.scripts.exceptions import ArgumentPatternError
            raise ArgumentPatternError('No "__N__" to scale an problem size!')
        self.init_code = init_code
        self.example_invoke = example_invoke
        self.clean_up_code = clean_up_code

    def stringify_init(self, N):
        return self.init_code.replace('__N__', str(N))

    def stringify_clean_up(self, N):
        return self.clean_up_code.replace('__N__', str(N))

    def stringify_example_invoke(self, N):
        return self.example_invoke.replace('__N__', str(N))
