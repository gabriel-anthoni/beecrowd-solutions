<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1005">
    <img src="https://skillicons.dev/icons?i=c" width="45" alt="C Logo" />
  </a>

  <h3>beecrowd 1005 — Média 1</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-C99-A8B9CC?style=flat-square&logo=c&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-2-blue?style=flat-square"/>
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
      A entrada contém dois valores de ponto flutuante de dupla precisão (<code>double</code>).<br><br>
      <b>🧠 Lógica:</b><br>
      • Ler dois valores de ponto flutuante (<code>double</code>) com <code>scanf()</code> nas variáveis <code>a</code> e <code>b</code>.<br>
      • Calcular a média ponderada com pesos 3.5 e 7.5 (soma dos pesos = 11):<br>
      <code>MEDIA = ((a * 3.5) + (b * 7.5)) / 11.0</code><br>
      • Exibir o resultado formatado no padrão <code>MEDIA = X.XXXXX</code> com 5 casas decimais e quebra de linha <code>\n</code> utilizando <code>printf()</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a mensagem <code>MEDIA = </code> seguida do valor da variável <code>MEDIA</code> com 5 casas após o ponto decimal e de uma quebra de linha.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains two double-precision floating-point values (<code>double</code>).<br><br>
      <b>🧠 Logic:</b><br>
      • Read two double-precision floating-point numbers (<code>double</code>) using <code>scanf()</code> into variables <code>a</code> and <code>b</code>.<br>
      • Calculate the weighted average with weights 3.5 and 7.5 (total weight = 11):<br>
      <code>MEDIA = ((a * 3.5) + (b * 7.5)) / 11.0</code><br>
      • Output the result formatted as <code>MEDIA = X.XXXXX</code> with 5 decimal places and a newline <code>\n</code> using <code>printf()</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the message <code>MEDIA = </code> followed by the calculated average formatted to 5 decimal places and a newline character.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
5.0
7.1
```

### 📤 Exemplo de Saída / Example Output

```txt
MEDIA = 6.43182
```