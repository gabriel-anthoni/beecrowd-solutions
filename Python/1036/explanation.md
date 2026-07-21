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
      <p align="center"><i>beecrowd | 1036</i></p>
      <h3 align="center">Fórmula de Bhaskara</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém três valores de ponto flutuante ($A$, $B$ e $C$).

*Exemplo de entrada:*
```
10.0 20.1 5.1
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O objetivo é calcular as raízes de uma equação de segundo grau utilizando a fórmula de Bhaskara:
  $$x = \frac{-b \pm \sqrt{\Delta}}{2a}$$
- O primeiro passo é calcular o discriminante Delta ($\Delta$):
  $$\Delta = b^2 - 4ac$$
- Em seguida, validamos as condições que impossibilitam o cálculo das raízes reais:
  1. Se $A = 0$, teremos uma divisão por zero (indefinição matemática).
  2. Se $\Delta < 0$, não existem raízes reais (apenas raízes complexas/imaginárias).
- Se qualquer uma dessas duas condições for verdadeira, imprimimos a mensagem de erro. Caso contrário, calculamos as duas raízes ($R1$ e $R2$) utilizando a raiz quadrada de Delta ($\Delta^{0.5}$).

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Se não for possível calcular, imprima a mensagem `Impossivel calcular`.
- Caso contrário, imprima o resultado com 5 casas decimais formatadas como `R1 = X.XXXXX` e `R2 = X.XXXXX`.

*Exemplo de saída:*
```
R1 = -0.29610
R2 = -1.71390
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
      <p align="center"><i>beecrowd | 1036</i></p>
      <h3 align="center">Bhaskara's Formula</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains three floating-point values ($A$, $B$, and $C$).

*Example Input:*
```
0.0 20.0 5.0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The goal is to compute the roots of a quadratic equation using Bhaskara's formula:
  $$x = \frac{-b \pm \sqrt{\Delta}}{2a}$$
- The first step is to calculate the discriminant Delta ($\Delta$):
  $$\Delta = b^2 - 4ac$$
- Next, we validate the conditions that make it impossible to calculate real roots:
  1. If $A = 0$, we would have a division by zero (mathematically undefined).
  2. If $\Delta < 0$, there are no real roots (only complex/imaginary roots).
- If either condition is true, we print the error message. Otherwise, we calculate both roots ($R1$ and $R2$) using the square root of Delta ($\Delta^{0.5}$).

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- If the calculation is impossible, print `Impossivel calcular`.
- Otherwise, print the roots formatted with 5 decimal places as `R1 = X.XXXXX` and `R2 = X.XXXXX`.

*Example Output:*
```
Impossivel calcular
```