from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    # Can change the admin.something so the something changes how it's displayed!
    model = Choice
    extra = 3
    # By default, provide enough fields for 3 choices

#  create a model admin class, 
# then pass it as the second argument to admin.site.register() – any time you need to change the admin options for a model.


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # Makes pub date come before the question text question
    list_filter = ['pub_date']
    # Filter date
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Search box
    search_fields = ['question_text']
    

admin.site.register(Question, QuestionAdmin)