# Generated by Django 3.0.5 on 2021-03-31 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210331_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rider',
        ),
        migrations.AddField(
            model_name='pedido',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedidouser', to='api.User'),
        ),
        migrations.AddField(
            model_name='rider',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]