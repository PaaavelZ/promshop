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
        verbose_name = '1. Главная страница'
        verbose_name_plural = '1. Главная страница'

    def __str__(self) -> str:
        return self.company_name


class Offer(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Название слайда'),)
    lang = models.ForeignKey('Language',
                             related_name='offers',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Язык'),)

    class Meta:
        verbose_name = '2. Слайд с предложениями'
        verbose_name_plural = '2. Слайды с предложениями'

    def __str__(self) -> str:
        return self.name


class ChildOffer(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    text = RichTextField(verbose_name=_('Текст заголовка'),)
    img = models.ImageField(verbose_name='Картинка позади текста')
    offer = models.ForeignKey('Offer',
                            related_name='childoffers',
                            on_delete=models.SET_NULL,
                            null=True,
                            verbose_name=_('Слайд'),)
    
    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

    def __str__(self) -> str:
        return self.name


class Info(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    lang = models.ForeignKey('Language',
                             related_name='infos',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Язык'),)
    class Meta:
        verbose_name = '3. Информация'
        verbose_name_plural = '3. Информация'

    def __str__(self) -> str:
        return self.name

        
class CategoryInfo(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    info = models.ForeignKey('Info',
                             related_name='categoryinfos',
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name=_('Главный текст'),)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class ChildCategoryInfo(models.Model):
    name = models.CharField(max_length=100, 
                            blank=False, 
                            null=False,
                            verbose_name=_('Заголовок'),)
    category_info = models.ForeignKey('CategoryInfo',
                                  related_name='childcategoryinfos',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  verbose_name=_('Слайд'))
    
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегория'

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
                              verbose_name=_('Почта'),)
    text = RichTextField()

    class Meta:
        verbose_name = '4. Клиентская заявка'
        verbose_name_plural = '4. Клиентские заявки'

    def __str__(self) -> str:
        return self.email
    

class EmailEntry(models.Model):
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

    class Meta:
        verbose_name = '5. Имейлы'
        verbose_name_plural = '5. Имейлы'

    def __str__(self) -> str:
        return self.to_email