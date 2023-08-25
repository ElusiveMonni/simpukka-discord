
from discord.ext import commands
import discord

class Emoji:
    """Emoji of a discord server."""
    __slots__ = (
        "_guild",
        "_emoji",
    )

    def __init__(self, bot: commands.Bot, guild_id: int, emoji_id: int):
        self._guild = bot.get_guild(guild_id)
        self._emoji = self._guild.get_emoji(emoji_id)

    def data(self):
        return {"id": self.id, "name": self.name, "require_colons": self.require_colons, "animated": self.animated,
                "available": self.available, "url": self.url, "created_at": self.created_at}

    @property
    def id(self) -> int:
        """Id of the emoji."""
        return self._emoji.id

    @property
    def name(self) -> str:
        """Name of the emoji."""
        return self._emoji.name

    @property
    def require_colons(self) -> bool:
        """Whether the emoji requires colons."""
        return self._emoji.require_colons

    @property
    def animated(self) -> bool:
        """Whether the emoji is animated."""
        return self._emoji.animated

    @property
    def managed(self) -> bool:
        """Whether the emoji is managed by third party integration."""
        return self._emoji.managed

    @property
    def available(self) -> bool:
        """Whether the emoji is currently available."""
        return self._emoji.available

    @property
    def url(self) -> str:
        """Url of the emoji image."""
        return self._emoji.url

    @property
    def created_at(self) -> int:
        """Creation date of the emoji as unix timestamp."""
        return int(self._emoji.created_at.timestamp())
