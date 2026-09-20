<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1050">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1050 — DDD</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-2-green?style=flat-square" />
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
      A entrada consiste em um único valor inteiro representando o código do DDD.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia a entrada diretamente como string ou inteiro usando <code>input().strip()</code>.<br>
      • Mapeie os códigos DDD para as cidades usando um dicionário em Python:<br>
      &nbsp;&nbsp;- <code>61</code>: <code>Brasilia</code><br>
      &nbsp;&nbsp;- <code>71</code>: <code>Salvador</code><br>
      &nbsp;&nbsp;- <code>11</code>: <code>Sao Paulo</code><br>
      &nbsp;&nbsp;- <code>21</code>: <code>Rio de Janeiro</code><br>
      &nbsp;&nbsp;- <code>32</code>: <code>Juiz de Fora</code><br>
      &nbsp;&nbsp;- <code>19</code>: <code>Campinas</code><br>
      &nbsp;&nbsp;- <code>27</code>: <code>Vitoria</code><br>
      &nbsp;&nbsp;- <code>31</code>: <code>Belo Horizonte</code><br>
      • Utilize o método <code>dict.get(ddd, "DDD nao cadastrado")</code> para retornar a cidade ou a mensagem de não cadastrado caso a chave não exista.<br><br>
      <b>📤 Saída:</b><br>
      Imprima o nome da cidade correspondente ao DDD lido ou a mensagem <code>DDD nao cadastrado</code>.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input consists of a single integer value representing an area code (DDD).<br><br>
      <b>🧠 Logic:</b><br>
      • Read the input directly as a string or integer using <code>input().strip()</code>.<br>
      • Map the DDD codes to their corresponding cities using a Python dictionary:<br>
      &nbsp;&nbsp;- <code>61</code>: <code>Brasilia</code><br>
      &nbsp;&nbsp;- <code>71</code>: <code>Salvador</code><br>
      &nbsp;&nbsp;- <code>11</code>: <code>Sao Paulo</code><br>
      &nbsp;&nbsp;- <code>21</code>: <code>Rio de Janeiro</code><br>
      &nbsp;&nbsp;- <code>32</code>: <code>Juiz de Fora</code><br>
      &nbsp;&nbsp;- <code>19</code>: <code>Campinas</code><br>
      &nbsp;&nbsp;- <code>27</code>: <code>Vitoria</code><br>
      &nbsp;&nbsp;- <code>31</code>: <code>Belo Horizonte</code><br>
      • Use <code>dict.get(ddd, "DDD nao cadastrado")</code> to safely return the city name or the default fallback message if the key does not exist.<br><br>
      <b>📤 Output:</b><br>
      Print the city name corresponding to the given DDD code or <code>DDD nao cadastrado</code>.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
11
```

### 📤 Exemplo de Saída / Example Output

```
Sao Paulo
```