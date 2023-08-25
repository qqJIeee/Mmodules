import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
from asyncio import sleep
from .. import loader, utils
from ..inline.types import InlineCall


@loader.tds
class mlogs(loader.Module):
    '''Модуль для логгирования в боте MineEvo'''
    strings = {
        "name" : "mlogs", 
    }
    async def client_ready(self):
        s = self.get('kt')
        if s == None:
            self.set('kt', True)
        
        s = self.get('rkt')
        if s == None:
            self.set('rkt', True)
        
        s = self.get('k')
        if s == None:
            self.set('k', True)

        s = self.get('rk')
        if s == None:
            self.set('rk', True)

        s = self.get('mif')
        if s == None:
            self.set('mif', True)

        s = self.get('kr')
        if s == None:
            self.set('kr', True)

        s = self.get('zv')
        if s == None:
            self.set('zv', True)

        s = self.get('trade')
        if s == None:
            self.set('trade', True)

        s = self.get('boosters')
        if s == None:
            self.set('boosters', True)

        s = self.get('bosses')
        if s == None:
            self.set('bosses', True)

        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "mlogs",
            "Группа для работы модуля mlogs",
            silent=True,
            archive=True,
            _folder="hikka",
        )
            
    @loader.watcher()
    async def watcher(self, message):


        if self.get('kt'):
            if message.chat_id == 5522271758 and "✉ Ты нашел(ла) конверт." in message.raw_text:
                await self.client.send_message("mlogs","✉️ Конверт +1" )

        if self.get('rkt'):        
            if message.chat_id == 5522271758 and "🧧 Ты нашел(ла) редкий конверт." in message.raw_text:
                await self.client.send_message("mlogs", "🧧 Редкий Конверт +1")
        
        if self.get('k'):                
            if message.chat_id == 5522271758 and "📦 Ты нашел(ла) Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "📦 Кейс +1")
        
        if self.get('rk'):
            if message.chat_id == 5522271758 and "🗳 Ты нашел(ла) Редкий Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "🗳 Редкий Кейс +1")
        if self.get('mif'):         
            if message.chat_id == 5522271758 and "🕋 Ты нашел(ла) Мифический Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "Грац! 🕋 Миф. Кейс +1!")
        
        if self.get('kr'):
            if message.chat_id == 5522271758 and "💎 Ты нашел(ла) Кристальный Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "Congratulations! 💎 Кристальный кейс +1! ")
        
        if self.get('zv'):
            if message.chat_id == 5522271758 and "💫" in message.raw_text:
                await self.client.send_message("mlogs", "🌌 Звездный Кейс +1")
        
        if self.get('trade'):                
            if message.chat_id == 5522271758 and "передал(а) тебе" in message.raw_text:
                await self.client.send_message("mlogs", message.text)
        
        if self.get('bosses'):
            if message.chat_id == 5522271758 and "побежден игроком" in message.raw_text:
                await self.client.send_message("mlogs", message.text)
        
        if self.get('boosters'):
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


    @loader.command()
    async def mlogs(self, message):
        "Управление модулем"
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('boosters'):
            bosst = '<b>Бусты: </b><i>Логируются</i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = '<b>Перевод вам кейсов: </b><i>Логируется</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = '<b>Боссы: </b><i>Логируются</i>\n'
        else:
            bosss = ''
        await self.inline.form(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}\n{bosst}{bosss}{tradee}",
                message=message,
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




    async def icases(self, call: InlineCall):
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('boosters'):
            bosst = '<b>Бусты: </b><i>Логируются</i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = '<b>Перевод вам кейсов: </b><i>Логируется</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = '<b>Боссы: </b><i>Логируются</i>\n'
        else:
            bosss = ''
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )
    async def ikt(self, call: InlineCall):
        self.set('kt', not self.get('kt'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )

    


    async def irkt(self, call: InlineCall):
        self.set('rkt', not self.get('rkt'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def ik(self, call: InlineCall):
        self.set('k', not self.get('k'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def irk(self, call: InlineCall):
        self.set('rk', not self.get('rk'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def imif(self, call: InlineCall):
        self.set('mif', not self.get('mif'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )

    async def ikr(self, call: InlineCall):
        self.set('kr', not self.get('kr'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def izv(self, call: InlineCall):
        self.set('zv', not self.get('zv'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def itrade(self, call: InlineCall):
        self.set('trade', not self.get('trade'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('boosters'):
            bosst = '<b>Бусты: </b><i>Логируются</i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = '<b>Перевод вам кейсов: </b><i>Логируется</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = '<b>Боссы: </b><i>Логируются</i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}\n{bosst}{bosss}{tradee}",
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


    async def iboss(self, call: InlineCall):
        self.set('bosses', not self.get('bosses'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('boosters'):
            bosst = '<b>Бусты: </b><i>Логируются</i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = '<b>Перевод вам кейсов: </b><i>Логируется</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = '<b>Боссы: </b><i>Логируются</i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}\n{bosst}{bosss}{tradee}",
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

    async def iboost(self, call: InlineCall):
        self.set('boosters', not self.get('boosters'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('boosters'):
            bosst = '<b>Бусты: </b><i>Логируются</i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = '<b>Перевод вам кейсов: </b><i>Логируется</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = '<b>Боссы: </b><i>Логируются</i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}\n{bosst}{bosss}{tradee}",
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
    async def iback(self, call: InlineCall):
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('boosters'):
            bosst = '<b>Бусты: </b><i>Логируются</i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = '<b>Перевод вам кейсов: </b><i>Логируется</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = '<b>Боссы: </b><i>Логируются</i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}\n{bosst}{bosss}{tradee}",
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
                            import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
from asyncio import sleep
from .. import loader, utils
from ..inline.types import InlineCall

__version__ = (1, 1)

@loader.tds
class mlogs(loader.Module):
    '''Модуль для логгирования в боте MineEvo'''
    strings = {
        "name" : "mlogs", 
    }
    async def client_ready(self):
        s = self.get('kt')
        if s == None:
            self.set('kt', True)
        
        s = self.get('rkt')
        if s == None:
            self.set('rkt', True)
        
        s = self.get('k')
        if s == None:
            self.set('k', True)

        s = self.get('rk')
        if s == None:
            self.set('rk', True)

        s = self.get('mif')
        if s == None:
            self.set('mif', True)

        s = self.get('kr')
        if s == None:
            self.set('kr', True)

        s = self.get('zv')
        if s == None:
            self.set('zv', True)

        s = self.get('trade')
        if s == None:
            self.set('trade', True)

        s = self.get('boosters')
        if s == None:
            self.set('boosters', True)

        s = self.get('bosses')
        if s == None:
            self.set('bosses', True)

        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "mlogs",
            "Группа для работы модуля mlogs",
            silent=True,
            archive=True,
            _folder="hikka",
        )
            
    @loader.watcher()
    async def watcher(self, message):


        if self.get('kt'):
            if message.chat_id == 5522271758 and "✉ Ты нашел(ла) конверт." in message.raw_text:
                await self.client.send_message("mlogs","✉️ Конверт +1" )

        if self.get('rkt'):        
            if message.chat_id == 5522271758 and "🧧 Ты нашел(ла) редкий конверт." in message.raw_text:
                await self.client.send_message("mlogs", "🧧 Редкий Конверт +1")
        
        if self.get('k'):                
            if message.chat_id == 5522271758 and "📦 Ты нашел(ла) Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "📦 Кейс +1")
        
        if self.get('rk'):
            if message.chat_id == 5522271758 and "🗳 Ты нашел(ла) Редкий Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "🗳 Редкий Кейс +1")
        if self.get('mif'):         
            if message.chat_id == 5522271758 and "🕋 Ты нашел(ла) Мифический Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "Грац! 🕋 Миф. Кейс +1!")
        
        if self.get('kr'):
            if message.chat_id == 5522271758 and "💎 Ты нашел(ла) Кристальный Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "Congratulations! 💎 Кристальный кейс +1! ")
        
        if self.get('zv'):
            if message.chat_id == 5522271758 and "💫" in message.raw_text:
                await self.client.send_message("mlogs", "🌌 Звездный Кейс +1")
        
        if self.get('trade'):                
            if message.chat_id == 5522271758 and "передал(а) тебе" in message.raw_text:
                await self.client.send_message("mlogs", message.text)
        
        if self.get('bosses'):
            if message.chat_id == 5522271758 and "побежден игроком" in message.raw_text:
                await self.client.send_message("mlogs", message.text)
        
        if self.get('boosters'):
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


    @loader.command()
    async def mlogs(self, message):
        "Управление модулем"
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('boosters'):
            bosst = '<b>Бусты: </b><i>Логируются</i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = '<b>Перевод вам кейсов: </b><i>Логируется</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = '<b>Боссы: </b><i>Логируются</i>\n'
        else:
            bosss = ''
        await self.inline.form(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}\n{bosst}{bosss}{tradee}",
                message=message,
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




    async def icases(self, call: InlineCall):
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('boosters'):
            bosst = '<b>Бусты: </b><i>Логируются</i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = '<b>Перевод вам кейсов: </b><i>Логируется</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = '<b>Боссы: </b><i>Логируются</i>\n'
        else:
            bosss = ''
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )
    async def ikt(self, call: InlineCall):
        self.set('kt', not self.get('kt'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )

    


    async def irkt(self, call: InlineCall):
        self.set('rkt', not self.get('rkt'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def ik(self, call: InlineCall):
        self.set('k', not self.get('k'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def irk(self, call: InlineCall):
        self.set('rk', not self.get('rk'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def imif(self, call: InlineCall):
        self.set('mif', not self.get('mif'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )

    async def ikr(self, call: InlineCall):
        self.set('kr', not self.get('kr'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def izv(self, call: InlineCall):
        self.set('zv', not self.get('zv'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}",
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
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def itrade(self, call: InlineCall):
        self.set('trade', not self.get('trade'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('boosters'):
            bosst = '<b>Бусты: </b><i>Логируются</i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = '<b>Перевод вам кейсов: </b><i>Логируется</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = '<b>Боссы: </b><i>Логируются</i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}\n{bosst}{bosss}{tradee}",
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


    async def iboss(self, call: InlineCall):
        self.set('bosses', not self.get('bosses'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('boosters'):
            bosst = '<b>Бусты: </b><i>Логируются</i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = '<b>Перевод вам кейсов: </b><i>Логируется</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = '<b>Боссы: </b><i>Логируются</i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}\n{bosst}{bosss}{tradee}",
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

    async def iboost(self, call: InlineCall):
        self.set('boosters', not self.get('boosters'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('boosters'):
            bosst = '<b>Бусты: </b><i>Логируются</i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = '<b>Перевод вам кейсов: </b><i>Логируется</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = '<b>Боссы: </b><i>Логируются</i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}\n{bosst}{bosss}{tradee}",
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
    async def iback(self, call: InlineCall):
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('boosters'):
            bosst = '<b>Бусты: </b><i>Логируются</i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = '<b>Перевод вам кейсов: </b><i>Логируется</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = '<b>Боссы: </b><i>Логируются</i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{zvv}\n{bosst}{bosss}{tradee}",
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
                            
