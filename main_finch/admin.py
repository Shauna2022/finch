from django.contrib import admin

from .models import Finch
from .models import Feeding


# make sure to register the model

admin.site.register(Finch)
admin.site.register(Feeding)
