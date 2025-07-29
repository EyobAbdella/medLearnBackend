import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MoodleCompatiblePasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError(_("Password must be at least 8 characters long."))

        if not re.search(r"[A-Z]", password):
            raise ValidationError(
                _("Password must contain at least 1 uppercase letter.")
            )

        if not re.search(r"[a-z]", password):
            raise ValidationError(
                _("Password must contain at least 1 lowercase letter.")
            )

        if not re.search(r"[0-9]", password):
            raise ValidationError(_("Password must contain at least 1 digit."))

        if not re.search(r"[!*@#$%^&*()_\-+=\[\]{}|\\;:'\",.<>?/~`]", password):
            raise ValidationError(
                _("Password must contain at least 1 special character.")
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 8 characters, including 1 digit, "
            "1 lowercase letter, 1 uppercase letter, and 1 special character (*, -, #, etc.)."
        )
