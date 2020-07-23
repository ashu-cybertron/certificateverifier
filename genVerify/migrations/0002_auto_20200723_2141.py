# Generated by Django 3.0.2 on 2020-07-23 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('genVerify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='certificate_id',
            field=models.CharField(default='syed0python02134', max_length=20),
        ),
        migrations.AddField(
            model_name='attendee',
            name='event_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date of Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendee',
            name='event_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]