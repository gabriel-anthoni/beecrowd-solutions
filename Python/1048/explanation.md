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
      <p align="center"><i>beecrowd | 1048</i></p>
      <h3 align="center">Aumento de Salário</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém apenas um valor de ponto flutuante, com duas casas decimais, que representa o salário atual do funcionário.

*Exemplo de entrada:*
```
400.00
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O objetivo é calcular o reajuste salarial baseado em faixas de renda predefinidas.
- Utilizamos uma estrutura condicional encadeada (`if-elif-else`) para identificar em qual faixa o salário atual se encaixa e determinar o percentual de aumento correspondente:
  - Até 400.00 $\implies$ **15%**
  - De 400.01 até 800.00 $\implies$ **12%**
  - De 800.01 até 1200.00 $\implies$ **10%**
  - De 1200.01 até 2000.00 $\implies$ **7%**
  - Acima de 2000.00 $\implies$ **4%**
- Com o percentual definido, calculamos o valor do reajuste em dinheiro e o somamos ao salário antigo para obter o novo salário.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima três linhas contendo o novo salário, o valor do reajuste ganho (ambos formatados com duas casas decimais) e o percentual de aumento utilizado.

*Exemplo de saída:*
```
Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %
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
      <p align="center"><i>beecrowd | 1042</i></p>
      <h3 align="center">Salary Increase</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains a single floating-point number with two decimal places, representing the employee's current salary.

*Example Input:*
```
800.01
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The goal is to calculate a salary adjustment based on predefined income brackets.
- We use a cascading conditional block (`if-elif-else`) to evaluate which range the current salary falls into and assign the appropriate percentage rate:
  - Up to 400.00 $\implies$ **15%**
  - From 400.01 to 800.00 $\implies$ **12%**
  - From 800.01 to 1200.00 $\implies$ **10%**
  - From 1200.01 to 2000.00 $\implies$ **7%**
  - Above 2000.00 $\implies$ **4%**
- Once the rate is identified, we compute the exact monetary value of the raise and add it to the original salary to get the new total.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print three lines displaying the new salary, the earned money increase (both formatted to two decimal places), and the percentage rate applied.

*Example Output:*
```
Novo salario: 880.01
Reajuste ganho: 80.00
Em percentual: 10 %
```