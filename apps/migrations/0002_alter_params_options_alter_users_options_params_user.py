# Generated by Django 4.2.1 on 2023-05-31 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='params',
            options={'verbose_name_plural': 'Params'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='params',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='params', to='apps.users'),
            preserve_default=False,
        ),
    ]