from django.contrib import admin
from django.http.request import HttpRequest
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from dbcore.models import (Language, MainPage, MainOffer, Offer, FullInfo, MainInfo, Info, ChildInfo, Feedback)


class OfferInLine(admin.StackedInline):
    model = Offer
    extra = 1


class ChildInfoInLine(NestedStackedInline):
    model = ChildInfo
    extra = 1


class InfoInLine(NestedStackedInline):
    model = Info
    extra = 1
    inlines = [ChildInfoInLine]


class MainInfoInLine(NestedStackedInline):
    model = MainInfo
    extra = 1
    inlines = [InfoInLine]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    list_display = ('company_name',)


@admin.register(MainOffer)
class MainOfferAdmin(admin.ModelAdmin):
    list_display = ('name',)

    inlines = [OfferInLine]


@admin.register(FullInfo)
class MainInfoAdmin(NestedModelAdmin):
    list_display = ('name',)

    inlines = [MainInfoInLine]


@admin.register(Feedback)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'email')
