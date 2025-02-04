from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

# os models (classes) definem a estrutura dos dados de uma aplicação
class Evento(models.Model):
    titulo = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    descricao = models.TextField(validators=[MinLengthValidator(10)])
    local = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    data_evento = models.DateTimeField()
    capacidade = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        # retorna o nome do evento ao invés do endereço de memória
        return self.titulo


class Participante(models.Model):
    nome  = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    cpf = models.CharField(max_length=11, unique=True, validators=[MinLengthValidator(11)])
    email = models.EmailField(max_length=100, validators=[EmailValidator()])
    telefone = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="inscricoes") # se o evento for excluído a inscrição tbm será
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name="inscricoes")
    data_inscricao = models.DateTimeField(auto_now_add=True) # armazena a data e a hora da inscricao

    def __str__(self):
        return f"{self.participante.nome} inscrito em: {self.evento.titulo}"



