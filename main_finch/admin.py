from django.contrib import admin

from .models import finch
from .models import Feeding


# make sure to register the model

admin.site.register(finch)
admin.site.register(Feeding)
