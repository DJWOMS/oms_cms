# Generated by Django 2.2.5 on 2019-09-16 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(choices=[('en', 'English'), ('ru', 'Russian')], default='en', max_length=7, verbose_name='Язык')),
                ('slug', models.SlugField(blank=True, help_text='Укажите url', max_length=500, null=True, verbose_name='url')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('edit_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата редактирования')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовать?')),
                ('template', models.CharField(default='pages/home.html', max_length=500, verbose_name='Шаблон')),
                ('registration_required', models.BooleanField(default=False, help_text='Если флажок установлен, только зарегистрированные пользователи могут просматривать страницу.', verbose_name='Требуется регистрация')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'unique_together': {('lang', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='BlockPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Для обращения в шаблоне', max_length=100, verbose_name='Имя')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок')),
                ('sub_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Под заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Pages')),
            ],
            options={
                'verbose_name': 'Блок страницы',
                'verbose_name_plural': 'Блоки страницы',
                'ordering': ['sort'],
            },
        ),
    ]
