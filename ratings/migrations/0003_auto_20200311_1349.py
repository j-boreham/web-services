# Generated by Django 3.0.4 on 2020-03-11 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20200311_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moduleinstance',
            old_name='name',
            new_name='code',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='module_code',
        ),
    ]