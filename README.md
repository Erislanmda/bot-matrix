
# Bot para Matrix.org com Matrix-Nio

Este repositório contém um bot simples desenvolvido para o **Matrix.org** utilizando a biblioteca **[matrix-nio](https://github.com/poljar/matrix-nio)**. Ele é projetado para ser usado em um servidor Matrix e se comunica via o cliente **Element**.

## Funcionalidades

- Responde a mensagens específicas enviadas no chat.
- Exemplos de comandos e respostas:
  - **"oi"** → Responde: *"Olá! você está bem?"*
  - **"estou bem"** → Responde: *"É ótimo saber disso, tenha um ótimo dia!"*
  - Qualquer outra mensagem → Responde: *"Desculpe, eu não entendi. Tente 'oi' ou 'estou bem'."*

## Requisitos

- Python 3.7 ou superior
- Instalar a biblioteca **matrix-nio**:  
  ```bash
  pip install matrix-nio
  ```

## Configuração

1. **Clone o repositório**:  
   ```bash
   git clone https://github.com/Erislanmda/bot-matrix.git
   cd bot-matrix/
   ```

2. **Edite o arquivo**:  
   Atualize as variáveis no código para refletir suas credenciais e configurações:
   - `matrix_server_url`: URL do servidor Matrix (exemplo: `"https://matrix.org"`).
   - `room_id`: Substitua pelo ID da sala onde o bot será usado.
   - `client = AsyncClient(matrix_server_url, "@nome_do_bot:matrix.org")`: Substitua `@nome_do_bot:matrix.org` pelo ID completo do seu bot.
   - `await client.login(password="senha_do_bot")`: Substitua `"senha_do_bot"` pela senha do bot.

3. **Execute o bot**:  
   Certifique-se de ter configurado corretamente e execute:
   ```bash
   python main.py
   ```

## Estrutura do Código

- **`message_callback`**: Lida com mensagens recebidas. Verifica o texto e responde de acordo com comandos predefinidos.
- **`main`**: Função principal que realiza:
  - Login no servidor Matrix.
  - Adição do bot à sala especificada.
  - Sincronização constante para monitorar novas mensagens.
- **Sincronização manual**: O bot sincroniza mensagens a cada 30 segundos.

## Recursos

- [Documentação do Matrix-Nio](https://matrix-nio.readthedocs.io/en/latest/)
- [Servidor público Matrix.org](https://matrix.org/)

## Observações
- Criar uma conta para o bot.
- Lembre-se de ajustar variáveis como senha, usuario do bot e id da sala para as suas credenciais.
- Certifique-se de que o ID da sala está correto. IDs de sala geralmente começam com `!` (exemplo: `!abc123:matrix.org`).
