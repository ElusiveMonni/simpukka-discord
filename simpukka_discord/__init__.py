import pprint
import typing
import math
import asyncio

from discord.ext import commands
from attrs import define
import discord
import multiprocessing
from multiprocessing.managers import BaseManager

from simpukka import template
from simpukka import utils
from simpukka_discord.objects.user import User
from simpukka_discord.objects.guild import Guild
from simpukka_discord.objects.member import Member
from simpukka_discord.objects.embed import Embed
from simpukka_discord.objects.ctx import Ctx

from simpukka_discord.objects.role import Role

from simpukka_discord.objects.voice import Voice
from simpukka_discord.objects.stage import Stage
from simpukka_discord.objects.text import Text
from simpukka_discord.objects.forum import Forum

from warnings import warn

class DiscordErrors(Exception):
    pass

class NoRequestsLeft(DiscordErrors):
    pass

@define(frozen=False, slots=False)
class DiscordResult:
    discord_api_calls: int = 0
    error = None
    ctx = None


class DiscordBindings(utils.SimpukkaPlugin):
    def __init__(self, data=None, pre_hook_func=None, after_hook_func=None, **kwargs):
        self.stack = []
        self.bot = kwargs.get("bot")

        BaseManager.register('Ctx', Ctx)
        class_manager = BaseManager()
        class_manager.start()
        ctx = class_manager.Ctx(kwargs.get("guild_id"), kwargs.get("channel_id"), kwargs.get("user_id"))

        manager = multiprocessing.Manager()
        stack = manager.list()

        self.stack = stack



        self.ctx = ctx


        discord_objects = {"embed": Embed, "ctx": ctx}

        if kwargs.get("user_id") is not None:
            discord_objects["user"] = User(self.bot, kwargs["user_id"]).data()

        if kwargs.get("guild_id") is not None:

            discord_objects["guild"] = Guild(self.bot, kwargs["guild_id"], stack).data()

            if kwargs.get("user_id") is not None:
                discord_objects["member"] = Member(self.bot,  kwargs["guild_id"], kwargs["user_id"], stack).data()

            if kwargs.get("role_id") is not None:
                discord_objects["member"] = Role(self.bot,  kwargs["guild_id"], kwargs["role_id"], stack).data()

            if kwargs.get("channel_id") is not None:
                channel = self.bot.get_guild(kwargs["guild_id"]).get_channel(kwargs["channel_id"])
                if channel.type.name == "text":
                    discord_objects["channel"] = Text(self.bot, kwargs["guild_id"], channel.id, stack).data()
                elif channel.type.name == "forum":
                    discord_objects["channel"] = Forum(self.bot, kwargs["guild_id"], channel.id, stack).data()
                elif channel.type.name == "voice":
                    discord_objects["channel"] = Voice(self.bot, kwargs["guild_id"], channel.id, stack).data()
                elif channel.type.name == "stage_voice":
                    discord_objects["channel"] = Stage(self.bot, kwargs["guild_id"], channel.id, stack).data()


        super(DiscordBindings, self).__init__(None, pre_hook_func, after_hook_func)

        self.data = discord_objects

    async def async_after_hook(self, res):
        discord_res = DiscordResult(discord_api_calls=len(self.stack))
        discord_res.ctx = self.ctx

        res.discord = discord_res

        if len(self.stack) > self.kwargs.get("requests_left", math.inf):
            discord_res.error = NoRequestsLeft("Out of web requests.")
            return
        for x in self.stack:
            try:
                await x[0](self.bot, *x[1])
            except Exception as e:
                print(e)

    def after_hook(self, res):
        if self.kwargs.get("silence_non_async", False):
            warn("Only async_start supports discord actions. This can be disabled with providing flag 'silence_non_async'=True")


def register(**kwargs):
    print("Register", kwargs)
    return DiscordBindings(**kwargs)

class Main(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned,
                         intents=discord.Intents(guilds=True, members=True, messages=True),
                         application_id=962052721354084413)


if __name__ == "__main__":
    bot = Main()


    @bot.listen()
    async def on_ready():
        print("Logged in as:", bot.user.name)
        '''

        t = template.Template("""
        (% set e = embed() %)
        ((channel.send("HELLO", embed=e)))
        """, bot=bot)
        r = await t.async_start()
        print("DONE", r)'''

    @bot.command()
    @commands.is_owner()
    async def simpukka(ctx: commands.Context, *, template_str):

        t = template.Template(template_str, bot=bot, guild_id=ctx.guild.id, user_id=ctx.author.id, filter_level=template.FilterLevel.disabled)
        r = await t.async_start()


        embed = r.discord.ctx.get_embed()

        if r.discord.ctx.get_message_state():
            try:
                embed = discord.Embed.from_dict(embed._to_json())
            except Exception as e:
                print("ERROR", e)
                embed = None

            await ctx.channel.send("Simpukka render\n" + "-"*20 + "\n" + r.result, embed=embed)

        # Debug mode related stuff
        embed = discord.Embed(title="Debug information", description=f"`{template_str}`", colour=0x850f62)

        embed.add_field(name="Render error", value=r.error, inline=True)
        embed.add_field(name="Discord error", value=r.discord.error, inline=True)
        embed.add_field(name="Runtime usage", value=f"**Runtime**: {round(r.time_taken, 5)} s\n**Peak ram use**: {r.peak_ram / 1024 ** 2} Mb\n**Api_calls**: {r.api_calls}", inline=False)

        await ctx.channel.send(embed=embed)

    bot.run("OTYyMDUyNzIxMzU0MDg0NDEz.Gui8i3.7Yf7dBOTsXVKsrzZpmLi9akMgtv6B_yCaYb3Mo")
