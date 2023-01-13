from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def only_letters_validator(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError("Ensure this value contains only letters.")


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError(self.__get_error_message())

    def __get_error_message(self):
        return f"Max file size is {self.max_size} MB"