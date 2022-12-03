
class UserNotFoundException(Exception):
    """Exception for user not found situation"""
    def __str__(self):
        return 'User not found'


class DataNotFoundException(Exception):
    """Exception if data came empty"""
    def __str__(self):
        return 'Data not found'
