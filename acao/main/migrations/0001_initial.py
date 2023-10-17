# Generated by Django 4.2.6 on 2023-10-16 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Acao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('preco_pago', models.FloatField()),
                ('valor_pago', models.FloatField()),
                ('quantidade', models.IntegerField()),
                ('data_compra', models.DateField()),
                ('preco_atual', models.FloatField()),
                ('valor_atual', models.FloatField()),
                ('Lucro_prejuizo', models.FloatField()),
                ('rentabilidade', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
