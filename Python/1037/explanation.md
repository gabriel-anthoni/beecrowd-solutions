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
      <p align="center"><i>beecrowd | 1037</i></p>
      <h3 align="center">Intervalo</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém um único número de ponto flutuante.

*Exemplo de entrada:*
```
25.01
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O problema pede para identificar a qual intervalo matemático um determinado número pertence. Os intervalos possíveis são:
  - $[0,25]$: valores de 0 a 25 (inclusive ambos).
  - $(25,50]$: valores maiores que 25 e menores ou iguais a 50.
  - $(50,75]$: valores maiores que 50 e menores ou iguais a 75.
  - $(75,100]$: valores maiores que 75 e menores ou iguais a 100.
- Lembre-se da notação matemática: colchetes `[` ou `]` representam limites fechados (inclusivos), enquanto parênteses `(` representam limites abertos (exclusivos).
- Se o número digitado for menor que 0 ou maior que 100, ele não pertence a nenhum grupo.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima o intervalo correspondente ao número fornecido. Se o valor estiver fora de todos os intervalos descritos, exiba a mensagem `Fora de intervalo`.

*Exemplo de saída:*
```
Intervalo (25,50]
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
      <p align="center"><i>beecrowd | 1037</i></p>
      <h3 align="center">Interval</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains a single floating-point number.

*Example Input:*
```
25.00
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The goal is to determine which mathematical interval a given number belongs to. The intervals are defined as:
  - $[0,25]$: values from 0 to 25 (inclusive).
  - $(25,50]$: values greater than 25 up to 50 (inclusive).
  - $(50,75]$: values greater than 50 up to 75 (inclusive).
  - $(75,100]$: values greater than 75 up to 100 (inclusive).
- Note the mathematical notation: brackets `[` or `]` denote closed (inclusive) boundaries, whereas parentheses `(` denote open (exclusive) boundaries.
- If the number is less than 0 or greater than 100, it does not belong to any interval.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the matching interval label. If the value does not fall into any of the specified boundaries, display the message `Fora de intervalo`.

*Example Output:*
```
Intervalo [0,25]
```