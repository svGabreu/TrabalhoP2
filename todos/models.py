from django.db import models

class Produto(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100, null=False, blank=False)
    descricao = models.TextField(verbose_name="Descrição", null=False, blank=False)  # Usar TextField para descrições mais longas
    preco = models.DecimalField(verbose_name="Preço", max_digits=10, decimal_places=2, null=False)  # Usar DecimalField para preço
    categoria = models.CharField(verbose_name="Categoria", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
