from functools import partial

from discord.ext import commands
import discord

from simpukka_discord.objects import emoji, sticker, stage, voice, text, member, role, thread, forum
from simpukka_discord.object_utils import ban, unban, kick


import typing

class Guild:
    """Simpukka guild data object with majority of safe to expose data."""
    __slots__ = (
        "_bot",
        "_guild",
        "_stack"
    )

    def __init__(self, bot: commands.Bot, guild_id: int, stack: list):
        self._bot = bot
        self._guild = self._bot.get_guild(guild_id)
        self._stack = stack

    def data(self):
        return {
            "name": self._guild.name, "afk_timeout": self.afk_timeout, "id": self.id,
            "max_video_channel_users": self.max_stage_video_users, "description": self.description,
            "vanity_url_code": self.vanity_url_code, "premium_tier": self.premium_tier,
            "premium_subscription_count": self.premium_subscription_count, "nsfw_level": self.nsfw_level,
            "max_stage_video_users": self.max_stage_video_users, "rules_channel": self.rules_channel,
            "icon": self.icon, "banner": self.banner, "splash": self.splash, "discovery_splash": self.discovery_splash,
            "created_at": self.created_at,
            "members": self.members, "channels": self.channels, "threads": self.threads, "roles": self.roles,

            "premium_subscriber_role": self.premium_subscriber_role, "premium_subscribers": self.premium_subscribers,

            "emojis": self.emojis,
            "stickers": self.stickers,

            "ban": partial(ban, self._stack, self._guild.id),
            "unban": partial(unban, self._stack, self._guild.id),
            "kick": partial(kick, self._stack, self._guild.id),
            "afk_channel": self.afk_channel, "system_channel": self.system_channel,
            "owner": self.owner,

            "find_snowflake": self.find_snowflake
        }

    @property
    def name(self) -> str:
        """Name of the guild."""
        return self._guild.name

    @property
    def afk_timeout(self) -> int:
        """Afk timeout of the guild."""
        return self._guild.afk_timeout

    @property
    def id(self) -> int:
        """Id of the guild."""
        return self._guild.id

    @property
    def max_video_channel_users(self) -> int:
        """Max people in video channel."""
        return self._guild.max_video_channel_users

    @property
    def description(self) -> str:
        """Description of the guild."""
        return self._guild.description

    @property
    def vanity_url_code(self) -> str:
        """Vanity URL code of the guild."""
        return self._guild.vanity_url_code

    @property
    def premium_tier(self) -> int:
        """Boost level of the guild."""
        return self._guild.premium_tier

    @property
    def premium_subscription_count(self) -> int:
        """Booster count of the guild."""
        return self._guild.premium_subscription_count

    @property
    def nsfw_level(self) -> str:
        """Nsfw level of the guild."""
        return self._guild.nsfw_level.name

    @property
    def max_stage_video_users(self) -> int:
        """Maximum amount of video users in stage."""
        return self._guild.premium_subscription_count

    @property
    def afk_channel(self) -> stage.Stage|voice.Voice:
        """Afk channel set for guild. |channel"""
        if self._guild.afk_channel is None:
            return None
        if self._guild.afk_channel.type == "voice":
            return voice.Voice(self._bot, self._guild.id, self._guild.afk_channel.id, self._stack).data()
        elif self._guild.afk_channel.type == "stage":
            return stage.Stage(self._bot, self._guild.id, self._guild.afk_channel.id, self._stack).data()

    @property
    def system_channel(self) -> text.Text:
        """System channel set for guild. |channel"""
        if self._guild.system_channel is None:
            return None
        return text.Text(self._bot, self._guild.id, self._guild.system_channel.id, self._stack).data()

    @property
    def rules_channel(self) -> text.Text:
        """Rules channel set for guild. |channel"""
        if self._guild.rules_channel is None:
            return None
        return text.Text(self._bot, self._guild.id, self._guild.rules_channel.id, self._stack).data()

    @property
    def icon(self) -> str:
        """Icon url of the guild."""
        if self._guild.icon is not None:
            return self._guild.icon.url

    @property
    def banner(self) -> str:
        """banner url of the guild."""
        if self._guild.banner is not None:
            return self._guild.banner.url

    @property
    def splash(self) -> str:
        """Splash url of the guild."""
        if self._guild.splash is not None:
            return self._guild.splash.url

    @property
    def discovery_splash(self) -> str:
        """Discovery splash url of the guild."""
        if self._guild.discovery_splash is not None:
            return self._guild.discovery_splash.url

    @property
    def created_at(self) -> int:
        """Creation time of the guild as unix timestamp"""
        return int(self._guild.created_at.timestamp())

    @property
    def owner(self) -> dict:
        """Owner of the guild. |member"""
        return member.Member(self._bot, self._guild.id, self._guild.owner.id, self._stack).data()

    @property
    def roles(self) -> list[dict]:
        """List of roles that exist in the guild.|list|role """
        return [
            role.Role(self._bot, self._guild.id, r.id, self._stack).data()
            for r in self._guild.roles
        ]

    @property
    def premium_subscriber_role(self):
        """Nitro role of the guild. |role"""
        if self._guild.premium_subscriber_role is not None:
            return role.Role(self._bot, self._guild.id, self._guild.premium_subscriber_role.id, self._stack).data()

    @property
    def premium_subscribers(self):
        """List of nitro boosters. |list|member"""
        return [
            member.Member(self._bot, self._guild.id, m.id, self._stack).data()
            for m in self._guild.premium_subscribers
        ]

    @property
    def members(self):
        """List of members in the guild. |list|member"""
        return [
            member.Member(self._bot, self._guild.id, m.id, self._stack).data()
            for m in self._guild.members
        ]

    @property
    def channels(self):
        """List of channels in the guild. |list|channel"""
        channels = []
        for c in self._guild.channels:
            if c.type.name == "text":
                channels.append(text.Text(self._bot, self._guild.id, c.id, self._stack).data())
            elif c.type.name == "forum":
                channels.append(forum.Forum(self._bot, self._guild.id, c.id, self._stack).data())
            elif c.type.name == "voice":
                channels.append(voice.Voice(self._bot, self._guild.id, c.id, self._stack).data())
            elif c.type.name == "stage_voice":
                channels.append(stage.Stage(self._bot, self._guild.id, c.id, self._stack).data())
        return channels

    @property
    def threads(self):
        """List of threads in a guild. |list|thread"""
        return [
            thread.Thread(self._bot, self._guild.id, t.parent_id, t.id, self._stack).data()
            for t in self._guild.threads
        ]

    @property
    def emojis(self) -> typing.Iterable[emoji.Emoji]:
        """List of emojis in a guild. |list|emoji"""
        return [
            emoji.Emoji(self._bot, self._guild.id, e.id).data()
            for e in self._guild.emojis
        ]

    @property
    def stickers(self) -> typing.Iterable[sticker.Sticker]:
        """List of sticker in a guild. |list|sticker"""
        return [
            sticker.Sticker(self._bot, self._guild.id, s).data()
            for s in self._guild.stickers
        ]

    def ban(self, member_id, reason="", time=None):
        """Bans a member from the guild."""
        pass

    def unban(self, member_id, reason=""):
        """Unbans a member from the guild."""
        pass

    def kick(self, member_id, reason=""):
        """Kicks a member from the guild."""
        pass

    @staticmethod
    def find_snowflake(data, snowflake: int|str, key: str="id"):
        """Helper function which loops list of objects and returns one with the same snowflake."""
        for x in data:
            try:
                if int(x[key]) == int(snowflake):
                    return x
            except KeyError:
                return None
