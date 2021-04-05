# Generated by Django 2.2 on 2021-04-05 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0003_auto_20210404_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='next_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='photo_app.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='previous_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous', to='photo_app.Post'),
        ),
    ]