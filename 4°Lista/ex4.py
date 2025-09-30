def verifica_json(json_str):
    pares = {']': '[', '}': '{'}
    pilha = []
    for ch in json_str:
        if ch in "[{":
            pilha.append(ch)
        elif ch in "]}":
            if not pilha or pilha[-1] != pares[ch]:
                return False
            pilha.pop()
    return len(pilha) == 0

print(verifica_json('{"nome": "João", "idade": 25}'))   
print(verifica_json('{"a": [1, 2, 3]}'))                
print(verifica_json('{"a": [1, 2, 3}'))                 
