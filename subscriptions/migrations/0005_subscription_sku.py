# Generated by Django 3.1.5 on 2021-02-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_category_friendly_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
