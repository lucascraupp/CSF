# Campanha de medição LoRaWan com gateway do campus IFSC-SJ

## Introdução


As medições foram conduzidas por meio da utilização do dispositivo [IoT DevKit - LoRaWAN](https://www.robocore.net/tutoriais/iot-devkit-introducao) em uma série de campanhas. O objetivo dessas campanhas era coletar dados na área central de São José, em Santa Catarina, o gateway utilizado estava posicionado no topo da caixa d'água do IFSC-SJ, em uma altura aproximada de 18 metros. Neste repositório, você encontrará os dados coletados, bem como uma análise dos mesmos.

## Fundamentação teórica

### Modelo de Perda de Caminho Log-Distância

Os modelos de propagação teóricos e baseados em medições indicam que a potência média do sinal recebido diminui de forma logarítmica à medida que a distância aumenta, tanto em canais de rádio internos como externos.

 A perda de caminho média em grande escala para uma separação transmissor ($T$) e receptor ($R$),  qualquer $T-R$ é expressa como a função da distância usando um expoente de perda de caminho, $n$. Como na equação abaixo:



$$ \overline{PL}(dB) = \overline{PL}(d_0) + 10n\log_{}\left(\frac{d}{d_0}\right)
$$

onde:
- $\overline{PL}(dB)$ é a perda de caminho estimado em $dB$
- $\overline{PL}(d_0)$ é a perda de caminho na distância de referência em $dB$
- $n$ é expoente de perda de caminho que indica a velocidade com a qual essa perda aumenta com relação à distância e depende do ambiente de propagação específico.
- $d_0$ é a distância de referência próxima determinada pelas medições perto do transmissor.
- $d$ é a distância de separação $T-R$
- As barras na equação indicam a média conjunta de todos os valores possíveis de perda de caminho para determinado valor de $d$.

### Sombreamento log-normal

<!-- a equação anterior não considera o fato de o ruído ambiental ao redor pode ser diferente em dois locais distintos tendo a mesma separação $T-R$, o que leva a sinais medidos diferentes do valor médio da equação anterior -->

A distribuição log-normal descreve os efeitos aleatórios do sombreamento, que ocorrem em vários locais próximos que possuem a separação $T-R$ , mas com diferentes níveis de ruído no caminho de propagação. o sombreamento log-normal implica que os níveis de sinal medidos em uma separação $T-R$ específica seguem uma distribuição gaussiana (normal) em torno da média que depende da distância.
## Medições

Na tabela a seguir são apreentados os valores de latitude e longitude dos pontos de medições.

### Coordenadas dos pontos *outdoor*

|      Local            |   Distância (m)  |     Latitude     |    Longitude     |
|:---------------------:|:----------------:|:----------------:|:-----------------:|
| Milium                |  189.91          | -27.000000       | -48.641689       |
| MundoCar              | 1970.00          | -27.595877       | -48.619192       |
| Início da Beira-Mar   | 1999.00          | -27.603965       | -48.614106       |
| Fim da Beira-Mar      | 3015.00          | -27.602661       | -48.602376       |
| Posto Perto IFSC      |  407.45          | -27.604444       | -48.632901       |
| Laje                  |   84.11          | -27.608464       | -48.633043       |
| Florifarma            |  206.08          | -27.607763       | -48.661695       |
| Bradesco              |  544.97          | -27.595768       | -48.643806       |
| Multiuso              | 2285.27          | -27.603642       | -48.610991       |
| Frente IFSC           | 131.77           | -27.608117       | -48.632395       |
| Frente Bistek         | 1014.65          | -27.606824       | -48.623519       |
| Abraão Beira-Mar      | 3580.00          | -27.611220       | -48.597652       |
| Imobiliária Ideal     |  473.45          | -27.604298       | -48.635705       |
| Anhanguera            | 1060.46          | -27.608923       | -48.641857       |



## Simulação dos pontos *outdoor* no *Radio Mobile*

Os pontos das medições *outdoor* foram utilizados para simulação com o *software* *Radio Mobile* e os resultados estão em arquivos html no diretório [radio-mobile](./radio-mobile/).

## Comparação entre dados medidos e simulados e calculados

A tabela a seguir apresenta uma comparação dos valores de Potência Recebida (RSSI) e Perda de caminho (PL) entre o dados medidos, calculados e simulados, considerando somente os pontos *outdoor*.

| Local               | RSSI medido (dBm) | PL medido (dB)  | RSSI simulado (dBm) | PL simulado (dB) |
|---------------------|-------------------|-----------------|---------------------|------------------|
| Milium              | -109.045455       | 122.935455      | -90.85              | 102.83           |
| MundoCar            | -109.833333       | 123.723333      | -87.18              | 101.07           |
| Início da Beira-Mar | -98.87            | 112.76          | -85.98              | 99.87            |
| Fim da Beira-Mar    | -108.05           | 121.94          | -91.91              | 105.80           |
| Posto Perto IFSC    | -77.80            | 91.69           | -76.91              | 90.80            |
| Laje                | -82.43            | 96.32           | -61.59              | 75.48            |
| Florifarma          | -101.090909       | 114.980909      | -97.71              | 109.71           |
| Bradesco            | -107.000000       | 120.890000      | -88.72              | 100.73           |
| Centro Multiuso     | -100.421053       | 114.311053      | -88.14              | 102.03           |
| Frente IFSC         | -90.46            | 104.34          | -62.16              | 76.05            |
| Frente Bistek       | -96.80            | 110.69          | -79.38              | 93.27            |
| Abraão Beira-Mar    | -102.60           | 116.49          | -101.96             | 115.85           |
| Imobiliária Ideal   | -85.656250        | 99.546250       | -73.66              | 85.64            |
| Anhanguera          | -96.608696        | 110.498696      | -119.09             | 131.09           |



<!-- > 1. Valores obtidos adicionando uma variável aleatória gaussiana de média 0 e desvio padrão de 10,91 ao valor calculado, então podem mudar a cada execução.
> 2. Simulação realizada no software *Radio Mobile*  -->

<!-- ## Parâmetros obtidos
A partir do método de minimização de erro MSE utilizado no código, o valor do parâmetro N obtido está representado na tabela abaixo.

|        | p0 ($dB$) | d0 (m)  | N     |
|--------|------------|---------|-------|
| Outdoor| -77,8      | -80,89  | 2,519 | -->

<!-- ## Mapa de calor

Com o N estimado pela minimização citada acima, foram obtidos estes valores de RSSI (estes valores utilizam uma variável aleatória gaussiana e podem mudar a cada execução).

| Distância (m) | RSSI ($dB$)          |
|-----------|---------------|
| 1         | -21.42376652  |
| 500       | -89.43267884  |
| 1000      | -97.00470094  |
| 1500      | -101.43679616 |
| 2000      | -104.58218069 |
| 2500      | -107.02225042 |
| 3000      | -109.01609695 |
| 3500      | -110.70196579 |

Abaixo o mapa de calor:

![](mapa.png) -->
