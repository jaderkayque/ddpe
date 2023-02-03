# Generated by Django 4.1.5 on 2023-02-01 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mmgd', '0002_orcamento_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]