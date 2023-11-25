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

        if self.get("ps") == None:
            self.set('ps', True)

        if self.get('ss') == None:
            self.set('ss', True)

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
            
        if self.get('kts') == None or "{colvo}" not in self.get('kts'):
            self.set("kts", "✉️ <b>Конверт +<code>{colvo}</code></b>")

        if self.get('rkts') == None or "{colvo}" not in self.get('rkts'):
            self.set('rkts', "🧧 <b>Редкий Конверт +<code>{colvo}</code></b>")

        if self.get('ks') == None or "{colvo}" not in self.get('ks'):
            self.set('ks', "📦 <b>Кейс +<code>{colvo}</code></b>")

        if self.get('rks') == None or "{colvo}" not in self.get('rks'):
            self.set('rks', "🗳 <b>Редкий Кейс +<code>{colvo}</code></b>")
        
        if self.get('mifs') == None or "{colvo}" not in self.get('mifs'):
            self.set('mifs', "<i>Грац!</i>\n🕋 <b>Мифический Кейс +<code>{colvo}</code>!</b>")

        if self.get('krs') == None or "{colvo}" not in self.get('krs'):
            self.set("krs", "<i>Congratulations!</i>\n💎 <b>Кристальный кейс +<code>{colvo}</code>!</b>")

        if self.get('dks') == None or "{colvo}" not in self.get('dks'):
            self.set('dks', "<i>Good luck!</i>\n🎲 <b>Кейс кубик +1<code>{colvo}</code></b>")

        if self.get('zvs') == None or "{colvo}" not in self.get('zvs'):
            self.set('zvs', "<i>WOW, you are lucky!</i>\n🌌 <b>Звездный Кейс +<code>{colvo}</code></b>")

        if self.get('pss') == None or "{colvo}" not in self.get('pss'):
            self.set('pss', "<i>Luck is on your side!</i>\n💼 <b>Портфель с Эскизами +<code>{colvo}</code></b>")

        if self.get('sss') == None or "{colvo}" not in self.get('sss'):
            self.set('sss', "<i>A pleasant surprise!</i>\n👜 <b>Сумка с предметами +<code>{colvo}</code></b>")

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

        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, [self.inline.bot.id]))                                
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id=self.inline.bot.id,
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="Logger",
            )
          )

        mess = await self.client.send_message("mlogs", ".")
        self.set("chid", f"-100{mess.peer_id.channel_id}")
        await mess.delete()

    @loader.command()
    async def strs(self, m: Message):
        '''Строки'''
        await utils.answer(m, f"<b>Текущие строки</b>:\n\n<i>Кт</i>:\n{self.get('kts')}\n<i>Ркт</i>:\n{self.get('rkts')}\n<i>К</i>:\n{self.get('ks')}\n<i>Рк</i>:\n{self.get('rks')}\n<i>Миф</i>:\n{self.get('mifs')}\n<i>Псэ</i>:\n{self.get('pss')}\n<i>Ссп</i>:\n{self.get('sss')}\n<i>Кр</i>:\n{self.get('krs')}\n<i>Зв</i>:\n{self.get('zvs')}\n\n<i>Трейды</i>:\n{self.get('tradett')}\n<i>Кредиты</i>:\n{self.get('creditss')}")


    @loader.watcher()
    async def watcher(self, message):
        chid = int(self.get("chid"))
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Найден" in message.raw_text:
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "✉" in message.raw_text and "Конверт" in message.raw_text:
                if self.get('kt'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('kts').format(colvo=colvo))

            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🧧" in message.raw_text and "Редкий Конверт" in message.raw_text:
                if self.get('rkt'):     
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('rkts').format(colvo=colvo))
            
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "📦" in message.raw_text and "Кейс" in message.raw_text:
                if self.get('k'):              
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inlihe.bot.send_message(chid, self.get('ks').format(colvo=colvo))
            
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🗳" in message.raw_text and "Редкий Кейс" in message.raw_text:
                if self.get('rk'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('rks').format(colvo=colvo))

            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🕋" in message.raw_text and "Мифический Кейс" in message.raw_text:
                if self.get('mif'):         
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('mifs').format(colvo=colvo))
            
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Портфель" in message.raw_text:
                if self.get('ps'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('pss').format(colvo=colvo))

            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Сумка" in message.raw_text:    
                if self.get('ss'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('sss').format(colvo=colvo))

            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💎" in message.raw_text and "Кристальный Кейс" in message.raw_text:
               if self.get('kr'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('krs').format(colvo=colvo))

            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🎲" in message.raw_text and "Дайс Кейс" in message.raw_text:
                if self.get('dk'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('dks').format(colvo=colvo))  

            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🌌" in message.raw_text and "Звёздный Кейс" in message.raw_text or hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💫" in message.raw_text:
                if self.get('zv'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    if search:
                        colvo = search[0]
                    else:
                        colvo = 1
                    await self.inline.bot.send_message(chid, self.get('zvs').format(colvo=colvo))
        
        if self.get('trade'):                
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.raw_text:
                nick = "<code>(.*?)</code>"
                kolvo = "тебе  (.*?) шт."

                nickname = re.search(nick, message.text, re.DOTALL)
                kol = re.search(kolvo, message.raw_text, re.DOTALL)
                
                nick = nickname.group(1)
                cases = kol.group(1)

                await self.inline.bot.send_message(chid, self.get('tradett').format(nick=nick, cases=cases))

        
        if self.get('bosses'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "побежден игроком" in message.raw_text:
                await self.inline.bot.send_message(chid, message.text)
        
        if self.get('boosters'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×2.0!" in message.raw_text:
                    await self.inline.bot.send_message(chid, self.get('boostersr2'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×2.0!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersd2'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×1.5!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersd1.5'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×1.5!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersr1.5'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×2.5!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersd2.5'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×2.5!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersr2.5'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×3.0!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersr3'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×3.0!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersd3'))
                
        if self.get('credits'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💳" in message.raw_text and 'перечислил(а) тебе ' in message.raw_text:
                nickc = "<code>(.*?)</code>"
                kolvoc = "тебе (.*?) эво"

                kolvocredits = re.search(kolvoc, message.text, re.DOTALL)
                nickcredits = re.search(nickc, message.text, re.DOTALL)

                cred = kolvocredits.group(1)
                nick = nickcredits.group(1)

                await self.inline.bot.send_message(chid, self.get('creditss').format(cred=cred, nick=nick))
            
            
    @loader.command()
    async def setstr(self, message: Message):
        '''- Изменить строку\n[Тип строки] [Новая строка\Ничего]\nТип строки и как её изменять можно посмотреть в .sethelp'''
        args = utils.get_args_raw(message.text)
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if not args:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nУкажите тип строки")
            return
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
            type = args.split(' ', maxsplit=1)[0].lower()
            stri = None
            if len(args.split(' ', maxsplit=1)) > 1:
                stri = args.split(' ', maxsplit=1)[1]

            if type == "кт":
                if stri == None:
                    self.set('kts', "✉️ <b>Конверт +<code>{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('kts')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('kts', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка ✉️ <i>Конверт</i> на</b>:\n{self.get('kts')}")
            
            elif type == "ркт":
                if stri == None:
                    self.set('rkts', "🧧 <b>Редкий Конверт +<code>{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('rkts')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('rkts', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🧧 <i>Редкий Конверт</i> на</b>:\n{self.get('rkts')}")

            elif type == "к":
                if stri == None:
                    self.set('ks', "📦 <b>Кейс +<code>{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('ks')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('ks', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 📦 <i>Кейс</i> на</b>:\n{self.get('ks')}")

            elif type == "рк":
                if stri == None:
                    self.set('rks', "🗳 <b>Редкий Кейс +<code>{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('rks')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('rks', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🗳 <i>Редкпй Кейс</i> на</b>:\n{self.get('rks')}")
            
            elif type == "миф":
                if stri == None:
                    self.set('mifs', "<i>Грац!</i>\n🕋 <b>Мифический Кейс +<code>{colvo}</code>!</b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('mifs')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('mifs', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🕋 <i>Мифический Кейс</i> на</b>:\n{self.get('mifs')}")

            elif type == "псэ":
                if stri == None:
                    self.set('pss', "<i>Luck is on your side!</i>\n💼 <b>Портфель с Эскизами +<code>{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('pss')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('pss', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 💼 <i>Портфель с Эскизами</i> на</b>:\n{self.get('pss')}")

            elif type == "ссп":
                if stri == None:
                    self.set('sss', "<i>A pleasant surprise!</i>\n👜 <b>Сумка с предметами +<code>{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('sss')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('sss', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 👜 <i>Сумка с Предметами</i> на</b>:\n{self.get('sss')}")

            elif type == "кр":
                if stri == None:
                    self.set('krs', "<i>Congratulations!</i>\n💎 <b>Кристальный кейс +<code>{colvo}</code>!</b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('krs')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('krs', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 💎 <i>Кристальный Кейс</i> на</b>:\n{self.get('krs')}")

            elif type == "дк":
                if stri == None:
                    self.set('dks', "<i>Good luck!</i>\n🎲 <b>Кейс кубик +1<code>{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('dks')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('dks', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🎲 <i>Дайс Кейс</i> на</b>:\n{self.get('dks')}")
            elif type == 'зв':
                if stri == None:
                    self.set('zvs', "<i>WOW, you are lucky!</i>\n🌌 <b>Звездный Кейс +<code>{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('zvs')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
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
                    return
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}{tradee}",
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}{tradee}",
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
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
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
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
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
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

    
    async def ips(self, call: InlineCall):
        self.set('ps', not self.get('ps'))
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
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
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
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
        
    async def iss(self, call: InlineCall):
        self.set('ss', not self.get('ss'))
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
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
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
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
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
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
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
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
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
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
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
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
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
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
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
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
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}{tradee}",
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}{tradee}",
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}{tradee}",
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

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

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
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}{tradee}",
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
                            
