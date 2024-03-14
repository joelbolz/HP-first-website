from wtforms import BooleanField
from wtforms.widgets import Input


class ButtonInput(Input):
    """
    Renders a button.

    The field's label is used as the text of the button instead of the
    data on the field.
    """

    input_type = "button"

    def __call__(self, field, **kwargs):
        kwargs.setdefault("value", field.label.text)
        return super().__call__(field, **kwargs)
    
class ButtonField(BooleanField):
    """
    Represents an ``<input type="button">``.  This allows checking if a given
    button has been pressed.
    """

    widget = ButtonInput()