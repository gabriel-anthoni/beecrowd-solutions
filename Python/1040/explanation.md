<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1040">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1040 — Média 3</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-5-green?style=flat-square" />
  </p>

</div>

---

### 📌 Resumo / Overview

<table align="center" width="100%">
  <tr>
    <th width="50%">🇧🇷 Português (PT-BR)</th>
    <th width="50%">🇺🇸 English (EN)</th>
  </tr>
  <tr>
    <td valign="top">
      <b>📥 Entrada:</b><br>
      A entrada contém quatro números de ponto flutuante representando as notas do aluno. Se o aluno ficar em exame, haverá uma quinta nota em uma linha posterior.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia as quatro notas na mesma linha usando <code>input().split()</code>.<br>
      • Calcule a média ponderada com pesos 2, 3, 4 e 1:<br>
      &nbsp;&nbsp;<code>Média = (N1 · 2 + N2 · 3 + N3 · 4 + N4 · 1) / 10</code><br>
      • Avalie o status acadêmico com base no valor da média:<br>
      &nbsp;&nbsp;- <code>Média ≥ 7.0</code>: <code>Aluno aprovado.</code><br>
      &nbsp;&nbsp;- <code>Média < 5.0</code>: <code>Aluno reprovado.</code><br>
      &nbsp;&nbsp;- <code>5.0 ≤ Média ≤ 6.9</code>: <code>Aluno em exame.</code><br>
      • Em caso de exame, leia a nota do exame e recalcule:<br>
      &nbsp;&nbsp;<code>Média Final = (Média + NotaExame) / 2</code><br>
      &nbsp;&nbsp;- Se <code>Média Final ≥ 5.0</code>, exiba <code>Aluno aprovado.</code>; caso contrário, <code>Aluno reprovado.</code><br>
      • Exiba todas as médias e notas com exatamente 1 casa decimal.<br><br>
      <b>📤 Saída:</b><br>
      Imprima as mensagens de status e valores das médias formatados com 1 casa decimal conforme as regras do problema.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains four floating-point numbers representing student grades. If the student goes to the exam, a fifth float value will be provided on a subsequent line.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the four grades on a single line using <code>input().split()</code>.<br>
      • Calculate the weighted average using weights 2, 3, 4, and 1:<br>
      &nbsp;&nbsp;<code>Average = (N1 · 2 + N2 · 3 + N3 · 4 + N4 · 1) / 10</code><br>
      • Determine the student status based on the average:<br>
      &nbsp;&nbsp;- <code>Average ≥ 7.0</code>: <code>Aluno aprovado.</code><br>
      &nbsp;&nbsp;- <code>Average < 5.0</code>: <code>Aluno reprovado.</code><br>
      &nbsp;&nbsp;- <code>5.0 ≤ Average ≤ 6.9</code>: <code>Aluno em exame.</code><br>
      • If in exam, read the exam score and recalculate:<br>
      &nbsp;&nbsp;<code>Final Average = (Average + ExamScore) / 2</code><br>
      &nbsp;&nbsp;- If <code>Final Average ≥ 5.0</code>, display <code>Aluno aprovado.</code>; otherwise, <code>Aluno reprovado.</code><br>
      • Format all output grades and averages to exactly 1 decimal place.<br><br>
      <b>📤 Output:</b><br>
      Print the academic status messages and formatted average values with 1 decimal place.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
2.0 4.0 7.5 8.0
6.4
```

### 📤 Exemplo de Saída / Example Output

```txt
Media: 5.4
Aluno em exame.
Nota do exame: 6.4
Aluno aprovado.
Media final: 5.9
```