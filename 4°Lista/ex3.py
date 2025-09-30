def verifica_tags_html(html):
    pilha = []
    i = 0
    while i < len(html):
        if html[i] == "<":
            j = html.find(">", i)
            tag = html[i+1:j]
            if not tag.startswith("/"):
                pilha.append(tag)
            else:
                if not pilha or pilha[-1] != tag[1:]:
                    return False
                pilha.pop()
            i = j
        i += 1
    return len(pilha) == 0

print(verifica_tags_html("<html><body></body></html>")) 
print(verifica_tags_html("<div><p></div></p>"))          
print(verifica_tags_html("<h1><b></b></h1>"))            
