import asyncio

# Exemplo 1
async def corrotina():
    print('Início')
    await asyncio.sleep(2)
    print('Fim')
    
asyncio.run(corrotina())

# Exemplo 2
async def corrotina(numero):
    print(f"Iniciando tarefa {numero}.")
    await asyncio.sleep(2)
    print(f"Tarefa {numero} concluída!")

async def main():
    await corrotina(1)
    await corrotina(2)

asyncio.run(main())

# Exemplo 3
async def corrotina(numero, tempo):
    print(f"Iniciando tarefa {numero}.")
    await asyncio.sleep(tempo)
    print(f"Tarefa {numero} concluída!")

async def main():
    tarefa1 = asyncio.create_task(corrotina(1, 6))
    tarefa2 = asyncio.create_task(corrotina(2, 3))
    await tarefa1
    await tarefa2

asyncio.run(main())

# Exemplo 4
async def corrotina1(futuro):
    print("Tarefa 1 iniciada.")
    await asyncio.sleep(2)
    futuro.set_result("Resultado da Tarefa 1")
    print("Tarefa 1 finalizada.")

async def corrotina2(futuro):
    print("Tarefa 2 iniciada, aguardando o futuro.")
    resultado = await futuro
    print("Tarefa 2 finalizada com o resultado:", resultado)

async def main():
    futuro = asyncio.Future()
    tarefa1 = asyncio.create_task(corrotina1(futuro))
    tarefa2 = asyncio.create_task(corrotina2(futuro))

    await tarefa1
    await tarefa2

asyncio.run(main())

# Exemplo 5
async def corrotina(nome, tempo):
    print(f"Tarefa {nome} iniciada.")
    await asyncio.sleep(tempo)
    print(f"Tarefa {nome} concluída.")

async def main():
    await asyncio.gather(
        corrotina("1",2),
        corrotina("2",3),
        corrotina("3",1),
    )

asyncio.run(main())