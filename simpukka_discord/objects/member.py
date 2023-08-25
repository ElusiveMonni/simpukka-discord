from functools import partial

from discord.ext import commands
import discord
from simpukka_discord.objects.user import User
from simpukka_discord.objects.role import Role

from simpukka_discord.object_utils import ban, unban, kick, timeout, untimeout, add_role, remove_role, set_nickname


class Member(User):

    __slots__ = (
        "_member",
        "_guild",
        "_bot",
        "_stack"
    )

    def __init__(self, bot: commands.Bot, guild_id: int, member_id: int, stack: list):
        super().__init__(bot, member_id)
        self._guild = bot.get_guild(guild_id)
        self._member = self._guild.get_member(member_id)
        self._bot = bot
        self._stack = stack

    def data(self):
        return super().data() | {"pending": self.pending, "nick": self.nick, "created_at": self.created_at,
                                 "joined_at": self.joined_at, "timeout_until": self.timeout_until, "color": self.color,
                                 "top_role": self.top_role, "roles": self.roles,
                                 "ban": partial(ban, self._stack, self._guild.id, self._member.id),
                                 "unban": partial(unban, self._stack, self._guild.id, self._member.id),
                                 "kick": partial(kick, self._stack, self._guild.id, self._member.id),
                                 "timeout": partial(timeout, self._stack, self._guild.id, self._member.id),
                                 "untimeout": partial(untimeout, self._stack, self._guild.id, self._member.id),
                                 "add_role": partial(add_role, self._stack, self._guild.id, self._member.id),
                                 "remove_role": partial(remove_role, self._stack, self._guild.id, self._member.id),
                                 "set_nickname": partial(set_nickname, self._stack, self._guild.id, self._member.id),
                                 }

    @property
    def pending(self) -> bool:
        """Whether member is pending verification."""
        return self._member.pending

    @property
    def nick(self) -> str:
        """Nickname of the member."""
        return self._member.nick

    @property
    def created_at(self) -> int:
        """Creation date of members account."""
        return int(self._member.created_at.timestamp())

    @property
    def joined_at(self) -> int:
        """Join date of the member."""
        return int(self._member.created_at.timestamp())

    @property
    def timeout_until(self) -> int:
        """Join date of the member."""
        if self._member.timed_out_until is not None:
            return int(self._member.timed_out_until.timestamp())

    @property
    def color(self) -> int:
        """Color of the member. Determined from top role."""
        return self._member.color.value

    @property
    def top_role(self):
        return Role(self._bot, self._guild.id, self._member.top_role.id, self._stack).data()

    @property
    def roles(self):
        """List of all the role's member has."""
        return [
            Role(self._bot, self._guild.id, r.id, self._stack).data()
            for r in self._guild.roles
        ]

    @property
    def is_admin(self) -> True:
        """Whether the person is admin."""
        return self._member.resolved_permissions.administrator

    def ban(self, reason: str = "", delete_message_seconds: int = None):
        """Ban a user from the guild."""
        raise NotImplementedError

    def unban(self, reason: str):
        """Unban a user from the guild."""
        raise NotImplementedError

    def kick(self, reason: str = ""):
        """Kick a user from the guild."""
        raise NotImplementedError

    def timeout(self, until, reason=""):
        """Timeout the user. Until (time) in seconds."""
        raise NotImplementedError

    def untimeout(self, reason=""):
        """Untimeout the user."""
        raise NotImplementedError

    def add_role(self, role_id: str, reason: str = ""):
        """Add a role to the user."""
        raise NotImplementedError

    def remove_role(self, role_id: str, reason: str = ""):
        """Remove a role to the user."""
        raise NotImplementedError

    def set_nickname(self, nickname: str):
        """Function to set nickname to the member"""
        raise NotImplementedError