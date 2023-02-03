# Generated by Django 4.1.5 on 2023-01-26 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usina', models.CharField(max_length=200)),
                ('lat_cliente', models.CharField(max_length=200)),
                ('long_cliente', models.CharField(max_length=200)),
                ('lat_conexao', models.CharField(max_length=200)),
                ('long_conexao', models.CharField(max_length=200)),
                ('potencia', models.FloatField(max_length=10)),
                ('mapa', models.CharField(max_length=100000)),
                ('endereco', models.CharField(max_length=200)),
                ('municipio', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('etd', models.CharField(max_length=200)),
                ('sigla_etd', models.CharField(max_length=3)),
                ('alm', models.CharField(max_length=10)),
                ('empresa', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=200)),
                ('resp_tecnico', models.CharField(max_length=200)),
                ('endereco_tec', models.CharField(max_length=200)),
                ('telefone_tec', models.CharField(max_length=200)),
                ('email_tec', models.CharField(max_length=200)),
                ('documento_emitido', models.BooleanField(default=False)),
                ('obra1', models.CharField(max_length=200)),
                ('obra2', models.CharField(max_length=200)),
                ('obra_valor1', models.CharField(max_length=50)),
                ('obra_valor2', models.CharField(max_length=50)),
                ('ddpe_regiao', models.CharField(max_length=200)),
                ('gci_id', models.CharField(max_length=20)),
                ('observacao', models.CharField(max_length=1000)),
                ('tensao', models.FloatField(max_length=4)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
