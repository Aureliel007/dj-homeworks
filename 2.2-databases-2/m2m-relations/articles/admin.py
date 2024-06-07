from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        counter = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                counter += 1
            if counter > 1:
                raise ValidationError('Для каждой статьи можно выбрать только один главный тэг.')

        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 3

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_at')
    list_display_links = ('id', 'title')
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
