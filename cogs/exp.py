import os
import r
from discord.ext import commands
import discord
import random
import asyncio

logch=723818798905425971
expch=676738177062535168

class jgame(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        conn=r.connect()
        ky=conn.exists(message.author.id)
        if ky==0:
            uset=conn.set(message.author.id,'0')
            ch=self.bot.get_channel(logch)
            if uset == True:
                embed=discord.Embed(title="登録通知",description=f'{message.author.name}さんを登録しました',color=0x3498db)       
                await ch.send(embed=embed)
            else:
                embed=discord.Embed(title="登録通知",description=f'{message.author.name}さんの登録に失敗しました',color=0xe74c3c)       
                await ch.send(embed=embed)

        else:
            ps=conn.smembers("exp")
            pss=[pl for pl in ps]
            p=random.choice(pss)
            up=conn.get(message.author.id)
            up=int(up)
            up+=p
            upd=conn.set(message.author.id,up)
            ch=self.bot.get_channel(expch)
            if upd == True:
                embed=discord.Embed(title="登録通知",description=f'{message.author.name}さんに{up}exp付与しました',color=0x3498db)       
                await ch.send(embed=embed)
            else:
                embed=discord.Embed(title="登録通知",description=f'{message.author.name}さんの付与に失敗しました',color=0xe74c3c)       
                await ch.send(embed=embed)

    @commands.command()
    async def myexp(self, ctx, user=None):
        if user == None:
            user=ctx.author.id
        conn=r.connect()
        q=conn.exists(user)
        ui=self.bot.get_user(user)
        if q>0:
            up=conn.get(user)
            embed=discord.Embed(title="現在経験値",description=f'{ui.name}さんの経験値\n`{up}`',color=0x3498db)       
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="現在経験値",description=f'{ui.name}さんの経験値\n`登録されていません`',color=0xe74c3c)       
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(jgame(bot))
