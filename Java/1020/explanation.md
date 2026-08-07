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

- Leia o valor inteiro correspondente aos dias usando a classe `Scanner`.
- Calcule a quantidade de anos dividindo o total de dias por 365 (divisão inteira `/`):

$$
Anos = TotalDias / 365
$$

- Calcule a quantidade de meses obtendo o resto da divisão do total de dias por 365 e dividindo de forma inteira por 30:

$$
Meses = (TotalDias \% 365) / 30
$$

- Calcule a quantidade de dias restantes obtendo o resto da divisão por 365 e em seguida por 30 (operador `%`):

$$
Dias = (TotalDias \% 365) \% 30
$$

- Utilize `System.out.printf` para formatar a saída exibindo anos, meses e dias em linhas separadas, garantindo a quebra de linha `\n` ao final.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima a saída conforme o modelo especificado com a quantidade de anos, meses e dias.

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
      <p align="center"><img src="https://skillicons.dev/icons?i=java"></p>
      <p align="center"><code>Java 19</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1020</i></p>
      <h3 align="center">Age in Days</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains an integer value representing a person's age in days.

*Example Input:*
```
400
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read the total age in days as an integer using `Scanner`.
- Calculate the number of years by dividing the total days by 365 (integer division `/`):

$$
Years = TotalDays / 365
$$

- Calculate the number of months by taking the remainder of total days divided by 365 and dividing it by 30:

$$
Months = (TotalDays \% 365) / 30
$$

- Calculate the remaining days using the modulo operator `%` by 365 and then by 30:

$$
Days = (TotalDays \% 365) \% 30
$$

- Use `System.out.printf` to format the output displaying years, months, and days on separate lines including a newline `\n` at the end.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the output according to the specified pattern with the total years, months, and days.

*Example Output:*
```
1 ano(s)
1 mes(es)
5 dia(s)
```