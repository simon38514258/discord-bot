# @bot.event
# async def on_member_join(member):
#     guild_id = int(jdata["Guild"]) 
#     if member.guild.id == guild_id:
#         channel = bot.get_channel(int(jdata["Member_channel"]))
#         await channel.send(f"{member.mention}歡迎參觀咩咩教堂")

# @bot.event
# async def on_member_remove(member):
#     guild_id = int(jdata["Guild"]) 
#     if member.guild.id == guild_id:
#         channel = bot.get_channel(int(jdata["Member_channel"]))
#         await channel.send(f"{member.mention}離開咩咩身邊惹")

# ----------------------------------------------------------
# class SoldierConverter(commands.Converter):
#     async def convert(self, ctx, argument):
#         return argument

# @bot.command(name="兵種")
# async def soldier(ctx, *, soldier: SoldierConverter):
#     if soldier in jdata.get("Soldier", []):
#         index = jdata["Soldier"].index(soldier)
#         soldierPic = jdata["pic_soldier"][index]
#         pic = discord.File(soldierPic)
#         message="本圖由驅邪提供"
#         await ctx.send(content=message,file=pic)

# # 註冊一個別名為兵種名稱的指令，方便直接使用 !0.0兵種名稱
# for soldier_name in jdata.get("Soldier", []):
#     @bot.command(name=soldier_name.lower())
#     async def _soldier(ctx):
#         await soldier(ctx, soldier=soldier_name)

# ----------------------------------------------------------
#圖片傳送(基本)
# @bot.command()
# async def 刀盾(ctx):
#     soldierPic = jdata["pic_soldier"][0]
#     pic = discord.File(soldierPic)
#     await ctx.send(file = pic)

# ----------------------------------------------------------