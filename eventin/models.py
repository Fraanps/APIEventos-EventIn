from django.db import models

# os models (classes) definem a estrutura dos dados de uma aplicação
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    local = models.CharField(max_length=100)
    data_evento = models.DateTimeField()
    capacidade = models.PositiveIntegerField()

    def __str__(self):
        # retorna o nome do evento ao invés do endereço de memória
        return self.titulo


class Participante(models.Model):
    nome  = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="inscricoes") # se o evento for excluído a inscrição tbm será
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name="inscricoes")
    data_inscricao = models.DateTimeField(auto_now_add=True) # armazena a data e a hora da inscricao

    def __str__(self):
        return f"{self.participante.nome} inscrito em: {self.evento.titulo}"






