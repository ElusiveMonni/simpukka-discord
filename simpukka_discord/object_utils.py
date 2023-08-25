from stack_functions import StackFunctions


def send(stack: list, guild_id: int, channel_id: int, content: str = "", embed=None, reply=None):
    stack.append([StackFunctions.Send, (guild_id, channel_id, content, embed, reply)])
    return ""

def thread_add_user(stack: list, guild_id: int, thread_id: int, user_id: int):
    stack.append([StackFunctions.ThreadAddUser, (guild_id, thread_id, user_id)])
    return ""

def thread_remove_user(stack: list, guild_id: int, thread_id: int, user_id: int):
    stack.append([StackFunctions.ThreadRemoveUser, (guild_id, thread_id, user_id)])
    return ""

def thread_delete(stack: list, guild_id: int, thread_id: int):
    stack.append([StackFunctions.ThreadDelete, (guild_id, thread_id)])
    return ""

def ban(stack: list, guild_id: int, member_id: int, reason: str = "", delete_message_seconds: int = None):
    stack.append([StackFunctions.Ban, (guild_id, member_id, delete_message_seconds, reason)])
    return ""

def unban(stack: list, guild_id: int, member_id: int, reason: str = ""):
    stack.append([StackFunctions.Unban, (guild_id, member_id, reason)])
    return ""

def kick(stack: list, guild_id: int, member_id: int, reason: str = ""):
    stack.append([StackFunctions.Kick, (guild_id, member_id, reason)])
    return ""

def timeout(stack: list, guild_id: int, member_id: int, until: int = None, reason: str = None):
    stack.append([StackFunctions.Timeout, (guild_id, member_id, until, reason)])
    return ""

def untimeout(stack: list, guild_id: int, member_id: int, reason: str = ""):
    stack.append([StackFunctions.Untimeout, (guild_id, member_id, reason)])
    return ""

def add_role(stack: list, guild_id: int, member_id: int, role_id: int, reason: str = ""):
    stack.append([StackFunctions.AddRole, (guild_id, member_id, role_id, reason)])
    return ""

def remove_role(stack: list, guild_id: int, member_id: int, role_id: int, reason: str):
    stack.append([StackFunctions.RemoveRole, (guild_id, member_id, role_id, reason)])
    return ""

def set_nickname(stack: list, guild_id: int, member_id: int, nick: str):
    stack.append([StackFunctions.SetNickname, (guild_id, member_id, nick)])
    return ""

def create_thread(stack: list, guild_id: int, channel_id: int, message_id: int, name: str, slowmode_delay: int = None, reason=""):
    stack.append([StackFunctions.SetNickname, (guild_id, channel_id, message_id, name, slowmode_delay, reason)])
    return ""

def delete_message(stack: list, guild_id: int, channel_id: int, message_id: int):
    stack.append([StackFunctions.SetNickname, (guild_id, channel_id, message_id)])