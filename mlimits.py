from asyncio import sleep
from .. import loader, utils
import asyncio
import re
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions, types, errors
from ..inline.types import InlineCall
import inspect


@loader.tds
class mlimits(loader.Module):
    '''Модуль для автоматического перевода лимитов в боте MineEvo'''
    strings = {
        "name" : "mlimits",
    }
    async def client_ready(self):
        self.bb = False
        self.limitsx = False

        s = self.get('dly')
        if s == None:
            self.set('dly', 2.0)
        
        s = self.get('ag', None)
        if s == None:
            self.set('ag', False)

        s = self.get('as', None)
        if s == None:
            self.set('as', False)
        
        s = self.get('fw', None)
        if s == None:
            self.set('fw', False)

        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "hikka-logs",
            "Логи юзербота",
            silent=True,
            archive=False,
            _folder="hikka",
        )


        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "mlimits",
            "Группа для работы модуля mlimits",
            silent=True,
            archive=True,
            _folder="hikka",
        )
        

        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel='mlimits',
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="EVO",
            )
        )
    @loader.command()
    async def mlp(self,message):
        '''- Перевод лимитов\n[ник игрока] [количество лимитов]'''
        args = utils.get_args_split_by(message, " ")
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        if len(args) == 1:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВведите количество лимитов</b>")
        if not args:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВведите ник игрока и и количество лимитов</b>")
        if len(args) > 2:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВы ввели слишком много аргументов</b>")
        if len(args) == 2:
            player = args[0]
            self.db.set(self.name, "args1",args[1])
            self.db.set(self.name, "player",player)
            limits = int(args[1])
            self.db.set(self.name, "limitsf", args[1])
            limitp = self.get("Sum", None)
            limitsf = self.get('limitsf')
            if limitp == None:
                await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nУстановите сумму для проверки лимита</b>")
            else:
                limitsr = 0
                self.limitsx = True
                await asyncio.sleep(1)
                await self.client.send_message("@mine_evo_bot", f"Перевести {player} {limitp}")
                await utils.answer(message, f"<emoji document_id=5215239948420003628>💵</emoji> <b>Начинаю перевод лимитов игроку</b> <code>{player}</code> <b>:</b> {limits}")
                if self.limitsx:
                    while self.limitsx:
                        dly = self.get('dly')
                        limits -= 1
                        limitsr += 1
                        limitss = self.db.get(self.name, "limitss","")
                        self.db.set(self.name, 'limitsr',limitsr)
                        if limits == 0:
                            self.limitsx = False
                        try:
                            await self.client.send_message("mlimits", f"Перевести {player} {limitss}")
                            await asyncio.sleep(dly)
                        except errors.FloodWaitError as f:
                            self.limitsx = False
                            see = se + 5
                            if self.get('fw'):
                                await asyncio.sleep(see)
                                await self.mcon(message)
                        
                    if limits <= 0:
                        await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> <b>Все лимиты игроку <code>{player}</code> переведены:</b> <code>{limitsf}</code>")
                    limits = args[1]
                    limmmm = int(limits) - int(limitsr)
                    self.db.set(self.name, "limmm",limmmm)
                    
                    
                else:
                    return
    @loader.command()
    async def mstop(self,message):
        '''- Остановить перевод лимитов'''
        self.limitsx = False
        await utils.answer(message, "<emoji document_id=5447644880824181073>⚠️</emoji> Вы остановили перевод лимитов")
    @loader.command()
    async def mcon(self,message):
        '''- Продолжить переводить лимиты после перезапуска хикки/фв и т.д.''' 
        limmm = self.db.get(self.name, "limmm",0)
        limitsr = self.db.get(self.name, "limitsr",0)
        limitsf = self.db.get(self.name, "limitsf",0)
        player = self.db.get(self.name, "player","")
        args = self.db.get(self.name, "args1", None)
        limitp = self.get('Sum', None)
        limitsf = self.get('limitsf')
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if limitp == None:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nУстановите сумму для проверки лимита</b>")
        else:
            limmm = int(limitsf) - int(limitsr)
            limits = limmm
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
            if args:
                cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
            if limits > 0:
                self.limitsx = True
                await asyncio.sleep(1)
                await self.client.send_message("@mine_evo_bot", f"Перевести {player} {limitp}")
                await self.client.send_message(message.chat_id, f"<emoji document_id=5215239948420003628>💵</emoji> Продолжаю перевод лимитов игроку <code>{player}</code>\nОсталось перевести : <code>{limmm}</code>")
                while self.limitsx:
                    dly = self.get('dly')
                    limits -= 1
                    limitsr += 1 
                    self.db.set(self.name, 'limitsr',limitsr)
                    limitsx = self.get("limitsx",0)
                    if limits == 0:
                        self.limitsx = False
                    limitss = self.db.get(self.name, "limitss", "")
                    try:
                        await self.client.send_message("mlimits", f"Перевести {player} {limitss}")
                        await asyncio.sleep(dly)
                    except errors.FloodWaitError as f:
                        self.limitsx = False
                        see = se + 5
                        if self.get('fw'):
                            await asyncio.sleep(see)
                            await self.mcon(message)
                if limits <= 0:
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> <b>Все лимиты игроку <code>{player}</code> переведены:</b> <code>{limitsf}</code>")
                limits = limmm
                limmmm = int(limits) - int(limitsr)
                self.db.set(self.name,"limmm", limmmm)
            else:
                await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВсе лимиты переведены</b>")
    @loader.command()
    async def lchk(self,message):
        '''- Посмотреть сколько осталось перевести лимитов и времени до конца перевода'''
        player = self.db.get(self.name, "player","")
        limitsr = self.db.get(self.name, "limitsr",0)
        limitsf = self.db.get(self.name, 'limitsf',0)
        limitsr = int(limitsf) - int(limitsr)
        dly = self.get('dly')
        time = limitsr * dly
        ss = int(time) 
        sss = ss % 60
        mm = ss // 60
        hh = ss // 3600 
        dd = ss // 86400
        ww = ss // 604800
        mmth = ss // 2592000
        y = ss // 31536000
        mmm = mm % 60
        hhh = hh % 24
        ddd = dd % 7
        www = ww % 4.28
        mmmth = mmth % 12
        y = round(y)
        mmm = round(mmm)
        sss = round(sss)
        hhh = round(hhh)
        ddd = round(ddd)
        www = round(www)
        mmmth = round(mmmth)
        mm = round(mm)
        hh = round(hh)
        dd = round(dd)
        ww = round(ww)
        mmth = round(mmth)
        if ss > 2592000:
            mmth = int(dd) / 30
        mmth = round(mmth, 1)
        if mm < 1:
            await utils.answer(message, f"<b><emoji document_id=5215239948420003628>💵</emoji> Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n<emoji document_id=5981043230160981261>⏱</emoji> <b>Осталось времени</b> : <i>{sss}с.</i>")
        if hh < 1 and mm > 0:
            await utils.answer(message, f"<b><emoji document_id=5215239948420003628>💵</emoji> Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n<emoji document_id=5981043230160981261>⏱</emoji> <b>Осталось времени</b> : <i>{mmm}мин. {sss}с.</i>")
        if dd < 1 and hh > 0 : 
            await utils.answer(message, f"<b><emoji document_id=5215239948420003628>💵</emoji> Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n<emoji document_id=5981043230160981261>⏱</emoji> <b>Осталось времени</b> : <i>{hhh}ч. {mmm}мин. {sss}с.</i>")
        if ww < 1 and dd > 0:
            await utils.answer(message, f"<b><emoji document_id=5215239948420003628>💵</emoji> Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n<emoji document_id=5981043230160981261>⏱</emoji> <b>Осталось времени</b> : <i>{ddd}д. {hhh}ч. {mmm}мин. {sss}с.</i>")
        if mmth < 1 and ww > 0:
            await utils.answer(message, f"<b><emoji document_id=5215239948420003628>💵</emoji> Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n<emoji document_id=5981043230160981261>⏱</emoji> <b>Осталось времени</b> : <i>{www}нед. {ddd}д. {hhh}ч. {mmm}мин. {sss}с.</i>")
        if y < 1 and mmth > 0:
            await utils.answer(message, f"<b><emoji document_id=5215239948420003628>💵</emoji> Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n<emoji document_id=5981043230160981261>⏱</emoji> <b>Осталось времени</b> : <i>{mmmth}мес. {www}нед. {ddd}д. {hhh}ч. {mmm}мин. {sss}с.</i>")
        if y > 0:
            await utils.answer(message, f"<b><emoji document_id=5215239948420003628>💵</emoji> Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n<emoji document_id=5981043230160981261>⏱</emoji> <b>Осталось времени</b> : <i>{y}г. {mmmth}мес. {www}нед. {ddd}д. {hhh}ч. {mmm}мин. {sss}с.</i>")
    @loader.watcher()
    async def lim(self,message):
        dly = self.get("dly")
        if message.chat_id == 5522271758 and "можно перевести максимум" in message.raw_text:
            pattern = "можно перевести максимум(.*?)$"
            match = re.search(pattern, message.raw_text, re.DOTALL)
            if match:
                limitss = match.group(1)
                limitsss = limitss.replace("$","") 
                self.db.set(self.name,"limitss",limitsss)
    @loader.watcher()
    async def bosses_fw(self,message):
        dly = self.get("dly")
        if self.get('as'):
            if self.limitsx:
                if message.chat_id == 5522271758 and "🔶 Ты выбрал босса" in message.raw_text:
                    self.limitsx = False
                    self.bb = True
        if self.get('ag'):
            if self.bb:
                if message.chat_id == 5522271758 and "для атаки выбери босса" in message.raw_text:
                    self.bb = False
                    await asyncio.sleep(dly)
                    await self.mcon(message)

    @loader.command()
    async def lautoset(self,message):
        '''- Автоматически устанавливать лимит\n[Ник игрока] [Задержка]'''
        args = utils.get_args_split_by(message, " ")
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        if len(args) == 1:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВведите задержку</b>")
        if not args:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВведите ник игрока и задержку</b>")
        if len(args) > 2:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВы ввели слишком много аргументов</b>")
        if len(args) == 2:
            chel = args[0]
            time = args[1]
            dly = self.get("dly")
            limitsf = self.db.get(self.name, "limitsf", None)
            limitsr = self.db.get(self.name, "limitsr", None)
            limitsf = int(limitsf) - int(limitsr)
            kolvo = int(limitsf) / (int(time) / int(dly))
            kolvo = round(int(kolvo))
            time = str(time)
            self.set("qq",chel)
            self.db.set(self.name, "tt", time)
            limitp = self.get("Sum")
            self.limitsxx = True
            timee = time[-1]
            if timee in ['1']:
                await self.client.send_message(message.peer_id, f"<emoji document_id=5332533929020761310>✅</emoji> <b> Автоматическая установка лимита игроку <code>{chel}</code> раз в <code>{time}</code> секунду <code>{kolvo}</code> раз начата</b>")
            if timee in ['2', '3', '4']:
                await self.client.send_message(message.peer_id, f"<emoji document_id=5332533929020761310>✅</emoji> <b> Автоматическая установка лимита игроку <code>{chel}</code> раз в <code>{time}</code> секунды <code>{kolvo}</code> раз начата</b>")
            if timee in ['5', '6', '7', '8', '9', '0']:
                await self.client.send_message(message.peer_id, f"<emoji document_id=5332533929020761310>✅</emoji> <b> Автоматическая установка лимита игроку <code>{chel}</code> раз в <code>{time}</code> секунд <code>{kolvo}</code> раз начата </b>")
            time = int(time)
            if self.limitsxx:
                while self.limitsxx:
                    kolvo -= 1 
                    if kolvo == 0:
                        self.limitsxx = False
                    await self.client.send_message("@mine_evo_bot", f"Перевести {chel} {limitp}")
                    await asyncio.sleep(time)
    @loader.command()
    async def lastop(self,message):
        '''Остановить автоматическую установку лимита'''
        self.limitsxx = False
        await utils.answer(message, "<emoji document_id=5332533929020761310>✅</emoji> Автоматическая установка лимита остановлена")
    @loader.command(alias = 'lsc')
    async def lscfg(self,message: Message):
        '''- Установить значение в конфиг\n[Название] [Значение]\nНе работат с параметром cmt'''
        args = utils.get_args_split_by(message, " ")
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        else:
            await utils.answer(message, f'<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | {cmd}\nУкажите аргументы')
        if len(args) == 1:
            await utils.answer(message, f'<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | {cmd}\nВы указали только один аргумент, а нужно два')
        if len(args) > 2:
            await utils.answer(message, f'<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | {cmd}\nВы указали больше двух аргументов')
        pp = args[0]
        zz = args[1]
        if pp == "dly":
            try:
                zz = float(zz)
                self.set("dly",zz)
                await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b>Успешно!\nПараметр {pp} изменён на {zz}</b> ")
            except ValueError:
                await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nУкажите число в значении!</b>")

        if pp == "sm":
            self.set("Sum" ,zz)
            await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b>Успешно!\nПараметр Sum изменён на {zz}</b> ")

        if pp not in ['sm', 'dly']:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nДанного параметра не существует!</b>")

    @loader.command()
    async def mlcfg(self,message):
        '''Конфиг модуля mlimits'''
        if self.get('ag'):
            dpg = ' ▫️ <i>Продолжать перевод лимитов после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать перевод лимитов во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Продолжать перевод лимитов после FloodWait</i>\n'
        else: 
            dpf = ''

        if self.limitsx:
            dpl = '<i>Включён</i>'
        else:
            dpl = '<i>Выключен</i>'

        await self.inline.form(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка перевода лимитов: <code>{self.get('dly')}</code>\n<b><emoji document_id=5215239948420003628>💵</emoji> Сумма проверки лимита</b>: {self.get('Sum')}\n<emoji document_id=5416117059207572332>➡️</emoji> Перевод лимитов: </b><i>{dpl}</i>\n➕ <b>Дополнительные параметры:</b>\n{dpg}{dps}{dpf}",
            message=message,
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка перевода лимитов',
                        'callback' : self.idly,
                    },
                    {
                        'text' : '💵 Сумма проверки',
                        'callback' : self.lsm,
                    },
                ],
                [
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.iddl,
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
    async def ibackl(self,call:InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Продолжать перевод лимитов после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать перевод лимитов во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Продолжать перевод лимитов после FloodWait</i>\n'
        else: 
            dpf = ''

        if self.limitsx:
            dpl = '<i>Включён</i>'
        else:
            dpl = '<i>Выключен</i>'

        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка перевода лимитов: <code>{self.get('dly')}</code>\n<b><emoji document_id=5215239948420003628>💵</emoji> Сумма проверки лимита</b>: {self.get('Sum')}\n<emoji document_id=5416117059207572332>➡️</emoji> Перевод лимитов: </b><i>{dpl}</i>\n➕ <b>Дополнительные параметры:</b>\n{dpg}{dps}{dpf}",
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка перевода лимитов',
                        'callback' : self.idly,
                    },
                    {
                        'text' : '💵 Сумма проверки',
                        'callback' : self.lsm,
                    },
                ],
                [
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.iddl,
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
    async def idly(self,call:InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Продолжать перевод лимитов после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать перевод лимитов во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Продолжать перевод лимитов после FloodWait</i>\n'
        else: 
            dpf = ''
        if self.limitsx:
            dpl = '<i>Включён</i>'
        else:
            dpl = '<i>Выключен</i>'
        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка перевода лимитов: <code>{self.get('dly')}</code>\n<b><emoji document_id=5215239948420003628>💵</emoji> Сумма проверки лимита</b>: {self.get('Sum')}\n<emoji document_id=5416117059207572332>➡️</emoji> Перевод лимитов: </b><i>{dpl}</i>\n➕ <b>Дополнительные параметры:</b>\n{dpg}{dps}{dpf}\n\n<i><emoji document_id=5452069934089641166>❓</emoji> Чтобы изменить задержку перевода лимитов напишите:\n</i><code>.lscfg dly [задержка]</code>",
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка перевода лимитов',
                        'callback' : self.idly,
                    },
                    {
                        'text' : '💵 Сумма проверки',
                        'callback' : self.lsm,
                    },
                ],
                [
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.iddl,
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
    async def iddl(self,call: InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Продолжать перевод лимитов после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать перевод лимитов во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Продолжать перевод лимитов после FloodWait</i>\n'
        else: 
            dpf = ''
        await call.edit(
            text=f'➕ <b>Дополнительные параметры:</b>:\n{dpg}{dps}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Перевод лимитов после убийства босса',
                        'callback' : self.ibgl,
                    },
                ],
                [
                    {
                        'text' : 'Выкл/не выкл перевод лимитов во время убийства босса',
                        'callback' : self.ibsl
                    },
                ],
                [
                    {
                        'text' : 'Перевод лимитов после FloodWait',
                        'callback' : self.ifsl,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.ibackl,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def ibgl(self,call:InlineCall):
        self.set('ag', not self.get('ag'))
        if self.get('ag'):
            dpg = ' ▫️ <i>Продолжать перевод лимитов после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать перевод лимитов во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Продолжать перевод лимитов после FloodWait</i>\n'
        else: 
            dpf = ''
        await call.edit(
            text=f'➕ <b>Дополнительные параметры:</b>:\n{dpg}{dps}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Перевод лимитов после убийства босса',
                        'callback' : self.ibgl,
                    },
                ],
                [
                    {
                        'text' : 'Выкл/не выкл перевод лимитов во время убийства босса',
                        'callback' : self.ibsl
                    },
                ],
                [
                    {
                        'text' : 'Перевод лимитов после FloodWait',
                        'callback' : self.ifsl,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.ibackl,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def ibsl(self,call:InlineCall):
        self.set('as', not self.get('as'))
        if self.get('ag'):
            dpg = ' ▫️ <i>Продолжать перевод лимитов после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать перевод лимитов во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Продолжать перевод лимитов после FloodWait</i>\n'
        else: 
            dpf = ''
        await call.edit(
            text=f'➕ <b>Дополнительные параметры:</b>:\n{dpg}{dps}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Перевод лимитов после убийства босса',
                        'callback' : self.ibgl,
                    },
                ],
                [
                    {
                        'text' : 'Выкл/не выкл перевод лимитов во время убийства босса',
                        'callback' : self.ibsl
                    },
                ],
                [
                    {
                        'text' : 'Перевод лимитов после FloodWait',
                        'callback' : self.ifsl,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.ibackl,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def ifsl(self,call:InlineCall):
        self.set('fw', not self.get('fw'))
        if self.get('ag'):
            dpg = ' ▫️ <i>Продолжать перевод лимитов после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать перевод лимитов во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Продолжать перевод лимитов после FloodWait</i>\n'
        else: 
            dpf = ''
        await call.edit(
            text=f'➕ <b>Дополнительные параметры:</b>:\n{dpg}{dps}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Перевод лимитов после убийства босса',
                        'callback' : self.ibgl,
                    },
                ],
                [
                    {
                        'text' : 'Выкл/не выкл перевод лимитов во время убийства босса',
                        'callback' : self.ibsl
                    },
                ],
                [
                    {
                        'text' : 'Перевод лимитов после FloodWait',
                        'callback' : self.ifsl,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.ibackl,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def lsm(self,call:InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Продолжать перевод лимитов после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать перевод лимитов во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Продолжать перевод лимитов после FloodWait</i>\n'
        else: 
            dpf = ''

        if self.limitsx:
            dpl = '<i>Включён</i>'
        else:
            dpl = '<i>Выключен</i>'

        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка перевода лимитов: <code>{self.get('dly')}</code>\n<b><emoji document_id=5215239948420003628>💵</emoji> Сумма проверки лимита</b>: {self.get('Sum')}\n<emoji document_id=5416117059207572332>➡️</emoji> Перевод лимитов: </b><i>{dpl}</i>\n➕ <b>Дополнительные параметры:</b>\n{dpg}{dps}{dpf}\n\n<i><emoji document_id=5452069934089641166>❓</emoji> Чтобы изменить сумму проверки лимитов напишите:\n</i><code>.lscfg sm [Сумма]</code>",
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка перевода лимитов',
                        'callback' : self.idly,
                    },
                    {
                        'text' : '💵 Сумма проверки',
                        'callback' : self.lsm,
                    },
                ],
                [
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.iddl,
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
