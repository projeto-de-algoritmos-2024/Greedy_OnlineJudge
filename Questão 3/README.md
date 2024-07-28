### 192. Goodland Electricity
Dificuldade: Difícil

[Link para enunciado completo](https://www.hackerrank.com/challenges/three-month-preparation-kit-pylons/problem)

Enunciado:

## Problema: Usinas de Energia em Goodland

Goodland é um país com várias cidades uniformemente espaçadas ao longo de uma linha. A distância entre cidades adjacentes é de uma unidade. Há uma reunião de planejamento de projeto de infraestrutura de energia, e o governo precisa saber o menor número de usinas de energia necessárias para fornecer eletricidade para toda a lista de cidades. Determine esse número. Se não puder ser feito, retorne `-1`.

### Descrição do Problema

Você recebe uma lista de dados da cidade. Cidades que podem conter uma usina de energia foram rotuladas com `1`. Outras não adequadas para a construção de uma planta são rotuladas `0`. Dada uma faixa de distribuição de `k`, encontre o menor número de usinas que devem ser construídas de modo que todas as cidades sejam atendidas. O intervalo de distribuição limita o fornecimento a cidades onde a distância é menor que `k`.

### Exemplo

```plaintext
k = 3
arr = [0, 1, 1, 1, 0, 0, 0]

Submissões: <br>
![image](Imagem da submissão)
