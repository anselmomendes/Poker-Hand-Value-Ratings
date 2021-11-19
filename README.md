# Poker Hand

Poker, ou pôquer, é um jogo de cartas tradicional de cassinos, onde dois ou mais jogadores tomam lugar em uma mesa e participam das rodadas de apostas em dinheiro (real ou fictício), vencendo aquele que tiver a combinação mais forte conforme a hierarquia das cartas.

O poker possui diversas versões de jogo, sendo as mais famosas:

* Texas Hold’em, Omaha;
* Seven Card Stud;
* Seven Card Draw;
* Five Card Stud
* Five Card Draw.

Uma mão de poker pode possuir diversas combinações que são:

![pokerhands_big](https://www.pokerharder.com/img/p/3/pokerhands_big.jpg) 

* Straight Flush: Cinco cartas em ordem numérica, todas do mesmo naipe.
* Quadra: Quatro cartas de mesmo valor, e uma outra carta como 'Kicker'.
* Full House: Três cartas do mesmo valor, e duas outras cartas diferentes de mesmo valor.
* Flush: Cinco cartas do mesmo naipe.
* Sequência: Cinco cartas em sequência.
* Trinca: Três cartas do mesmo valor, e duas outras cartas não relacionadas.
* Dois pares: Duas cartas de um mesmo valor, outras duas cartas diferentes de mesmo valor, e uma outra carta não relacionada.
* Um Par: Duas cartas do mesmo valor, e três outras cartas não relacionadas.
* Carta Alta: Qualquer mão que não esteja nas categorias acima.

Durante o jogo é possível que os jogadores possuem a mesma combinação e dessa forma é necessário estabelecer critérios de desempate.

Esse código foi desenvolvido para automatizar esse processo e evitar erros durante a verificação.

A classe PokerHand possui as seguintes métodos

* bool:compare_with -> recebe uma mão de poker e retorna qual melhor mão. True mão atual, False outra mão.
* str:show_score -> mostra o resultado para todas as combinações das mãos de Poker.
* bool:royal_flush -> Verifica se houve a combinação.
* bool:straight_flush  -> Verifica se houve a combinação.
* bool:four_of_a_kind  -> Verifica se houve a combinação.
* bool:full_house  -> Verifica se houve a combinação.
* bool:flush  -> Verifica se houve a combinação.
* bool:straight  -> Verifica se houve a combinação.
* bool:three_of_a_kind  -> Verifica se houve a combinação.
* bool:tho_pair  -> Verifica se houve a combinação.
* bool:one_pair  -> Verifica se houve a combinação.
* int:high_card  -> Retorna a maior carta.


Lista de classes abstratas com as assinaturas dos métodos:

* interface/Hand
* interface/Card

Classes com variáveis de apoio:

* settings/Common
* settings/Result

Classe de teste

* tests/TestPoker

Classe dos objetos do poker

* core/CardPoker
* core/PokeHand

Classe de verificação individual dos métodos de combinação.

# Saída do código

Teste individual

<p align="center"><img src="https://raw.githubusercontent.com/anselmomendes/Poker-Hand-Value-Ratings/test/docs/img02.png" width="80%"</p>

Execução do Teste

<p align="center"><img src="https://raw.githubusercontent.com/anselmomendes/Poker-Hand-Value-Ratings/test/docs/img03.png" width="80%"></p>

<p align="center"><img src="https://raw.githubusercontent.com/anselmomendes/Poker-Hand-Value-Ratings/test/docs/img04.png" width="80%"></p>

## Autor

- [Anselmo Mendes](https://github.com/anselmomendes)
