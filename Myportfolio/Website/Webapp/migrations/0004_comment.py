# Generated by Django 4.1.2 on 2022-11-08 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0003_rename_describtion_skill_detial_profile_selfexplain_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('ratting', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': ['Comment'],
                'ordering': ['id'],
            },
        ),
    ]
