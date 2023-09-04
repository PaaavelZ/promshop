from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Language(models.Model):
    LANGUAGE = (
        ('ru', 'ru'),
        ('eng', 'eng'),
        ('kz', 'kz'),
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
    
    def __str__(self) -> str:
        return self.name
    

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
        verbose_name_plural = 'Главная страница'

    def __str__(self) -> str:
        return self.company_name


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

    def __str__(self) -> str:
        return self.name


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

    def __str__(self) -> str:
        return self.name


class FullInfo(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    lang = models.ForeignKey('Language',
                             related_name='fullinfos',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Язык'),)
    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информации'

    def __str__(self) -> str:
        return self.name

        
class MainInfo(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    full_info = models.ForeignKey('FullInfo',
                             related_name='maininfos',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Главный текст'),)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class Info(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    main_info = models.ForeignKey('MainInfo',
                                  related_name='infos',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  verbose_name=_('Слайд'))
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name
    

class SliderMainInfo(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    lang = models.ForeignKey('Language',
                             related_name='sliderfullinfos',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Язык'),)
    class Meta:
        verbose_name = 'Категория (слайдер)'
        verbose_name_plural = 'Категории (слайдер)'

    def __str__(self) -> str:
        return self.name
    

class SliderInfo(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    slider_main_info = models.ForeignKey('SliderMainInfo',
                                  related_name='sliderinfos',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  verbose_name=_('Слайд'))
    
    class Meta:
        verbose_name = 'Подкатегория (слайлдер)'
        verbose_name_plural = 'Подкатегория (слайлдер)'

    def __str__(self) -> str:
        return self.name
        

class SliderMainInfo(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    lang = models.ForeignKey('Language',
                             related_name='sliderfullinfos',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Язык'),)
    class Meta:
        verbose_name = 'Категория (слайдер)'
        verbose_name_plural = 'Категории (слайдер)'


class SliderInfo(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    slider_main_info = models.ForeignKey('SliderMainInfo',
                                  related_name='sliderinfos',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  verbose_name=_('Слайд'))
    
    class Meta:
        verbose_name = 'Подкатегория (слайлдер)'
        verbose_name_plural = 'Подкатегория (слайлдер)'


class SliderChildInfo(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    img = models.FileField(verbose_name='Фото', null=True, blank=True)
    text = RichTextField(verbose_name='Текст')
    slider_info = models.ForeignKey('SliderInfo',
                             related_name='sliderchildinfos',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Слайд'))
    
    class Meta:
        verbose_name = 'Пример (слайлдер)'
        verbose_name_plural = 'Примеры (слайлдер)'

    def __str__(self) -> str:
        return self.name


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

    def __str__(self) -> str:
        return self.name
    

class EmailEntry(models.Model):
    from_email = models.CharField(max_length=255, 
                                  blank=False, 
                                  null=False,)
    to_email = models.CharField(max_length=255, 
                                blank=False, 
                                null=False,)
    subject = models.CharField(max_length=255, 
                               blank=False, 
                               null=False,)
    text = models.TextField()
    is_sent = models.BooleanField(default=False)

    def mark_as_sent(self):
        self.is_sent = True
        self.save(update_fields=['is_sent'])