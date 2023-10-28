

class Ctx:
    """Context class for Simpukka runtime. Tells context and metadata. Metadata like who is author of the action,
    what triggered it, where it will send the result. It also allows you to add embed to the result message."""
    def __init__(self, guild_id, channel_id, author_id):
        self.send_message = True
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.author_id = author_id
        self.embed = None

    def set_embed(self, embed):
        """Set embed which will be sent to with the result message. Ensure embed is edited set before calling this.
        Changes after won't show up."""
        self.embed = embed
        return ""

    def disable_message(self):
        """Disable sending the result message to the context channel."""
        self.send_message = False
        return ""

    @property
    def message_state(self) -> bool:
        """Gets the state of whether the message sending has been disabled."""
        return self.send_message

    def get_embed(self):
        """Get the currently set embed."""
        return self.embed