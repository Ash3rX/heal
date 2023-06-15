import discord
from discord.ext.commands import Cog, command, group, has_permissions
from discord.ext import commands
from heal.config import Color
from typing import Optional
from discord import Embed

class Moderation(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @command(
        name = 'ban',
        description = 'Bans a member from the server',
        aliases = ['boot'],
        usage = 'ban (Member)',
        extras = 'ban @jinxisaskid1234',
        parameters = {
            "Member": discord.Member | discord.User
        }
    )
    @has_permissions(manage_guild=True)
    async def ban(self, ctx, member: discord.Member | discord.User, *, reason: str = None):
        if not reason:
            reason = 'Unspecified reason'
        """Manage Guild"""
        try:
            await member.ban(reason=reason)
            await ctx.send(
                ":thumbsup:"
            )
        except Exception as e:
            await ctx.warn(
                "There was a problem banning this Member"
            )


async def setup(bot):
    await bot.add_cog(Moderation(bot))