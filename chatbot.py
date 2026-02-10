import discord
import random
from discord.ext import commands
from app import get_password 

permisos = discord.Intents.default()
permisos.message_content = True

harvis = commands.Bot(command_prefix="/", intents=permisos)



#-------------------------------EVENTOS--------------------------------#
@harvis.event
async def on_ready():
    print("el bot esta en linea")
#-------------------------------COMANDOS-------------------------------#
@harvis.command()
async def hola(ctx):
    await ctx.send("bienvenido al servidor, ¿En que puedo ayudarte?")

@harvis.command()
async def password(ctx, longitud:int):
    contraseña = get_password(longitud)
    await ctx.send(f"la contraseña generada es: {contraseña}")

@harvis.command()
async def moneda(ctx):
    flip = random.randint(1, 2)
    if flip == 1:
        await ctx.send(f"SALIÓ: CARA")
    else:
        await ctx.send(f"SALIÓ: CRUZ")
    
@harvis.command()
async def emoji(ctx):
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)



@harvis.command()
async def comandos(ctx):
    await ctx.send(f"mis comandos son: /moneda, /password, /hola, /comandos, /emoji")

harvis.run("token")
