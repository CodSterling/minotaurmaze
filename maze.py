import discord
from discord.ext import commands
import random
import asyncio
import json
import flask
from flask import Flask

# Choose your character, randomly assigned Minotaurs, Mazes
# Minotaur classes
# Maze classes (different Path definitions)
# Path definitions (pass, block, door)
# Path definition Triggers
# Character definitions (project creatures that travel with Cod)
# Character definition triggers
# Item definition
# Item use
# Item usage triggers
# Add different command sets to different paths (outlined in the text returned)


with open('token.json', 'r') as f:
    config = json.load(f)
    token = config['token']

# token = "MTIzNDYzMTcwMDg1NjcwMDkzOQ.GZCPRe.75ehNsvtUhb6aH6lu940U36QSTIDLbu231WkzI"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='.', intents=intents)
intents.members = True
intents.message_content = True
intents.reactions = True


@bot.event
async def on_ready():
    print(f'("Badass Bot is running!")')
    channel_id = 1205749795268861962
    channel = bot.get_channel(channel_id)

    if channel:
        embed = discord.Embed(
            title="WELCOME TO THE\n"
                  "MAZE of the MINOTAUR!\n\n"
                  "Enter your name to START",
            description="*** use .create yourname to enter your name***",
            color=discord.Color.purple()
        )
        embed.add_field(name=f'***MINOTAURS CREED***', value=f'***{script}***', inline=False)
        # Add fields to the embed
        embed.set_image(url="https://cdn.discordapp.com/attachments/1205749795268861962/1235027565895352360/10.gif?ex=6632e08d&is=66318f0d&hm=e99c1bb336167b286e30d719afe52a21716ee8f83f383878f08466f5807a3e08&")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1205749795268861962/1235027565895352360/10.gif?ex=6632e08d&is=66318f0d&hm=e99c1bb336167b286e30d719afe52a21716ee8f83f383878f08466f5807a3e08&")
        await channel.send(embed=embed)
    else:
        print("Channel not found")


@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        pass
    # Define the word-to-emoji mapping
    word_emoji_map = {
        'hunnys': '❤️',  # Heart emoji
        'dream': '☁️',  # Cloud emoji
        'morning': '☀️',  # Sun emoji
        'hello':   '👋'
    }

    # Check each word in the message
    for word, emoji in word_emoji_map.items():
        if word in message.content.lower():  # Case-insensitive check
            await message.add_reaction(emoji)

script = "⋋⁠✿⁠ ⁠⁰⁠ ⁠o⁠ ⁠⁰⁠ ⁠✿⁠⋌(⁠ʘ⁠ᗩ⁠ʘ⁠’⁠)✧⁠\⁠(⁠>⁠o⁠<⁠)⁠ﾉ⁠✧\nლ⁠(⁠^⁠o⁠^⁠ლ⁠)ヽ⁠༼⁠⁰⁠o⁠⁰⁠；⁠༽⁠ノლ⁠(⁠^⁠o⁠^⁠ლ⁠)(⁠´⁠⊙⁠ω⁠\n⊙⁠`⁠)⁠！⊙⁠.⁠☉(ﾟ⁠οﾟ⁠人⁠)⁠)(⁠´⁠(⁠ｪ⁠)⁠｀⁠）ʕ⁠·⁠ᴥ⁠·⁠ʔヾ⁠(⁠*⁠\n⁠Ｏ⁠’⁠*⁠)⁠/ᕙ⁠[⁠･⁠۝･⁠]⁠ᕗᕙ⁠(⁠ ͡⁠◉⁠ ͜⁠ ⁠ʖ⁠ ͡⁠◉⁠)⁠ᕗ"


class Minotaurs:
    def __init__(self, size, name, power):
        self.size = size
        self.name = name
        self.power = power

    @classmethod
    def create_from_message(cls, content):
        parts = content.split(',')
        if len(parts) != 3:
            return None
        size, name, power = parts
        return cls(size.strip(), name.strip(), power.strip())

    names = "Gorthak"

    @classmethod
    def gorthok(self, size, name, power):
        self.size = "Large"
        self.name = "Gorthak"
        self.power = "Blast"

    @classmethod
    def largor(self, size, name, power):
        self.size = "Medium"
        self.name = "Largor"
        self.power = "Ram"

    @classmethod
    def thalnir(self, size, name, power):
        self.size = "Medium"
        self.name = "Thalnir"
        self.power = "Punch"


