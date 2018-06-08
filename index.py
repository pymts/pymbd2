import discord

import asyncio

import os



client = discord.Client()

token = os.environ['BOT_TOKEN']



renkinn = os.environ['renkinn']


roudousya = os.environ['roudousya']


kapurasu = os.environ['kapurasu']


3syou = os.environ['3syou']


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
    
  if message.content.startswith('�{�X'):

   await client.send_find(message.channel, './wb.png',message='���Ƃ���A���Ƃ���`')
        
  
  elif message.content.startswith('A'):
        
   await client.send_find(message.channel, './a�{�[�i�X.png')
  

  elif message.content.startswith('D'):
        
   await client.send_find(message.channel, './d�{�[�i�X.png')


  elif message.content.startswith('����'):
        
   await client.send_find(message.channel, 'a����.png')

   await client.send_find(message.channel, 'd����.png')


  elif message.content.startswith('�o�����V�A'):
        
   await client.send_find(message.channel, './�o�����V�A.png')


  elif message.content.startswith('�J�[�}�X'):
        
   await client.send_find(message.channel, './�J�[�}�X.png')


  elif message.content.startswith('�B��'):
        
   await client.send_find(message.channel, renkinn)


  elif message.content.startswith('�J����'):
        
   await client.send_find(message.channel, roudousya)


  elif message.content.startswith('�J�v���X'):
        
   await client.send_find(message.channel, kapurasu)


  elif message.content.startswith('�Ȃł�'):
        
   await client.send_find(message.channel, '.v�A�h.png')


  elif message.content.startswith('3��'):
        
   await client.send_message(message.channel, 3syou)


  elif message.content.startswith('��]'):
        
   await client.send_message(message.channel, zetubou)


  elif message.content.startswith('�M������������ �_���_���b���^�b�^�b�^ �_�_�����~4 �`������������~����~����~����~��'):
        
   await client.send_message(message.channel, anga)


  elif message.content.startswith('�ޭ���`݁� �������� �������� ������������݁� ������������݁�'):
       
   await client.send_message(message.channel, barurona)


  elif message.content.startswith('��b�R�}���h'):
        
   await client.send_message(message.channel, '
   �E����
   �{�X
   a
   d
   ����
   �o�����V�A
   �J�[�}�X
   �B��
   �J����
   �J�v���X
   �Ȃł�

   �EBGM
   3��
   ��]
   �A���K
   �o�����i
   ')


client.run(token)