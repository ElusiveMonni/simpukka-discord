from .voice import Voice
from .member import Member

from discord.ext import commands
import discord


class Stage(Voice):
    def __init__(self, bot: commands.Bot, guild_id: int, channel_id: int, stack: list):
        super().__init__(bot, guild_id, channel_id, stack)
        self._stack = stack
        self._bot = bot

    def data(self):
        return super().data() | {"moderators": self.moderators, "requesting_to_speak": self.requesting_to_speak,
                                 "speakers": self.speakers, "listeners": self.listeners}

    @property
    def moderators(self):
        """Returns list of stage moderators |list|member"""
        return [
            Member(self._bot, self._guild.id, m.id, self._stack).data()
            for m in self._channel.moderators
        ]

    @property
    def requesting_to_speak(self):
        """Returns list of people requesting to speak |list|member"""
        return [
            Member(self._bot, self._guild.id, m.id, self._stack).data()
            for m in self._channel.requesting_to_speak
        ]

    @property
    def speakers(self):
        """Returns list of people currently allowed to speak |list|member"""
        return [
            Member(self._bot, self._guild.id, m.id, self._stack).data()
            for m in self._channel.speakers
        ]

    @property
    def listeners(self):
        """Returns list of people currently listening |list|member"""
        return [
            Member(self._bot, self._guild.id, m.id, self._stack).data()
            for m in self._channel.listeners
        ]
