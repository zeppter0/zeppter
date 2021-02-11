from django.db.models.expressions import Func

class ArrayAppend(Func):

    function = 'array_append'
    template = "%(function)s(%(expressions)s, %(element)s)"
    arity = 1

    def __init__(self, expression: str, element, **extra):
        if not isinstance(element, (str, int)):
            raise TypeError(
                f'Type of "{element}" must be int or str, '
                f'not "{type(element).__name__}".'
            )

        super().__init__(
            expression,
            element=isinstance(element, int) and element or f"'{element}'",
            **extra,
        )