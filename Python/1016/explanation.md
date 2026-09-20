<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1016">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1016 — Distância</h3>

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
      A entrada contém um único valor inteiro, correspondendo à distância (em Km) que o carro Y deve tomar de distância do carro X.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o valor inteiro da distância usando <code>int(input())</code>.<br>
      • O carro X tem velocidade constante de 60 km/h e o carro Y de 90 km/h (o carro Y se afasta 1 km a cada 2 minutos).<br>
      • Calcule o tempo necessário multiplicando a distância por 2: <code>Tempo = Distancia · 2</code>.<br>
      • Exiba o resultado concatenando com a palavra " minutos".<br><br>
      <b>📤 Saída:</b><br>
      Imprima o tempo necessário seguido da mensagem <code> minutos</code>.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input file contains one integer value, representing the distance (in Km) that car Y must put between itself and car X.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the integer value for the distance using <code>int(input())</code>.<br>
      • Car X travels at 60 km/h and car Y at 90 km/h (car Y moves away at a rate of 1 km every 2 minutes).<br>
      • Calculate the required time in minutes by multiplying the distance by 2: <code>Time = Distance · 2</code>.<br>
      • Display the result formatted with the message " minutos".<br><br>
      <b>📤 Output:</b><br>
      Print the necessary time followed by a space and the message <code>minutos</code>.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
30
```

### 📤 Exemplo de Saída / Example Output

```txt
60 minutos
```