# Generated by Django 3.1.3 on 2021-02-24 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0021_auto_20210224_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainarticle',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mainarticle', to='index.category'),
        ),
    ]
