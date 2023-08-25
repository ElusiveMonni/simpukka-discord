import discord
import datetime
import utils

class Embed:
    def __init__(self, title=None, color=None, url=None, description=None, time=None):
        if description is None and title is None:
            title = "Description or Title required."
        timestamp = datetime.datetime.fromtimestamp(time)
        self.embed = discord.Embed(title=title, color=color, url=utils.clean_url_filter(url), description=description, timestamp=timestamp)

    def field_count(self) -> int:
        return len(self.embed.fields)

    def clear_fields(self):
        self.embed.clear_fields()

    def set_footer(self, icon_url: str, text: str):
        self.embed.set_footer(icon_url=utils.clean_url_filter(icon_url), text=text)

    def set_thumbnail(self, thumbnail_url):
        self.embed.set_thumbnail(url=utils.clean_url_filter(thumbnail_url))

    def set_author(self, name: str, url: str, icon_url: str):
        self.embed.set_author(name=name, url=url, icon_url=icon_url)

    def set_image(self, image_url):
        self.embed.set_image(url=utils.clean_url_filter(image_url))

    def add_field(self, name=None, value=None):
        self.embed.add_field(name=name, value=value)