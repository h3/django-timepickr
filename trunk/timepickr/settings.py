# coding: utf-8

from django.conf import settings

# Media path
MEDIA_ROOT = getattr(settings, "TIMEPICKR_MEDIA_ROOT", settings.ADMIN_MEDIA_PREFIX +'/jquery/ui-timepickr/')

