import discord
from discord.ext import commands

class ping():
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def ping(self, ctx, *, user: discord.Member=None):

       embed=discord.Embed(title="PONG", description="<a:ping:512065320320761867>")
       embed.add_field(name="Meu ping é aproximadamente", value=f"`{int(self.client.latency  * 1000)} ms` <a:ping:512065320320761867> ", inline=False)
       embed.set_footer(text="Direitos reservador")
       await ctx.send(embed=embed)

def setup(client):
    print("[Comando ping] Carregado")
    client.add_cog(ping(client))
