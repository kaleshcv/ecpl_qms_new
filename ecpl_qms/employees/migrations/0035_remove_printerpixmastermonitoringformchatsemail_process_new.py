# Generated by Django 3.2.4 on 2021-06-28 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0034_printerpixmastermonitoringformchatsemail_process_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printerpixmastermonitoringformchatsemail',
            name='process_new',
        ),
    ]
