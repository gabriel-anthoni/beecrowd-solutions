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
      <p align="center"><i>beecrowd | 1035</i></p>
      <h3 align="center">Teste de Seleção 1</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém quatro valores inteiros: $A$, $B$, $C$ e $D$.

*Exemplo de entrada:*
```
5 6 7 8
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O problema pede para validar uma série de condições matemáticas simultâneas sobre quatro variáveis inteiras ($A$, $B$, $C$, $D$):
  1. $B > C$ (B maior que C)
  2. $D > A$ (D maior que A)
  3. $(C + D) > (A + B)$ (a soma de C e D deve ser maior que a soma de A e B)
  4. $C > 0$ e $D > 0$ (ambos C e D devem ser valores positivos)
  5. $A \pmod 2 = 0$ (A deve ser um número par)
- No Python, conectamos todas essas expressões lógicas utilizando o operador lógico `and`. Se qualquer uma das condições falhar, o fluxo cai no bloco `else`.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima `Valores aceitos` se todas as condições forem verdadeiras.
- Caso contrário, imprima `Valores nao aceitos`.

*Exemplo de saída:*
```
Valores nao aceitos
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
      <p align="center"><i>beecrowd | 1035</i></p>
      <h3 align="center">Selection Test 1</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains four integer values: $A$, $B$, $C$, and $D$.

*Example Input:*
```
2 3 2 6
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The problem asks us to validate a series of simultaneous mathematical conditions on four integer variables ($A$, $B$, $C$, $D$):
  1. $B > C$ (B is greater than C)
  2. $D > A$ (D is greater than A)
  3. $(C + D) > (A + B)$ (the sum of C and D is greater than the sum of A and B)
  4. $C > 0$ and $D > 0$ (both C and D must be positive values)
  5. $A \pmod 2 = 0$ (A must be an even number)
- In Python, we connect all these logical expressions using the `and` logical operator. If any condition fails, the code falls into the `else` block.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print `Valores aceitos` (Accepted values) if all conditions are met.
- Otherwise, print `Valores nao aceitos` (Values not accepted).

*Example Output:*
```
Valores aceitos
```