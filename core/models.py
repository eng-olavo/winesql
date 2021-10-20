# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acucares(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome


    class Meta:
        managed = False
        db_table = 'acucares'

    verbose_name = 'Açucar'
    verbose_name_plural = 'Açucares'


class Nacionalidades(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'nacionalidades'

    verbose_name = 'Nacionalidade'
    verbose_name_plural = 'Nacionalidades'


class Tipos(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'tipos'

    verbose_name = 'tipo'
    verbose_name_plural = 'tipos'


class Uvas(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'uvas'

    verbose_name = 'uva'
    verbose_name_plural = 'Uvas'


class UvasVinhos(models.Model):
    #percentual_uva = models.IntegerField()
    id_vinho = models.ForeignKey('Vinhos', models.DO_NOTHING, db_column='id_vinho')
    id_uva = models.ForeignKey(Uvas, models.DO_NOTHING, db_column='id_uva')

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'uvas_vinhos'

    verbose_name = 'uva_vinho'
    verbose_name_plural = 'uvas_vinhos'


class Vinhos(models.Model):
    nome = models.CharField(max_length=45)
    safra = models.IntegerField()
    vinicola = models.CharField(max_length=45)
    alcool = models.DecimalField(max_digits=2, decimal_places=1)
    temperatura = models.IntegerField()
    volume = models.IntegerField()
    guarda = models.IntegerField()
    amadurecimento = models.CharField(max_length=256)
    visual = models.CharField(max_length=45)
    olfativo = models.CharField(max_length=512)
    gustativo = models.CharField(max_length=512)
    destaque = models.IntegerField()
    promocao = models.IntegerField()
    avaliacao = models.DecimalField(max_digits=1, decimal_places=1)
    numero_avaliacoes = models.IntegerField()
    maior_avaliacao = models.DecimalField(max_digits=1, decimal_places=1)
    ativo = models.IntegerField()
    data_criacao = models.DateField()
    data_atualizacao = models.DateField()
    id_tipo = models.ForeignKey(Tipos, models.DO_NOTHING, db_column='id_tipo')
    id_acucar = models.ForeignKey(Acucares, models.DO_NOTHING, db_column='id_acucar')
    id_uvas = models.ForeignKey(UvasVinhos, models.DO_NOTHING, db_column='id_uvas')
    id_nacionalidade = models.ForeignKey(Nacionalidades, models.DO_NOTHING, db_column='id_nacionalidade')

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'vinhos'

    verbose_name = 'vinho'
    verbose_name_plural = 'vinhos'
