import discord
import asyncio
import os

client = discord.Client()
token = os.environ['BOT_TOKEN']

renkinn = os.environ['renkinn']
roudousya = os.environ['roudousya']
kapurasu = os.environ['kapurasu']
karate = os.environ['karate']
zetubou = os.environ['zetubou']
anga = os.environ['anga']
barurona = os.environ['barurona']

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')
  
@client.event
async def on_message(message):
   if message.content.startswith('ボス'):
      await client.send_find(message.channel, './wb.png',message='見とけよ、見とけよ～')

   elif message.content.startswith('A'):
      await client.send_find(message.channel, './aボーナス.png')

   elif message.content.startswith('D'):
      await client.send_find(message.channel, './dボーナス.png')

   elif message.content.startswith('名声'):
      await client.send_find(message.channel, 'a名声.png')
      await client.send_find(message.channel, 'd名声.png')

   elif message.content.startswith('バレンシア'):
      await client.send_find(message.channel, './バレンシア.png')

   elif message.content.startswith('カーマス'):
      await client.send_find(message.channel, './カーマス.png')

   elif message.content.startswith('錬金'):
      await client.send_find(message.channel, renkinn)

   elif message.content.startswith('労働者'):
      await client.send_find(message.channel, roudousya)

   elif message.content.startswith('カプラス'):
      await client.send_find(message.channel, kapurasu)

   elif message.content.startswith('なでこ'):
      await client.send_find(message.channel, '.vアド.png')

   elif message.content.startswith('3章'):
      await client.send_message(message.channel, karate)

   elif message.content.startswith('絶望'):
     await client.send_message(message.channel, zetubou)

   elif message.content.startswith('ギュルルルルル ダンダンッ↓タッタッタ ダダン↑×4 チャラララララ~→ラ~↑ラ~↓ラ~→'):
      await client.send_message(message.channel, anga)

   elif message.content.startswith('ｷﾞｭｲｲ～ﾝ♪ ｽﾞﾀﾞﾀﾞﾀﾞ ｽﾞﾀﾞﾀﾞﾀﾞ ﾃﾞﾃﾞﾝﾃﾞﾝﾃﾞﾃﾞﾝ♪ ﾃﾞﾃﾞﾝﾃﾞﾝﾃﾞﾃﾞﾝ♪'):
      await client.send_message(message.channel, barurona)

   elif message.content.startswith('野獣コマンド'):
     await client.send_message(message.channel, '
     ・砂漠
     ボス
     a
     d
     名声
     バレンシア
     カーマス
     錬金
     労働者
     カプラス
     なでこ
     
     ・BGM
     3章
     絶望
     アンガ
     バルロナ
     ')
     
client.run(token)