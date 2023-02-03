from django.db import models
from users.models import User
# Create your models here.


class Orcamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField()
    usina = models.CharField(max_length=200)
    lat_cliente = models.CharField(max_length=200)
    long_cliente = models.CharField(max_length=200)
    lat_conexao = models.CharField(max_length=200)
    long_conexao = models.CharField(max_length=200)
    potencia = models.FloatField(max_length=10)
    mapa = models.CharField(max_length=100000)
    endereco = models.CharField(max_length=200)
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    etd = models.CharField(max_length=200)
    sigla_etd = models.CharField(max_length=3)
    alm = models.CharField(max_length=10)
    empresa = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=200)
    resp_tecnico = models.CharField(max_length=200)
    endereco_tec = models.CharField(max_length=200)
    telefone_tec = models.CharField(max_length=200)
    email_tec = models.CharField(max_length=200)
    documento_emitido = models.BooleanField(default=False)
    obra1 = models.CharField(max_length=200)
    obra2 = models.CharField(max_length=200)
    obra_valor1 = models.CharField(max_length=50)
    obra_valor2 = models.CharField(max_length=50)
    ddpe_regiao = models.CharField(max_length=200)
    gci_id = models.CharField(max_length=20)
    observacao = models.CharField(max_length=1000)
    tensao = models.FloatField(max_length=4)

    def __str__(self):
        return f"Usuario: {self.usuario}, data: {self.data} ,usina: {self.usina}, potencia: {self.potencia}, municipio: {self.municipio}, empresa: {self.empresa}, documento emitido: {self.documento_emitido}"
