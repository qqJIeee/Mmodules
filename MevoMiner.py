from asyncio import sleep
from .. import loader, utils
import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions, TelegramClient, errors
from ..inline.types import InlineCall
import inspect

@loader.tds
class MevoMiner(loader.Module):
    '''Модуль для автоматического копание в боте MineEvo'''
    strings = {
        "name" : "MevoMiner"
    }
    async def client_ready(self,client,db):
        self.bb = False
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
        
        if self.get('mm'):
            await self.client.send_message(message.chat_id, "⛏ <b>Копание включено</b>")
            await message.delete()
        else:
            await self.client.send_message(message.chat_id, "⛏ <b>Копание выключено</b>")
            await message.delete()
        while self.get('mm'):
            dly = self.get('dly')
            try:
                await self.client.send_message("@mine_evo_bot", "коп")
                await asyncio.sleep(dly)
            except errors.FloodWaitError as f:
                self.set('mm', False)
                se = f.seconds 
                see = se + 5
                if self.get('fw'):
                    await asyncio.sleep(see)
                    await self.mmm(message)
    @loader.watcher()
    async def bosses_fw(self,message):
        dly = self.get('dly')
        
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
    async def emdly(self,message: Message):
        '''- Установить задержку копания [значение]'''
        args = utils.get_args_split_by(message, " ")
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        else:
            await utils.answer(message, f'<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | {cmd}\nУкажите значение которое хотите установить')
        if len(args) > 1:
            await utils.answer(message, f'<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | {cmd}\nВы указали больше одного аргумента')
        zz = args[0]    
        try:
            zz = float(zz)
            self.set('dly',zz)
            await utils.answer(message, f"✅ <b>Успешно!\nЗадержка копания изменена на {zz}</b> ")
        except ValueError:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji> <b>Ошибка | {cmd}\nУкажите число в значении!</b>")


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
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n⛏ <b>Статус копания:</b> <i>{dpm}</i>\n<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}\n\n<i><emoji document_id=5452069934089641166>❓</emoji> Чтобы изменить задержку копания напишите:\n</i><code>.emscfg dly [задержка]</code>",
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
         
