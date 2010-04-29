from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from timepickr import settings


class AdminTimepickrWidget(forms.TimeInput):
    '''
    '''

    def __init__(self, attrs={}, format=None):
        super(AdminTimepickrWidget, self).__init__(attrs={'class': 'ui-timepickr', 'size': '8'}, format=format)
    
    
    class Media:
        js  = (settings.MEDIA_ROOT + "src/ui.timepickr.js",)
        css = (settings.MEDIA_ROOT + "css/ui-timepickr.css", )


class AdminDateTimepickrWidget(forms.SplitDateTimeWidget):
    """
    A SplitDateTime Widget that has some admin-specific styling.
    """
    def __init__(self, attrs=None):
        widgets = [AdminDateWidget, AdminTimepickrWidget]
        # Note that we're calling MultiWidget, not SplitDateTimeWidget, because
        # we want to define widgets.
        forms.MultiWidget.__init__(self, widgets, attrs)

    def format_output(self, rendered_widgets):
        return mark_safe(u'<p class="ui-datetimepickr">%s<span class="spacer"></span>%s</p>' % \
            (rendered_widgets[0], rendered_widgets[1]))
    
        
    class Media:
        js  = (settings.MEDIA_ROOT + "src/ui.timepickr.js",)
        css = (settings.MEDIA_ROOT + "css/ui-timepickr.css", )
