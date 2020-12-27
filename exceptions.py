class IsNotFile(Exception):
    def __init__(self):
        message = "Is not a file"
        super().__init__(message)


class FileDeleted(Exception):
    def __init__(self):
        message = "File has been renamed or removed or deleted"
        super().__init__(message)
