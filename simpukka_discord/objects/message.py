from functools import partial

from simpukka_discord.objects import member, user, emoji
from discord.ext import commands
import discord
from simpukka_discord.object_utils import create_thread, delete_message


class Message:
    __slots__ = (
        "_bot",
        "_message",
        "_guild",
        "_stack"
    )

    def __init__(self, bot: commands.Bot, message: discord.Message, guild: discord.Guild, stack: list):
        self._message = message
        self._guild = guild
        self._bot = bot
        self._stack = stack

    def data(self):
        return {"id": self.id, "content": self.content, "author": self.author, "jump_url": self.jump_url,
                "created_at": self.created_at, "edited_at": self.edited_at,
                "create_thread": partial(create_thread, self._stack, self._guild.id, self._message.channel.id,
                                         self._message.id),
                "delete_message": partial(delete_message, self._stack, self._guild.id, self._message.channel.id,
                                          self._message.id)}

    @property
    def id(self) -> int:
        """Role name."""
        return self._message.id

    @property
    def content(self) -> str:
        """Content of the message."""
        return self._message.content

    @property
    def author(self) -> member.Member | user.User:
        """Author of the message."""
        if isinstance(self._message.author, discord.abc.User):
            return user.User(self._bot, self._message.author.id)
        else:
            return member.Member(self._bot, self._guild.id, self._message.author.id, self._stack)

    @property
    def jump_url(self) -> str:
        """Url to the message."""
        return self._message.jump_url

    @property
    def created_at(self) -> int:
        """Unix timestamp of when message was created."""
        return int(self._message.created_at.timestamp())

    @property
    def edited_at(self) -> int:
        """Unix timestamp of when message was edited."""
        return int(self._message.created_at.timestamp())

    def create_thread(self, name, archive_duration, slowmode_delay=0, reason=""):
        """Create a new thread on the message"""
        raise NotImplementedError

    def delete(self):
        """Delete the message."""
        raise NotImplementedError
