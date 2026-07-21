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
      <p align="center"><i>beecrowd | 1047</i></p>
      <h3 align="center">Tempo de Jogo com Minutos</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém quatro valores inteiros na mesma linha: a hora inicial, o minuto inicial, a hora final e o minuto final de um jogo.

*Exemplo de entrada:*
```
7 8 9 10
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Calcular a duração exata envolvendo horas e minutos pode gerar muitas árvores de decisão condicionais (`if/else`) para tratar os empréstimos de minutos e viradas de dia.
- A estratégia matemática mais limpa e elegante é **transformar todo o tempo em minutos** desde o início do dia:
  $$\text{Tempo Inicial (minutos)} = (\text{Hora Inicial} \times 60) + \text{Minuto Inicial}$$
  $$\text{Tempo Final (minutos)} = (\text{Hora Final} \times 60) + \text{Minuto Final}$$
- A duração total inicial será a diferença:
  $$\Delta t = \text{Tempo Final} - \text{Tempo Inicial}$$
- Como o jogo dura no mínimo $1$ minuto e no máximo $24$ horas ($1440$ minutos), se o resultado de $\Delta t$ for menor ou igual a zero, significa que o jogo terminou no dia seguinte. Portanto, basta somar $1440$ minutos ao total.
- Por fim, convertemos de volta para horas e minutos usando divisão inteira (`//`) e o operador de resto (`%`):
  $$\text{Horas} = \Delta t // 60$$
  $$\text{Minutos} = \Delta t \pmod{60}$$

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima a mensagem de duração no formato exato: `"O JOGO DUROU X HORA(S) E Y MINUTO(S)"`.

*Exemplo de saída:*
```
O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)
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
      <p align="center"><i>beecrowd | 1047</i></p>
      <h3 align="center">Game Time with Minutes</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains four integer values on a single line: starting hour, starting minute, ending hour, and ending minute of a game.

*Example Input:*
```
7 10 8 9
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Calculating precise durations involving hours and minutes concurrently often leads to complex nested conditional structures to handle minute borrowing and overnight transitions.
- The cleanest mathematical approach is to **convert all time inputs entirely into minutes** past midnight:
  $$\text{Start Time (minutes)} = (\text{Start Hour} \times 60) + \text{Start Minute}$$
  $$\text{End Time (minutes)} = (\text{End Hour} \times 60) + \text{End Minute}$$
- The preliminary duration is simply the difference:
  $$\Delta t = \text{End Time} - \text{Start Time}$$
- Given that the game must last at least $1$ minute and at most $24$ hours ($1440$ minutes), if $\Delta t$ is less than or equal to zero, it means the game wrapped up on the following day. We handle this effortlessly by adding $1440$ minutes to our duration.
- Finally, we extract the hours and minutes back from the total runtime using integer division (`//`) and the modulo operator (`%`):
  $$\text{Hours} = \Delta t // 60$$
  $$\text{Minutes} = \Delta t \pmod{60}$$

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the game duration matching the strict template: `"O JOGO DUROU X HORA(S) E Y MINUTO(S)"`.

*Example Output:*
```
O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)
```