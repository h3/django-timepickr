from django.forms.fields import TimeField, DateTimeField


class TimepickrFormField(TimeField):
    def clean(self, data, initial=None):
        if data != '__deleted__':
            return super(TimepickrFormField, self).clean(data, initial)
        else:
            return '__deleted__'


class DateTimepickrFormField(DateTimeField):
    def clean(self, data, initial=None):
        if data != '__deleted__':
            return super(DateTimepickrFormField, self).clean(data, initial)
        else:
            return '__deleted__'

