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
      <p align="center"><i>beecrowd | 1044</i></p>
      <h3 align="center">Múltiplos</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém dois valores inteiros $A$ e $B$ na mesma linha.

*Exemplo de entrada:*
```
6 24
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Dois números são múltiplos entre si se o maior deles for divisível pelo menor sem deixar resto (resto igual a zero).
- Matematicamente, dizemos que $A$ e $B$ são múltiplos se:
  $$A \pmod B = 0 \quad \text{ou} \quad B \pmod A = 0$$
- Em termos de código, podemos simplesmente verificar se o resto da divisão do maior pelo menor é $0$, ou testar diretamente se $A$ é divisível por $B$ ou vice-versa.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Deve-se imprimir a mensagem `"Sao Multiplos"` ou `"Nao sao Multiplos"` (atente-se para a falta de acentos nas mensagens, conforme exigido pelo Beecrowd).

*Exemplo de saída:*
```
Sao Multiplos
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
      <p align="center"><i>beecrowd | 1044</i></p>
      <h3 align="center">Multiples</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains two integer values, $A$ and $B$, on a single line.

*Example Input:*
```
6 25
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Two numbers are multiples of each other if the larger number is perfectly divisible by the smaller one with a remainder of zero.
- Mathematically, we say $A$ and $B$ are multiples if:
  $$A \pmod B = 0 \quad \text{or} \quad B \pmod A = 0$$
- Code-wise, we can either check if the remainder of dividing the maximum value by the minimum value is $0$, or check if either $A \% B == 0$ or $B \% A == 0$.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the message `"Sao Multiplos"` or `"Nao sao Multiplos"`. Note that the output strings on Beecrowd do not contain Portuguese accentuation marks.

*Example Output:*
```
Nao sao Multiplos
```