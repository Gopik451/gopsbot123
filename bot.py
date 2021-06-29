import discord
from discord import *
import discord.ext
from discord.ext import commands
import requests
from Cybernator import Paginator as pag

prefix = '!'


client = commands.Bot(command_prefix = prefix)

#Удаление команды help
client.remove_command('help')
#status = discord.Status.online, 
@client.event
async def on_ready():
	await client.change_presence(activity = discord.Game('!bot'))

#=====================================================================================================================================

#Инфа о боте
@client.command()
async def bot(ctx):
	await ctx.channel.purge(limit = 1)
	i = discord.Embed(title = 'Я:', description = 'GOPS#3844', colour = discord.Color.blue())
	gopik = discord.Embed(title = 'Создатель:', description = 'gopik#3880', colour = discord.Color.blue())
	helpcmd = discord.Embed(title = 'Я создан для:', description = '!help', colour = discord.Color.blue())
	initebot = discord.Embed(title = 'Пригласить меня:', description = 'https://discord.com/api/oauth2/authorize?client_id=825421904641785906&permissions=8&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2F&scope=bot', colour = discord.Color.blue())
	serverorigin = discord.Embed(title = 'Мой основной сервер:', description = 'https://discord.gg/rctxN3m2qJ', colour = discord.Color.blue())
	embeds = [i, gopik, helpcmd, serverorigin, initebot]

	message = await ctx.send(embed = i)
	page = pag(client, message, only=ctx.author, use_more=False, embeds=embeds)
	await page.start()

#======================================================================================================================================

#Embed_msg
@client.command()
@commands.has_permissions(administrator = True)
async def say(ctx, *, text):
	await ctx.channel.purge(limit = 1)
	emb = discord.Embed(title = text, colour = discord.Color.blue())

	await ctx.send(embed = emb)

#========================================================================================================================================

#Отчистка чата
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear(ctx):
	await ctx.channel.purge(limit=1000)

#=========================================================================================================================================

#Кик
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def kick(ctx, member: discord.Member, *, text):
	await ctx.channel.purge(limit = 1)
	if text == text:
		await member.kick(reason = text)
		await ctx.send(f'Участник {member.mention} был изгнан модератором {ctx.author} по причине {text}!')
	elif text == None:
		await ctx.send(f'{ctx.author}, укажите причину!')

#==========================================================================================================================================

#Бан
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def ban(ctx, member: discord.Member, *, text):
	await ctx.channel.purge(limit = 1)
	if text == text:
		await member.ban(reason = text)
		await ctx.send(f'Участник {member.mention} был забанен модератором {ctx.author} по причине {text}!')
	elif text == None:
		await ctx.send(f'{ctx.author}, укажите причину!')

#==========================================================================================================================================

#Разбан
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
	await ctx.channel.purge(limit = 1)

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)
		await ctx.send(f'{ctx.author} разбанил {user.mention}!')

		return

#=========================================================================================================================================

#Команда help. Новая настройка!
@client.command(pass_context = True)
async def help(ctx):
	await ctx.channel.purge(limit = 1)
	helpinfo = discord.Embed(title = 'Помощь', description = 'Здесь вы можете найти помощь по командам!', colour = discord.Color.blue())
	ban = discord.Embed(title = '!ban @ник причина', description = 'Банит участника', colour = discord.Color.blue())
	kick = discord.Embed(title = '!kick @ник причина', description = 'Кикает участника', colour = discord.Color.blue())	
	mute = discord.Embed(title = '!mute @ник причина', description = 'Мутит участника', colour = discord.Color.blue())
	clear = discord.Embed(title = '!clear', description = 'Отчистка чата', colour = discord.Color.blue())
	clan = discord.Embed(title = '!clan', description = 'Инфо о кланах', colour = discord.Color.blue())
	unban = discord.Embed(title = '!unban ник#тег', description = 'Разбанивает участника', colour = discord.Color.blue())
	unmute = discord.Embed(title = '!unmute @ник', description = 'unмутит участника', colour = discord.Color.blue())
	stat = discord.Embed(title = '!clan_admin', description = 'помощь по кланам для модерации', colour = discord.Color.blue())
	bc = discord.Embed(title = '!bc сообщение', description = 'Обьявления', colour = discord.Color.blue())
	say = discord.Embed(title = '!say сообщение', description = 'Писать от имени бота', colour = discord.Color.blue())

	embeds = [helpinfo, ban, kick, mute, clear, unban, unmute, clan, stat, bc, say]

	message = await ctx.send(embed = helpinfo)
	page = pag(client, message, only=ctx.author, use_more=False, embeds=embeds)
	await page.start()

#===========================================================================================================================================

#Мут
@client.command()
@commands.has_permissions(administrator = True)

async def mute(ctx, member: discord.Member, text):
	await ctx.channel.purge(limit = 1)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Нарушитель')
	if text == text:
		await member.add_roles(mute_role)
		await ctx.send(f'Участника {member.mention} заткнул модератор {ctx.author} по причине {text}!')
	elif text == None:
		await ctx.send(f'{ctx.author}, укажите причину!')

#==========================================================================================================================================

#unмут
@client.command()
@commands.has_permissions(administrator = True)
async def unmute(ctx, member: discord.Member):
	await ctx.channel.purge(limit = 1)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Нарушитель')

	await member.remove_roles(mute_role)
	await ctx.send(f'Участника {member.mention} размутил модератор {ctx.author}!')

#=========================================================================================================================================

