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
      <p align="center"><i>beecrowd | 1040</i></p>
      <h3 align="center">Média 3</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém quatro números de ponto flutuante representando as notas dos alunos.
- Se o aluno ficar em recuperação (em exame), haverá uma quinta nota flutuante em uma linha posterior representativa da nota do exame.

*Exemplo de entrada:*
```
2.0 4.0 7.5 8.0
6.4
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O objetivo é calcular a média ponderada de quatro notas com os pesos 2, 3, 4 e 1, respectivamente:
  $$\text{Média} = \frac{(N_1 \times 2) + (N_2 \times 3) + (N_3 \times 4) + (N_4 \times 1)}{10}$$
- A partir dessa média calculada, aplicamos as seguintes regras de negócio:
  1. **Média >= 7.0**: O aluno é aprovado diretamente.
  2. **Média < 5.0**: O aluno é reprovado diretamente.
  3. **Média entre 5.0 e 6.9**: O aluno fica em exame. Deve-se ler uma nova nota e recalcular a média final:
     $$\text{Média Final} = \frac{\text{Média} + \text{Nota do Exame}}{2}$$
     - Se a média final for **>= 5.0**, o aluno é aprovado no exame.
     - Se a média final for **< 5.0**, o aluno é reprovado.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima todas as mensagens de status acadêmico e as notas formatadas exatamente com uma casa decimal.

*Exemplo de saída:*
```
Media: 5.4
Aluno em exame.
Nota do exame: 6.4
Aluno aprovado.
Media final: 5.9
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
      <p align="center"><i>beecrowd | 1040</i></p>
      <h3 align="center">Average 3</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input contains four floating-point numbers representing the student's grades.
- If the student goes to the exam, there will be a fifth float number in a subsequent line representing the exam score.

*Example Input:*
```
2.0 6.5 4.0 9.0
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- The goal is to calculate the weighted average of four grades using weights 2, 3, 4, and 1, respectively:
  $$\text{Average} = \frac{(N_1 \times 2) + (N_2 \times 3) + (N_3 \times 4) + (N_4 \times 1)}{10}$$
- Based on the calculated average, we apply these decision boundaries:
  1. **Average >= 7.0**: Student is approved.
  2. **Average < 5.0**: Student is reproved.
  3. **Average between 5.0 and 6.9**: Student must take a recovery exam. We must read a new score and calculate the final average:
     $$\text{Final Average} = \frac{\text{Average} + \text{Exam Score}}{2}$$
     - If the final average is **>= 5.0**, the student is approved.
     - If the final average is **< 5.0**, the student is reproved.

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print all the corresponding academic status messages and averages formatted to exactly one decimal place.

*Example Output:*
```
Media: 4.8
Aluno reprovado.
```