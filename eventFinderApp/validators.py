from django.core.exceptions import ValidationError


def file_size_validator(fl):
    if fl.size > 5242880:
        raise ValidationError('The maximum file size is 5MB')
    else:
        return fl
