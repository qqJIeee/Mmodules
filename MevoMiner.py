from asyncio import sleep
from .. import loader, utils
import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions, TelegramClient, errors
from ..inline.types import InlineCall

__version__ = (1, 1)

@loader.tds
class MevoMiner(loader.Module):
    '''Модуль для автоматического копание в боте MineEvo'''
    strings = {
        "name" : "MevoMiner"
    }
    async def client_ready(self,client,db):
        self.bb = False
        chat_entity = await self.client.get_entity("hikka-logs")
        chat_id = chat_entity.id
        chat_id = '-100' + str(chat_id)
        self.db.set(self.name, "mid", int(chat_id))
        s = self.get('dly')
        if s == None:
            self.set('dly', 1.0)
        s = self.get('mm')
        if s == None:
            self.set('mm', False)
        s = self.get('ag')
        if s == None:
            self.set('ag', False)
        s = self.get('as')
        if s == None:
            self.set('as', False)
        s = self.get('fw')
        if s == None:
            self.set('fw', False)
        
    @loader.command()
    async def mmm(self,message):
        '''- Включить/выключить копание'''
        self.set('mm', not self.get('mm'))
        dly = self.get('dly')
        if self.get('mm'):
            await self.client.send_message(message.peer_id, "⛏ <b>Копание включено</b>")
            await message.delete()
        else:
            await self.client.send_message(message.peer_id, "⛏ <b>Копание выключено</b>")
            await message.delete()
        if self.get('mm'):
            while self.get('mm'):
                await self.client.send_message("@mine_evo_bot", "коп")
                await asyncio.sleep(dly)
        else:
            return
    @loader.watcher()
    async def bosses_fw(self,message):
        mid = self.db.get(self.name, "mid", None)
        dly = self.get('dly')
        
        if self.get('fw'):
            if self.get('mm)'):
                if message.chat_id == mid and "A wait of" in message.raw_text and "seconds is required" in message.raw_text:
                    fss = message.text.index("A wait of") + len("A wait of")
                    fsss = message.text.index("seconds is required")
                    fs = int(message.text[fss:fsss]) + 5
                    self.set('mm' , False)
                    await asyncio.sleep(fs)
                    await self.mmm(message)
                    await message.delete()
        if self.get('as'):
            if self.get('mm'):
                if message.chat_id == 5522271758 and "🔶 Ты выбрал босса" in message.raw_text:
                    self.bb = True
                    await self.mmm(message)
        if self.get('ag'):
            if self.bb:
                if message.chat_id == 5522271758 and "для атаки выбери босса" in message.raw_text:
                    self.bb = False
                    await asyncio.sleep(dly)
                    await self.mmm(message)
    @loader.command(alias = 'msc')
    async def emscfg(self,message: Message):
        '''- Установить значение в конфиг\n[Название] [Значение]\nНе работат с параметром cmt'''
        args = utils.get_args_split_by(message, " ")
        pp = args[0]
        zz = args[1]
        if pp == "dly":
            try:
                zz = float(zz)
                self.set('dly',zz)
                await utils.answer(message, f"✅ <b>Успешно!\nЗадержка копания изменена на {zz}</b> ")
            except ValueError:
                await utils.answer(message, f"🚫 <b>Ошибка!\nУкажите число в значении!</b>")


    @loader.command()
    async def emcfg(self,message):
        '''- Конфиг модуля MevoMiner'''
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        if self.get('mm'):
            dpm = 'Включено'
        else:
            dpm = 'Выключено'
        
        await self.inline.form(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n⛏ <b>Статус копания:</b> <i>{dpm}</i>\n<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}",
            message=message,
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка копания ',
                        'callback' : self.mdlym,
                    },
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.idd,
                    },
                ],
                [
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def mdlym(self,call:InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        if self.get('mm'):
            dpm = 'Включено'
        else:
            dpm = 'Выключено'
        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n⛏ <b>Статус копания:</b> <i>{dpm}</i>\n<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}\n\n<i><emoji document_id=5452069934089641166>❓</emoji> Чтобы изменить задержку атаки напишите:\n</i><code>.asdly [задержка]</code>",
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка копания ',
                        'callback' : self.mdlym,
                    },
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.idd,
                    },
                ],
                [
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def iback(self,call:InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        if self.get('mm'):
            dpm = 'Включено'
        else:
            dpm = 'Выключено'

        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n⛏ <b>Статус копания:</b> <i>{dpm}</i>\n<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}",
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка копания ',
                        'callback' : self.mdlym,
                    },
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.idd,
                    },
                ],
                [
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def idd(self,call:InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Выкл/не выкл копание во время убийства босса',
                        'callback' : self.ibs
                    },
                ],
                [
                    {
                        'text' : 'Копание после убийства босса',
                        'callback' : self.ibg,
                    },
                ],
                [
                    {
                        'text' : 'Копание после FloodWait',
                        'callback' : self.ifs,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.iback,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def ibg(self,call:InlineCall):
        self.set('ag', not self.get('ag'))
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Выкл/не выкл копание во время убийства босса',
                        'callback' : self.ibs
                    },
                ],
                [
                    {
                        'text' : 'Копание после убийства босса',
                        'callback' : self.ibg,
                    },
                ],
                [
                    {
                        'text' : 'Копание после FloodWait',
                        'callback' : self.ifs,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.iback,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def ibs(self,call:InlineCall):
        self.set('as', not self.get('as'))
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Выкл/не выкл копание во время убийства босса',
                        'callback' : self.ibs
                    },
                ],
                [
                    {
                        'text' : 'Копание после убийства босса',
                        'callback' : self.ibg,
                    },
                ],
                [
                    {
                        'text' : 'Копание после FloodWait',
                        'callback' : self.ifs,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.iback,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def ifs(self,call:InlineCall):
        self.set('fw', not self.get('fw'))
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Выкл/не выкл копание во время убийства босса',
                        'callback' : self.ibs
                    },
                ],
                [
                    {
                        'text' : 'Копание после убийства босса',
                        'callback' : self.ibg,
                    },
                ],
                [
                    {
                        'text' : 'Копание после FloodWait',
                        'callback' : self.ifs,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.iback,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
         