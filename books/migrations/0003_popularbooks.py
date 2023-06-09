# Generated by Django 4.2 on 2023-04-07 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_authors_options_alter_books_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ManyToManyField(max_length=100, to='books.books', verbose_name='book')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
    ]
