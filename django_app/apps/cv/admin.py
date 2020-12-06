from django.contrib import admin
from django.utils.html import format_html
from .models import Resume
from .documents import ResumeDocument

admin.site.site_title = 'CV Catcher'
admin.site.site_header = 'CV Catcher'
admin.site.admin_name = 'CV Catcher'
# admin.site.site_url = '/'
admin.site.index_title = 'Admin'


class NoEditAdmin(admin.ModelAdmin):
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + [field.name for field in obj._meta.fields] + [field.name for field in
                                                                                          obj._meta.many_to_many]


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    # list_display = ('full_name', 'first_name', 'last_name', 'attached_file')
    list_display = ('full_name', 'first_name', 'last_name', 'sow_resume_button')
    search_fields = ('',)

    def has_change_permission(self, request, obj=None):
        return False

    def sow_resume_button(self, obj):
        return format_html("""
            <a class="button show_resume_button" target="_blank" href="{}">{}</a>
        """, obj.attached_file.url, 'Show CV')

    sow_resume_button.short_description = "Show"

    def get_search_results(self, request, queryset, search_term: str):
        if not search_term:
            return queryset, True
        terms = search_term.split(',')
        for term in terms:
            queryset &= ResumeDocument.search().query("match", text=term).to_queryset()
        return queryset, True
