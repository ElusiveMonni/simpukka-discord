
from discord.ext import commands
import discord


class Role:

    __slots__ = (
        "_guild",
        "_role",
        "_bot",
        "_stack"
    )

    def __init__(self, bot: commands.Bot, guild_id: int, role_id: int, stack, override=None):
        self._guild = bot.get_guild(guild_id)
        self._role = self._guild.get_role(role_id) if override is None else override
        self._stack = stack
        self._bot = bot

    def data(self):
        return {"name": self.name, "id": self.id, "hoist": self.hoist, "managed": self.managed,
                "mentionable": self.mentionable, "is_default_role": self.is_default_role,
                "is_bot_managed": self.is_bot_managed, "is_premium_subscriber": self.is_premium_subscriber,
                "is_integration": self.is_integration, "is_assignable": self.is_assignable, "color": self.color,
                "icon": self.icon, "created_at": self.created_at, "mention": self.mention}

    @property
    def name(self) -> str:
        """Role name."""
        return self._role.name

    @property
    def id(self) -> int:
        """Role id."""
        return self._role.id

    @property
    def hoist(self) -> bool:
        """Whether role should be displayed separately."""
        return self._role.hoist

    @property
    def managed(self) -> bool:
        """Whether role is managed by third party application."""
        return self._role.managed

    @property
    def mentionable(self) -> bool:
        """Whether role is mentionable."""
        return self._role.mentionable

    @property
    def is_default_role(self) -> bool:
        """Whether role is default role."""
        return self._role.is_default()

    @property
    def is_bot_managed(self) -> bool:
        """Whether role is managed by a bot."""
        return self._role.is_bot_managed()

    @property
    def is_premium_subscriber(self) -> bool:
        """Whether role is booster role of a server."""
        return self._role.is_premium_subscriber()

    @property
    def is_integration(self) -> bool:
        """Whether role is managed by integration."""
        return self._role.is_premium_subscriber()

    @property
    def is_assignable(self) -> bool:
        """Whether role can be added and removed by a bot."""
        return self._role.is_premium_subscriber()

    @property
    def color(self) -> int:
        """Color of the role"""
        return self._role.color.value

    @property
    def icon(self) -> str:
        """Icon of the role"""
        if self._role.unicode_emoji is not None:
            return self._role.unicode_emoji
        elif self._role.icon is not None:
            return self._role.icon.url

    @property
    def created_at(self) -> int:
        """Creation date of the role as unix timestamp."""
        return int(self._role.created_at.timestamp())

    @property
    def mention(self) -> str:
        """Mention string of the role."""
        return self._role.mention


