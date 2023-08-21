from asyncio import sleep
from .. import loader, utils
import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions, TelegramClient, errors
from ..inline.types import InlineCall



@loader.tds
class MevoMiner(loader.Module):
    strings = {
        "name" : "MevoMiner"
    }
    def __init__(self):
        self.mem = False
        self.mm = False
        self.fw = False
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "dly", 2.0,
                lambda: "Интервал копания",
                validator=loader.validators.Float()
            ),
            loader.ConfigValue(
                "cmt", ["fw"],
                lambda: "Включить/выключить автовыполнение команды 'mmm'\nas - Выключать во время убийства боссов\nag - Включать после убийства боссов\nfw - Включать после фв ",
                validator=loader.validators.MultiChoice(["ag", "as", "fw"])
            )
    )
    @loader.command()
    async def mehelp(self,message):
        '''- Помощь для модуля mevominer'''
        await self.inline.form(
            text='<b>Ку! Это помощь модуля Mevominer\n\nВ модуле всё понятно, но на всякий случай сделана эта команда\n\nЕсли вам всё в этом модуле понятно можете закрывать, ну а если нет нажмите продолжить</b>' ,
            message=message,
            reply_markup=[
                [
                    {
                        "text" : "Продолжить",
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
    async def mmm(self,message):
        '''- Включить/выключить копание'''
        await self.www(message)
        self.mm = not self.mm
        dly = self.config["dly"]
        if self.mm:
            await self.client.send_message(message.peer_id, "⛏ | <b>Вы начали копать</b>")
            await message.delete()
        else:
            await self.client.send_message(message.peer_id, "⛏ | <b>Вы перестали копать</b>")
            await message.delete()
        if self.mm:
            while self.mm:
                await self.client.send_message("@mine_evo_bot", "коп")
                await asyncio.sleep(dly)
                # except self.errors.FloodWaitError as e:
                #     e += 5
                #     asyncio.sleep(e)
                #     await self.mmm(message) 
        else:
            return
    @loader.watcher()
    async def watcher(self,message):
        ag = False
        ass = False
        for c in self.config["cmt"]:
            if c == "ag":
                ag = True
            elif c == "as":
                ass = True
            elif c == "fw":
                self.fw = True
        mid = self.db.get(self.name, "mid", None)
        dly = self.config["dly"]
        if self.fw:
            if self.mm:
                if message.chat_id == mid and "A wait of" in message.raw_text and "seconds is required" in message.raw_text:
                    fss = message.text.index("A wait of") + len("A wait of")
                    fsss = message.text.index("seconds is required")
                    fs = int(message.text[fss:fsss]) + 5
                    self.mm = False
                    await asyncio.sleep(fs)
                    await self.mmm(message)
                    await message.delete()
        if ass:
            if self.mm:
                if message.chat_id == 5522271758 and "🔶 Ты выбрал босса" in message.raw_text:
                    self.mem = True
                    await self.mmm(message)
        if ag:
            if self.mem:
                if message.chat_id == 5522271758 and "для атаки выбери босса" in message.raw_text:
                    self.mem = False
                    await asyncio.sleep(dly)
                    await self.mmm(message)
    @loader.command(alias = 'msc')
    async def miscfg(self,message: Message):
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
    async def www(self,message):
        chat_entity = await self.client.get_entity("hikka-logs")
        chat_id = chat_entity.id
        chat_id = '-100' + str(chat_id)
        self.db.set(self.name, "mid", int(chat_id))
    async def hnext(self, call: InlineCall):
        await call.edit(
            text="<b>1. Для начала поставьте задержку в конфиг - это можно сделать с помощью команды miscfg(alais=msc) параметр dly или же с помощью .cfg mevominer\n2. В конфиге параметре 'cmt' выберите дополнительные параметры:\n▫️  ag - Включает копание после убийтсва босса\n▫️  as - Выключает копание когда начинаешь убивать босса\n▫️  fw - Запускает копание после флудвейта\n3. Напишите .mmm и копание включится</b>",
            reply_markup=[
                [
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    }
                ]
            ]
        )