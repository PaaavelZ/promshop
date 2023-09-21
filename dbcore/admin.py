from django.contrib import admin
from django.contrib.admin.options import StackedInline, TabularInline
from django.http.request import HttpRequest
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from dbcore.models import (Language, MainPage, Offer, ChildOffer, Info, CategoryInfo, ChildCategoryInfo, Feedback, EmailEntry)


class ChildOfferInLine(admin.StackedInline):
    model = ChildOffer
    extra = 1


class ChildCategoryInfoInLine(NestedStackedInline):
    model = ChildCategoryInfo
    extra = 0


class CategoryInfoInLine(NestedStackedInline):
    model = CategoryInfo
    extra = 0
    inlines = [ChildCategoryInfoInLine]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    list_display = ('text',)


@admin.register(Offer)
class MainOfferAdmin(admin.ModelAdmin):
    list_display = ('name',)

    inlines = [ChildOfferInLine]


@admin.register(Info)
class InfoAdmin(NestedModelAdmin):
    list_display = ('name',)

    inlines = [CategoryInfoInLine]

    
@admin.register(Feedback)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'email')


@admin.register(EmailEntry)
class EntryMailAdmin(admin.ModelAdmin):
    list_display = ('feedback',)
