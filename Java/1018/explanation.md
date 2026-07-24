### <img src="https://static.wikia.nocookie.net/duolingo/images/1/17/Brazil_bandera.png/revision/latest?cb=20230710181600&path-prefix=es" width="20"> PT-BR

<!----------------------------------------------------------------------------------------->

<table>
  <tr>
    <th width="300">Linguagem</th>
    <th width="1000">Questão</th>
  </tr>
  <tr>
    <td>
      <p align="center"><img src="https://skillicons.dev/icons?i=java"></p>
      <p align="center"><code>Java 19</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1018</i></p>
      <h3 align="center">Cédulas</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém um valor inteiro $N$ ($0 < N < 1000000$).

*Exemplo de entrada:*
```
576
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Defina uma lista/vetor com os valores das cédulas possíveis: `[100, 50, 20, 10, 5, 2, 1]`.
- Imprima o valor lido originalmente (requisito do problema).
- Itere sobre a lista de cédulas. Para cada cédula:
  - Calcule a quantidade de notas necessárias utilizando a divisão `/`.
  - Exiba o resultado formatado com `%d`.
  - Atualize o valor restante a ser computado utilizando o operador de resto `%`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias no formato `X nota(s) de R$ Y,00`.

*Exemplo de saída:*
```
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
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
      <p align="center"><img src="https://skillicons.dev/icons?i=java"></p>
      <p align="center"><code>Java 19</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1018</i></p>
      <h3 align="center">Banknotes</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input file contains an integer value $N$ ($0 < N < 1000000$).

*Example Input:*
```
576
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Define an array with the possible banknote values: `[100, 50, 20, 10, 5, 2, 1]`.
- Print the original read value (problem requirement).
- Iterate over the banknote array. For each banknote:
  - Calculate the required quantity of notes using integer division `/`.
  - Output the formatted string using `%d`.
  - Update the remaining amount to be computed using the modulo operator `%`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the read number and the minimum number of each necessary banknote in the format `X nota(s) de R$ Y,00`.

*Example Output:*
```
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
```