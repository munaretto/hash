# hash

Este projeto tem como objetivo a prática de funções resumo através de uma simulação do mecanismo de criptografia para arquivos de vídeo em um serviço de streaming. Dado um arquivo F, o programa em questão irá dividi-lo em blocos de 1024 bytes cada, fazer o hash com SHA256 do último bloco e concatenar o resultado em binário no penúltimo bloco. Este processo se repetirá até o bloco 0. Ao gerar o hash para o bloco 0, o programa irá então devolver esta informação ao usuário, sendo ela então denominada de h0.

## Modo de execução

**OBS: Para executar esta aplicação, garanta que a sua máquina possui python 3.8 instalado.**

1. Clone o repositório com o comando ```https://github.com/munaretto/hash.git``` ou ```git@github.com:munaretto/hash.git```.
2. No diretório ```/hash```, abra um terminal e digite ```python3 hash.py <nome_do_arquivo>```.