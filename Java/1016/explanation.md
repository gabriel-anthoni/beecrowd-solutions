### <img src="https://static.wikia.nocookie.net/duolingo/images/1/17/Brazil_bandera.png/revision/latest?cb=20230710181600&path-prefix=es" width="20"> PT-BR

<!----------------------------------------------------------------------------------------->

<table>
  <tr>
    <th width="300">Linguagem</th>
    <th width="1000">Questão</th>
  </tr>
  <tr>
    <td>
      <p align="center"><img src="https://skillicons.dev/icons?i=java"></p>
      <p align="center"><code>Java 19</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1016</i></p>
      <h3 align="center">Distância</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Entrada:

- A entrada contém um único valor inteiro representando a distância $D$ (em km) que o carro Y deve se distanciar do carro X.

*Exemplo de entrada:*
```
30
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Lógica:

- O carro X roda a uma velocidade constante de 60 km/h e o carro Y roda a 90 km/h.
- A velocidade relativa do carro Y em relação ao carro X é:
  $$\text{Velocidade Relativa} = 90 - 60 = 30 \text{ km/h}$$
- Se o carro Y ganha 30 km de vantagem em 60 minutos, ele ganha 1 km a cada 2 minutos:
  $$\text{Tempo por km} = \frac{60 \text{ min}}{30 \text{ km}} = 2 \text{ min/km}$$
- Portanto, para uma distância $D$, o tempo necessário em minutos é dado por:
  $$\text{Tempo} = D \times 2$$

---

<!----------------------------------------------------------------------------------------->

#### 📤 Saída:

- Imprima o tempo necessário seguido da mensagem `minutos` e uma quebra de linha `\n`.

*Exemplo de saída:*
```
60 minutos
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
      <p align="center"><img src="https://skillicons.dev/icons?i=java"></p>
      <p align="center"><code>Java 19</code></p>
    </td>
    <td>
      <p align="center"><i>beecrowd | 1016</i></p>
      <h3 align="center">Distance</h3>
    </td>
  </tr>
</table>

<!----------------------------------------------------------------------------------------->

#### 📥 Input:

- The input file contains a single integer value representing the distance $D$ (in km) that car Y needs to take away from car X.

*Example Input:*
```
30
```

---

<!----------------------------------------------------------------------------------------->

#### 🧠 Logic:

- Car X travels at a constant speed of 60 km/h and car Y travels at 90 km/h.
- The relative speed of car Y compared to car X is:
  $$\text{Relative Speed} = 90 - 60 = 30 \text{ km/h}$$
- Since car Y gains 30 km of distance in 60 minutes, it gains 1 km every 2 minutes:
  $$\text{Time per km} = \frac{60 \text{ min}}{30 \text{ km}} = 2 \text{ min/km}$$
- Thus, for a distance $D$, the total required time in minutes is calculated as:
  $$\text{Time} = D \times 2$$

---

<!----------------------------------------------------------------------------------------->

#### 📤 Output:

- Print the calculated time followed by the message `minutos` and a newline `\n`.

*Example Output:*
```
60 minutos
```