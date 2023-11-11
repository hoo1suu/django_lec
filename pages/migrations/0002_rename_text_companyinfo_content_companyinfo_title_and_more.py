# Generated by Django 4.2.7 on 2023-11-11 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinfo',
            old_name='text',
            new_name='content',
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='title',
            field=models.CharField(default='Default Title', max_length=200),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='title',
            field=models.CharField(default='Default Title', max_length=200),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='image',
            field=models.ImageField(upload_to='company_info/'),
        ),
    ]