# Conteúdo do arquivo test_soma.py
from matematica import Matematica

# A instância do objeto deve ser criada, ou o método deve ser chamado.
# Usando a instância no teste:

def test_somar_corretamente():
    # Cria a instância da classe DENTRO da função de teste
    calc = Matematica() 
    assert calc.somar(1, 2) == 3