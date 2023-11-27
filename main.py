#導入 Discord.py 及 from discord.ext import commands
import discord
from discord.ext import commands

#bot 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="@mei",intents=intents)
@bot.event

#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：咩0.0', bot.user)
    game = discord.Game('窩ㄞ咩咩')#暱稱欄位文字
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.online, activity=game)


#TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
bot.run('MTE3ODY4NjI0NDQxOTU1MTI2Mw.GLjhH7.B2Kmi-7ERkzbiDOg7jBvdWOi_a582bhPzt4Wyo') 
