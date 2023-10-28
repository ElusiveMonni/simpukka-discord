from discord.ext import commands
import discord
from simpukka_discord.objects.user import User

class Invite:
    """Information about discord invite."""
    __slots__ = (
        "_invite",
        "_bot"
    )

    def __init__(self, bot: commands.Bot, invite: discord.Invite):
        self._invite: discord.Invite = invite
        self._bot = bot

    def data(self):
        return {
            "max_age": self.max_age, "max_uses": self.max_uses, "code": self.code, "revoked": self.revoked,
            "created_at": self.created_at, "uses": self.uses, "temporary": self.temporary, "inviter": self.inviter,
            "url": self.url
        }

    @property
    def max_age(self) -> int:
        """Max age of invite"""
        return self._invite.max_age

    @property
    def max_uses(self) -> int:
        """Max uses of invite"""
        return self._invite.max_uses

    @property
    def code(self) -> str:
        """Identifier of the invite."""
        return self._invite.code

    @property
    def revoked(self) -> bool:
        """Indicates whether invite has been revoked or not."""
        return self._invite.revoked

    @property
    def created_at(self) -> int:
        """Unix timestamp of creation time."""
        if self._invite.created_at is not None:
            return round(self._invite.created_at.timestamp())

    @property
    def temporary(self) -> bool:
        """Indicates whether the invite provides temporary membership."""
        return self._invite.temporary

    @property
    def uses(self) -> int:
        """Uses left for the invite."""
        return self._invite.uses
    @property
    def inviter(self) -> dict:
        """Creator of the invite"""
        if self._invite.inviter is not None:
            return User(self._bot, user_override=self._invite.inviter).data()
    @property
    def url(self) -> str:
        """Url of the invite"""
        return self._invite.url