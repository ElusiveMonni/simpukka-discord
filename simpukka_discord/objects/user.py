from discord.ext import commands
import discord


class User:

    __slots__ = (
        "_user",
    )

    def __init__(self, bot: commands.Bot, user_id: int):
        self._user: discord.User = bot.get_user(user_id)

    def data(self):
        return {
            "id": self.id, "name": self.name, "global_name": self.global_name, "bot": self.bot,
            "mention": self.mention, "avatar_url": self.avatar_url, "display_name": self.display_name,
            "display_avatar": self.display_avatar
        }

    @property
    def id(self) -> int:
        """Id of the user."""
        return self._user.id

    @property
    def name(self) -> str:
        """Name of the user."""
        return self._user.name

    @property
    def global_name(self) -> str:
        """Global username. One used to add you as friend."""
        return self._user.global_name

    @property
    def bot(self) -> bool:
        """Whether user is a bot"""
        return self._user.bot

    @property
    def display_name(self) -> str:
        """Display name of the user"""
        return self._user.display_name

    @property
    def mention(self) -> str:
        """Mention string for mentioning the user."""
        return self._user.mention

    @property
    def avatar_url(self) -> str:
        """Global avatar of the user"""
        if self._user.avatar is not None:
            return self._user.avatar.url

    @property
    def display_avatar(self) -> str:
        """Avatar thats displayed on discord."""
        if self._user.display_avatar is not None:
            return self._user.display_avatar.url
