import discord
import asyncio
from discord.ext.commands import Cog, command, group, has_permissions

class Discrim(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @Cog.listener()
    async def on_member_update(self, before, after):
        if before.discriminator != after.discriminator:
            if before.discriminator == ('0', '0001'):
                for guild in self.bot.guilds:
                    check = await self.bot.db.fetchrow('SELECT channel FROM discrim WHERE Guild = $1', guild.id)
                    if check:
                        channel = self.bot.get_channel(check['channel'])
                        await channel.send(
                            f"**{f'@{before.name}' if before.discriminator == '0' else before}** is now available"
                        )
            
    @group(
        name = 'discrim',
        description = 'Sets an discrim channel/remove one',
        usage = ',discrim (Subcommand)',
        extras = ',discrim add #chat-is-this-real',
        aliases = [
            'tracker', 
            'tags',
        ],
        parameters = {
            "subcommand": 'Bot Command'
        }
    )
    async def discrim(self, ctx): ...
    
    
    @discrim.command(
        name = 'add',
        description = 'Adds an discrim channel',
        usage = 'discrim add (channel)',
        extras = 'discrim add #chat-is-this-real',
        aliases = ['create'],
        parameters = {
            "Channel": discord.TextChannel | discord.Thread
        }
    )
    @has_permissions(manage_channels=True)
    async def DiscrimAdd(   
        self, ctx, *,
        channel: discord.TextChannel | discord.Thread = None
    ):
        if not channel: 
            return await ctx.warn(
                f"{ctx.author.mention}: "
                "You havn't provided a channel."
            )
        try:
            check = await self.bot.db.fetch('SELECT * FROM discrim WHERE Guild = $1', ctx.guild.id)
            if not check:
                await self.bot.db.execute(
                    'INSERT INTO discrim (guild, channel) VALUES ($1, $2);', 
                    ctx.guild.id, channel.id
                )
            if check:
                await self.bot.db.execute(
                    'UPDATE discrim SET channel = $1 WHERE guild = $2',
                    channel.id, ctx.guild.id
                )
            await ctx.approve(
                f"{ctx.author.mention}: {f'Updated **{channel.name}** for' if check else 'Now logging'} "
                f"Discriminators in {channel.mention}."
            )
        except Exception as e:
            await ctx.warn(
                f"{ctx.author.mention}: Could not do this operation: "
                f"{e}"
            )


async def setup(bot):
    await bot.add_cog(Discrim(bot))