# Generated by Django 4.2.1 on 2023-05-12 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_bot', '0002_alter_chatflow_answer_alter_chatflow_option_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatflow',
            name='step',
        ),
    ]
