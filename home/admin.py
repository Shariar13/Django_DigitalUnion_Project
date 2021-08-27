from django.contrib import admin
from .models import post
from .models import comment
from .models import complain
from .models import next_project

admin.site.register (post)
admin.site.register (comment)
admin.site.register (complain)
admin.site.register (next_project)
