# Generated by Django 4.0 on 2021-12-14 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('review', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField()),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer_book', to='auth.user')),
            ],
        ),
        migrations.AlterField(
            model_name='highlight',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]