from discord.ext import commands
from functools import partial
from simpukka_discord.object_utils import thread_delete, thread_remove_user, thread_add_user


class Thread:
    """Class which shares the common information and operations between channels"""

    __slots__ = (
        "_guild",
        "_channel",
        "_thread",
        "_stack"
    )

    def __init__(self, bot: commands.Bot, guild_id: int, channel_id: int, thread_id: int, stack: list):
        self._guild = bot.get_guild(guild_id)
        self._channel = self._guild.get_channel(channel_id)
        self._thread = self._channel.get_thread(thread_id)
        self._stack = stack

    def data(self):
        return {
            "name": self.name, "id": self.id, "parent_id": self.parent_id, "owner_id": self.owner_id,
            "slowmode_delay": self.slowmode_delay, "message_count": self.message_count, "member_count": self.member_count,
            "archived": self.archived, "locked": self.locked, "invitable": self.invitable, "archiver_id": self.archiver_id,
            "auto_archive_duration": self.auto_archive_duration, "mention": self.mention, "jump_url": self.jump_url,
            "is_private": self.is_private, "is_news": self.is_news, "created_at": self.created_at,
            "thread_delete": partial(thread_delete, self._stack, self._guild.id, self._thread.id),
            "thread_remove_user": partial(thread_remove_user, self._stack, self._guild.id, self._thread.id),
            "thread_add_user": partial(thread_add_user, self._stack, self._guild.id, self._thread.id)
        }

    @property
    def name(self) -> str:
        """Name of the thread."""
        return self._thread.name

    @property
    def id(self) -> int:
        """Id of the thread."""
        return self._thread.id

    @property
    def parent_id(self) -> int:
        """Parent id of the thread."""
        return self._thread.parent_id

    @property
    def owner_id(self) -> int:
        """Owner id of the thread."""
        return self._thread.owner_id

    @property
    def slowmode_delay(self) -> int:
        """Slowmode delay of the thread."""
        return self._thread.slowmode_delay

    @property
    def message_count(self) -> int:
        """An approximate number of messages in this thread."""
        return self._thread.message_count

    @property
    def member_count(self) -> int:
        """Member count of this thread."""
        return self._thread.member_count

    @property
    def archived(self) -> bool:
        """Whether the thread is archived."""
        return self._thread.archived

    @property
    def locked(self) -> bool:
        """Whether the thread is locked."""
        return self._thread.locked

    @property
    def invitable(self) -> bool:
        """Whether non moderator can add people to thread."""
        return self._thread.invitable

    @property
    def archiver_id(self) -> int:
        """Person who archived the thread."""
        return self._thread.archiver_id

    @property
    def auto_archive_duration(self) -> int:
        """Default archive duration of thread."""
        return self._thread.auto_archive_duration

    @property
    def mention(self) -> str:
        """Mention of the thread."""
        return self._thread.mention

    @property
    def jump_url(self) -> str:
        """jump url of the thread."""
        return self._thread.jump_url

    @property
    def is_private(self) -> bool:
        """Whether the thread is private."""
        return self._thread.is_private()

    @property
    def is_news(self) -> bool:
        """Whether the thread is news thread."""
        return self._thread.is_news()

    @property
    def is_nsfw(self) -> bool:
        """Whether the thread is set as nsfw."""
        return self._thread.is_nsfw()

    @property
    def created_at(self) -> int:
        """Channel creation time"""
        return int(self._channel.created_at.timestamp())

    def add_user(self, user_id: int):
        """Add user to a thread."""
        raise NotImplementedError

    def remove_user(self, user_id: int):
        """Remove user from a thread."""
        raise NotImplementedError

    def delete(self):
        """Delete the thread."""
        raise NotImplementedError
