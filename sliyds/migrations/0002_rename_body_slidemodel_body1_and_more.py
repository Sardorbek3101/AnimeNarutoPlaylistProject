# Generated by Django 4.0.6 on 2022-08-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sliyds', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slidemodel',
            old_name='body',
            new_name='body1',
        ),
        migrations.RenameField(
            model_name='slidemodel',
            old_name='name',
            new_name='name1',
        ),
        migrations.AddField(
            model_name='slidemodel',
            name='body2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='slidemodel',
            name='body3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='slidemodel',
            name='body4',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='slidemodel',
            name='body5',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='slidemodel',
            name='name2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='slidemodel',
            name='name3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='slidemodel',
            name='name4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='slidemodel',
            name='name5',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='slidemodel',
            name='title',
            field=models.CharField(default='AnimeFan', max_length=50),
        ),
    ]
