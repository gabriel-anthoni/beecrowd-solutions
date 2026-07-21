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
      <p align="center"><i>beecrowd | 1018</i></p>
      <h3 align="center">Cédulas</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém um valor inteiro N (0 < N < 1000000).

*Exemplo de entrada:*
```
576
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Leia o valor inteiro usando `int(input())`.
- Defina uma lista com os valores das cédulas possíveis: `[100, 50, 20, 10, 5, 2, 1]`.
- Imprima o valor lido originalmente (requisito do problema).
- Itere sobre a lista de cédulas. Para cada cédula:
  - Calcule a quantidade de notas necessárias utilizando a divisão inteira `//`.
  - Atualize o valor restante a ser computado utilizando o operador de resto `%`.
- utilize f-string para exibir a quantidade de cada nota no formato exigido.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada valor necessárias, conforme o exemplo fornecido.

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
      <p align="center"><img src="https://skillicons.dev/icons?i=python"></p>
      <p align="center"><code>Python 3.11</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1018</i></p>
      <h3 align="center">Banknotes</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input file contains an integer value N (0 < N < 1000000).

*Example Input:*
```
576
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read the integer value using `int(input())`.
- Define a list containing the possible banknote values: `[100, 50, 20, 10, 5, 2, 1]`.
- Print the originally read value (problem requirement).
- Iterate through the list of banknotes. For each banknote:
  - Calculate the quantity of notes needed using integer division `//`.
  - Update the remaining amount to be calculated using the modulo operator `%`.
- Use f-string to display the quantity of each banknote in the required format.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the read number and the minimum quantity of each necessary banknotes, as shown in the example.

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