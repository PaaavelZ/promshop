from django.contrib import admin
from django.contrib.admin.options import StackedInline, TabularInline
from django.http.request import HttpRequest
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from dbcore.models import (Language, MainPage, MainOffer, Offer, FullInfo, MainInfo, Info, SliderMainInfo, SliderInfo, SliderChildInfo, Feedback)


class OfferInLine(admin.StackedInline):
    model = Offer
    extra = 1


class SliderChildInfoInLine(NestedStackedInline):
    model = SliderChildInfo
    extra = 1


class SliderInfoInLine(NestedStackedInline):
    model = SliderInfo
    extra = 1
    inlines = [SliderChildInfoInLine]


# class SliderMainInfoInLine(NestedStackedInline):
#     model = SliderMainInfo
#     extra = 0
#     inlines = [SliderInfoInLine]


class InfoInLine(NestedStackedInline):
    model = Info
    extra = 0


class MainInfoInLine(NestedStackedInline):
    model = MainInfo
    extra = 0
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
class FullInfoAdmin(NestedModelAdmin):
    list_display = ('name',)

    inlines = [MainInfoInLine]


@admin.register(SliderMainInfo)
class SliderMainInfoAdmin(NestedModelAdmin):
    list_display = ('name',)

    inlines = [SliderInfoInLine]


@admin.register(SliderChildInfo)
class SliderChildInfoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('slider_info',)
    search_fields = ('slider_info',)

    
@admin.register(Feedback)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'email')
