# Generated by Django 3.2.5 on 2021-08-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0028_alter_book_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=30),
        ),
    ]