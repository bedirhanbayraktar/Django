# Generated by Django 3.2.9 on 2023-03-11 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_blog_category_blog_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.Category'),
        ),
    ]
