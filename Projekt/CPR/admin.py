from django.contrib import admin
from .models import Choice, Question, Zgloszenie, Policja, Szpital, StrazPozarna
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
#^tuples


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Zgloszenie)
admin.site.register(Policja)
admin.site.register(Szpital)
admin.site.register(StrazPozarna)