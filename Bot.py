import discord, json, asyncio, time, random, aiohttp, re, os, sys, math, asyncpg
from time import gmtime
from discord.ext import commands

#-------------------DATA---------------------
bot = commands.Bot(command_prefix="p!", description=None, help_command=None)
client = discord.Client()
prefix = "p!"
LogRoom = client.get_channel(id=568344705616707585)
underworking = ":warning: **This command isn't finished.** :warning:"
disabled = "**:no_entry_sign: Command disabled! :no_entry_sign:**"
"""timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())"""
Botserver = client.get_guild(id=56647658324819968)

#-----------------SETUP----------------------
@client.event
async def on_ready():
    print("Ready\n>>>")
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name='yeaa boii'))

#----------------COMMANDS--------------------
@commands.cooldown(1, 60, commands.BucketType.user) 
@bot.command(pass_context=True)
async def suggest(ctx, pref=None, *, text=None):
    if pref is None:
        await ctx.send("**The usage is `p!suggest {prefix (Q, S, C, B)} {text}`**")
    elif text is None:
        await ctx.send("**The usage is `p!suggest {prefix (Q, S, C, B)} {text}`**")
    else:
        try:
            if pref is "S":
                msg = "SUGGESTION"
            if pref is "Q":
                msg = "QUESTION"
            if pref is "C":
                msg = "COMMAND SUGGESTION"
            if pref is "B":
                msg = "BUGS"
            else:
                ctx.send("**Please use a valid prefix! The available prefixes: __Q__uestion, __Suggestion__, __Command Suggestion__, __Bugs__**")
        finally:
            colours = [0x11806a, 0x1abc9c, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
            col = random.choice(colours)
            em = discord.Embed(title=f"{msg}", description=f"**From {ctx.message.author.mention}**\n⋙ {text}", colour=col)
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            Sugchannel = bot.get_channel(id=568344705616707585)
            await ctx.send(f"**:white_check_mark: Sent in {Sugchannel.mention}**")
            mesg = await Sugchannel.send(embed=em)
            if pref is "S":
                await mesg.add_reaction("👍")
                await mesg.add_reaction("👎")
            if pref is "C":
                await mesg.add_reaction("👍")
                await mesg.add_reaction("👎")

@bot.command(pass_context=True)
async def info(ctx):
    await ctx.send(underworking)

@bot.command(pass_context=True)
async def im_disabled(ctx):
    await ctx.send(disabled)

@bot.command(pass_context=True)
async def typing(ctx):
    async with channel.typing():
        await cxt.send("**Im typing something**")

@bot.command(pass_context=True)
async def slap(ctx, member : discord.Member=None, *, Reason=None):
    if member is None:
        await ctx.send("**The usage is `>slap {member} {Reason}`**")
    else:
        await ctx.send(f"**{ctx.message.author} slaped {member.mention} for __{Reason}__**")

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.User=None, Day : int=None, *, Reason=None):
    if user is None:
        await ctx.send("**The usage is `p!ban {member} {0 - 7 amount of days to delete his messages} {Reason}`**")
    elif Reason is None:
        await ctx.send("**The usage is `p!ban {member} {0 - 7 amount of days to delete his messages} {Reason}`**")
    elif Day is None:
        await ctx.send("**The usage is `p!ban {member} {0 - 7 amount of days to delete his messages} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await ctx.send("**I wont let you ban yourself xD**")
        else:
            await user.ban(delete_message_days=Day, reason=Reason)
            await ctx.send(f"**{user.mention} got Banned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="BAN", description=None, colour=0xad1457)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/388945761611808769/453211671935057920/banned.gif")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await LogRoom.send(embed=em)
            await discord.DMChannel(recipient=user).send(f"**`Server: {Botserver.name}`\nBAMM!! You got banned from {Botserver.name}, bai bai!**")

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await ctx.send("**The usage is `p!unban {member} {Reason}`**")
    elif Reason is None:
        await ctx.send("**The usage is `p!unban {member} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await ctx.send("**I wont let you unban yourself xD**")
        else:
            await user.unban(reason=Reason)
            await ctx.send(f"**{user.mention} got UnBanned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="BAN", description=None, colour=0xad1457)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/388945761611808769/453211671935057920/banned.gif")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await LogRoom.send(embed=em)
            await discord.DMChannel(recipient=user).send(f"**`Server: {Botserver.name}`\nUNBAMM!! You got unbanned from {Botserver.name}, ready to join back?**")

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.HTTPException):
        await ctx.send("**Hmm... looks like that member isn't banned...**")

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await ctx.send("**The usage is `p!kick {member} {Reason}`**")
    elif Reason is None:
        await ctx.send("**The usage is `p!kick {member} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await ctx.send("**I won't let you kick yourself xD**")
        else:
            await bot.kick(user, reason=Reason)
            await ctx.send(f"**{user.mention} got Kicked by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="KICK", description=None, colour=0xe74c3c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await LogRoon.send(embed=em)
            await discord.DMChannel(recipient=user).send(f"**`Server: {Botserver.name}`\nHey! You got kicked from {Botserver.name}, bai bai!**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user : discord.User=None, duration : int=None, *, Reason=None):
    if user is None:
        await ctx.send("**The usage is `p!mute {member} {duration(in sec)} {Reason}`**")
    elif Reason is None:
        await ctx.send("**The usage is `p!mute {member} {duration(in sec)} {Reason}`**")
    elif duration is None:
        await ctx.send("**The usage is `p!mute {member} {duration(in sec)} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await ctx.send("**I won't let you mute yourself xD**")
        else:
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await user.add_roles(MutedRole, reason=Reason)
            await ctx.send(f"**{user.mention} got Muted (for {duration} sec) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="MUTE", description=None, colour=0x11806a)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.add_field(name="Duration", value=f"{duration} sec")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await LogRoom.send(embed=em)
            await discord.DMChannel(recipient=user).send(f"**`Server: {Botserver.name}`\nRoses are red, violets are blue and {user.mention} is muted!**")
            await asyncio.sleep(duration)
            await user.remove_roles(MutedRole, reason="Time is up...")
            em = discord.Embed(title="UNMUTE", description=None, colour=0x1abc9c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value="Time is up...")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await LogRoom.send(embed=em)
            await discord.DMChannel(recipient=user).send(f"**`Server: {Botserver.name}`\nHey! You got unmuted, don't get too excited..**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await ctx.send("**The usage is `p!unmute {member} {Reason}`**")
    elif Reason is None:
        await ctx.send("**The usage is `p!unmute {member} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await ctx.send("**I won't let you unmute yourself :P**")
        else:
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await user.remove_roles(MutedRole, reason=Reason)
            await ctx.send(f"**{user.mention} got UnMuted by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="UNMUTE", description=None, colour=0x1abc9c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await LogRoom.send(embed=em)
            await discord.DMChannel(recipient=user).send(f"**`Server: {Botserver.name}`\nHey! You got unmuted, dont get too excited..**")
        
@bot.command(pass_context=True)
async def ping(ctx):
    before = time.monotonic()
    embed = discord.Embed(description=":ping_pong: **...**", colour=0x3498db)
    msg = await ctx.send(embed=embed)
    ping = (time.monotonic() - before) * 1000
    pinges = int(ping)
    if 999 > pinges > 400:
        mesg = "Thats a lot!"
    elif pinges > 1000:
        mesg = "Omg, really sloooooow...."
    elif 399 > pinges > 141:
        mesg = "Ahhh, not good!"
    elif pinges < 140:
        mesg = "Its Good, Boi ;)"
    em = discord.Embed(title=None, description=f":ping_pong: Seems like `{pinges}` MS\n{mesg}", colour=0x3498db)
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await msg.edit_message(embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, duration : int=None, *, Reason=None):
    if Reason is None:
        await ctx.send("**The usage is `p!lock {duration (in sec)} {Reason}`**")
    elif duration is None:
        await ctx.send("**The usage is `p!lock {duration (in sec)} {Reason}`**")
    else:
        Basicrole = discord.utils.get(ctx.message.server.roles, name="Member")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        await ctx.message.channel.edit_channel_permissions(Basicrole, overwrite, reason=Reason)
        await ctx.send(f"**{ctx.message.channel.mention} is now locked for __{Reason}__**")
        em = discord.Embed(title="LOCK", description=None, colour=0x1f8b4c)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.add_field(name="Duration", value=f"{duration} sec")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await LogRoom.send(embed=em)
        await asyncio.sleep(duration)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await ctx.message.channel.edit_channel_permissions(Basicrole, overwrite, reason=Reason)
        await ctx.send(f"**{ctx.message.channel.mention} is now unlocked for __{Reason}__**")
        em = discord.Embed(title="UNLOCK", description=None, colour=0x2ecc71)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await LogRoom.send(embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, *, Reason=None):
    if Reason is None:
        await ctx.send("**The usage is `p!unlock {Reason}`**")
    else:
        Basicrole = discord.utils.get(ctx.message.server.roles, name="Member")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await ctx.message.channel.edit_channel_permissions(Basicrole, overwrite, reason=Reason)
        await ctx.send(f"**{ctx.message.channel.mention} is now unlocked for __{Reason}__**")
        em = discord.Embed(title="UNLOCK", description=None, colour=0x2ecc71)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await LogRoom.send(embed=em)
    
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number : int=None):
    if number is None:
        await ctx.send("**The usage is `p!clear {number of messages to delete}`**")
    else:
        number += 1
        deleted = await ctx.message.channel.purge_from(limit=number)
        num = number - 1
        em = discord.Embed(title=None, description=f'{ctx.message.author} deleted __{num}__ messages', colour=0x3498db)
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        msg = await ctx.send(embed=em)
        await LogRoom.send(embed=em)
        await asyncio.sleep(4)
        await msg.delete_message()

#-----------------------------------------------
@bot.command(pass_context=True)
async def sub(ctx, x : int=None, y : int=None):
    if x is None:
        await ctx.send("**The usage is `p!sub {number} {number}`**")
    elif y is None:
        await ctx.send("**The usage is `p!sub {number} {number}`**")
    else:
        msg = x - y
        text = await ctx.send("**Hmmm...**")
        await asyncio.sleep(3)
        await text.edit_message(f"**Oh, the result: {msg}**")

@bot.command(pass_context=True)
async def mul(ctx, x : int=None, y : int=None):
    if x is None:
        await ctx.send("**The usage is `p!mul {number} {number}`**")
    elif y is None:
        await ctx.send("**The usage is `p!mul {number} {number}`**")
    else:
        msg = x * y
        text = await ctx.send("**Hmmm...**")
        await asyncio.sleep(3)
        await text.edit_message(f"**Oh, the result: {msg}**")

@bot.command(pass_context=True)
async def div(ctx, x : int=None, y : int=None):
    if x is None:
        await ctx.send("**The usage is `p!div {number} {number}`**")
    elif y is None:
        await ctx.send("**The usage is `p!div {number} {number}`**")
    else:
        msg = x / y
        text = await ctx.send("**Hmmm...**")
        await asyncio.sleep(3)
        await text.edit_message(f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def exp(ctx, x : int=None, y : int=None):
    if x is None:
        await ctx.send("**The usage is `p!exp {number} {number}`**")
    elif y is None:
        await ctx.send("**The usage is `p!exp {number} {number}`**")
    else:
        msg = x ** y
        text = await ctx.send("**Hmmm...**")
        await asyncio.sleep(3)
        await text.edit_message(f"**Oh, the result: {msg}**")
    
@bot.command(pass_context=True)
async def add(ctx, x : int=None, y : int=None):
    if x is None:
        await ctx.send("**The usage is `p!add {number} {number}`**")
    elif y is None:
        await ctx.send("**The usage is `p!add {number} {number}`**")
    else:
        msg = x + y
        text = await ctx.send("**Hmmm...**")
        await asyncio.sleep(3)
        await text.edit_message(f"**Oh, the result: {msg}**")

@bot.command(pass_context=True)
async def roll(ctx, x : int=None, y : int=None):
    if x is None:
        await ctx.send("**The usage is `p!roll {number} {number}`**")
    elif y is None:
        await ctx.send("**The usage is `p!roll {number} {number}`**")
    else:
        msg = random.randint(x, y)
        text = await ctx.send("**Hmmm...**")
        await asyncio.sleep(3)
        await text.edit_message(f"**My choose: {msg}**")
    
@bot.command()
async def game(*, play=None):
    if play is None:
        await ctx.send("**The usage is `p!game {Something to set for the Bot}`**")
    else:
        await bot.change_presence(game=discord.Game(name=play))
        em = discord.Embed(title="Game Status", description=f"Game status changed to __{play}__!", colour=0x3498db)
        await ctx.send(embed=em)

@bot.command(pass_context=True)
async def nick(ctx, *, name=None):
    if name is None:
        await ctx.send("**The usage is `p!nick {Reason: optional} {Something to set as your name}`**")
    else:
        await ctx.message.author.edit(nick=name)
        em = discord.Embed(title="Nickname", description=f"{ctx.message.author}'s nick set to __{name}__!", colour=0x3498db)
        await ctx.send(embed=em)

@bot.command(pass_context=True)
async def say(ctx, *, words=None):
    if words is None:
        await ctx.send("**The usage is `p!say {Something}`**")
    else:
        await ctx.send(f"**{words}**")

@bot.command(pass_context=True)
async def time(ctx):
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    await ctx.send(f"**{ctx.message.author.mention}, the time is __{timer}__**")

@bot.command(pass_context=True)
async def lenny(ctx):
    ears = ['q{}p', 'ʢ{}ʡ', '⸮{}?', 'ʕ{}ʔ', 'ᖗ{}ᖘ', 'ᕦ{}ᕥ', 'ᕦ({})ᕥ', 'ᕙ({})ᕗ', 'ᘳ{}ᘰ', 'ᕮ{}ᕭ', 'ᕳ{}ᕲ', '({})', '[{}]', '୧{}୨', '୨{}୧', '⤜({})⤏', '☞{}☞', 'ᑫ{}ᑷ', 'ᑴ{}ᑷ', 'ヽ({})ﾉ', '乁({})ㄏ', '└[{}]┘', '(づ{})づ', '(ง{})ง', '|{}|']
    eyes = ['⌐■{}■', ' ͠°{} °', '⇀{}↼', '´• {} •`', '´{}`', '`{}´', 'ó{}ò', 'ò{}ó', '>{}<', 'Ƹ̵̡ {}Ʒ', 'ᗒ{}ᗕ', '⪧{}⪦', '⪦{}⪧', '⪩{}⪨', '⪨{}⪩', '⪰{}⪯', '⫑{}⫒', '⨴{}⨵', "⩿{}⪀", "⩾{}⩽", "⩺{}⩹", "⩹{}⩺", "◥▶{}◀◤", "≋{}≋", "૦ઁ{}૦ઁ", "  ͯ{}  ͯ", "  ̿{}  ̿", "  ͌{}  ͌", "ළ{}ළ", "◉{}◉", "☉{}☉", "・{}・", "▰{}▰", "ᵔ{}ᵔ", "□{}□", "☼{}☼", "*{}*", "⚆{}⚆", "⊜{}⊜", ">{}>", "❍{}❍", "￣{}￣", "─{}─", "✿{}✿", "•{}•", "T{}T", "^{}^", "ⱺ{}ⱺ", "@{}@", "ȍ{}ȍ", "x{}x", "-{}-", "${}$", "Ȍ{}Ȍ", "ʘ{}ʘ", "Ꝋ{}Ꝋ", "๏{}๏", "■{}■", "◕{}◕", "◔{}◔", "✧{}✧", "♥{}♥", " ͡°{} ͡°", "¬{}¬", " º {} º ", "⍜{}⍜", "⍤{}⍤", "ᴗ{}ᴗ", "ಠ{}ಠ", "σ{}σ"]
    mouth = ['v', 'ᴥ', 'ᗝ', 'Ѡ', 'ᗜ', 'Ꮂ', 'ヮ', '╭͜ʖ╮', ' ͟ل͜', ' ͜ʖ', ' ͟ʖ', ' ʖ̯', 'ω', '³', ' ε ', '﹏', 'ل͜', '╭╮', '‿‿', '▾', '‸', 'Д', '∀', '!', '人', '.', 'ロ', '_', '෴', 'ѽ', 'ഌ', '⏏', 'ツ', '益']
    lenny = random.choice(ears).format(random.choice(eyes)).format(random.choice(mouth))
    await ctx.send("**A wild Lenny appeard:**\n\n\t" + lenny)

@bot.command(pass_context=True)
async def help(ctx):
    await ctx.send(underworking)

@bot.command(pass_context=True)
async def bot(ctx):
    em = discord.Embed(description= "The Bot of Pan-Da Server\n`Made by Rettend`", colour=0x3498db)
    awaitctx.send(embed=em)

#-----------------------------------------------
@client.event
async def on_message(message):
    if message.content.startswith(f"{prefix} + mod"):
        em = discord.Embed(title="MODERATION COMMANDS", description=None, colour=0x3498db)
        em.add_field(name="Admin commands", value=":small_blue_diamond: p!ban {member} {0 - 7 amount of days to delete his messages} {Reason}\n"
                     ":black_small_square: Kicks the user and removes his messages for the given days, the user can't rejoin, until he gots unbanned\n"
                     "\n"
                     ":small_orange_diamond: p!unban {member} {0 - 7 amount of days to delete his messages} {Reason}\n"
                     ":black_small_square: Kicks the user and removes his messages for the given days, the user can't rejoin, until he gots unbanned\n"
                     "\n\n\n")
        em.add_field(name="Mod commands", value=":small_blue_diamond: p!kick {member} {Reason}\n"
                     ":black_small_square: Kicks the user from the server, the user can rejoin by instant-invite links\n"
                     "\n"
                     ":small_orange_diamond: p!mute {member} {duration(in sec)} {Reason}\n"
                     ":black_small_square: Mutes the user, this user can't send messages for the given duration, if the _time is up,_ he will auto get unmuted\n"
                     "\n"
                     ":small_blue_diamond: p!unmute {member} {Reason}\n"
                     ":black_small_square: UnMutes the Muted user, this user now allowed to send messages\n"
                     "\n"
                     ":small_orange_diamond: p!lock {Reason} {duration(in sec)}\n"
                     ":black_small_square: Locks down the currently channel, only Admins can send messages until an unlock\n"
                     "\n"
                     ":small_blue_diamond: p!unlock {Reason}\n"
                     ":black_small_square: Unlocks the currently locked channel, now everyone can send messages there\n"
                     "\n"
                     ":small_orange_diamond: p!clear {number of messages to delete}\n"
                     ":black_small_square: Deletes a specific amount of messages")
        await message.channel.send(embed=em)
    if message.content.startswith(f"{prefix} + 8ball"):
        await message.channel.send(random.choice(['**It is certain :8ball:**',
                                                              '**It is decidedly so :8ball:**',
                                                              '**Without a doubt :8ball:**',
                                                              '**No U :8ball:**',
                                                              '**Boi, go sleep... :8ball:**',
                                                              '**As i see it, yes :8ball:**',
                                                              '**As i see it, *No U*   :8ball:**',
                                                              '**Most likely :8ball:**',
                                                              '**Outlook good :8ball:**',
                                                              '**Yes :8ball:**',
                                                              '**Signs point to yes :8ball:**',
                                                              '**Reply hazy try again :8ball:**',
                                                              '**Ask again later, nub :8ball:**',
                                                              '**Better not tell you :8ball:**',
                                                              '**Cannot predict now :8ball:**',
                                                              '**Concentrate and ask again :8ball:**',
                                                              '**8ball.exe not found :8ball:**',
                                                              '**Dont count on it :8ball:**',
                                                              '**My reply is no :8ball:**',
                                                              '**My sources say no :8ball:**',
                                                              '**Outloook not so good :8ball:**',
                                                              '**Very doubtful :8ball:**',
                                                              '**Ha! :8ball:**',
                                                              '**Not today man, not today :8ball:**']))
    await bot.process_commands(message) #IMPORTANT

      
token = os.environ.get('DISCORD_TOKEN')
client.run(token)
