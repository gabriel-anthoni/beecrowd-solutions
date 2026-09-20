<div align="center">

  <a href="https://judge.beecrowd.com/pt/problems/view/1047">
    <img src="https://skillicons.dev/icons?i=python" width="45" alt="Python Logo" />
  </a>

  <h3>beecrowd 1047 — Tempo de Jogo com Minutos</h3>

  <p>
    <img src="https://img.shields.io/badge/Linguagem-Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/N%C3%ADvel-9-green?style=flat-square" />
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
      A entrada contém quatro valores inteiros na mesma linha: hora inicial, minuto inicial, hora final e minuto final de um jogo.<br><br>
      <b>🧠 Lógica:</b><br>
      • Leia os quatro valores usando <code>map(int, input().split())</code>.<br>
      • Converta o horário inicial e o final inteiramente para minutos desde a meia-noite:<br>
      &nbsp;&nbsp;<code>Início = HoraInicial · 60 + MinutoInicial</code><br>
      &nbsp;&nbsp;<code>Fim = HoraFinal · 60 + MinutoFinal</code><br>
      • Calcule a diferença em minutos: <code>Δt = Fim - Início</code>.<br>
      • Se <code>Δt ≤ 0</code>, significa que o jogo durou até o dia seguinte (ou durou 24h exatas). Adicione 1440 minutos (24 horas) ao resultado: <code>Δt = Δt + 1440</code>.<br>
      • Converta de volta para horas e minutos usando <code>Horas = Δt // 60</code> e <code>Minutos = Δt % 60</code>.<br><br>
      <b>📤 Saída:</b><br>
      Imprima a duração do jogo no formato <code>O JOGO DUROU X HORA(S) E Y MINUTO(S)</code>.
    </td>
    <td valign="top">
      <b>📥 Input:</b><br>
      The input contains four integer values on a single line: start hour, start minute, end hour, and end minute of a game.<br><br>
      <b>🧠 Logic:</b><br>
      • Read the four values using <code>map(int, input().split())</code>.<br>
      • Convert start and end times entirely into total minutes past midnight:<br>
      &nbsp;&nbsp;<code>Start = StartHour · 60 + StartMinute</code><br>
      &nbsp;&nbsp;<code>End = EndHour · 60 + EndMinute</code><br>
      • Calculate total elapsed minutes: <code>Δt = End - Start</code>.<br>
      • If <code>Δt ≤ 0</code>, the game crossed midnight (or lasted exactly 24 hours). Add 1440 minutes (24 hours) to <code>Δt</code>: <code>Δt = Δt + 1440</code>.<br>
      • Extract hours and minutes using integer division and modulo: <code>Hours = Δt // 60</code> and <code>Minutes = Δt % 60</code>.<br><br>
      <b>📤 Output:</b><br>
      Print the duration formatted as <code>O JOGO DUROU X HORA(S) E Y MINUTO(S)</code>.
    </td>
  </tr>
</table>

### 📥 Exemplo de Entrada / Example Input

```txt
7 8 9 10
```

### 📤 Exemplo de Saída / Example Output

```
O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)
```