class ComputeComplexityException(Exception):  # super exception for module
    pass


class TimeoutCCException(ComputeComplexityException):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.val


class WrongTimeoutCCException(ComputeComplexityException):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.val


class InitializationError(ComputeComplexityException):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.val


class ArgumentPatternError(ComputeComplexityException):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.val


class AnalyzablePatternError(ComputeComplexityException):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.val
