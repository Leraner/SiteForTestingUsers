class RefreshTokenNotFoundException(Exception):
    """Exception if refresh token not found"""

    def __str__(self) -> str:
        return 'Refresh token not found'


class ImageRequiredException(Exception):
    """Exception if image not found"""
    def __str__(self) -> str:
        return 'Image file is required'
