import asyncio
import string
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
from asyncio import sleep
from .. import loader, utils
import re
from ..inline.types import InlineCall
import inspect


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
            
        if self.get('kts') == None:
            self.set("kts", "✉️ <b>Конверт +1</b>")

        if self.get('rkts') == None:
            self.set('rkts', "🧧 <b>Редкий Конверт +1</b>")

        if self.get('ks') == None:
            self.set('ks', "📦 <b>Кейс +1</>")

        if self.get('rks') == None:
            self.set('rks', "🗳 <b>Редкий Кейс +1</b>")
        
        if self.get('mifs') == None:
            self.set('mifs', "<i>Грац!</i>\n🕋 <b>Мифический Кейс +1!</b>")

        if self.get('krs') == None:
            self.set("krs", "<i>Congratulations!</i>\n💎 <b>Кристальный кейс +1!</b>")

        if self.get('dks') == None:
            self.set('dks', "<i>Good luck!</i>\n🎲 <b>Кейс кубик +1!</b> ")

        if self.get('zvs') == None:
            self.set('zvs', "<i>WOW, you are lucky!</i>\n🌌 <b>Звездный Кейс +1</b>")

        if self.get('boostersd1.5') == None:
            self.set('boostersd1.5', "⚡️ <b>Буст денег 1.5 </b><i>+1</i>")

        if self.get('boostersr1.5') == None:
            self.set('boostersr1.5', "⚡️ <b>Буст руды 1.5 </b><i>+1</i>")
        
        if self.get('boostersd2') == None:
            self.set('boostersd2', "⚡️ <b>Буст денег 2.0 </b><i>+1</i>")

        if self.get('boostersr2') == None:
            self.set('boostersr2', "⚡️ <b>Буст руды 2.0 </b><i>+1</i>")
        
        if self.get('boostersd2.5') == None:
            self.set('boostersd2.5', "⚡️ <b>Буст денег 2.5 </b><i>+1</i>")

        if self.get('boostersr2.5') == None:
            self.set('boostersr2.5', "⚡️ <b>Буст руды 2.5 </b><i>+1</i>")

        if self.get('boostersd3') == None:
            self.set('boostersd3', "⚡️ <b>Буст денег 3.0 </b><i>+1</i>")

        if self.get('boostersr3') == None:
            self.set('boostersr3', "⚡️ <b>Буст руды 3.0 </b><i>+1</i>")

        if self.get('creditss') == None:
            self.set('creditss', "<code>{nick}</code> <b>перечислил тебе:</b>\n💳 <code>{cred}</code> <b>эво-коинов</b>")


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
                await self.client.send_message("mlogs", self.get('kts') )

        if self.get('rkt'):        
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🧧 Ты нашел(ла) редкий конверт." in message.raw_text:
                await self.client.send_message("mlogs", self.get('rkts'))
        
        if self.get('k'):                
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "📦 Ты нашел(ла) Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", self.get('ks'))
        
        if self.get('rk'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🗳 Ты нашел(ла) Редкий Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", self.get('rks'))
        if self.get('mif'):         
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🕋 Ты нашел(ла) Мифический Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", self.get('mifs'))
        
        if self.get('kr'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💎 Ты нашел(ла) Кристальный Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", self.get('krs'))

        if self.get('dk'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🎲 Ты нашел(ла) Дайс Кейс!" in message.raw_text:
                await self.client.send_message("mlogs", self.get('dks'))  
        if self.get('zv'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💫" in message.raw_text:
                await self.client.send_message("mlogs", self.get('zvs'))
        
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
                    await self.client.send_message("mlogs", self.get('boostersr2'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×2.0!" in message.raw_text:
                await self.client.send_message("mlogs", self.get('boostersd2'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×1.5!" in message.raw_text:
                await self.client.send_message("mlogs", self.get('boostersd1.5'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×1.5!" in message.raw_text:
                await self.client.send_message("mlogs", self.get('boostersr1.5'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×2.5!" in message.raw_text:
                await self.client.send_message("mlogs", self.get('boostersd2.5'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×2.5!" in message.raw_text:
                await self.client.send_message("mlogs", self.get('boostersr2.5'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×3.0!" in message.raw_text:
                await self.client.send_message("mlogs", self.get('boostersr3'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×3.0!" in message.raw_text:
                await self.client.send_message("mlogs", self.get('boostersd3'))
                
        if self.get('credits'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💳" in message.raw_text and 'перечислил(а) тебе ' in message.raw_text:
                nickc = "<code>(.*?)</code>"
                kolvoc = "тебе (.*?) эво"

                kolvocredits = re.search(kolvoc, message.text, re.DOTALL)
                nickcredits = re.search(nickc, message.text, re.DOTALL)

                cred = kolvocredits.group(1)
                nick = nickcredits.group(1)

                await self.client.send_message("mlogs", self.get('creditss').format(cred=cred, nick=nick))
            
            
    @loader.command()
    async def setstr(self, message: Message):
        '''- Изменить строку\n[Тип строки] [Новая строка\Ничего]\nТип строки и как её изменять можно посмотреть в .sethelp'''
        args = utils.get_args_raw(message.text)
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if not args:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nУкажите тип строки")
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
            type = args.split(' ', maxsplit=1)[0].lower()
            stri = None
            if len(args.split(' ', maxsplit=1)) > 1:
                stri = args.split(' ', maxsplit=1)[1]

            if type == "кт":
                if stri == None:
                    self.set('kts', "✉️ <b>Конверт +1</b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('kts')}")
                    return
                else:
                    self.set('kts', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка ✉️ <i>Конверт</i> на</b>:\n{self.get('kts')}")
            
            elif type == "ркт":
                if stri == None:
                    self.set('rkts', "🧧 <b>Редкий Конверт +1</b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('rkts')}")
                    return
                else:
                    self.set('rkts', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🧧 <i>Редкий Конверт</i> на</b>:\n{self.get('rkts')}")

            elif type == "к":
                if stri == None:
                    self.set('ks', "📦 <b>Кейс +1</>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('ks')}")
                    return
                else:
                    self.set('ks', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 📦 <i>Кейс</i> на</b>:\n{self.get('ks')}")

            elif type == "рк":
                if stri == None:
                    self.set('rks', "🗳 <b>Редкий Кейс +1</b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('rks')}")
                    return
                else:
                    self.set('rks', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🗳 <i>Редкпй Кейс</i> на</b>:\n{self.get('rks')}")
            
            elif type == "миф":
                if stri == None:
                    self.set('mifs', "<i>Грац!</i>\n🕋 <b>Мифический Кейс +1!</b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('mifs')}")
                    return
                else:
                    self.set('mifs', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🕋 <i>Мифический Кейс</i> на</b>:\n{self.get('mifs')}")

            elif type == "кр":
                if stri == None:
                    self.set('krs', "<i>Congratulations!</i>\n💎 <b>Кристальный кейс +1!</b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('krs')}")
                    return
                else:
                    self.set('krs', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 💎 <i>Кристальный Кейс</i> на</b>:\n{self.get('krs')}")

            elif type == "дк":
                if stri == None:
                    self.set('dks', "<i>Good luck!</i>\n🎲 <b>Кейс кубик +1!</b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('dks')}")
                    return
                else:
                    self.set('dks', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🎲 <i>Дайс Кейс</i> на</b>:\n{self.get('dks')}")
            elif type == 'зв':
                if stri == None:
                    self.set('zvs', "<i>WOW, you are lucky!</i>\n🌌 <b>Звездный Кейс +1</b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('zvs')}")
                    return
                else: 
                    self.set('zvs', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🌌 <i>Звёздный Кейс</i> на</b>:\n{self.get('zvs')}")

            elif type == "обмен":
                if stri == None:
                    self.set('tradett', "<b><code>{nick}</code> дал тебе</b>:\n<i>{cases}</i>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('tradett')}")
                    return
                if not "{cases}" in stri or not "{nick}" in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строки 'обмен'</b>")
                if "{cases}" in stri and "{nick}" in stri:
                    self.set('tradett', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка <i>Обмен</i> на</b>:\n{self.get('tradett')}")

            elif type == "бд15":
                if stri == None:
                    self.set('boostersd1.5', "⚡️ <b>Буст денег 1.5 </b><i>+1</i>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('boostersd1.5')}")
                    return
                else: 
                    self.set('boostersd1.5', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка ⚡️ <i>Бустер денег 1.5</i> на</b>:\n{self.get('boostersd1.5')}")

            elif type == "бр15":
                if stri == None:
                    self.set('boostersr1.5', "⚡️ <b>Буст руды 1.5 </b><i>+1</i>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('boostersr1.5')}")
                    return
                else: 
                    self.set('boostersr1.5', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка ⚡️ <i>Бустер руды 1.5</i> на</b>:\n{self.get('boostersr1.5')}")

            elif type == "бд2":
                if stri == None:
                    self.set('boostersd2', "⚡️ <b>Буст денег 2.0 </b><i>+1</i>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('boostersd2')}")
                    return
                else: 
                    self.set('boostersd2', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка ⚡️ <i>Бустер денег 2</i> на</b>:\n{self.get('boostersd2')}")

            elif type == "бр2":
                if stri == None:
                    self.set('boostersr2', "⚡️ <b>Буст руды 2.0 </b><i>+1</i>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('boostersr2')}")
                    return
                else: 
                    self.set('boostersr2', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка ⚡️ <i>Бустер руды 2</i> на</b>:\n{self.get('boostersr2')}")

            elif type == "бд25":
                if stri == None:
                    self.set('boostersd2.5', "⚡️ <b>Буст денег 2.5 </b><i>+1</i>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('boostersd2.5')}")
                    return
                else: 
                    self.set('boostersd2.5', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка ⚡️ <i>Бустер денег 2.5</i> на</b>:\n{self.get('boostersd2.5')}")

            elif type == "бр25":
                if stri == None:
                    self.set('boostersr2.5', "⚡️ <b>Буст руды 2.5 </b><i>+1</i>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('boostersr2.5')}")
                    return
                else: 
                    self.set('boostersr2.5', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка ⚡️ <i>Бустер руды 2.5</i> на</b>:\n{self.get('boostersr2.5')}")

            elif type == "бд3":
                if stri == None:
                    self.set('boostersd3', "⚡️ <b>Буст денег 3.0 </b><i>+1</i>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('boostersd3')}")
                    return
                else: 
                    self.set('boostersd3', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка ⚡️ <i>Бустер денег 3</i> на</b>:\n{self.get('boostersd3')}")

            elif type == "бр3":
                if stri == None:
                    self.set('boostersr3', "⚡️ <b>Буст руды 3.0 </b><i>+1</i>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('boostersr3')}")
                    return
                else: 
                    self.set('boostersr3', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка ⚡️ <i>Бустер руды 3</i> на</b>:\n{self.get('boostersr3')}")   

            elif type == "кредиты":
                if stri == None:
                    self.set('creditss', "<code>{nick}</code> <b>перечислил тебе:</b>\n💳 <code>{cred}</code> <b>эво-коинов</b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('creditss')}")
                    return
                if not "{nick}" in stri or not "{cred}" in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строки 'кредиты'</b>")
                if "{nick}" in stri and "{cred}" in stri: 
                    self.set('creditss', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 💳 <i>Кредиты</i> на</b>:\n{self.get('creditss')}")   
            
            else:
                await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Введён некорретный тип строки</b>")

    @loader.command()
    async def sethelp(self, message: Message):
        '''Помощь для команды .setstr'''
        await utils.answer(message, "<u>Типы строк:</u>\n• <code>Кт</code> - <b>Сообщение при выпадении ✉️ Конверта</b>\n• <code>Ркт</code> - <b>Сообщение при выпадении 🧧 Редкого Конверта</b>\n• <code>К</code> - <b>Сообщение при выпадении 📦 Кейса</b>\n• <code>Рк</code> - <b>Сообщение при выпадении 🗳 Редкого Кейса</b>\n• <code>Миф</code> - <b>Сообщение при выпадении 🕋 Мифического Кейса</b>\n• <code>Кр</code> - <b>Сообщение при выпадении 💎 Кристального Кейса</b>\n• <code>Дк</code> - <b>Сообщение при выпадении 🎲 Дайс Кейса</b>\n• <code>Зв</code> - <b>Сообщение при выпадении 🌌 Звёздного Кейса</b>\n• <code>Бусты</code> - <b>⚡️ Сообщения при выпадении бустов<b>\n    - <code>бд15</code> - <b>Буст денег 1.5</b>\n    - <code>бр15</code> - <b>Буст руды 1.5</b>\n    - <code>бд2</code> - <b>Буст денег 2.0</b>\n    - <code>бр2</code> - <b>Буст руды 2.0</b>\n    - <code>бд25</code> - <b>Буст денег 2.5</b>\n    - <code>бр25</code> - <b>Буст руды 2.5</b>\n    - <code>бд3</code> - <b>Буст денег 3.0</b>\n    - <code>бр3</code> - <b>Буст руды 3.0</b>\n<i>Поддерживаемых перемен нету</i>\n\n• <code>Кредиты</code> - <b>Сообщение при перечислении тебе кредитов</b>\n    - <i>Поддерживаемые переменные:</i> <code>{nick}</code>, <code>{cred}</code>\n• <code>Обмен</code> - <b>Сообщение при переводе тебе кейсов</b>\n    - <i>Поддерживаемые переменные:</i> <code>{nick}</code>, <code>{cases}</code>\n\n<u>Переменные</u>:\n• <code>{nick}</code> - <b>Ник человека, который переводит тебе кейсы/кредиты</b>\n• <code>{cases}</code> - <b>Кейсы которые тебе переводят</b>\n• <code>{cred}</code> - <b>Количество кредитов которые тебе перечисляют</b>")
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
                            
