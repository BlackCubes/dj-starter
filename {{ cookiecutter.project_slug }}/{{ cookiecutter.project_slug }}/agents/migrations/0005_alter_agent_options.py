# Generated by Django 4.0.3 on 2022-03-24 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0004_alter_agent_id_alter_historicalagent_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'ordering': ['name']},
        ),
    ]
