# Generated by Django 4.2.3 on 2023-08-15 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbcore', '0006_alter_feedback_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maininfo',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RemoveField(
            model_name='maininfo',
            name='lang',
        ),
        migrations.CreateModel(
            name='FullInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fullinfos', to='dbcore.language', verbose_name='Язык')),
            ],
            options={
                'verbose_name': 'Информация',
                'verbose_name_plural': 'Информации',
            },
        ),
        migrations.AddField(
            model_name='maininfo',
            name='full_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='maininfos', to='dbcore.fullinfo', verbose_name='Главный текст'),
        ),
    ]
