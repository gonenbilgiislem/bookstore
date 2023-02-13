# Generated by Django 4.1 on 2023-02-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
