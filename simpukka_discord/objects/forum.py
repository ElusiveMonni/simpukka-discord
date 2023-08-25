from functools import partial

from .text import Text
from .emoji import Emoji

from discord.ext import commands
import discord


class Forum(Text):
    """Forum channel of a discord guild."""
    def __init__(self, bot: commands.Bot, guild_id: int, channel_id: int, stack: list):
        super().__init__(bot, guild_id, channel_id, stack)
        self._bot = bot

    def data(self):
        return super().data() | {"default_layout": self.default_layout, "default_reaction_emoji": self.default_reaction_emoji,
                "available_tags": self.available_tags}

    @property
    def default_layout(self):
        """Default layour of the forum"""
        return self._channel.default_layout.name

    @property
    def default_reaction_emoji(self):
        """Default reaction for new posts."""
        return Emoji(self._bot, self._guild.id, self._channel.default_reaction_emoji.id).data()

    @property
    def available_tags(self):
        """All available tags in the forum channel."""
        tags = []
        for x in self._channel.available_tags:
            tags.append(ForumTag(self._bot, self._guild.id, self._channel.id, x, self._stack).data())
        return tags



class ForumTag(Forum):
    """Discord.py forum tag wrapper. Takes tag"""
    def __init__(self, bot: commands.Bot, guild_id: int, channel_id: int, tag: discord.ForumTag, stack):
        super().__init__(bot, guild_id, channel_id, stack)
        self.tag = tag

    def data(self):
        return {"name": self.tag.name, "moderated": self.tag.moderated, "id": self.tag.id,
         "emoji": Emoji(self._bot, self._guild.id, self.tag.emoji.id).data() if self.tag.emoji is not None else None}