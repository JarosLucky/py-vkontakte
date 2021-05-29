class VKError(Exception):
    def __init__(self, message, code):
        super(VKError, self).__init__(message)
        self.code = code
        self.message = message


class VKParseJsonError(Exception):
    pass
