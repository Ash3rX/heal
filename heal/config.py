from discord.ext.commands import (Flag, ColorConverter)

class Authorzation:
    token = '' # Bot Token
    prefix = ',' # Guild Prefix / Bot Prefix
    owner_ids = [] # You're account ID 
    
    class database:
        """Want to make you're on database go to https://supabase.com/ to create one"""
        """
        its easy to create one just to let you know for you skids..
        """
        host = 'db.kjhdqqpqrshxkcyzfrfc.supabase.co'
        password = 'HEALDBPASSWORD1234ELMO'
        database = 'postgres'
        user = 'postgres'
        port: int = 5432
        
class Color:
    """Jinx just uses white idk why this guy does its stupid :skull:"""
    normal = 0xffffff
    warn = 0xffffff
    approve = 0xffffff
    
class Emoji:
    approve = '<:approve:1118825630692282439>'
    locked = '<:locked:1118825629362688092>'
    deny = '<:deny:1118828244276367433>'
    warn = '<:warn:1118828239301906512>'
    information = '<:information:1118828235812257813>'
    negative = '<:negative:1118828232746221632>'
    add = '<:add:1118828243030642739>'
    unlocked = '<:unlocked:1118828231060099154>'
