from django.core.exceptions import ValidationError
from validate_docbr import CPF
import re


# função para validar cpf
def cpf_invalido(value):
    cpf = CPF()
    cpf_valido = cpf.validate(value)
    return not cpf_valido
    # if not cpf.validate(value):
    #     raise ValidationError('CPF inválido')


def nome_invalido(nome):
    # verifica se o nome é maior que 3, se é alfanúmerico ou se contém espaço
    return len(nome) <= 3 or not all(char.isalpha() or char.isspace() for char in nome)

def email_invalido(email):
    return '@' not in email or '.' not in email.split('@')[1]

def telefone_invalido(telefone):
    modelo = "[0-9]{2} [0-9]{5} [0-9]{4}"
    response = re.findall(modelo, telefone)
    return not response
    # return len(telefone) != 10 or not telefone.isdigit()

# # validações
# def validate_nome(self, nome):
#     if not nome.replace(' ', '').isalpha():
#         raise serializers.ValidationError("O nome só pode conter letras e espaços!!")
#     if len(nome) < 3:
#         raise serializers.ValidationError("O nome deve ter pelo menos 3 caracteres")
#
#
# def validate_email(self, email):
#     if '@' not in email or '.' not in email.split('@')[1]:
#         raise serializers.ValidationError("O email deve ser valido")
#     return email
#
#
# def validate_telefone(self, telefone):
#     # if not telefone:
#     #     return telefone

    # # if len(telefone) < 10 or not telefone.isdigit():
    #     raise serializers.ValidationError("O Telefone deve ter pelo menos 10 digitos")
    # return telefone
