from functools import partial

import discord
from discord.ext import commands


class Rule:
    """Discord automod rule object."""
    __slots__ = (
        "_rule",
        "_guild",
        "_bot",
    )

    def __init__(self, bot: commands.Bot, rule: discord.AutoModRule):
        self._guild = rule.guild
        self._rule = rule
        self._bot = bot


    def data(self):
        return {"id": self.id, "name": self.name, "enabled": self.enabled,
                "exempt_role_ids": self.exempt_role_ids, "exempt_channel_ids": self.exempt_channel_ids}
    @property
    def id(self) -> int:
        """Id of the rule."""
        return self._rule.id

    @property
    def name(self) -> str:
        """Name of the rule."""
        return self._rule.name

    @property
    def enabled(self) -> bool:
        """Whether the rule is enabled."""
        return self._rule.enabled
    @property
    def exempt_role_ids(self):
        """List of exempt role ids."""
        return self._rule.exempt_role_ids
    @property
    def exempt_channel_ids(self):
        """list of exempt channel ids."""
        return self._rule.exempt_channel_ids


