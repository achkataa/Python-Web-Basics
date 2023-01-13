from online_ibrary.main.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None


class DisabledFieldsMixin:
    fields = {}

    def _init_disable_fields(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['readonly'] = 'readonly'
