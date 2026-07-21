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
      <p align="center"><i>beecrowd | 1046</i></p>
      <h3 align="center">Tempo de Jogo</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém dois valores inteiros representando a hora de início e a hora de fim de um jogo.

*Exemplo de entrada:*
```
16 2
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O objetivo é calcular a duração de um jogo em horas.
- O jogo pode começar em um dia e terminar no outro, sabendo que a duração mínima é de $1$ hora e a máxima de $24$ horas.
- Temos três cenários:
  1. **Início é menor que o Fim (mesmo dia)**:
     $$\text{Duração} = \text{Fim} - \text{Início}$$
  2. **Início é maior que o Fim (termina no dia seguinte)**:
     $$\text{Duração} = (24 - \text{Início}) + \text{Fim}$$
  3. **Início é igual ao Fim**:
     - Como a duração máxima é de $24$ horas (e não $0$), a duração será exatamente $24$ horas.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima a duração do jogo conforme o padrão `"O JOGO DUROU X HORA(S)"`.

*Exemplo de saída:*
```
O JOGO DUROU 10 HORA(S)
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
      <p align="center"><i>beecrowd | 1046</i></p>
      <h3 align="center">Game Time</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains two integer values representing the start time and end time of a game.

*Example Input:*
```
0 0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The goal is to calculate the total duration of a game in hours.
- The game can start on one day and finish on the next, keeping in mind that the minimum duration is $1$ hour and the maximum is $24$ hours.
- We have three distinct scenarios:
  1. **Start is less than End (same day)**:
     $$\text{Duration} = \text{End} - \text{Start}$$
  2. **Start is greater than End (ends on the next day)**:
     $$\text{Duration} = (24 - \text{Start}) + \text{End}$$
  3. **Start is equal to End**:
     - Since the maximum duration is $24$ hours (not $0$), the duration is exactly $24$ hours.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the calculated duration matching the template `"O JOGO DUROU X HORA(S)"`.

*Example Output:*
```
O JOGO DUROU 24 HORA(S)
```