<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1006">
    <img src="https://skillicons.dev/icons?i=c" width="45" alt="C Logo" />
  </a>

  <h3>beecrowd 1006 — Média 2</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-C99-A8B9CC?style=flat-square&logo=c&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-1-blue?style=flat-square"/>
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
      A entrada contém três valores de ponto flutuante de dupla precisão (<code>double</code>).<br><br>
      <b>🧠 Lógica:</b><br>
      • Ler três valores de ponto flutuante (<code>double</code>) com <code>scanf()</code> nas variáveis <code>a</code>, <code>b</code> e <code>c</code>.<br>
      • Calcular a média ponderada com pesos 2, 3 e 5 (soma dos pesos = 10):<br>
      <code>MEDIA = ((a * 2) + (b * 3) + (c * 5)) / 10.0</code><br>
      • Exibir o resultado formatado no padrão <code>MEDIA = X.X</code> com 1 casa decimal e quebra de linha <code>\n</code> utilizando <code>printf()</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a mensagem <code>MEDIA = </code> seguida do valor da variável <code>MEDIA</code> com 1 casa após o ponto decimal e de uma quebra de linha.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains three double-precision floating-point values (<code>double</code>).<br><br>
      <b>🧠 Logic:</b><br>
      • Read three double-precision floating-point numbers (<code>double</code>) using <code>scanf()</code> into variables <code>a</code>, <code>b</code>, and <code>c</code>.<br>
      • Calculate the weighted average with weights 2, 3, and 5 (total weight = 10):<br>
      <code>MEDIA = ((a * 2) + (b * 3) + (c * 5)) / 10.0</code><br>
      • Output the result formatted as <code>MEDIA = X.X</code> with 1 decimal place and a newline <code>\n</code> using <code>printf()</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the message <code>MEDIA = </code> followed by the calculated average formatted to 1 decimal place and a newline character.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
5.0
6.0
7.0
```

### 📤 Exemplo de Saída / Example Output

```txt
MEDIA = 6.3
```