import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
from asyncio import sleep
from .. import loader, utils
import re
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

        if self.get("credits") == None:
            self.set('credits', True)

        if self.get('dk') == None:
            self.set('dk', True)

        if self.get('tradett') == None:
            self.set('tradett', "<b><code>{nick}</code> дал тебе</b>:\n<i>{cases}</i>")

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
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "✉ Ты нашел(ла) конверт." in message.raw_text:
                await self.client.send_message("mlogs","✉️ <b>Конверт +1</b>" )

        if self.get('rkt'):        
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🧧 Ты нашел(ла) редкий конверт." in message.raw_text:
                await self.client.send_message("mlogs", "🧧 <b>Редкий Конверт +1</b>")
        
        if self.get('k'):                
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "📦 Ты нашел(ла) Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "📦 <b>Кейс +1</>")
        
        if self.get('rk'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🗳 Ты нашел(ла) Редкий Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "🗳 <b>Редкий Кейс +1</b>")
        if self.get('mif'):         
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🕋 Ты нашел(ла) Мифический Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "<i>Грац!</i>\n🕋 <b>Мифический Кейс +1!</b>")
        
        if self.get('kr'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💎 Ты нашел(ла) Кристальный Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "<i>Congratulations!</i>\n💎 <b>Кристальный кейс +1!</b> ")

        if self.get('dk'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🎲 Ты нашел(ла) Дайс Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", "<i>Good luck!</i>\n🎲 <b>Кейс кубик +1!</b> ")  
        if self.get('zv'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💫" in message.raw_text:
                await self.client.send_message("mlogs", "<i>WOW, you are lucky!</i>\n🌌 <b>Звездный Кейс +1</b>")
        
        if self.get('trade'):                
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.raw_text:
                nick = "<code>(.*?)</code>"
                kolvo = "тебе  (.*?) шт."

                nickname = re.search(nick, message.text, re.DOTALL)
                kol = re.search(kolvo, message.raw_text, re.DOTALL)
                
                nick = nickname.group(1)
                cases = kol.group(1)
                await self.client.send_message("mlogs", self.get('tradett').format(nick=nick, cases=cases))

        
        if self.get('bosses'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "побежден игроком" in message.raw_text:
                await self.client.send_message("mlogs", message.text)
        
        if self.get('boosters'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×2.0!" in message.raw_text:
                    await self.client.send_message("mlogs", "⚡️ <b>Буст руды 2.0 </b><i>+1</i>")
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×2.0!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст денег 2.0 </b><i>+1</i>")
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×1.5!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст денег 1.5 </b><i>+1</i>")
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×1.5!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст руды 1.5 </b><i>+1</i>")
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×2.5!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст денег 2.5 </b><i>+1</i>")
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×2.5!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст руды 2.5 </b><i>+1</i>")
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×3.0!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст денег 3.0 </b><i>+1</i>")
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×3.0!" in message.raw_text:
                await self.client.send_message("mlogs", "⚡️ <b>Буст руды 3.0 </b><i>+1</i>")
                
        if self.get('credits'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💳" in message.raw_text and 'перечислил(а) тебе ' in message.raw_text:
                await self.client.send_message("mlogs", message.raw_text)
                


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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = ' ▫️<i> 💸 Перевод вам кейсов</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await self.inline.form(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}{tradee}",
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
                                'text' : "💳 Кредиты",
                                'callback' : self.icrd,
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


    async def icrd(self,call:InlineCall):
        self.set('credits', not self.get('credits'))
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = ' ▫️<i> 💸 Перевод вам кейсов</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}{tradee}",
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
                                'text' : "💳 Кредиты",
                                'callback' : self.icrd,
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = ' ▫️<i> 💸 Перевод вам кейсов</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}",
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
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}",
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
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}",
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
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}",
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
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}",
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
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}",
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
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}",
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
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}",
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
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
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

    async def idk(self,call:InlineCall):
        self.set('dk', not self.get('dk'))
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}",
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
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = ' ▫️<i> 💸 Перевод вам кейсов</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}{tradee}",
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
                                'text' : "💳 Кредиты",
                                'callback' : self.icrd,
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = ' ▫️<i> 💸 Перевод вам кейсов</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}{tradee}",
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
                                'text' : "💳 Кредиты",
                                'callback' : self.icrd,
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = ' ▫️<i> 💸 Перевод вам кейсов</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}{tradee}",
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
                                'text' : "💳 Кредиты",
                                'callback' : self.icrd,
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

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('trade'):
            tradee = ' ▫️<i> 💸 Перевод вам кейсов</i>\n'
        else:
            tradee = ''
        
        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{krr}{dkk}{zvv}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}{tradee}",
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
                                'text' : "💳 Кредиты",
                                'callback' : self.icrd,
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
                            