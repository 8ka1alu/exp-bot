import os
import r
from discord.ext import commands
import discord
import asyncio

class jrole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def role(self, ctx):
        """役職関連"""
        conn=r.connect()
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            jack=conn.smembers("人狼役職")
            jr=[j for j in jack]          
            embed=discord.Embed(title="現在人狼役職",description=None)
            for i in jr:
                p=conn.get(i)
                embed.add_field(name=f'**{i}**',value=f'`{p}`')
            await ctx.send(embed=embed)

    @role.command()
    async def set(self, ctx, what=None, whats=None):
        conn=r.connect()
        kk=conn.smembers("開発管理者")
        k=[l for l in kk]
        cai=ctx.author.id
        cai=str(cai)
        if cai not in k:
            return await ctx.send("使用できません")
        rk=conn.smembers("人狼役職")
        kr=[l for l in rk]
        cai=what
        cai=str(cai)
        if cai not in kr:
            return await ctx.send("その役職はありません")
        if what==None:
            return await ctx.send("役職を指定して下さい")
        if whats==None:
            return await ctx.send("変更値を指定して下さい")
        rs=conn.set(what,whats)
        if rs ==True:
            embed=discord.Embed(title="役職変更成功",description=None)
            embed.add_field(name=f'**{what}**',value=f'`{whats}`')
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="役職変更失敗",description="`変更に失敗しました`")
            await ctx.send(embed=embed)

    @role.command()
    async def reset(self, ctx, what=None):
        conn=r.connect()
        kk=conn.smembers("開発管理者")
        k=[l for l in kk]
        cai=ctx.author.id
        cai=str(cai)
        if cai not in k:
            return await ctx.send("使用できません")
        if what==None:
            return await ctx.send("役職を指定して下さい")
        if what=="all":
            return
        else:
            rk=conn.smembers("人狼役職")
            kr=[l for l in rk]
            cai=what
            cai=str(cai)
            if cai not in kr:
                return await ctx.send("その役職はありません")
            else:
                pp=conn.set(what,'0')
                if pp==True:
                    embed=discord.Embed(title="役職変更成功",description=None)
                    embed.add_field(name=f'**{what}**',value=f'`0`')
                    await ctx.send(embed=embed)
                else:
                    embed=discord.Embed(title="役職変更失敗",description="`変更に失敗しました`")
                    await ctx.send(embed=embed)
             
def setup(bot):
    bot.add_cog(jrole(bot))
