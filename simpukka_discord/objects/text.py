from functools import partial

import discord

from ._guildChannel import GuildChannel
from .thread import Thread
from discord.ext import commands



class Text(GuildChannel):
    def __init__(self, bot: commands.Bot, guild_id: int, channel_id: int, stack: list):
        super().__init__(bot, guild_id, channel_id, stack)
        self._stack = stack
        self._bot = bot

    def data(self):
        return super().data() | {"topic": self.topic, "default_auto_archive_duration": self.default_auto_archive_duration,
                                 "default_thread_slowmode_delay": self.default_thread_slowmode_delay,
                                 "is_news": self.is_news, "slowmode_delay": self.slowmode_delay,
                                 "threads": self.threads
                                 }

    @property
    def topic(self) -> str:
        """Topic of the channel."""
        return self._channel.topic

    @property
    def default_auto_archive_duration(self) -> int:
        """Default auto-archive duration of channel."""
        return self._channel.default_auto_archive_duration

    @property
    def default_thread_slowmode_delay(self) -> int:
        """Default thread slowmode."""
        return self._channel.default_thread_slowmode_delay

    @property
    def is_news(self) -> bool:
        """Whether the channel is set as news channel."""
        return self._channel.is_news()

    @property
    def slowmode_delay(self) -> int:
        """Slow mode of the channel."""
        return self._channel.slowmode_delay

    @property
    def threads(self) -> list[Thread]:
        """Returns list of threads in the channel |list|threads"""
        return [
            Thread(self._bot, self._guild.id, self._channel.id, t.id, self._stack).data()
            for t in self._channel.threads
        ]

    def get_thread(self, thread_id: int) -> Thread:
        """Get thread with id |thread"""
        return Thread(self._bot, self._guild.id, self._channel.id, thread_id, self._stack).data()
