from collections import OrderedDict


def get_json_data(success: bool = True, error=None, message: str = None, result=None, *args, **kwargs):
    return OrderedDict([
        ('success', success),
        ('error', error),
        ('message', message),
        ('result', result)
    ])
