import datetime

import validators

from simpukka import filters


class EmbedErrors(Exception):
    """Exception which all embed exceptions inherit from"""
    pass


class InputTooShort(EmbedErrors):
    """Raised when input is too short."""
    pass


def truncate(text, max_length, end="..."):
    if text is None:
        return
    return text[:max_length - len(end)] + end if len(text) > max_length else text


def url_validator(url):
    return filters.url_filter(url) if validators.url(str(url)) else None


class EmbedAuthor:
    def __init__(self, name: str = None, author_url: str = None, author_icon_url: str = None):
        """Embed author proxy."""
        if not len(name) or not isinstance(name, str):
            name = None

        self.name = truncate(name, 256)

        self.url = url_validator(author_url)
        self.author_icon_url = url_validator(author_icon_url)

    def __repr__(self):
        return f"<Embed author(name: {self.name}, author url: {self.url}, author icon url: {self.author_icon_url})>"

    def _to_json(self):
        json_data = {"name": self.name}
        if self.url is not None:
            json_data["url"] = self.url

        if self.author_icon_url is not None:
            json_data["icon_url"] = self.author_icon_url

        return json_data

class EmbedFooter:
    def __init__(self, text: str = None, icon_url: str = None, timestamp: int = None):
        """Embed author proxy."""
        self.text = None
        if text is not None:
            self.text = truncate(text, 2048)

        self.icon_url = url_validator(icon_url)

        self.timestamp = None
        if timestamp is not None:
            self.timestamp = datetime.datetime.fromtimestamp(timestamp).isoformat()
        if timestamp is None and text is None:
            raise EmbedErrors("Footer requires either text or timestamp.")


    def __repr__(self):
        return f"<Embed footer(text: {self.text}, icon url: {self.icon_url}, timestamp: {self.timestamp})>"


    def _to_json(self):
        json_data = {}
        if self.text is not None:
            json_data["text"] = self.text
        if self.icon_url is not None:
            json_data["icon_url"] = self.icon_url

        if self.timestamp is not None:
            json_data["timestamp"] = self.timestamp

        return json_data

class EmbedField:
    def __init__(self, name: str, value: str, inline: bool = False):
        """Embed author proxy."""
        if not len(name) or not isinstance(name, str):
            raise InputTooShort("Name must be a string with at least one character and max 256 characters.")
        self.name = truncate(name, 256)

        if not len(value) or not isinstance(value, str):
            raise InputTooShort("value must be a string with at least one character and max 1024 characters.")
        self.value = truncate(value, 1024)

        self.inline = inline
        if not isinstance(inline, bool):
            self.inline = False

    def __repr__(self):
        return f"<Embed field(name: {self.name}, value: {self.value})>"

    def _to_json(self):
        return {"name": self.name, "inline": self.inline, "value": self.value}

class EmbedImages:
    def __init__(self):
        self.thumbnail = None
        self.image = None

    def __repr__(self):
        return f"<Embed images(image: {self.image}, thumbnail: {self.thumbnail})>"



class Embed:
    """
    Filter respecting simpukka safe Embed class. Malformed urls are ignored and longer than allowed input is truncated.
    Some Invalid inputs will raise errors if the automatic fix would be unreasonably aggressive. There is global
    limit 6000 combined characters.
    """

    def __init__(self, title: str = None, description: str = None, color: int = None, url: str = None):
        self.title = truncate(title, 256)
        self.description = truncate(description, 4096)
        self.color = color
        self.url = url_validator(url)
        self.fields = []
        self.author = None
        self.footer = None
        self.images = EmbedImages()

    def set_author(self, name: str, author_url: str = None, author_icon_url: str = None):
        """Set author for the embed. """
        self.author = EmbedAuthor(name, author_url, author_icon_url)
        return ""

    def add_field(self, name: str, value: str, inline: bool = False):
        """Add field to the embed. Up to 25 fields can exist."""
        # Refuse to create more fields if limit has been reached.
        if len(self.fields) > 25:
            return "Field limit"

        self.fields.append(EmbedField(name, value, inline))
        return ""

    def set_thumbnail(self, thumbnail_url: str):
        """Set thumbnail for the embed. Thumbnail is the smaller image near top."""
        self.images.thumbnail = url_validator(thumbnail_url)
        return ""

    def set_image(self, image_url: str):
        """Set image for the embed. Image is the larger bottom middle image."""
        self.images.image = url_validator(image_url)
        return ""

    def set_footer(self, text=None, icon_url = None, timestamp = None):
        """Set footer for the embed."""
        self.footer = EmbedFooter(text, icon_url, timestamp)
        return ""

    def _to_json(self):
        embed_json = {}

        if self.title is not None:
            embed_json["title"] = self.title

        if self.description is not None:
            embed_json["description"] = self.description

        if self.color is not None:
            embed_json["color"] = self.color

        if self.url is not None:
            embed_json["url"] = self.url

        if self.author is not None:
            embed_json["author"] = self.author._to_json()

        if self.footer is not None:
            embed_json["footer"] = self.footer._to_json()

        if self.images.thumbnail is not None:
            embed_json["thumbnail"] = {"url": self.images.thumbnail}

        if self.images.image is not None:
            embed_json["image"] = {"url": self.images.image}


        if len(self.fields):
            embed_json["fields"] = []
            for x in self.fields:
                embed_json["fields"].append(x._to_json())

        return embed_json

if __name__ == '__main__':
    embed = Embed()
