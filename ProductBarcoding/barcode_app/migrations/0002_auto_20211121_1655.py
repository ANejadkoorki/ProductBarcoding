# Generated by Django 3.2.9 on 2021-11-21 16:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barcode_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mother_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='barcode_app.mothercategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='second_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='barcode_app.secondcategory'),
        ),
        migrations.AlterField(
            model_name='colour',
            name='code',
            field=models.CharField(max_length=2, unique=True, validators=[django.core.validators.RegexValidator(message='the code should be matched with the correct format : 01-99', regex='^[0-9]{1}[1-9]{1}$')], verbose_name='colour code'),
        ),
        migrations.AlterField(
            model_name='mothercategory',
            name='code',
            field=models.CharField(max_length=2, unique=True, validators=[django.core.validators.RegexValidator(message='the code should be matched with the correct format : 01-99', regex='^[0-9]{1}[1-9]{1}$')], verbose_name='mother category code'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=5, unique=True, validators=[django.core.validators.RegexValidator(message='the code should be matched with the correct format : 00001-99999', regex='^[0-9]{4}[1-9]{1}$')], verbose_name='product code'),
        ),
        migrations.AlterField(
            model_name='secondcategory',
            name='code',
            field=models.CharField(max_length=2, unique=True, validators=[django.core.validators.RegexValidator(message='the code should be matched with the correct format : 01-99', regex='^[0-9]{1}[1-9]{1}$')], verbose_name='second category code'),
        ),
        migrations.AlterField(
            model_name='size',
            name='code',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(message='the code should be matched with the correct format : 01-99', regex='^[0-9]{1}[1-9]{1}$')], verbose_name='size code'),
        ),
        migrations.AlterField(
            model_name='store',
            name='code',
            field=models.CharField(max_length=4, unique=True, validators=[django.core.validators.RegexValidator(message='the code should be matched with the correct format : 0001-9999', regex='^[0-9]{3}[1-9]{1}$')], verbose_name='store code'),
        ),
        migrations.AlterField(
            model_name='thirdcategory',
            name='code',
            field=models.CharField(max_length=3, unique=True, validators=[django.core.validators.RegexValidator(message='the code should be matched with the correct format : 001-999', regex='^[0-9]{2}[1-9]{1}$')], verbose_name='third category code'),
        ),
    ]