class Character:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_from_message(cls, name):
        return cls(name)


class Paths:
    def __init__(self):
        self.turn1 = None
        self.turn2 = None
        self.turn3 = None
        self.turn4 = None
        self.turn5 = None

    def path1(self):
        self.turn1 = "pass"
        self.turn2 = "trap"
        self.turn3 = "pass"
        self.turn4 = "blocked"
        self.turn5 = "pass"

    def path2(self):
        self.turn1 = "pass"
        self.turn2 = "DOOR"
        self.turn3 = "blocked"
        self.turn4 = "pass"
        self.turn5 = "trap"

    def path3(self):
        self.turn1 = "trap"
        self.turn2 = "pass"
        self.turn3 = "pass"
        self.turn4 = "blocked"
        self.turn5 = "pass"

    def path4(self):
        self.turn1 = "blocked"
        self.turn2 = "trap"
        self.turn3 = "pass"
        self.turn4 = "DOOR"
        self.turn5 = "pass"

    def path5(self):
        self.turn1 = "DOOR"
        self.turn2 = "pass"
        self.turn3 = "blocked"
        self.turn4 = "pass"
        self.turn5 = "trap"

@bot.command(name="create")
async def create_character(ctx, user_name):
    character = Character.create_from_message(user_name)
    embed = discord.Embed(title="use .start to begin\n"
                          ".start num1 num2 (1 - 5)", color=0x800080)
    embed.add_field(name=f"****WELCOME****\n***{character.name}***!\n",
                    value="***ENTER HERE***", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1205749795268861962/1235030503690600549/11.gif?ex=6632e349&is=663191c9&hm=b0a43866e2e95319d1c8afec0ddf6072dda16049a90ce2cd38b645f65b8d11b8&")
    await ctx.send(embed=embed)


async def choose_turn(paths, path_number, turn_number):
    path_func = getattr(paths, f"path{path_number}")
    if not hasattr(path_func, '__call__'):
        return "Invalid path number."

    path_func()
    turn = getattr(paths, f"turn{turn_number}")
    if turn == "pass":
        return (f"Path {path_number}, Turn {turn_number}: Pass")

    if turn == "DOOR":
        return (f"Path {path_number}, Turn {turn_number}: Door\n"
                f"Use .collect command to claim your prize!")

    if turn == "blocked":
        message = (f"Path {path_number}, Turn {turn_number}: Blocked\n"
                   f"You hear a RUMBLING\n")
        return message

    if turn == "trap":
        message = (f"Path {path_number}, Turn {turn_number}: Trapped!\n"
                   f"You have been trapped!\n"
                   f"Use the .free to FREE YOURSELF!")
        return message


@bot.command(name="start")
async def check_turn(ctx, path_number: int, turn_number: int):
    paths = Paths()
    status = await choose_turn(paths, path_number, turn_number)  # Await the async function

    embed = discord.Embed(title="Turn Status", color=800080)
    embed.add_field(name="****Selected Turn****", value=f'***{status}***', inline=False)
    embed.add_field(name="Use .walk command to proceed", value=".walk + num1 num2 ", inline=False)
    images = ["https://cdn.discordapp.com/attachments/1205749795268861962/1235027568181248162/6.gif?ex=6632e08d&is=66318f0d&hm=3687cdd54d8dc06516567ee7a505ab60c73fe0b09b637f70aea35b171c2d7888&"]
    selectedImage = random.choice(images)
    embed.set_image(url=selectedImage)
    await ctx.send(embed=embed)


@bot.command(name="walk")
async def check_turn(ctx, path_number: int, turn_number: int):
    paths = Paths()
    status = await choose_turn(paths, path_number, turn_number)  # Await the async function

    embed = discord.Embed(title="Turn Status", color=800080)
    embed.add_field(name="****Selected Turn****", value=f'***{status}***', inline=False)
    images = [
        "https://cdn.discordapp.com/attachments/1205749795268861962/1235027567715553381/7.gif?ex=6632e08d&is=66318f0d&hm=c6d427a7bedd272c43b2198932a505740862b06d06d1df95af39ab5e3c56eff7&"]
    selectedImage = random.choice(images)
    embed.set_image(url=selectedImage)
    await ctx.send(embed=embed)


@bot.command(name="run")
async def check_turn(ctx, path_number: int, turn_number: int):
    paths = Paths()
    status = await choose_turn(paths, path_number, turn_number)  # Await the async function

    embed = discord.Embed(title="Turn Status", color=800080)
    embed.add_field(name="****Selected Turn****", value=f'***{status}***', inline=False)
    images = [
        "https://cdn.discordapp.com/attachments/1205749795268861962/1235027567271084102/8.gif?ex=6632e08d&is=66318f0d&hm=69c45ceb32aaf6754f7e2f3dcb387c36a12215a50cb1e8ea811d49a2137e6c70&"]
    selectedImage = random.choice(images)
    embed.set_image(url=selectedImage)
    await ctx.send(embed=embed)


@bot.command(name="free")
async def free(ctx):
    embed = discord.Embed(title="You have FREED yourself!", color=800080)
    embed.add_field(name="You hear a rumbling in the distance", value="", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1205749795268861962/1235027568730832917/5.gif?ex=6632e08e&is=66318f0e&hm=56db85e439964c7414609a46af9dd023730b7bcdde6da528b6ce05576eeef559&")
    await ctx.send(embed=embed)
    await asyncio.sleep(5)
    await ctx.invoke(bot.get_command('beast'))


@bot.command(name="beast")
async def beast(ctx):
    minotaur_names = ["Gromthar", "Brakor", "Tharuk", "Grimnash", "Drak"]
    random_regular_name = random.choice(minotaur_names)
    weapons = ["axe", "hammer", "fists", "horns", "staff"]
    random_weapon = random.choice(weapons)
    embed = discord.Embed(title=f'***{random_regular_name}*** has APPEARED!\n'
                                f'***They are using their {random_weapon} RUN!***')
    embed.add_field(name="use .run + num1 num2", value="", inline=False)
    image_urls = ["https://cdn.discordapp.com/attachments/1205749795268861962/1235027569179492404/4.gif?ex=6632e08e&is=66318f0e&hm=bf29df7f1eeb857fe53ae327e5d644880e33c2960568018b70c4483fcffa372a&",
                  "https://cdn.discordapp.com/attachments/1205749795268861962/1235027569712042074/3.gif?ex=6632e08e&is=66318f0e&hm=89585ae6881bba69d5177a9fedf166009574541b2fc187923a8d5e397ee5d4a4&",
                  "https://cdn.discordapp.com/attachments/1205749795268861962/1235027570211422259/2.gif?ex=6632e08e&is=66318f0e&hm=964736d512e73ab261fde83c0f44e4a0558efc465e93a37e4bed0a081d76c4c3&"]
    selected_image_url = random.choice(image_urls)

    # Create an embed and set the image
    embed.set_image(url=selected_image_url)
    await ctx.send(embed=embed)


@bot.command(name='collect')
async def collect(ctx):
    random_prize = ["https://opensea.io/assets/matic/0x11bc733e719198e2b3746f6841d2818ca87af6da/91",
                    "https://opensea.io/assets/matic/0x11bc733e719198e2b3746f6841d2818ca87af6da/80",
                    "https://opensea.io/assets/matic/0x11bc733e719198e2b3746f6841d2818ca87af6da/105"]
    prize = random.choice(random_prize)
    embed = discord.Embed(title="YOU HAVE MADE IT OUT!\n"
                                "***Here is a PRIZE!***")
    embed.add_field(name=f'***LINK TO PRIZE!***', value=f'{prize}', inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1205749795268861962/1235027566364987453/9.gif?ex=6632e08d&is=66318f0d&hm=91555c779225f0d77b7408393040135716145fc152a255d3545ee4ee4dab1b1b&")
    await ctx.send(embed=embed)




