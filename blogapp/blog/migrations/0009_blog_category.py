# Generated by Django 4.1.5 on 2023-03-10 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]
