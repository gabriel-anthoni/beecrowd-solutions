<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1038">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1038 — Lanche</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-1-green?style=flat-square" />
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
      A entrada contém dois valores inteiros: o código do item (de 1 a 5) e a quantidade deste item.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o código do item e a quantidade na mesma linha usando <code>input().split()</code>.<br>
      • Mapeie os preços em uma lista ordenada: <code>precos = [4.00, 4.50, 5.00, 2.00, 1.50]</code>.<br>
      • Acesse o preço correspondente utilizando o índice ajustado <code>codigo - 1</code>.<br>
      • Calcule o total multiplicando o preço pela quantidade: <code>Total = Preco · Quantidade</code>.<br>
      • Exiba o resultado formatado com 2 casas decimais.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a mensagem <code>Total: R$ </code> seguida pelo valor a ser pago, formatado com 2 casas decimais.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains two integer values: the product code (from 1 to 5) and the quantity of this item.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the product code and quantity on a single line using <code>input().split()</code>.<br>
      • Map the prices directly into an ordered list: <code>prices = [4.00, 4.50, 5.00, 2.00, 1.50]</code>.<br>
      • Access the correct price using the zero-based index <code>code - 1</code>.<br>
      • Calculate the total by multiplying price by quantity: <code>Total = Price · Quantity</code>.<br>
      • Display the calculated total formatted with 2 decimal places.<br><br>
      <b>📤 Output:</b><br>
      Print the message <code>Total: R$ </code> followed by the calculated value, formatted with 2 decimal places.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
3 2
```

### 📤 Exemplo de Saída / Example Output

```txt
Total: R$ 10.00
```