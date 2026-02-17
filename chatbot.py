import discord
import random
from discord.ext import commands
import os
import requests
from app import get_password 
from numero_al_azar import numero_random
permisos = discord.Intents.default()
permisos.message_content = True

harvis = commands.Bot(command_prefix="/", intents=permisos)


#------------------------------VARIABLES-------------------------------#
juego_activo = False 
numero_secreto = None 
intentos = 5

#------------------------------API´s-----------------------------------#
def get_dog_image_url():    
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data["url"]

def get_fox_image_url():    
    url = "https://randomfox.ca/floof/"
    res = requests.get(url)
    data = res.json()
    return data["image"]

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_tokyo_image_url():    
    url = "https://kitsu.io/api/edge/anime?filter[text]=tokyo"
    res = requests.get(url)
    data = res.json()
    return data["links"]
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
    await ctx.send(f"{random.choice(emodji)}")

@harvis.command()
async def play(ctx, numero_del_usuario:int = None):
    global juego_activo, numero_secreto, intentos
    if not juego_activo:
        mensaje, numero_secreto, intentos, juego_activo = numero_random()
        await ctx.send(f"{mensaje}")
        return
    if numero_del_usuario == None:
        mensaje, numero_secreto, intentos, juego_activo = numero_random()
        await ctx.send(f"{mensaje}")
        return
    

@harvis.command()
async def comandos(ctx):
    await ctx.send(f"mis comandos son: /moneda, /password, /hola, /comandos, /emoji, /play(comando experimental), /meme /dogs, /foxs, /duck, /tokyo(comando experimental)")

@harvis.command()
async def meme(ctx):
    lista_imagenes = os.listdir("img")
    imagen_enviar = random.choice(lista_imagenes)
    with open(f"img/{imagen_enviar}", "rb") as f:
        image = discord.File(f)
        await ctx.send(file = image)

@harvis.command('dogs')
async def dogs(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@harvis.command('foxs')
async def foxs(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)

@harvis.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@harvis.command('tokyo')
async def tokyo(ctx):
    image_url = get_tokyo_image_url()
    await ctx.send(image_url)

harvis.run("token")
