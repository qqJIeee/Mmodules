from asyncio import sleep
from .. import loader, utils
import asyncio
import re
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions, types
from ..inline.types import InlineCall

@loader.tds
class mlimits(loader.Module):
    '''dev - @Kepperok'''
    strings = {
        "name" : "mlimits",
        "Sum" : "Поставьте сумму которой вы будете проверять лимит\nЧтобы изменить через lscfg пишите sm",
        "dly" : "Задержка переводов лимитов",
        "lct" : "Включить/выключить автовыполнение команды 'mcon'\nas - Выключать команду во время убийства босса\nag - Включать команду после убийства босса\nfw - Включать команду после флудвейта"
    }
    async def client_ready(self):
        
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
                channel=self._backup_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="EVO",
            )
        )
    def __init__(self):
        self.bb = False
        self.limitsx = False
        self.fw = False
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "Sum", "",
                lambda: self.strings,
                validator=loader.validators.String()
            ),
            loader.ConfigValue(
                "dly", 2.0,
                lambda: self.strings,
                validator=loader.validators.Float()
            ),
            loader.ConfigValue(
                "cmt", ["fw"],
                lambda: self.strings,
                validator=loader.validators.MultiChoice(["ag", "as", "fw"])
            )
        )

    @loader.command()
    async def mlhelp(self,message):
        ''' - Помощь для команды mlimits'''
        await self.inline.form(
            text="<b>Ку! Это помощь для модуля mlimits\n\nНажмите продолжить</b>",
            message=message,
            reply_markup=[
                [
                    {
                        'text' : 'Продолжить',
                        'callback' : self.hnext,
                    },
                ],
                [
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    }
                ]
            ]
        )
    
    @loader.command()
    async def mlp(self,message):
        '''- Перевод лимитов\n[ник игрока] [количество лимитов]'''
        await self.www(message)
        dly = self.config["dly"]
        args = utils.get_args_split_by(message, " ")
        if len(args) == 1:
            await utils.answer(message, "🚫 <b>| Ошибка!\n👉 | Введите количество лимитов</b>")
        if not args:
            await utils.answer(message, f"🚫 <b>| Ошибка!\n👉 | Введите имя пользователя и количество лимитов</b>")
        if len(args) > 2:
            await utils.answer(message, "🚫 <b>| Ошибка!\n👉 | Вы ввели слишком много аргументов</b>")
        if len(args) == 2:
            player = args[0]
            self.db.set(self.name, "args1",args[1])
            self.db.set(self.name, "player",player)
            limits = int(args[1])
            self.db.set(self.name, "limitsf", args[1])
            limitp = self.config["Sum"]
            limitsr = 0
            self.limitsx = True
            await asyncio.sleep(1)
            await self.client.send_message("@mine_evo_bot", f"Перевести {player} {limitp}")
            await utils.answer(message, f"💸 <b>Начинаю перевод лимитов игроку</b> <code>{player}</code> <b>:</b> {limits}")
            if self.limitsx:
                while self.limitsx:
                    limits -= 1
                    limitsr += 1
                    limitss = self.db.get(self.name, "limitss","")
                    self.db.set(self.name, 'limitsr',limitsr)
                    if limits == 0:
                        self.limitsx = False
                    await self.client.send_message("mlimits", f"Перевести {player} {limitss}")
                    await asyncio.sleep(dly)
                limits = args[1]
                limmmm = int(limits) - int(limitsr)
                self.db.set(self.name, "limmm",limmmm)
                if limmmm == 0:
                    await self.client.send_message(message.peer_id, f"✅ <b>Все лимиты игроку <code>{player}</code> переведены:</b> <code>{limits}</code>")
                if message.out:
                    await message.delete()
                
                
            else:
                return
    @loader.command()
    async def mstop(self,message):
        '''- Остановить перевод лимитов'''
        self.limitsx = False
        await self.client.send_message(message.peer_id, "⚠️ Вы остановили перевод лимитов")
        await message.delete()
    @loader.command()
    async def mcon(self,message):
        '''- Продолжить переводить лимиты после перезапуска хикки/фв и т.д.''' 
        await self.www(message)
        limmm = self.db.get(self.name, "limmm",0)
        limitsr = self.db.get(self.name, "limitsr",0)
        limitsf = self.db.get(self.name, "limitsf",0)
        player = self.db.get(self.name, "player","")
        args = self.db.get(self.name, "args1", None)
        limitp = self.config["Sum"]
        dly = self.config["dly"]
        limmm = int(limitsf) - int(limitsr)
        self.limitsx = True
        limits = limmm
        await asyncio.sleep(1)
        await self.client.send_message("@mine_evo_bot", f"Перевести {player} {limitp}")
        await utils.answer(message, f"💸 Продолжаю перевод лимитов игроку <code>{player}</code>\nОсталось перевести : <code>{limmm}</code>")
        if self.limitsx:
            while self.limitsx:
                limits -= 1
                limitsr += 1 
                self.db.set(self.name, 'limitsr',limitsr)
                limitsx = self.get("limitsx",0)
                if limits == 0:
                    self.limitsx = False
                limitss = self.db.get(self.name, "limitss", "")
                await self.client.send_message("mlimits", f"Перевести {player} {limitss}")
                await asyncio.sleep(dly)
            limits = limmm
            limmmm = int(limits) - int(limitsr)
            self.db.set(self.name,"limmm", limmmm)
            if limmmm == 0:
                await self.client.send_message(message.peer_id, f"✅ <b>Все лимиты игроку <code>{player}</code> переведены:</b> <code>{limits}</code>")
            if message.out:
                await message.delete()
    @loader.command()
    async def lchk(self,message):
        '''- Посмотреть сколько осталось перевести лимитов и времени до конца перевода'''
        player = self.db.get(self.name, "player","")
        limitsr = self.db.get(self.name, "limitsr",0)
        limitsf = self.db.get(self.name, 'limitsf',0)
        limitsr = int(limitsf) - int(limitsr)
        dly = self.config["dly"]
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
            await utils.answer(message, f"<b>💸 Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n⏱ <b>Осталось времени</b> : <i>{sss}с. </i>\n<i>Секунд : </i>{ss}")
        if hh < 1 and mm > 0:
            await utils.answer(message, f"<b>💸 Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n⏱ <b>Осталось времени</b> : <i>{mmm}мин. {sss}с.</i>\n<i>Минут</i> : {mm}\n<i>Секунд : </i>{ss}")
        if dd < 1 and hh > 0 : 
            await utils.answer(message, f"<b>💸 Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n⏱ <b>Осталось времени</b> : <i>{hhh}ч. {mmm}мин. {sss}с.</i>\n<i>Часов : {hh}</i>\n<i>Минут</i> : {mm}\n<i>Секунд : </i>{ss}")
        if ww < 1 and dd > 0:
            await utils.answer(message, f"<b>💸 Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n⏱ <b>Осталось времени</b> : <i>{ddd}д. {hhh}ч. {mmm}мин. {sss}с.</i>\n<i>Дней :</i> {dd}\n<i>Часов : {hh}</i>\n<i>Минут</i> : {mm}\n<i>Секунд : </i>{ss}")
        if mmth < 1 and ww > 0:
            await utils.answer(message, f"<b>💸 Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n⏱ <b>Осталось времени</b> : <i>{www}нед. {ddd}д. {hhh}ч. {mmm}мин. {sss}с.</i>\n<i>Недель : </i>{ww}\n<i>Дней :</i> {dd}\n<i>Часов : {hh}</i>\n<i>Минут</i> : {mm}\n<i>Секунд : </i>{ss}")
        if y < 1 and mmth > 0:
            await utils.answer(message, f"<b>💸 Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n⏱ <b>Осталось времени</b> : <i>{mmmth}мес. {www}нед. {ddd}д. {hhh}ч. {mmm}мин. {sss}с.</i>\n<i>Месяцев : </i>{mmth}\n<i>Недель : </i>{ww}\n<i>Дней :</i> {dd}\n<i>Часов : {hh}</i>\n<i>Минут</i> : {mm}\n<i>Секунд : </i>{ss}")
        if y > 0:
            await utils.answer(message, f"<b>💸 Осталось переводить игроку <code>{player}</code> : <code>{limitsr}</code>/</b><code>{limitsf}</code>\n⏱ <b>Осталось времени</b> : <i>{y}г. {mmmth}мес. {www}нед. {ddd}д. {hhh}ч. {mmm}мин. {sss}с.</i>\n<i>Лет : </i>{y}\n<i>Месяцев : </i>{mmth}\n<i>Недель : </i>{ww}\n<i>Дней :</i> {dd}\n<i>Часов : {hh}</i>\n<i>Минут</i> : {mm}\n<i>Секунд : </i>{ss}")
    @loader.watcher()
    async def lim(self,message):
        dly = self.config["dly"]
        if message.chat_id == 5522271758 and "можно перевести максимум" in message.raw_text:
            pattern = "можно перевести максимум(.*?)$"
            match = re.search(pattern, message.raw_text, re.DOTALL)
            if match:
                limitss = match.group(1)
                limitsss = limitss.replace("$","") 
                self.db.set(self.name,"limitss",limitsss)
    @loader.watcher()
    async def bosses_fw(self,message):
        dly = self.config["dly"]
        mid = self.db.get(self.name, "mid", None)
        ag = None
        ass = None
        for c in self.config["cmt"]:
            if c == "as":
                ass = True
            elif c == "ag":
                ag = True
            elif c == "fw":
                self.fw = True
        if self.bb:
            if self.limitsx:
                if message.chat_id == mid and "A wait of" in message.raw_text and "seconds is required" in message.raw_text:
                    fss = message.text.index("A wait of") + len("A wait of")
                    fsss = message.text.index("seconds is required")
                    fs = int(message.text[fss:fsss]) + 5
                    self.mm = False
                    await asyncio.sleep(fs)
                    await self.mcon(message)
                    await message.delete()
        if ass:
            if self.limitsx:
                if message.chat_id == 5522271758 and "🔶 Ты выбрал босса" in message.raw_text:
                    self.limitsx = False
                    self.bb = True
        if ag:
            if self.bb:
                if message.chat_id == 5522271758 and "для атаки выбери босса" in message.raw_text:
                    self.bb = False
                    await asyncio.sleep(dly)
                    await self.mcon(message)

    @loader.command()
    async def lautoset(self,message):
        '''- Автоматически устанавливать лимит\n[Ник игрока] [Задержка] [Количество]'''
        args = utils.get_args_split_by(message, " ")
        if len(args) == 1:
            await utils.answer(message, "🚫 <b>| Ошибка!\n👉 | Введите задержку и количество лимитов</b>")
        if not args:
            await utils.answer(message, "🚫 <b>| Ошибка!\n👉 | Введите имя пользователя задержку и количество</b>")
        if len(args) == 2:
            await utils.answer(message, "🚫 <b>| Ошибка!\n👉 | Введите количество</b>")
        if len(args) > 3:
            await utils.answer(message, "🚫 <b>| Ошибка!\n👉 | Вы ввели слишком много аргументов</b>")
        if len(args) == 3:
            chel = args[0]
            time = args[1]
            kolvo = args[2]
            time = str(time)
            kolvo = int(kolvo)
            self.set("qq",chel)
            limitp = self.config["Sum"]
            limitss = self.db.get(self.name, "limitss","")
            timee = time[-1]
            if timee in ['1']:
                await utils.answer(message, f"✅ Автоматическая установка лимита игроку <code>{chel}</code> раз в <code>{time}</code> секунду начата")
            if timee in ['2', '3', '4']:
                await utils.answer(message, f"✅ Автоматическая установка лимита игроку <code>{chel}</code> раз в <code>{time}</code> секунды начата")
            if timee in ['5', '6', '7', '8', '9', '0']:
                await utils.answer(message, f"✅ Автоматическая установка лимита игроку <code>{chel}</code> раз в <code>{time}</code> секунд начата")
            time = int(time)
            while kolvo > 0:
                kolvo -= 1 
                await self.client.send_message("@mine_evo_bot", f"Перевести {chel} {limitp}")
                await asyncio.sleep(time)
    async def www(self,message):
        chat_entity = await self.client.get_entity("hikka-logs")
        chat_id = chat_entity.id
        chat_id = '-100' + str(chat_id)
        self.db.set(self.name, "mid", int(chat_id))
    @loader.command(alias = 'lsc')
    async def lscfg(self,message: Message):
        '''- Установить значение в конфиг\n[Название] [Значение]\nНе работат с параметром cmt'''
        args = utils.get_args_split_by(message, " ")
        pp = args[0]
        zz = args[1]
        if pp == "dly":
            try:
                zz = float(zz)
                self.config["dly"] = zz
                await utils.answer(message, f"✅ <b>| Успешно!\n👉 | Параметр {pp} изменён на {zz}</b> ")
            except ValueError:
                await utils.answer(message, f"🚫 <b>| Ошибка!\n👉 | Укажите число в значении!</b>")

        if pp == "sm":
            self.config["Sum"] = zz
            await utils.answer(message, f"✅ <b>| Успешно!\n👉 | Параметр Sum изменён на {zz}</b> ")

    async def hnext(self, call: InlineCall):
        await call.edit(
            text="<b>1. Установите сумму для проверки лимита игрока(Свой лимит или 0.01 своего лимита). Сделать это можно через .lscfg(alias=lsc) параметр sm или через .config mlimits\n\n2. Установите задержку. Можно также через lscfg параметр dly или через .config\n\n3.Начните переводить лимиты командой .mlp\n\n4. Чтобы автоматически менялся лимит если игрок повышает уровень нужно написать команду .lautoset\n\n5. Советую ставить в lautoset 300 секунд т.е 5 минут\n\n6. Чтобы рассчитать количество в lautoset нужно:\n▫️  Вашу задержку которую вы пишете в lautoset разделить на задержку перевода лимитов(dly)\n▫️  Разделить количество лимитов которые вы переводите на то что у вас получилось в первом пункте\n\n7. Чтобы остановить перевод лимитов пишите .mstop | Продолжить .mcon\n\n Удачного пользования!</b>",
            reply_markup=[
                [
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    }
                ]
            ]
        )
