#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import asyncio
import random


client = discord.Client()
app_key = ""
data = {}
emojis = ["🎄", "🎁", "🔔", "⛄", "🔥", "🌟", "🎅", "🦌"]


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------------")


@client.event
async def on_message(message):
    if message.server is not None:
        if message.content.startswith("make it snow") and message.author.permissions.administrator:
            channels = {}
            names = {}
            for channel in message.server.channels:
                channels[channel.id] = channel.name
                emoji0 = random.choice(emojis)
                emoji1 = random.choice(emojis)
                await client.edit_channel(channel, name=f"{emoji0}{channel.name}{emoji1}")

            addserverdata(message.server.id, channels, names)

        if message.content.startswith("reverse") and message.author.permissions.administrator:
            for channel in message.server.channels:
                oldname = data[message.server.id]["channels"][channel.id]
                await client.edit_channel(channel, name=f"{oldname}")


@client.event
async def on_server_remove(server):
    del (data, server.id)


def addserverdata(server, channels, names):
    data[server] = {"channels": channels, "names": names}
    print(data)


client.run(app_key)
