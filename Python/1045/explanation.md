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
      <p align="center"><i>beecrowd | 1045</i></p>
      <h3 align="center">Tipos de Triângulos</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém três valores de ponto flutuante $A$, $B$ e $C$ na mesma linha ($A, B, C > 0$).

*Exemplo de entrada:*
```
7.0 5.0 2.0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O primeiro passo crucial é ordenar os três valores em ordem decrescente, garantindo que o maior valor fique na variável $A$, o intermediário na variável $B$ e o menor na variável $C$ ($A \ge B \ge C$).
- Em seguida, aplicamos as seguintes regras condicionais:
  1. **Validação de Existência**:
     - Se $A \ge B + C$, o triângulo não existe. Imprime-se `"NAO FORMA TRIANGULO"` e o programa não deve avaliar mais nada.
  2. **Classificação pelos Ângulos** (se passar no teste anterior):
     - Se $A^2 = B^2 + C^2 \implies$ `"TRIANGULO RETANGULO"`
     - Se $A^2 > B^2 + C^2 \implies$ `"TRIANGULO OBTUSANGULO"`
     - Se $A^2 < B^2 + C^2 \implies$ `"TRIANGULO ACUTANGULO"`
  3. **Classificação pelos Lados** (em paralelo à classificação por ângulos):
     - Se $A = B = C \implies$ `"TRIANGULO EQUILATERO"`
     - Se apenas dois lados forem iguais (ex: $A = B \neq C$ ou $B = C \neq A$) $\implies$ `"TRIANGULO ISOSCELES"`

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima todas as classificações que se aplicarem ao triângulo fornecido na entrada.

*Exemplo de saída:*
```
NAO FORMA TRIANGULO
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
      <p align="center"><i>beecrowd | 1045</i></p>
      <h3 align="center">Triangle Types</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains three floating-point values $A$, $B$, and $C$ on a single line ($A, B, C > 0$).

*Example Input:*
```
6.0 6.0 10.0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The first crucial step is to sort the three values in descending order, ensuring that the largest value goes to variable $A$, the middle to variable $B$, and the smallest to variable $C$ ($A \ge B \ge C$).
- Next, we apply the following conditional rules:
  1. **Existence Check**:
     - If $A \ge B + C$, the triangle cannot exist. Print `"NAO FORMA TRIANGULO"` and stop any further evaluations.
  2. **Classification by Angles** (if it is a valid triangle):
     - If $A^2 = B^2 + C^2 \implies$ `"TRIANGULO RETANGULO"` (Right Triangle)
     - If $A^2 > B^2 + C^2 \implies$ `"TRIANGULO OBTUSANGULO"` (Obtuse Triangle)
     - If $A^2 < B^2 + C^2 \implies$ `"TRIANGULO ACUTANGULO"` (Acute Triangle)
  3. **Classification by Sides** (checked concurrently with the angle classification):
     - If $A = B = C \implies$ `"TRIANGULO EQUILATERO"` (Equilateral Triangle)
     - If only two of the sides are equal (e.g., $A = B \neq C$ or $B = C \neq A$) $\implies$ `"TRIANGULO ISOSCELES"` (Isosceles Triangle)

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print all the classification messages that apply to the input triangle.

*Example Output:*
```
TRIANGULO OBTUSANGULO
TRIANGULO ISOSCELES
```