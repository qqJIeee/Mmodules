from asyncio import sleep
from .. import loader, utils
import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
import inspect
from ..inline.types import InlineCall


@loader.tds
class mattk(loader.Module):
    '''Модуль для автоматической атаки боссов в боте MineEvo'''
    strings = {
        "name" : "mattk"
    }

    async def client_ready(self,client, db):
        self.client = client
        self.hmtk = False
        self.tttk = False

        s = self.get('dly')
        if s == None:
            self.set('dly', 1.0)

        s = self.get('autk')
        if s == None:
            self.set("autk", False)
    @loader.command()
    async def attk(self,message):
        '''Вкл/выкл автоатаку'''
        self.set('autk', not self.get('autk'))
        if self.get('autk'):
            await utils.answer(message, "<b><emoji document_id=5463277406435422003>🗡</emoji> Автоатака включена</b>")
        else:
            await utils.answer(message, "<b><emoji document_id=5463277406435422003>🗡</emoji> Автоатака выключено</b>")

    @loader.command(alias='asd')
    async def asdly(self,message):
        ''' - Задержка атаки\n[Время]'''
        args = utils.get_args_raw(message)
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        try:
            args = float(args)
            self.set('dly', args)
            await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b>Успешно!\nЗадержка атаки изменена на {args}</b> ")
        except ValueError:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nУкажите число в значении!</b>")

    @loader.watcher()
    async def watcher(self,message):
        dly = self.get('dly', None)
        if message.chat_id == 5522271758 and "🔶 Ты выбрал босса" in message.raw_text:
            if self.get('autk'):
                self.tttk = True
                if not self.hmtk:
                    self.hmtk = True
                    if self.get('autk'):
                        while self.tttk:
                            await self.client.send_message("@mine_evo_bot", "Атк")
                            await asyncio.sleep(dly)
                        else:
                            self.hmtk = False   
        if message.chat_id == 5522271758 and "для атаки выбери босса" in message.raw_text:
            self.tttk = False
    @loader.command()
    async def mainfo(self,message):
        '''- Информация модуля mattk'''
        if self.get('autk'):
            aa = 'Включена'
        else:
            aa = 'Выключена'
        await self.inline.form(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка атаки: </b><code>{self.get('dly')}</code>\n<b><emoji document_id=5463277406435422003>🗡</emoji> Статус атаки: </b><i>{aa}</i>",
            message=message,
            reply_markup=[
                [
                    {
                        'text' : '🗡 Вкл/выкл атаку',
                        'callback' : self.matutk
                    },
                    {
                        'text' : '⏱ Задержка атаки',
                        'callback' : self.mdlya
                    }
                ],
                [
                    {
                        'text' : "🔻 Закрыть",
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def matutk(self,call:InlineCall):
        self.set('autk', not self.get('autk'))
        if self.get('autk'):
            aa = 'Включена'
        else:
            aa = 'Выключена'
        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка атаки: </b><code>{self.get('dly')}</code>\n<b><emoji document_id=5463277406435422003>🗡</emoji> Статус атаки: </b><i>{aa}</i>",
            reply_markup=[
                [
                    {
                        'text' : '🗡 Вкл/выкл атаку',
                        'callback' : self.matutk
                    },
                    {
                        'text' : '⏱ Задержка атаки',
                        'callback' : self.mdlya
                    }
                ],
                [
                    {
                        'text' : "🔻 Закрыть",
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def mdlya(self,call: InlineCall):
        if self.get('autk'):
            aa = 'Включена'
        else:
            aa = 'Выключена'
        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка атаки: </b><code>{self.get('dly')}</code>\n<b><emoji document_id=5463277406435422003>🗡</emoji> Статус атаки: </b><i>{aa}</i>\n\n<i><emoji document_id=5452069934089641166>❓</emoji> Чтобы изменить задержку атаки напишите:\n</i><code>.asdly [задержка]</code>",
            reply_markup=[
                [
                    {
                        'text' : '🗡 Вкл/выкл атаку',
                        'callback' : self.matutk
                    },
                    {
                        'text' : '⏱ Задержка атаки',
                        'callback' : self.mdlya
                    }
                ],
                [
                    {
                        'text' : "🔻 Закрыть",
                        'action' : 'close'
                    }
                ]
            ]
        )