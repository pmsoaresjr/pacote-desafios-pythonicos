"""
03. fix_start

Dada uma string s, retorne uma string onde
todas as ocorrências do primeiro caracter de s
foram substituidas por '*', exceto a primeira.

Exemplo: 'babble' retorna 'ba**le'

Assuma que a string tem tamanho 1 ou maior.

Dica: s.replace(stra, strb) retorna uma versão da string s
onde todas as instancias de stra foram substituidas por strb.
"""


def first_fix_start(s):
    # +++ SUA SOLUÇÃO +++
    string = ''
    for count, char in enumerate(s):
        if count == 0:
            first_letter = char
        if count > 0 and char == first_letter:
            string += '*'
        else:
            string += char
    return string


def second_fix_start(s):
    # +++ SUA SOLUÇÃO +++
    s = s[0] + s[1:].replace(s[0], "*")

    return s


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(first_fix_start, 'babble', 'ba**le')
    test(first_fix_start, 'aardvark', 'a*rdv*rk')
    test(first_fix_start, 'google', 'goo*le')
    test(first_fix_start, 'donut', 'donut')
    test(second_fix_start, 'babble', 'ba**le')
    test(second_fix_start, 'aardvark', 'a*rdv*rk')
    test(second_fix_start, 'google', 'goo*le')
    test(second_fix_start, 'donut', 'donut')
