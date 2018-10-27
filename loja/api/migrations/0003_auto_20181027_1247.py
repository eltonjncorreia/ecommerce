# Generated by Django 2.1.2 on 2018-10-27 15:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181027_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
