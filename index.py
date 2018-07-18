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
sito = os.environ['sito']
yju = os.environ['yju']

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')
  
@client.event
async def on_message(message):
   if message.content == 'ボス':
      await client.send_file(message.channel, './wb2.png',content='見とけよ、見とけよ～')

   elif message.content == ('A') or message.content == ('a') or message.content == ('A') or message.content == ('あ'):
      await client.send_file(message.channel, './aボーナス.png')

   elif message.content == ('D'):
      await client.send_file(message.channel, './dボーナス.png')

   elif message.content == ('名声'):
      await client.send_file(message.channel, 'a名声.png')
      await client.send_file(message.channel, 'd名声.png')

   elif message.content == ('バレンシア'):
      await client.send_file(message.channel, './バレンシア.png')

   elif message.content == ('カーマス'):
      await client.send_file(message.channel, './カーマス.png')

   elif message.content == ('錬金'):
      await client.send_message(message.channel, renkinn)

   elif message.content == ('労働者'):
      await client.send_message(message.channel, roudousya)

   elif message.content == ('カプラス'):
      await client.send_message(message.channel, kapurasu)

   elif message.content == ('なでこ'):
      await client.send_file(message.channel, 'vアド.png',content='いくでいくで～')
      await client.send_message(message.channel, 'ｺﾄｯ...')
      
   elif message.content == ('シート'):
      await client.send_message(message.channel, sito)
      
   elif message.content == ('強化'):
      await client.send_file(message.channel, './強化.png')

   elif message.content == ('3章'):
      await client.send_message(message.channel, karate)

   elif message.content == ('絶望'):
     await client.send_message(message.channel, zetubou)

   elif message.content == ('ギュルルルルル ダンダンッ↓タッタッタ ダダン↑×4 チャラララララ~→ラ~↑ラ~↓ラ~→'):
      await client.send_message(message.channel, anga)

   elif message.content == ('ｷﾞｭｲｲ～ﾝ♪ ｽﾞﾀﾞﾀﾞﾀﾞ ｽﾞﾀﾞﾀﾞﾀﾞ ﾃﾞﾃﾞﾝﾃﾞﾝﾃﾞﾃﾞﾝ♪ ﾃﾞﾃﾞﾝﾃﾞﾝﾃﾞﾃﾞﾝ♪'):
      await client.send_message(message.channel, barurona)

   elif message.content == ('砂漠コマンド'):
      await client.send_message(message.channel, 'ボス　錬金　労働者　カプラス　カーマス　バレンシア　A　D　名声　なでこ　シート　強化')
      
client.run(token)