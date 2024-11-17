import discord
from discord.ext import commands

#cofiguracion de las intenciones (permisos)
intenciones=discord.Intents.default()
intenciones.message_content=True

#creacion de la instancia del bot
bot=commands.Bot(command_prefix="/", intents=intenciones)

#crear el evento de inicio del boton
@bot.event
async def on_ready():
    print(f"El bot {bot.user} esta en linea")

#creacion de comando para clasificar residuos 
@bot.command()
async def clasificar(ctx, *, objeto:str):
    reciclables=['botella de plastico']
    no_reciclables=['pañal','cascara de platano']

    objeto=objeto.lower()
    if objeto in reciclables:
        await ctx.send(f'El {objeto} es reciclable')
    elif objeto in no_reciclables:
        await ctx.send(f'El {objeto} no es reciclable')
    else:
        await ctx.send(f'No se tiene informacion sobre {objeto}')

bot.run("tu token")
