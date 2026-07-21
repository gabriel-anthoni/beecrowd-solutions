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
      <p align="center"><i>beecrowd | 1028</i></p>
      <h3 align="center">Figurinhas</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A primeira linha da entrada contém um único inteiro N (1 <= N <= 3000) indicando o número de casos de teste.
- Cada caso de teste contém dois inteiros F1 e F2 (1 <= F1, F2 <= 1000) indicando, respectivamente, a quantidade de figurinhas que Ricardo e Vicente têm para trocar.

*Exemplo de entrada:*
```
3
8 12
9 27
259 111
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O problema pede para encontrar o tamanho máximo de um pacote de figurinhas que permita dividir as coleções de ambos os amigos em partes iguais, sem sobras.
- Isso equivale matematicamente a encontrar o **Máximo Divisor Comum (MDC)** entre a quantidade de figurinhas de Ricardo (F1) e Vicente (F2).
- Em Python, a forma mais eficiente e rápida de calcular o MDC é utilizando a função nativa `math.gcd()`, que roda em tempo logarítmico através do algoritmo de Euclides implementado diretamente em C.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Para cada caso de teste, imprima um único número inteiro correspondente ao tamanho máximo da pilha de figurinhas que ambos podem trocar.

*Exemplo de saída:*
```
4
9
37
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
      <p align="center"><i>beecrowd | 1028</i></p>
      <h3 align="center">Collectable Cards</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The first line contains an integer N (1 <= N <= 3000) indicating the number of test cases.
- Each testcase contains two integers F1 and F2 (1 <= F1, F2 <= 1000) indicating the number of cards Ricardo and Vicente have to trade, respectively.

*Example Input:*
```
3
8 12
9 27
259 111
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The problem asks for the maximum size of a package of cards that allows dividing both collections into equal-sized stacks with no cards left over.
- This is mathematically equivalent to finding the **Greatest Common Divisor (GCD)** of the two card counts.
- In Python, the most efficient way to compute this is by using the built-in function `math.gcd()`, which runs in logarithmic time utilizing the Euclidean algorithm implemented in C.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- For each testcase, print a single integer indicating the maximum size of the card stack they can trade.

*Example Output:*
```
4
9
37
```