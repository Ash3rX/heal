import discord

from discord.ext.commands import Cog, command, group
from discord.ext import commands
from heal.config import Color
from typing import Optional
from discord import Embed

class Miscellaneous(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @command(
        name = 'avatar',
        description = 'Shows a member avatar',
        usage = 'avatar (Member)',
        extras = 'avatar @Jinxisaskid123',
        parameters = {
            "Member": discord.Member | discord.User
        },
        aliases = [
            "av",
            "pfp"
        ]
    )
    async def avatar(self, ctx, *, Member: Optional[discord.User | discord.Member] = commands.Author):
        try:
            await ctx.send(
                embed = Embed(
                    title = f"{Member.name}'s avatar",
                    url = Member.display_avatar.url,
                    color = Color.normal
                ).set_image(
                    url = Member.display_avatar.url
                ).set_author(
                    name = ctx.author.name, icon_url = ctx.author.display_avatar.url
                )
            )
        except Exception as e:
            await ctx.warn(
                f"{ctx.author.mention}: I was unable to get that Member"
            )


async def setup(bot):
    await bot.add_cog(Miscellaneous(bot))