import discord

from discord.ext.commands import Cog, command, group
from discord.ext import commands
from heal.config import Color
from typing import Optional
from discord import Embed

class Information(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    async def create(self, ctx, command: str) -> None:
        Command = self.bot.get_command(command)
        if not Command:
            return await ctx.warn(
                f"{ctx.author.mention}: Command **{command}** not found."
            )
        embed = Embed(color = Color.normal).set_author(name = ctx.author.name, icon_url=ctx.author.display_avatar.url)
        embed.add_field(
            name = "**Aliases**",
            value=(
                ", ".join(Command.aliases) if Command.aliases else "N/A"
            ),
        )
        embed.add_field(
            name = 'Category',
            value =  Command.cog_name.lower() if Command.cog_name else "N/A"
        )
        embed.add_field(
            name = 'Permissions',
            value = Command.help if Command.help else "N/A"
        )
        embed.add_field(
            name = 'Usage',
            value = (
                f"```bf\nSyntax: {Command.usage}\n"
                f"Example: {Command.extras}```"
            )
        )
        await ctx.send(embed=embed)
        

    @command(
        name = 'help',
        description = '"Basic help command" he said.',
        aliases = ['h'],
        usage = 'help (Command)',
        extras = 'help avatar',
        parameters = {
            "Command": commands.command
        }
    )
    async def help(self, ctx, *, command: str = None):
        if not command:
            return await ctx.send(
                f"<https://heal.rip/commands>, server @ <https://heal.rip/discord>" # Server full of skids.
            )
        try:
            await self.create(ctx, command)
        except Exception as e:
            await ctx.warn(
                f"{ctx.author.mention}: There was an error getting this command information.. ({e})"
            )
            
async def setup(bot):
    await bot.add_cog(Information(bot))