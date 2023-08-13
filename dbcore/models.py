from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Language(models.Model):
    LANGUAGE = (
        ('RU', 'RU'),
        ('ENG', 'ENG'),
        ('KZ', 'KZ'),
    )

    name = models.CharField(max_length=3,
                            unique=True,
                            null=False,
                            blank=False,
                            choices=LANGUAGE,
                            verbose_name=_('Языковая раскладка'))
    
    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
    

class MainPage(models.Model):
    company_name = models.CharField(max_length=50, 
                                    blank=False, 
                                    null=False,
                                    verbose_name=_('Имя компании'),)
    text = RichTextField(verbose_name=_('Главный текст'),)
    lang = models.ForeignKey('Language',
                             related_name='mainpages',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Язык'),)

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главные страницы'


class MainOffer(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Название слайда'),)
    lang = models.ForeignKey('Language',
                             related_name='mainoffers',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Язык'),)

    class Meta:
        verbose_name = 'Слайд с предложениями'
        verbose_name_plural = 'Слайды с предложениями'


class Offer(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    text = RichTextField(verbose_name=_('Текст заголовка'),)
    img = models.ImageField(verbose_name='Картинка позади текста')
    main_offer = models.ForeignKey('MainOffer',
                                   related_name='offers',
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   verbose_name=_('Слайд'),)
    
    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'


class MainInfo(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    lang = models.ForeignKey('Language',
                             related_name='maininfos',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Язык'),)
    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информации'


class Info(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    text = RichTextField(verbose_name='Текст')
    main_info = models.ForeignKey('MainInfo',
                                  related_name='infos',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  verbose_name=_('Слайд'))
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ChildInfo(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    img = models.ImageField(verbose_name=_('Фото'))
    text = RichTextField(verbose_name='Текст')
    info = models.ForeignKey('Info',
                             related_name='childinfos',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Слайд'))
    
    class Meta:
        verbose_name = 'Пример'
        verbose_name_plural = 'Примеры'


class Feedback(models.Model):
    fio = models.CharField(max_length=255, 
                           blank=False, 
                           null=False,
                           verbose_name=_('ФИО'),)
    phone = models.CharField(max_length=20, 
                             blank=False, 
                             null=False,
                             verbose_name=_('Телефон'),)
    email = models.EmailField(max_length=20, 
                              blank=False, 
                              null=False,
                              verbose_name=_('Телефон'),)
    text =RichTextField()

    class Meta:
        verbose_name = 'Клиентская заявка'
        verbose_name_plural = 'Клиентские заявки'