# Generated by Django 4.1.7 on 2023-03-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=50)),
                ('contenuto', models.CharField(max_length=150)),
                ('autore', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'library',
            },
        ),
    ]
