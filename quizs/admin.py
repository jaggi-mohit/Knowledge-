from django.contrib import admin

from .models import EngQuiz,SciQuiz,CompQuiz

# Register your models here.

admin.site.register(EngQuiz)
admin.site.register(SciQuiz)
admin.site.register(CompQuiz)
