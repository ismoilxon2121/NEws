# Generated by Django 4.2.1 on 2023-06-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_image_blog_alter_image_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]