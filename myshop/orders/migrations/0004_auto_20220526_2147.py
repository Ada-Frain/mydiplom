# Generated by Django 3.2.5 on 2022-05-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=250, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=20, null=True, verbose_name='Почтовый индекс'),
        ),
    ]
