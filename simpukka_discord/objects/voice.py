from ._guildChannel import GuildChannel
from discord.ext import commands
import discord


class Voice(GuildChannel):
    """Discord voice channel."""
    def __init__(self, bot: commands.Bot, guild_id: int, channel_id: int, stack):
        super().__init__(bot, guild_id, channel_id, stack)

    def data(self):
        return super().data() | {"bitrate": self.bitrate, "user_limit": self.user_limit, "rtc_region": self.rtc_region,
                                 "video_quality_mode": self.video_quality_mode, "slowmode_delay": self.slowmode_delay
                                 }

    @property
    def bitrate(self) -> int:
        """Channel bitrate."""
        return self._channel.bitrate

    @property
    def user_limit(self) -> int:
        """User limit of the channel."""
        return self._channel.user_limit

    @property
    def rtc_region(self) -> str:
        """Region of the voice channel."""
        return self._channel.rtc_region

    @property
    def video_quality_mode(self) -> str:
        """Video quality mode of the voice channel."""
        return self._channel.video_quality_mode.name

    @property
    def slowmode_delay(self) -> int:
        """Slowmode of the channel in seconds."""
        return self._channel.slowmode_delay