# Generated by Django 2.2.4 on 2019-08-28 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendname', to='userprofile.UserProfile'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.UserProfile'),
        ),
    ]
