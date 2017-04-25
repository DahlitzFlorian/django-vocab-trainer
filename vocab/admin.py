from django.contrib import admin

from .models import Learnset, Vocabulary


class VocabularyInline(admin.TabularInline):
    model = Vocabulary
    extra = 3


class LearnsetAdmin(admin.ModelAdmin):
    # define inlines
    inlines = [VocabularyInline]

    # define search terms
    search_fields = ['learnset_name']

    # customize list displaying
    list_display = ('learnset_name', 'creation_date')


# register in admin panel
admin.site.register(Learnset, LearnsetAdmin)
