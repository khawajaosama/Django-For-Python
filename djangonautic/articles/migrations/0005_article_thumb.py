# Generated by Django 2.1.5 on 2019-01-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
