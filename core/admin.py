from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User, Experience, Education, Certification


class ExperienceAdmin(admin.ModelAdmin):
    # exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()
        super().save_model(request, obj, form, change)

class EducationAdmin(admin.ModelAdmin):
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

class CertificationAdmin(admin.ModelAdmin):
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('description',)}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
