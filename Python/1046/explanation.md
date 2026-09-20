<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1046">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1046 — Tempo de Jogo</h3>

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
      A entrada contém dois valores inteiros na mesma linha representando a hora de início e a hora de fim de um jogo.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia o horário inicial e final usando <code>map(int, input().split())</code>.<br>
      • Se <code>Início < Fim</code>: a duração é <code>Fim - Início</code>.<br>
      • Se <code>Início ≥ Fim</code>: o jogo passa da meia-noite, logo a duração é <code>(24 - Início) + Fim</code>.<br>
      • Essa fórmula unificada cobre tanto jogos que viram o dia quanto o caso em que <code>Início == Fim</code> (duração de 24 horas).<br><br>
      <b>📤 Saída:</b><br>
      Imprima a duração do jogo no formato <code>O JOGO DUROU X HORA(S)</code>.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains two integer values on a single line representing the start time and end time of a game.<br><br>
      <b>🧠 Logic:</b><br>
      • Read start and end times using <code>map(int, input().split())</code>.<br>
      • If <code>Start < End</code>: duration is <code>End - Start</code>.<br>
      • If <code>Start ≥ End</code>: the game spans overnight, so duration is <br><code>(24 - Start) + End</code>.<br>
      • This unified logic handles overnight games as well as the case where <code>Start == End</code> (24-hour duration).<br><br>
      <b>📤 Output:</b><br>
      Print the calculated duration matching the template <code>O JOGO DUROU X HORA(S)</code>.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
16 2
```

📤 Exemplo de Saída / Example Output

```
O JOGO DUROU 10 HORA(S)
```