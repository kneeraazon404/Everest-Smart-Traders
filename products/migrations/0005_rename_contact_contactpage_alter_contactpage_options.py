# Generated by Django 5.0.3 on 2024-03-29 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_position_contact_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactPage',
        ),
        migrations.AlterModelOptions(
            name='contactpage',
            options={'verbose_name': 'Contact Page', 'verbose_name_plural': 'Contact Page'},
        ),
    ]