#свой канал
@client.event
async def on_voice_state_update(member, before, after):
	if after.channel.id == 837963964151103488:
		for guild in client.guilds:
			maincategory = discord.utils.get(guild.categories, id=822328488563965984)
			channel2 = await guild.create_voice_channel(name=f'канал {member.display_name}', category = maincategory)
			await channel2.set_permissions(member,connect=True, mute_members=True, move_members=True, manage_channels=True)
			await member.move_to(channel2)
			def check(x, y, z):
				return len(channel2.members) == 0
			await client.wait_for('voice_state_update', check=check)
			await channel2.delete()


#Кланы
#=========================================================================================================================================
#=========================================================================================================================================

#клан top
@client.command()
async def clan_top(ctx, member: discord.Member):
	await ctx.channel.purge(limit = 1)
	superrole = discord.utils.get(ctx.message.guild.roles, name = 'Клан: Super')
	giper = discord.utils.get(ctx.message.guild.roles, name = 'Клан: Giper')
	top = discord.utils.get(ctx.message.guild.roles, name = 'Клан: top')
	mega = discord.utils.get(ctx.message.guild.roles, name = 'Клан: Mega')
	await member.add_roles(top)
	await Member.remove_roles(giper, superrole, mega)

#============================================

#клан giper
@client.command()
async def clan_giper(ctx, member: discord.Member):
	await ctx.channel.purge(limit = 1)
	superrole = discord.utils.get(ctx.message.guild.roles, name = 'Клан: Super')
	giper = discord.utils.get(ctx.message.guild.roles, name = 'Клан: Giper')
	top = discord.utils.get(ctx.message.guild.roles, name = 'Клан: top')
	mega = discord.utils.get(ctx.message.guild.roles, name = 'Клан: Mega')
	await member.add_roles(giper)
	await member.remove_roles(mega, superrole , top)

#============================================

#клан mega
@client.command()
async def clan_mega(ctx, member: discord.Member):
	await ctx.channel.purge(limit = 1)
	superrole = discord.utils.get(ctx.message.guild.roles, name = 'Клан: Super')
	giper = discord.utils.get(ctx.message.guild.roles, name = 'Клан: Giper')
	top = discord.utils.get(ctx.message.guild.roles, name = 'Клан: top')
	mega = discord.utils.get(ctx.message.guild.roles, name = 'Клан: Mega')
	await member.add_roles(mega)
	await member.remove_roles(giper, superrole, top)

#============================================

#клан super
@client.command()
async def clan_super(ctx, member: discord.Member):
	await ctx.channel.purge(limit = 1)
	superrole = discord.utils.get(ctx.message.guild.roles, name = 'Клан: Super')
	giper = discord.utils.get(ctx.message.guild.roles, name = 'Клан: Giper')
	top = discord.utils.get(ctx.message.guild.roles, name = 'Клан: top')
	mega = discord.utils.get(ctx.message.guild.roles, name = 'Клан: Mega')
	await member.add_roles(superrole)
	await member.remove_roles(giper, top, mega)

#============================================

#клан help
@client.command()
async def clan(ctx):
	await ctx.channel.purge(limit = 1)
	
	clanhelp = discord.Embed(title = 'Кланы', description = 'Здесь есть инфо о кланах!', colour = discord.Color.blue())
	toprolehelp = discord.Embed(title = 'Клан top', description = '!clan_top @свой ник', colour = discord.Color.blue())
	giperrolehelp = discord.Embed(title = 'Клан giper', description = '!clan_giper @свой ник', colour = discord.Color.blue())
	megarolehelp = discord.Embed(title = 'Клан mega', description = '!clan_mega @свой ник', colour = discord.Color.blue())
	superrolehelp = discord.Embed(title = 'Клан super', description = '!clan_super @свой ник', colour = discord.Color.blue())
	
	embeds = [clanhelp, toprolehelp, giperrolehelp, megarolehelp, superrolehelp]
	
	message = await ctx.send(embed = clanhelp)
	page = pag(client, message, only=ctx.author, use_more=False, embeds=embeds)
	await page.start()

#===============================================================================================================================
#===============================================================================================================================
#Кланы

#Обьявления
@client.command()
@commands.has_permissions(administrator = True)
async def bc(ctx, *, text):
	await ctx.channel.purge(limit = 1)
	emb = discord.Embed(title = f'{text} (Объявил {ctx.author})', colour = discord.Color.blue())

	await ctx.send(embed = emb)

#===============================================================================================================================

#sosi
@client.command()
@commands.has_permissions(administrator = True)
async def sosi(ctx, member):
	await ctx.channel.purge(limit = 1)
	await ctx.send(f'{member} отсосал у {ctx.author}')

#===============================================================================================================================

#Error
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound ):
		await ctx.channel.purge(limit = 1)
		await ctx.send(embed = discord.Embed(title = '❌', description = f'{ctx.author.name}, данной команды нет!',
			colour = discord.Color.red()))

#===============================================================================================================================



#===============================================================================================================================

#clan_admin
@client.command()
@commands.has_permissions(administrator = True)
async def clan_admin(ctx):
	await ctx.channel.purge(limit = 1)
	embed = discord.Embed(title = 'Создайте роли:', description = '(Копируйте) Клан: Super  Клан: Mega  Клан: Giper  Клан: top\nВы можете создать чаты и там выбрать только по одной роли! Например: в чате top могут общатся только люди у которых есть роль top(!clan)\nВы можете увидеть данную функцию на https://discord.gg/rctxN3m2qJ', colour = discord.Color.blue())
	
	await ctx.send(embed = embed)

#===============================================================================================================================

#===============================================================================================================================

#run
client.run('ODI1NDIxOTA0NjQxNzg1OTA2.YF9sDQ.Yuci7h6SroISPpCs4lZNOUR1ILk')