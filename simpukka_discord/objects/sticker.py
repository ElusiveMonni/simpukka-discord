
from discord.ext import commands
import discord


class Sticker:
    """Sticker of a discord server."""
    __slots__ = (
        "_guild",
        "_sticker",
    )

    def __init__(self, bot: commands.Bot, guild_id: int, sticker: discord.Sticker):
        self._guild = bot.get_guild(guild_id)
        self._sticker = sticker

    def data(self):
        return {
            "id": self.id, "name": self.name, "description": self.description, "url": self.url, "created_at": self.created_at
        }

    @property
    def id(self) -> int:
        """Id of the sticker."""
        return self._sticker.id

    @property
    def name(self) -> str:
        """Name of the sticker."""
        return self._sticker.name

    @property
    def description(self) -> str:
        """Description of the sticker."""
        return self._sticker.description

    @property
    def url(self) -> str:
        """Url of the sticker image."""
        return self._sticker.url

    @property
    def created_at(self) -> int:
        """Creation date of the sticker in unix timestamp."""
        return int(self._sticker.created_at.timestamp())
