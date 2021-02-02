# Generated by Django 3.1.5 on 2021-02-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='hello', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='duration',
            field=models.CharField(max_length=254),
        ),
    ]
