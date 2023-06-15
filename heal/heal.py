import discord
import os
import asyncpg
import colorama
import requests


from aiohttp.client_exceptions import (ClientConnectionError, ClientError, ClientProxyConnectionError)
from colorama import (Fore, Style)
from discord.ext.commands import Command
from discord import Embed, Guild
from discord.ext import commands


class GuildProxy:
    def __init__(self, guild_id):
        self.guild_id = guild_id
        self.guild = None
        self.url = None
        self.members = []

    async def fetch_guild(self, bot):
        """
        Fetches the guild object asynchronously using the provided bot instance.
        """
        self.guild = await bot.fetch_guild(self.guild_id)
        self.members = self.guild.members if self.guild else []

    def set_url(self, url):
        """
        Sets the URL for the guild proxy.
        """
        self.url = url

    def get_guild_id(self):
        """
        Returns the ID of the guild associated with the proxy.
        """
        return self.guild_id

    def get_guild(self):
        """
        Returns the guild object associated with the proxy.
        """
        return self.guild

    def get_url(self):
        """
        Returns the URL of the guild proxy.
        """
        return self.url

    def is_ready(self):
        """
        Checks if the guild proxy is ready (guild and URL are set).
        """
        return self.guild is not None and self.url is not None

    def get_member_names(self):
        """
        Returns a list of member names in the guild.
        """
        return [member.name for member in self.members]

    def get_member_count(self):
        """
        Returns the number of members in the guild.
        """
        return len(self.members)

    def find_member_by_name(self, name):
        """
        Finds a member in the guild by their name and returns their user object.
        Returns None if the member is not found.
        """
        for member in self.members:
            if member.name == name:
                return member
        return None

    def get_online_members(self):
        """
        Returns a list of online members in the guild.
        """
        return [member for member in self.members if member.status == "online"]

    def get_member_roles(self, member):
        """
        Returns a list of roles for the specified member.
        """
        return member.roles if member in self.members else []

    def get_member_top_role(self, member):
        """
        Returns the top role (highest position) of the specified member.
        """
        roles = self.get_member_roles(member)
        return max(roles, key=lambda role: role.position) if roles else None
    
    
class HealContext(discord.Context):
    """Custom Context for sending Messages"""
    async def approve(self, message: str) -> None:
        embed = Embed(description=f'', color=0xffffff)
        await self.send(embed=embed)
        
    async def warn(self, message: str) -> None:
        embed = Embed(description=f'', color=0xffffff)
    

class Worker(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def get_context(self, message, *, cls=HealContext):
        return await super().get_context(message, cls=cls)