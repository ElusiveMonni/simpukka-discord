from simpukka_discord.stack_functions import StackFunctions
import ray

def send(stack, guild_id: int, channel_id: int, content: str = "", embed=None, reply=None):
    ray.get(stack.append.remote([StackFunctions.Send, (guild_id, channel_id, content, embed, reply)]))
    return ""

def thread_add_user(stack, guild_id: int, thread_id: int, user_id: int):
    ray.get(stack.append.remote([StackFunctions.ThreadAddUser, (guild_id, thread_id, user_id)]))
    return ""

def thread_remove_user(stack, guild_id: int, thread_id: int, user_id: int):
    ray.get(stack.append.remote(([StackFunctions.ThreadRemoveUser, (guild_id, thread_id, user_id)])))
    return ""

def thread_delete(stack, guild_id: int, thread_id: int):
    ray.get(stack.append.remote(([StackFunctions.ThreadDelete, (guild_id, thread_id)])))
    return ""

def ban(stack, guild_id: int, member_id: int, reason: str = "", delete_message_seconds: int = None):
    ray.get(stack.append.remote(([StackFunctions.Ban, (guild_id, member_id, delete_message_seconds, reason)])))
    return ""

def unban(stack, guild_id: int, member_id: int, reason: str = ""):
    ray.get(stack.append.remote(([StackFunctions.Unban, (guild_id, member_id, reason)])))
    return ""

def kick(stack, guild_id: int, member_id: int, reason: str = ""):
    ray.get(stack.append.remote(stack.append([StackFunctions.Kick, (guild_id, member_id, reason)])))
    return ""

def timeout(stack, guild_id: int, member_id: int, until: int = None, reason: str = None):
    ray.get(stack.append.remote(stack.append([StackFunctions.Timeout, (guild_id, member_id, until, reason)])))
    return ""

def untimeout(stack, guild_id: int, member_id: int, reason: str = ""):
    ray.get(stack.append.remote(([StackFunctions.Untimeout, (guild_id, member_id, reason)])))
    return ""

def add_role(stack, guild_id: int, member_id: int, role_id: int, reason: str = ""):
    ray.get(stack.append.remote(([StackFunctions.AddRole, (guild_id, member_id, role_id, reason)])))
    return ""

def remove_role(stack, guild_id: int, member_id: int, role_id: int, reason: str):
    ray.get(stack.append.remote(([StackFunctions.RemoveRole, (guild_id, member_id, role_id, reason)])))
    return ""

def set_nickname(stack, guild_id: int, member_id: int, nick: str):
    ray.get(stack.append.remote(([StackFunctions.SetNickname, (guild_id, member_id, nick)])))
    return ""

def create_thread(stack, guild_id: int, channel_id: int, message_id: int, name: str, slowmode_delay: int = None, reason=""):
    ray.get(stack.append.remote(([StackFunctions.SetNickname, (guild_id, channel_id, message_id, name, slowmode_delay, reason)])))
    return ""

def delete_message(stack, guild_id: int, channel_id: int, message_id: int):
    ray.get(stack.append.remote(([StackFunctions.SetNickname, (guild_id, channel_id, message_id)])))
    return ""
