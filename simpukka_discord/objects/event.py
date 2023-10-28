import discord
from discord.ext import commands


class Event:
    """Discord event object."""
    __slots__ = (
        "_event",
        "_guild",
        "_bot",
    )

    def __init__(self, bot: commands.Bot, guild_id: int, event: discord.ScheduledEvent):
        self._guild = bot.get_guild(guild_id)
        self._event: discord.ScheduledEvent = event
        self._bot = bot

    def data(self):
        return {"id": self.id, "name": self.name, "description": self.description, "start_time": self.start_time,
                "end_time": self.end_time, "url": self.url}

    @property
    def id(self) -> int:
        """Id of the event."""
        return self._event.id

    @property
    def name(self) -> str:
        """Name of the event."""
        return self._event.name

    @property
    def description(self) -> str:
        """Description of the event."""
        return self._event.description

    @property
    def start_time(self) -> int:
        """Start time of the event"""
        if self._event.start_time:
            return round(self._event.start_time.timestamp())

    @property
    def end_time(self) -> int:
        """End time of the event"""
        if self._event.end_time:
            return round(self._event.end_time.timestamp())

    @property
    def url(self) -> str:
        """Url of the event."""
        return self._event.url