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
      <p align="center"><i>beecrowd | 1013</i></p>
      <h3 align="center">O Maior</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém três valores inteiros: $A$, $B$ e $C$.

*Exemplo de entrada:*
```
7 14 106
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- Ler três números inteiros $A$, $B$ e $C$.
- Calcular o maior número entre eles. O enunciado sugere a seguinte fórmula para o maior entre dois números $A$ e $B$:
  $$\text{MaiorAB} = \frac{A + B + |A - B|}{2}$$
- Em Java, a função `Math.abs()` calcula o valor absoluto ($|A - B|$). 
- Alternativamente, também é possível utilizar `Math.max(A, B)` ou condicionais `if/else`.
- Após encontrar o maior entre $A$ e $B$, compara-se esse resultado com o valor $C$.
- Exibir o maior valor encontrado seguido da mensagem `" eh o maior"`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima o maior dos três valores seguido por um espaço e a mensagem `eh o maior` com quebra de linha `\n`.

*Exemplo de saída:*
```
106 eh o maior
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
      <p align="center"><i>beecrowd | 1013</i></p>
      <h3 align="center">The Greatest</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains three integer values: $A$, $B$, and $C$.

*Example Input:*
```
7 14 106
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Read three integer values $A$, $B$, and $C$.
- Find the greatest value among them. The problem description suggests using the following formula to calculate the maximum between two values $A$ and $B$:
  $$\text{MaiorAB} = \frac{A + B + |A - B|}{2}$$
- In Java, `Math.abs()` computes the absolute difference ($|A - B|$).
- Alternatively, `Math.max(A, B)` or `if/else` checks can be used.
- After finding the maximum between $A$ and $B$, compare it with $C$.
- Output the greatest number followed by the string `" eh o maior"`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the maximum value followed by a space and the string `eh o maior` with a newline `\n`.

*Example Output:*
```
106 eh o maior
```