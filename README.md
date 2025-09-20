Respostas da Atividade de 
Complexidade Computacional
2ª Lista de Exercícios 

---

1. Cronometrar um algoritmo com diferentes tamanhos de problemas:
   Resposta: **b.**
   Justificativa: Porque medir tempos reais dá a informação sobre o comportamento do algoritmo numa plataforma de hardware ou sofware específica (CPU, SO, compilador etc.).Essas medições fornecem dados concretos dessa plataforma; 
---

2. Instruções de contagem:
   Resposta: **a.**
   Justificativa: contar instruções (ou operações elementares) produz uma medida mais independente de plataforma, é uma contagem abstrata que pode ser comparada entre máquinas.No entanto, a contagem também evidencia crescimento exponencial e sua impropriedade quando o problema cresce.

---

3. As expressões $O(n)$, $O(n^2)$ e $O(k^n)$ são, respectivamente:
   Resposta: **b. Linear, quadrática e exponencial.**
   Justificativa: $O(n)$ = linear; $O(n^2)$ = quadrática; $O(k^n)$ (com $k>1$) = exponencial.

---

4. De um modo geral, é melhor:
   Resposta: **b. Escolher um algoritmo com a ordem mais baixa de complexidade computacional.**
   Justificativa: reduzir a ordem (por exemplo, de $O(n^2)$ para $O(n \log n)$) tem impacto muito maior e escalável do que gastar esforço para poupar alguns segundos em casos concretos.

---

5. A função Fibonacci recursiva faz aproximadamente:
   Resposta: **b. $2^n$ chamadas recursivas para $n$ grande.**
   Justificativa: a versão recursiva simples (sem memoização) gera crescimento exponencial no número de chamadas, aproximadamente $\Theta(2^n)$.

---

6. Dois algoritmos A e B possuem complexidade $n^5$ e $2^n$, respectivamente. Quando você usaria B em vez de A? Explique.
   Resposta / Justificativa curta e prática:

* $n^5$ (polinomial) cresce muito mais devagar que $2^n$ (exponencial) para valores grandes de $n$. Portanto para grandes blocos de dados é quase sempre preferível o algoritmo $A$ (polinomial).
* Você usaria o algoritmo $B$ (exponencial) somente se o tamanho de entrada $n$ for pequeno o bastante que $2^n$ seja menor que $n^5$ na prática — e/ou se $B$ tiver constantes muito menores ou outros benefícios práticos (memória, simplicidade, precisão).Por Exemplo, calculei os termos e $2^n < n^5$ ocorre apenas para $n \le 22$. Para $n \ge 23$ já vale $2^n > n^5$. Então, se seus problemas têm $n \le 22$ (ou outro limite pequeno dependendo de constantes), B pode ser aceitável/mais rápido; para $n$ maiores, escolha A.Na prática, sempre verifique constantes e perfil real (implementação, hardware).
---

7. Simplificação de $O(3m^3 + 2mn^2 + n^2 + 10m + m^2)$:
   Resposta: **a. $O(m^3 + mn^2)$.**
   Justificativa: termos dominantes são $m^3$ e $mn^2$. Termos menores ($n^2, m^2, 10m$) ficam absorvidos. Em notação de duas variáveis devemos manter os dois termos dominantes, logo $O(m^3 + mn^2)$.

---


