# Generated by Django 2.2.2 on 2019-07-01 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='name',
        ),
        migrations.AddField(
            model_name='habit',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='description',
            field=models.TextField(help_text='Enter comment about blog here.', max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='habit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Habit'),
        ),
    ]
