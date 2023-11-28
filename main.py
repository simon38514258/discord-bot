#導入 Discord.py 及 from discord.ext import commands
import discord
from discord.ext import commands
import json
#讀取json檔
with open("setting.json","r",encoding="utf8")as jfile:
    jdata = json.load(jfile)

#bot 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!咩",intents=intents)

class SoldierConverter(commands.Converter):
    async def convert(self, ctx, argument):
        return argument

@bot.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', bot.user)
    game = discord.Game('窩ㄞ咩咩')#暱稱欄位文字
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_member_join(member):
    guild_id = int(jdata["Guild"]) 
    if member.guild.id == guild_id:
        channel = bot.get_channel(int(jdata["Member_channel"]))
        await channel.send(f"{member.mention}歡迎參觀咩咩教堂")

@bot.event
async def on_member_remove(member):
    guild_id = int(jdata["Guild"]) 
    if member.guild.id == guild_id:
        channel = bot.get_channel(int(jdata["Member_channel"]))
        await channel.send(f"{member.mention}離開咩咩身邊惹")
#---------------------------------------------------------------
@bot.command(name="兵種")
async def soldier(ctx, *, soldier: SoldierConverter):
    if soldier in jdata.get("Soldier", []):
        index = jdata["Soldier"].index(soldier)
        soldierPic = jdata["pic_soldier"][index]
        pic = discord.File(soldierPic)
        message="本圖由驅邪提供"
        await ctx.send(content=message,file=pic)

# 註冊一個別名為兵種名稱的指令，方便直接使用 !0.0兵種名稱
for soldier_name in jdata.get("Soldier", []):
    @bot.command(name=soldier_name.lower())
    async def _soldier(ctx):
        await soldier(ctx, soldier=soldier_name)


#圖片傳送(基基本)
# @bot.command()
# async def 刀盾(ctx):
#     soldierPic = jdata["pic_soldier"][0]
#     pic = discord.File(soldierPic)
#     await ctx.send(file = pic)


#TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
bot.run(jdata["TOKEN"]) 
