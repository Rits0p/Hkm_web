from django.contrib import admin
from .models import Faculty, Portfolio, StudentWork, StudentWorkImage

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'experience', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('name', 'role')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('name', 'role', 'tools')

class StudentWorkImageInline(admin.TabularInline):
    model = StudentWorkImage
    extra = 3
    sortable_field_name = "order"

@admin.register(StudentWork)
class StudentWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [StudentWorkImageInline]

