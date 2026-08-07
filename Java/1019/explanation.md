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
      <p align="center"><i>beecrowd | 1019</i></p>
      <h3 align="center">Conversão de Tempo</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém um valor inteiro correspondente ao tempo total em segundos.

*Exemplo de entrada:*
```
140211
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Leia o valor inteiro de segundos usando a classe `Scanner`.
- Calcule as horas dividindo o total de segundos por 3600 (divisão inteira `/`):

$$
Horas = TotalSegundos / 3600
$$

- Calcule os minutos dividindo o total de segundos por 60 e obtendo o resto da divisão por 60 (operador `%`):

$$
Minutos = (TotalSegundos / 60) \% 60
$$

- Calcule os segundos restantes obtendo o resto da divisão por 60:

$$
Segundos = TotalSegundos \% 60
$$

- Utilize `System.out.printf` para formatar a saída no padrão `horas:minutos:segundos` garantindo a quebra de linha `\n` ao final.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima o tempo lido convertido para o formato `horas:minutos:segundos`.

*Exemplo de saída:*
```
38:56:51
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
      <p align="center"><i>beecrowd | 1019</i></p>
      <h3 align="center">Time Conversion</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains an integer value representing the total time in seconds.

*Example Input:*
```
140211
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read the total seconds as an integer using `Scanner`.
- Calculate the hours by dividing the total seconds by 3600 (integer division `/`):

$$
Hours = TotalSeconds / 3600
$$

- Calculate the minutes by dividing the total seconds by 60 and then finding the remainder of division by 60 (modulo operator `%`):

$$
Minutes = (TotalSeconds / 60) \% 60
$$

- Calculate the remaining seconds using the modulo operator `%` by 60:

$$
Seconds = TotalSeconds \% 60
$$

- Use `System.out.printf` to format the output in the standard `hours:minutes:seconds` format including a newline `\n` at the end.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the read time converted to the format `hours:minutes:seconds`.

*Example Output:*
```
38:56:51
```