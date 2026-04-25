from django.contrib import admin
from .models import Instructor, Learner, Course, Enrollment

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [EnrollmentInline]
    list_display = ("name", "description")
    search_fields = ("name",)
    filter_horizontal = ("instructors",)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "full_time", "total_learners")
    search_fields = ("first_name", "last_name", "email")

class LearnerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "occupation", "social_link")
    search_fields = ("first_name", "last_name", "email")

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("learner", "course", "date_enrolled", "mode", "grade", "status", "progress", "last_accessed", "certificate_issued")
    search_fields = ("learner__first_name", "learner__last_name", "course__name")
    list_filter = ("status", "mode", "certificate_issued")

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Learner, LearnerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
