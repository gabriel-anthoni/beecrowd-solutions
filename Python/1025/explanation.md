### <img src="https://static.wikia.nocookie.net/duolingo/images/1/17/Brazil_bandera.png/revision/latest?cb=20230710181600&path-prefix=es" width="20"> PT-BR

<!----------------------------------------------------------------------------------------->

<table>
  <tr>
    <th width="300">Linguagem</th>
    <th width="1000">Questão</th>
  </tr>
  <tr>
    <td>
      <p align="center"><img src="https://skillicons.dev/icons?i=python"></p>
      <p align="center"><code>Python 3.11</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1025</i></p>
      <h3 align="center">Onde estão os Mármores?</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém vários casos de teste. Cada caso começa com dois inteiros: N correspondente ao número de mármores e Q correspondente ao número de consultas.
- As próximas N linhas contêm os números escritos em cada um dos mármores.
- As próximas Q linhas contêm as consultas (números a serem procurados nos mármores).
- A entrada termina quando N = 0 e Q = 0.

*Exemplo de entrada:*
```
4 1
2
3
5
1
5
5 2
1
3
3
3
1
2
3
0 0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Como o número de mármores e consultas pode ser grande, o algoritmo exige eficiência. A ordenação combinada com a Busca Binária garante excelente desempenho.
- Leia N e Q. Para cada caso de teste, armazene os N números de mármores em uma lista.
- Ordene a lista de mármores em ordem crescente. A ordenação é necessária porque a busca binária exige um conjunto de dados ordenado.
- Para cada uma das Q consultas, busque a primeira ocorrência do elemento utilizando a busca binária:
  - O método `bisect_left` da biblioteca `bisect` do Python localiza o ponto de inserção para manter a lista ordenada. Se o elemento já existir, retorna o índice da **primeira** ocorrência (perfeito para tratar duplicatas).
- Verifique se o índice retornado está dentro dos limites da lista e se o valor no índice coincide com o número procurado.
  - Se coincidir, o elemento foi encontrado. Imprima o índice somando 1 (já que o problema exige indexação começando em 1).
  - Caso contrário, o elemento não está no conjunto.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Para cada caso de teste, imprima o cabeçalho `CASE# X:` (onde X é o número do caso de teste, começando em 1).
- Para cada consulta, imprima se o número foi encontrado e em qual posição, ou se não foi encontrado, seguindo os padrões do exemplo.

*Exemplo de saída:*
```
CASE# 1:
5 found at 4
CASE# 2:
2 not found
3 found at 3
```

---

<!----------------------------------------------------------------------------------------->

### <img src="https://static.wikia.nocookie.net/duolingo/images/7/79/Ingles.png/revision/latest?cb=20230710181050&path-prefix=es" width="20"> EN

<!----------------------------------------------------------------------------------------->

<table>
  <tr>
    <th width="300">Language</th>
    <th width="1000">Problem</th>
  </tr>
  <tr>
    <td>
      <p align="center"><img src="https://skillicons.dev/icons?i=python"></p>
      <p align="center"><code>Python 3.11</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1025</i></p>
      <h3 align="center">Where are the Marbles?</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains several test cases. Each case starts with two integers: N indicating the number of marbles and Q indicating the number of queries.
- The next N lines contain the numbers written on each of the marbles.
- The next Q lines contain the queries (numbers to search for among the marbles).
- The input ends when N = 0 and Q = 0.

*Example Input:*
```
4 1
2
3
5
1
5
5 2
1
3
3
3
1
2
3
0 0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Because the number of marbles and queries can be quite large, efficiency is required. Sorting combined with Binary Search provides optimal performance.
- Read N and Q. For each test case, collect the N marble values in a list.
- Sort the list of marbles in ascending order. Sorting is necessary since binary search relies on an ordered dataset.
- For each of the Q queries, search for the first occurrence of the element using Binary Search:
  - Python's built-in library `bisect` provides `bisect_left`, which finds the insertion point to maintain order. If the item exists, it naturally returns the index of its **first** occurrence (ideal for handling duplicates).
- Verify if the returned index is within bounds and matches the queried value:
  - If it matches, the element exists. Print the 1-based index (`pos + 1`).
  - Otherwise, print that the element is not found.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- For each testcase, print the header `CASE# X:` (where X is the sequential case number, starting at 1).
- For each query, print whether the number was found and at which 1-based position, or if it was not found, matching the target format.

*Example Output:*
```
CASE# 1:
5 found at 4
CASE# 2:
2 not found
3 found at 3
```