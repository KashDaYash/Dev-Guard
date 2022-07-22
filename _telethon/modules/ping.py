import asyncio
import time
from telethon import events
  
async def init(bot):
 @bot.on(events.NewMessage(pattern='.ping', forwards=False))
  
  
 d = time.time() - s
 s = time.time()
 message = await event.reply('Pong!')
 async def handler(event):
 await message.edit(f'Pong! __(reply took {d:.2f}s)__')
 await asyncio.sleep(5)
 await asyncio.wait([event.delete(), message.delete()])
