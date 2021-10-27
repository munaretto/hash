from os import path
import sys
from Crypto.Hash import SHA256

# Função responsável por quebrar o arquivo em blocos de tamanho 
def get_blocks(file, blockSize):
    blocks = []
    buffer = open(file, 'rb')

    block = buffer.read(blockSize)
    while block:
        blocks.append(block)
        block = buffer.read(blockSize)

    return blocks

# Função responsável por calcular os hashes de todos os blocos e devolver 'previousHash' ao final do loop
def calculate_hash(blocks):
    previousHash = bytearray()
    while blocks:
        block = bytearray(blocks.pop())
        block += previousHash

        previousHash = bytearray(SHA256.new(data = block).digest())

    return previousHash

if __name__ == "__main__":

    args = sys.argv[1:]

    # Verifica se o usuário passou um arquivo ao inicializar o programa
    if(len(args) < 1):
        print(
            'A file name must is required in order to perform this action.' + 
            '\n\n' +
            'Try typing \'python3 hash.py <file name>\'.')
        exit()

    file = args[0]
    blockSize = 1024
    
    # Divide o arquivo em n blocos de tamanho 'blockSize'
    blocks = get_blocks(file, blockSize)
    
    # Calcula o hash para cada bloco, devolvendo no final o h0 do arquivo
    h0 = calculate_hash(blocks) # hash final h0 -> 302256b74111bcba1c04282a1e31da7e547d4a7098cdaec8330d48bd87569516
    print('h0:', h0.hex())