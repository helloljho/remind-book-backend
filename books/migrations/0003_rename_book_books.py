# Generated by Django 4.0 on 2021-12-14 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('books', '0002_book_alter_highlight_book_delete_books'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Books',
        ),
    ]