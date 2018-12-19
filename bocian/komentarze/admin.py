from django.contrib import admin

# Register your models here.
@admin.register(Auto)
class AdminAuto (admin.ModelAdmin):
    pass

#admin.site.register(Auto)
