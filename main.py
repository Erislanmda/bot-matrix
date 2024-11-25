# -*- coding: utf-8 -*-
# pip install matrix-nio

from nio import AsyncClient, RoomMessageText, LoginResponse, LoginError
import asyncio

# URL do servidor Matrix (pode ser o seu próprio servidor Matrix ou um público como o matrix.org)
matrix_server_url = "https://matrix.org"

# ID da sala que você deseja que o bot entre
room_id = "id_sala"  # Substitua pelo ID da sua sala

# Função para lidar com as mensagens recebidas e decidir como responder
async def message_callback(room, event):
    if isinstance(event, RoomMessageText):
        # Evitar que o bot responda a si próprio
        if event.sender == client.user_id:
            return

        message = event.body.lower()

        # Resposta básica
        if "oi" == message:
            resposta = "Olá! você está bem?"

        elif "estou bem" == message:
            resposta = "É ótimo saber disso, tenha um ótimo dia!"

        else:
            resposta = "Desculpe, eu não entendi. Tente 'oi' ou 'estou bem'."

        # Enviar resposta ao chat
        await client.room_send(
            room.room_id,
            message_type="m.room.message",
            content={"msgtype": "m.text", "body": resposta}
        )

# Função principal do bot
async def main():
    global client
    # Inicializa o cliente Matrix
    client = AsyncClient(matrix_server_url, "@nome_do_bot:matrix.org")

    # Realiza login com usuário e senha
    try:
        response = await client.login(password="senha_do_bot")

        # Verifica se o login foi bem-sucedido ou falhou
        if isinstance(response, LoginError):
            print(f"Erro no login: {response.message}")
            return
        elif isinstance(response, LoginResponse):
            print(f"Login bem-sucedido! Logado como {response.user_id}")

    except Exception as e:
        print(f"Erro ao fazer login: {e}")
        return

    # Entrar na sala especificada
    await client.join(room_id)
    print(f"Entrou na sala: {room_id}")

    # Adiciona o callback para lidar com mensagens de texto
    client.add_event_callback(message_callback, RoomMessageText)

    # Ciclo de sincronização manual
    try:
        while True:
            await client.sync(timeout=30000)  # Sincroniza a cada 30 segundos
            await asyncio.sleep(5)  # Espera um pouco antes da próxima sincronização
    except KeyboardInterrupt:
        print("Encerrando o bot...")
    finally:
        await client.close()

# Executa o bot de forma assíncrona
if __name__ == "__main__":
    asyncio.run(main())
