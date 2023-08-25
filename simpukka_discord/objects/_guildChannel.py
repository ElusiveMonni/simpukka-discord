from discord.ext import commands
import discord
from functools import partial
from simpukka_discord.object_utils import send


class GuildChannel:
    """Class which shares the common information and operations between channels"""

    __slots__ = (
        "_guild",
        "_channel",
        "_stack"
    )

    def __init__(self, bot: commands.Bot, guild_id: int, channel_id: int, stack: list):
        self._guild = bot.get_guild(guild_id)
        self._channel = self._guild.get_channel(channel_id)
        self._stack = stack


    def data(self):
        return {
            "id": self.id, "name": self.name, "nsfw": self.nsfw, "position": self.position, "jump_url": self.jump_url,
            "created_at": self.created_at, "type": self.type, "send": partial(send, self._stack, self._guild.id, self._channel.id)
        }

    @property
    def id(self) -> int:
        """Id of the channel."""
        return self._channel.id

    @property
    def name(self) -> str:
        """Name of the channel."""
        return self._channel.name

    @property
    def nsfw(self) -> bool:
        """Wether channel is set nsfw."""
        return self._channel.is_nsfw()

    @property
    def position(self) -> int:
        """Position of the channel."""
        return self._channel.position

    @property
    def jump_url(self) -> str:
        """Url to the channel."""
        return self._channel.jump_url

    @property
    def created_at(self) -> int:
        """Channel creation time"""
        return int(self._channel.created_at.timestamp())

    @property
    def type(self) -> str:
        """Channel type."""
        return self._channel.type.name

    def send(self, content: str = "", embeds=None, ephemeral=False, views=None):
        """Send message to a channel"""
        raise NotImplementedError