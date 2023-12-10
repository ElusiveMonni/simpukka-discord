import datetime
from enum import Enum

import discord
from discord.ext import commands

async def send(bot: commands.Bot, guild_id: int, channel_id: int, content: str, embed=None, reply: int=None, **kwargs):
    guild = bot.get_guild(guild_id)
    channel = guild.get_channel_or_thread(channel_id)

    if embed is not None:
        embed = discord.Embed.from_dict(embed._to_json())

    if reply is not None:
        reply = channel.get_partial_message(reply).to_reference(fail_if_not_exists=False)

    # TODO MAKE POSSIBLE TO CHANGE AND SET IN CONFIG
    await channel.send(content, embed=embed, allowed_mentions=discord.AllowedMentions(roles=False, everyone=False),
                       reference=reply)

async def thread_add_user(bot: commands.Bot, guild_id, thread_id, user_id, **kwargs):
    guild = bot.get_guild(guild_id)
    thread = guild.get_thread(thread_id)
    member = guild.get_member(user_id)
    await thread.add_user(member)


async def thread_remove_user(bot: commands.Bot, guild_id, thread_id, user_id, **kwargs):
    guild = bot.get_guild(guild_id)
    thread = guild.get_thread(thread_id)
    member = guild.get_member(user_id)
    await thread.remove_user(member)

async def thread_delete(bot: commands.Bot, guild_id, thread_id, **kwargs):
    guild = bot.get_guild(guild_id)
    thread = guild.get_thread(thread_id)
    await thread.delete()

async def ban(bot: commands.Bot, guild_id: int, member_id: int, delete_message_seconds: int, reason: str, **kwargs):
    if delete_message_seconds is None:
        delete_message_seconds = 0
    guild = bot.get_guild(guild_id)
    await guild.ban(user=discord.Object(member_id, type=discord.User), delete_message_seconds=delete_message_seconds, reason=reason)

async def unban(bot: commands.Bot, guild_id: int, member_id: int, reason: str, **kwargs):
    guild = bot.get_guild(guild_id)
    await guild.unban(discord.Object(member_id, type=discord.User), reason=reason)

async def kick(bot: commands.Bot, guild_id: int, member_id: int, reason: str, **kwargs):
    guild = bot.get_guild(guild_id)
    await guild.kick(user=discord.Object(member_id, type=discord.User), reason=reason)

async def timeout(bot: commands.Bot, guild_id: int, member_id: int, until: int, reason: str, **kwargs):
    guild = bot.get_guild(guild_id)
    member = guild.get_member(member_id)
    await member.timeout(datetime.timedelta(seconds=until), reason=reason)

async def untimeout(bot: commands.Bot, guild_id: int, member_id: int, reason: str, **kwargs):
    guild = bot.get_guild(guild_id)
    member = guild.get_member(member_id)
    await member.timeout(None, reason=reason)

async def add_role(bot: commands.Bot, guild_id: int, member_id: int, role_id: int, reason: str, **kwargs):
    guild = bot.get_guild(guild_id)
    member = guild.get_member(member_id)
    role = guild.get_role(role_id)
    await member.add_roles(role, reason=reason)

async def remove_role(bot: commands.Bot, guild_id: int, member_id: int, role_id: int, reason: str, **kwargs):
    guild = bot.get_guild(guild_id)
    member = guild.get_member(member_id)
    role = guild.get_role(role_id)
    await member.remove_roles(role, reason=reason)

async def set_nickname(bot: commands.Bot, guild_id: int, member_id: int, nick: str, **kwargs):
    guild = bot.get_guild(guild_id)
    member = guild.get_member(member_id)
    await member.edit(nick=nick)

async def create_thread(bot: commands.Bot, guild_id: int, channel_id: int, message_id: int, name: str, slowmode_delay: int = None, reason="", **kwargs):
    guild = bot.get_guild(guild_id)
    channel = guild.get_channel_or_thread(channel_id)
    message = channel.get_partial_message(message_id)
    await message.create_thread(name=name, slowmode_delay=slowmode_delay, reason=reason)

async def delete_message(bot: commands.Bot, guild_id: int, channel_id: int, message_id: int, **kwargs):
    guild = bot.get_guild(guild_id)
    channel = guild.get_channel_or_thread(channel_id)
    message = channel.get_partial_message(message_id)
    await message.delete()


class StackFunctions(Enum):

    Send = send

    ThreadAddUser = thread_add_user
    ThreadRemoveUser = thread_remove_user
    ThreadDelete = thread_delete
    CreateThread = create_thread

    Ban = ban
    Unban = unban
    Kick = kick
    Timeout = timeout
    Untimeout = untimeout
    AddRole = add_role
    RemoveRole = remove_role
    SetNickname = set_nickname

    DeleteMessage = delete_message
    
