from django.db import models

class Todo(models.Model):
    nome = models.CharField(verbose_name="Nome",max_length=100,null=False,blank=False)
    descricao = models.CharField(verbose_name="Descrição",max_length=100,null=False,blank=False)
    preco = models.BigIntegerField(verbose_name="Preço",null=False)
    categoria = models.CharField(verbose_name="Categoria",max_length=100,null=False,blank=False)
    created_at = models.DateTimeField(verbose_name="Criado em",auto_now_add=True,null=False,blank=False)
