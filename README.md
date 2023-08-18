# Checkers-P
Two player checkers game in python using sockets

## Objetivo
Fazer um jogo de damas entre dois jogadores em dois computadores diferentes ou/e mesmo computador usando a biblioteca sockets da linguagem python.

### O protocolo
Um dos jogadores inicia o `server.py` e se torna o host da partida.</br>
Um segundo jogador, que pode ser tanto da máquina do jogador-host ou outra máquina, inicia o `client.py` e estabelece uma conexão.</br> 
O jogador-host inicia `client.py` e assim a conexão com servidor é estabelecida e a partida começa.</br>
O jogo só pode começar se dois jogadores se conectarem ao servidor.</br>

### Mensagens servidor e cliente

| Mensagens cliente| |
|--- | --- | 
| ready| cliente estão conectados e mandam ready para o sevidor para começar o jogo|
| wait | jogador espera a jogada do oponente |
| send move + move| envia jogada ao server |

| Mensagem servidor | |
| --- | --- |
| welcome | mensagem ao cliente conectado |
| ok | mensagem de jogadas válidas |
| start + turn + board | manda mensagem que o jogo vai começar |
| invalid | envia mensagem que a jogada é inválida |
| update + board + turn | faz update do tabuleiro e envia mensagem da troca de turno |
| wait | envia mensagem ao jogador para esperar a jogada do oponente |

### Notas sobre o código
- `HOST` é o valor do IP da máquina:
    - `client.py` -> IP do cliente
    - `server.py` -> IP do host
- `PORT` -> o número da porta necessita ser o mesmo para todos
