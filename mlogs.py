import asyncio
import re
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
import logging
import argparse
from asyncio import sleep
from .. import loader, utils
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)
@loader.tds
class mlogs(loader.Module):
    '''dev - @Kepperok'''
    strings = {
        "name" : "mlogs", 
        "kt" : "Включить/Выключить отправку сообщения о нахождении кт\n Похуй по сути,всё равно не работает",
        "rkt" : "Включить/Выключить отправку сообщения о нахождении ркт",
        "k" : "Включить/Выключить отправку о сообщения нахождении к",
        "rk" : "Включить/Выключить отправку о сообщения нахождении рк",
        "mif" : "Включить/Выключить отправку о сообщения нахождении миф",
        "kr" : "Включить/Выключить отправку о сообщения нахождении кр",
        "zv" : "Включить/Выключить отправку о сообщения нахождении зв",
        "trade" : "Включить/Выключить сообщения о отправке кейсов",
        "bosses" : "Включить/Выключить отправку награды с боссов",
        "boosters" : "Включить/Выключить отправку сообщения о нахождение бустеров"
    }
    async def client_ready(self):
        
        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "mlogs",
            "Группа для работы модуля mlog",
            silent=True,
            archive=True,
            _folder="hikka",
        )
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "kt", True,
                lambda: self.strings("kt"),
                validator=loader.validators.Boolean()
            ),
             loader.ConfigValue(
                "rkt", True,
                lambda: self.strings("rkt"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "k", True,
                lambda: self.strings("k"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "rk", True,
                lambda: self.strings("rk"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "mif", True,
                lambda: self.strings("mif"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "kr", True,
                lambda: self.strings("kr"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "zv", True,
                lambda: self.strings("zv"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "trade", True,
                lambda: self.strings("trade"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "bosses", True,
                lambda: self.strings("bosses"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "boosters", True,
                lambda: self.strings("boosters"),
                validator=loader.validators.Boolean()
            )
        )
            



    @loader.command()
    async def mlogs(self, message):
        "Управление модулем"
        await self.inline.form(
                text="Управление модулем mlogs",
                message=message,
                reply_markup=[
                    [
                            {
                                "text": " 📦 Кейсы",
                                "callback": self.icases,
                            },
                            {
                                "text" : " ⚡️ Бусты",
                                "callback" : self.iboost,
                            },
                    ],
                    [
                            {
                                "text": " 🗡 Боссы",
                                "callback": self.iboss,
                            },
                            {
                                "text" : " 💸 Перевод вам кейсов",
                                "callback" : self.itrade,
                            },
                    ],
                    [
                            {
                                "text": "🔻 Закрыть",
                                "action" : "close",
                            }
                    ],
                ],
          )  


    @loader.watcher()
    async def watcher(self, message):
        kt = self.config["kt"]
        rkt = self.config["rkt"]
        k = self.config["k"]
        rk = self.config["rk"]
        mif = self.config["mif"]
        kr = self.config["kr"]
        zv = self.config["zv"]
        trade = self.config["trade"]
        bosses = self.config["bosses"]
        boosters = self.config["boosters"]



        if kt == True:
            if message.chat_id == 5522271758 and "✉ Ты нашел(ла) конверт." in message.raw_text:
                await self.client.send_message("mlogs","✉️ Конверт +1" )
        if rkt == True:        
            if message.chat_id == 5522271758 and "🧧 Ты нашел(ла) редкий конверт." in message.raw_text:
                await self.client.send_message("mlogs", "🧧 Редкий Конверт +1")
        if k == True:                
            if message.chat_id == 5522271758 and "📦 Ты нашел(ла) Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "📦 Кейс +1")
        if rk == True:
            if message.chat_id == 5522271758 and "🗳 Ты нашел(ла) Редкий Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "🗳 Редкий Кейс +1")
        if mif == True:         
            if message.chat_id == 5522271758 and "🕋 Ты нашел(ла) Мифический Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "Грац! 🕋 Миф. Кейс +1!")
        if kr == True:
            if message.chat_id == 5522271758 and "💎 Ты нашел(ла) Кристальный Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "Congratulations! 💎 Кристальный кейс +1! ")
        if zv == True:
            if message.chat_id == 5522271758 and "💫" in message.raw_text:
                await self.client.send_message("mlogs", "🌌 Звездный Кейс +1")
        if trade == True:                
            if message.chat_id == 5522271758 and "передал(а) тебе" in message.raw_text:
                await self.client.send_message("mlogs", message.text)
        if bosses == True:
            if message.chat_id == 5522271758 and "побежден игроком" in message.raw_text:
                await self.client.send_message("mlogs", message.text)
        if boosters == True:
            if message.chat_id == 5522271758 and "ты нашел(ла)" in message.text and "бустер: Руда ×2.0!" in message.raw_text:
                    await self.client.send_message("mlogs", "⚡️ <b>Буст руды 2.0 </b><i>+1</i>")
            if message.chat_id == 5522271758 and "ты нашел(ла)" in message.text and "бустер: Деньги ×2.0!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст денег 2.0 </b><i>+1</i>")
            if message.chat_id == 5522271758 and "ты нашел(ла)" in message.text and "бустер: Деньги ×1.5!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст денег 1.5 </b><i>+1</i>")
            if message.chat_id == 5522271758 and "ты нашел(ла)" in message.text and "бустер: Руда ×1.5!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст руды 1.5 </b><i>+1</i>")
            if message.chat_id == 5522271758 and "ты нашел(ла)" in message.text and "бустер: Деньги ×2.5!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст денег 2.5 </b><i>+1</i>")
            if message.chat_id == 5522271758 and "ты нашел(ла)" in message.text and "бустер: Руда ×2.5!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст руды 2.5 </b><i>+1</i>")
            if message.chat_id == 5522271758 and "ты нашел(ла)" in message.text and "бустер: Деньги ×3.0!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст денег 3.0 </b><i>+1</i>")
            if message.chat_id == 5522271758 and "ты нашел(ла)" in message.text and "бустер: Руда ×3.0!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст руды 3.0 </b><i>+1</i>")




    async def icases(self, call: InlineCall):
        kt = self.config["kt"]
        rkt = self.config["rkt"]
        k = self.config["k"]
        rk = self.config["rk"]
        mif = self.config["mif"]
        kr = self.config["kr"]
        zv = self.config["zv"]
        await call.edit(
            text="Включить/выключить отправку о нахождении кейсов",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "👈🏼 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )
    async def ikt(self, call: InlineCall):
        self.config["kt"] = not self.config["kt"]
        kt = self.config["kt"]
        await call.answer(f"Отправка Конвертов {kt}")

    


    async def irkt(self, call: InlineCall):
        self.config["rkt"] = not self.config["rkt"]
        rkt = self.config["rkt"]
        await call.answer(f"Отправка Редких Конвертов {rkt}")


    async def ik(self, call: InlineCall):
        self.config["k"] = not self.config["k"]
        k = self.config["k"]
        await call.answer(f"Отправка Кейсов {k}")


    async def irk(self, call: InlineCall):
        self.config["rk"] = not self.config["rk"]
        rk = self.config["rk"]
        await call.answer(f"Отправка Редкий Кейсов {rk}")


    async def imif(self, call: InlineCall):
        self.config["mif"] = not self.config["mif"]
        mif = self.config["mif"]
        await call.answer(f"Отправка Мифических Кейсов {mif}")


    async def ikr(self, call: InlineCall):
        self.config["kr"] = not self.config["kr"]
        kr = self.config["kr"]
        await call.answer(f"Отправка Кристальных Кейсов {kr}")


    async def izv(self, call: InlineCall):
        self.config["zv"] = not self.config["zv"]
        zv = self.config["zv"]
        await call.answer(f"Отправка Звездных Кейсов {zv}")


    async def itrade(self, call: InlineCall):
        self.config["trade"] = not self.config["trade"]
        trade = self.config["trade"]
        await call.answer(f"Отправка {trade}")


    async def iboss(self, call: InlineCall):
        self.config["bosses"] = not self.config["bosses"]
        bosses = self.config["bosses"]
        await call.answer(f"Отправка награды с боссов {bosses}")


    async def iboost(self, call: InlineCall):
        self.config["boosters"] = not self.config["boosters"]
        boosters = self.config["boosters"]
        await call.answer(f"Отправка бустеров {boosters}")  
    async def iback(self, call: InlineCall):
        await call.edit(
                text="Управление модулем mlogs",
                reply_markup=[
                        [
                            {
                                "text": "📦 Кейсы",
                                "callback": self.icases,
                            },
                            {
                                "text" : "⚡️ Бусты",
                                "callback" : self.iboost,
                            },
                        ],
                        [
                            {
                                "text": "🗡 Боссы",
                                "callback": self.iboss,
                            },
                            {
                                "text" : "💸 Перевод вам кейсов",
                                "callback" : self.itrade,
                            },
                        ],
                        [
                            {
                                "text": "🔻 Закрыть",
                                "action" : "close",
                            }
                        ],
                    ],
            )   
                            