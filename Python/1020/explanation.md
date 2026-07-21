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
      <p align="center"><i>beecrowd | 1020</i></p>
      <h3 align="center">Idade em Dias</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém um valor inteiro correspondente à idade de uma pessoa em dias.

*Exemplo de entrada:*
```
400
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Leia o valor inteiro de dias usando `int(input())`.
- Obtenha a quantidade de anos dividindo de forma inteira por 365:

$$
Anos = TotalDias // 365
$$

- Obtenha a quantidade de meses dividindo o resto da divisão dos anos por 30:

$$
Meses = (TotalDias \\% 365) // 30
$$

- Obtenha a quantidade de dias restantes aplicando o resto da divisão por 30 no saldo de dias restante:

$$
Dias = (TotalDias \\% 365) \\% 30
$$

- utilize f-string para formatar a saída com quebras de linha para cada unidade temporal.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima a saída formatada contendo a quantidade de anos, meses e dias, conforme o exemplo fornecido.

*Exemplo de saída:*
```
1 ano(s)
1 mes(es)
5 dia(s)
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
      <p align="center"><i>beecrowd | 1020</i></p>
      <h3 align="center">Age in Days</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input file contains one integer value.

*Example Input:*
```
400
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read the total days as an integer using `int(input())`.
- Obtain the number of years by dividing the total days by 365 (integer division `//`):

$$
Years = TotalDays // 365
$$

- Obtain the number of months by taking the remainder of days after subtracting years, and dividing it by 30:

$$
Months = (TotalDays \\% 365) // 30
$$

- Obtain the remaining days by applying the modulo operator `%` by 30 on the remaining days:

$$
Days = (TotalDays \\% 365) \\% 30
$$

- Use f-string to format the output with line breaks for each time unit.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the output formatted with the number of years, months, and days, as shown in the example.

*Example Output:*
```
1 ano(s)
1 mes(es)
5 dia(s)
``` 