import uuid
import random
import string
from django.db import models
from utils.models import BaseModel
from cuser.models import AbstractCUser
from django.conf import settings


class BrazilianState(models.TextChoices):
    AC = "AC", "Acre"
    AL = "AL", "Alagoas"
    AP = "AP", "Amapá"
    AM = "AM", "Amazonas"
    BA = "BA", "Bahia"
    CE = "CE", "Ceará"
    ES = "ES", "Espírito Santo"
    GO = "GO", "Goiás"
    MA = "MA", "Maranhão"
    MT = "MT", "Mato Grosso"
    MS = "MS", "Mato Grosso do Sul"
    MG = "MG", "Minas Gerais"
    PA = "PA", "Pará"
    PB = "PB", "Paraíba"
    PR = "PR", "Paraná"
    PE = "PE", "Pernambuco"
    PI = "PI", "Piauí"
    RJ = "RJ", "Rio de Janeiro"
    RN = "RN", "Rio Grande do Norte"
    RS = "RS", "Rio Grande do Sul"
    RO = "RO", "Rondônia"
    RR = "RR", "Roraima"
    SC = "SC", "Santa Catarina"
    SP = "SP", "São Paulo"
    SE = "SE", "Sergipe"
    TO = "TO", "Tocantins"
    DF = "DF", "Distrito Federal"

class TransactionType(models.TextChoices):
    RENT = "RENT", "Rent"
    SALE = "SALE", "Sale"


class User(AbstractCUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=100, help_text="Nome do usuário", verbose_name="Nome"
    )

    class Meta(AbstractCUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def save(self, **kwargs) -> None:
        return super().save(**kwargs)

    def __str__(self):
        return self.email + " | " + self.first_name + " " + self.last_name
    
class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    library_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    creation_date = models.DateField(auto_now_add=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'Stock {self.id} of user {self.user.name}'

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    rental_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

class BookTransaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    transaction_type = models.CharField(
        max_length=50,
        choices=TransactionType.choices,
        default=TransactionType.RENT,
    )
    transaction_date = models.DateField(auto_now_add=True)
    transaction_value = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Transaction {self.id} of book {self.book.title} by user {self.user.name} at library {self.library.library_name}'

    def __str__(self):
        return self.title