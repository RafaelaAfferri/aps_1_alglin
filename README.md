# Alien Hunt

## Descrição do Projeto

Este projeto foi desenvolvido por Rafaela Afférri para a disciplina de Algebra Linear e Teoria da Informação, durante o 3° semestre de Ciências da Computação. O projeto foi desenvolvido no período de 1 semana com o objetivo de entender melhor vetores.

## Descrição do Jogo

O jogo, nomeado de Alien Hunt, tem como premissa a ideia de que o mundo de Minecraft esta sendo atacado por aliens. Assim, seu objetivo como narrador é atirar nos aliens para mata-lós, porém existem planetas por perto que interferem na trajetória da preda, munição do jogador, com a sua força gravitacional. O jogo contém 2 fases, para passar de cada fase o jogador tem que acertar pelo menos 5 pedras na nave espacial dos aliens.

## Como Jogar

O jogador deve usar o mouse para selecionar a direção e a velocidade em que a pedra será atirada. Quanto mais longe do canhão maior a volecidade da pedra.

### Requisitos do Sistema

Certifique-se de ter o Python e o Pygame instalados no seu sistema.

- Pyhton 3
- Pygame

Para instalar o pygame digite o seguinte comando no seu terminal:

```
pip install pygame
```

### Instalação do Jogo
Para executar o jogo, siga estas etapas:

1. Acesse o repositório do projeto: [https://github.com/RafaelaAfferri/aps_1_alglin]

2. Faça dowload do arquivo zip do projeto. Isso pode ser feito clicando no botão escrito 'Códido' ou 'Code' , depois em 'Dowload zip'

    ![Print do github](foto_code.png)

3. Abra a pasta na sua IDE de preferencia e execute o arquivo Main.py


## Modelo Físico

Para poder realizar o lançamento das "pedras" no alvo do jogo, os aliens, foi necessário modelar fisicamente o Ambiente. Esse modelo foi baseado na lei da Gravitação Universal, que possui a seguinte formula: $$ F = \frac{{G \cdot m_1 \cdot m_2}}{{r^2}} $$

No caso do jogo, a massa dos corpos e constante gravitacional, foram subestituidas por uma única constante ficticia que foi atribuida para cada corpo celestial do jogo.

A parte do código que modelos isso foi a seguinte:

``` python
distance = np.linalg.norm(celestial_body.s0 - self.s0)
gravtional_direction = (celestial_body.s0 - self.s0) / distance
gravtional_force = (celestial_body.constant / distance**2) * gravtional_direction
self.v0 = self.v0 + gravtional_force
```

No código a variavél _distance_ armazena a distância entre o corpo celestial que estamos analisando e a posição da pedra. Depois normalizamos o vetor da distancia para encontrar a distancia do vetor, que por sua vez a distancia da atração gravitacional, armazenamos esse resultado na variavel _gravtional_direction_. Com essas informações é possivél agora calcular a força gravitacional, entre a pedra e o corpo celestial, para isso dividimos a constante do corpo celestial que foi citada acima pelo quadrado da distancia 




