from django.db.models.fields import TimeField, DateTimeField
from timepickr.forms import TimepickrFormField, DateTimepickrFormField
from timepickr.widgets import AdminTimepickrWidget, AdminDateTimepickrWidget

class TimepickrField(TimeField):
    
    description = "Django time field that uses as jQuery timepickr"

    def __init__(self, verbose_name=None, name=None, auto_now=False, auto_now_add=False, **kwargs):
        print self
        print dir(self)
        super(TimepickrField, self).__init__(verbose_name, name, auto_now, auto_now_add, **kwargs)

    def get_internal_type(self):
        return 'TimeField'

    def formfield(self, **kwargs):
        defaults = {'form_class': TimepickrFormField}
        kwargs['widget'] = AdminTimepickrWidget
        defaults.update(kwargs)
        return super(TimepickrField, self).formfield(**defaults)



class DateTimepickrField(DateTimeField):
    
    description = "Django datetime field that uses as jQuery timepickr"

    def __init__(self, verbose_name=None, name=None, auto_now=False, auto_now_add=False, **kwargs):
        super(DateTimepickrField, self).__init__(verbose_name, name, auto_now, auto_now_add, **kwargs)

    def get_internal_type(self):
        return 'TimeField'

    def formfield(self, **kwargs):
        defaults = {'form_class': DateTimepickrFormField}
        kwargs['widget'] = AdminDateTimepickrWidget
        defaults.update(kwargs)
        return super(DateTimepickrField, self).formfield(**defaults)
