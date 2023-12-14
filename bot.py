# BIBLIOTECAS
import discord
from discord.ext import commands
import os
from colorama import Fore, Style

# CONFIGURAÇÃO DO BOT
prefixo =">>" # SEU PREFIXO
token = "MTE4NDQzNzUyMjc5Mzc3OTIxMQ.Gbc8CX.aCFZqEuTU0737VZ-XruFgBMbNzRcm2DGKcAXyI" # SEU TOKEN

# Criançãoo de objetos bot
intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
intents.presences = True

bot = commands.Bot(command_prefix=prefixo, intents=intents)


# Função para carregar os comandos
def carregar_comandos():
    for pasta_raiz, subpastas, arquivos in os.walk("comandos"):
        for arquivo in arquivos:
            if arquivo.endswith(".py"):
                caminho_arquivo = os.path.join(pasta_raiz, arquivo)
                módulo = caminho_arquivo.replace("/", ".").replace("\\", ".")[:-3]  # Caminho do módulo para importação
                bot.load_extension(módulo)

# Evento de incialização do bot

@bot.event
async def on_ready():
    total_servers = len(bot.guilds)
    total_members = sum(guild.member_count for guild in bot.guilds)

    # Adicionado cores ao nome do bot
    bot_name = f'{Fore.GREEN}{Style.BRIGHT}{bot.user}{Style.RESET_ALL}'

    print('--------------------------------------------')
    print(f'🤖 Bot conectado com {bot_name}')
    print(f'🛡️ Está em {total_servers} servidores.')
    print(f'☕ Total de membros sendo lidos: {total_members}')
    print('--------------------------------------------')

# Carregar os comandos
carregar_comandos()

bot.run(token)