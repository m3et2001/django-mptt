# Generated by Django 4.2.1 on 2023-05-12 11:27

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='chatFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.BigIntegerField(default=0)),
                ('questions', models.CharField(blank=True, max_length=200, null=True)),
                ('option', models.CharField(blank=True, max_length=100, null=True)),
                ('answer', models.CharField(blank=True, max_length=200, null=True)),
                ('is_answer', models.BooleanField(default=False)),
                ('is_option', models.BooleanField(default=False)),
                ('is_question', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='chat_bot.chatflow')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
