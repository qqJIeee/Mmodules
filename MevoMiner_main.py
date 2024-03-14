from asyncio import sleep
from .. import loader, utils
import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions, TelegramClient, errors
from ..inline.types import InlineCall
import inspect
import re
import datetime
import time
import logging

# meta developer: большая часть кода @kepperok добавления и улучшения @tot_882
@loader.tds
class MevoMiner(loader.Module):
    strings = {
        "name": "MevoMiner_main",
        "kt": "\n<emoji document_id=5775973900580031963>✉️</emoji> Конверт",
        "rkt": "\n<emoji document_id=5422375702731170355>🧧</emoji> Редкий Конверт",
        "k": "\n📦 Кейс",
        "rk": "\n<emoji document_id=5350387571199319521>🗳</emoji> Редкий Кейс",
        "mif": "\n<emoji document_id=5210872082644083598>🕋</emoji> Мифический Кейс",
        "kr": "\n<emoji document_id=5309958691854754293>💎</emoji> Кристальный Кейс",
        "dk": "\n<emoji document_id=5353060651470176045>🎲</emoji> Дайс Кейс",
        "ssp": "\n<emoji document_id=5380056101473492248>👜</emoji> Сумка c Предметами",
        "pse": "\n<emoji document_id=5359785904535774578>💼</emoji> Портфель c Эскизами",
        "zv": "\n<emoji document_id=5438496463044752972>⭐️</emoji> Зв:",
        "plasma": "\n<emoji document_id=5431783411981228752>🎆</emoji>Плазма"
    }


    async def client_ready(self, client, db):
        self.bb = False
        s = self.get('dly')
        if s is None:
            self.set('dly', 1.0)
        s = self.get('mm')
        if s is None:
            self.set('mm', False)
        s = self.get('ag')
        if s is None:
            self.set('ag', False)
        s = self.get('as')
        if s is None:
            self.set('as', False)
        s = self.get('fw')
        if s is None:
            self.set('fw', False)
        if not self.get("time"):
            self.set("time", 0)
        if self.get("cases") == None:
            self.set("cases", {
                "kt": True,
                "rkt": True,
                "k": True,
                "rk": True,
                "mif": True,
                "kr": True,
                "dk": True,
                "zv": True,
                "ssp": True,
                "pse": True,
                "plasma": True
            })
        if self.get("kol_cases") == None:
            self.set("kol_cases", {
                "kt": 0,
                "rkt": 0,
                "k": 0,
                "rk": 0,
                "mif": 0,
                "kr": 0,
                "dk": 0,
                "zv": 0,
                "ssp": 0,
                "pse": 0,
                "plasma": 0,
                "clicks": 0
            })
        await self.continue_mining()

    @loader.watcher()
    async def watcher(self, message):
        a = self.get("kol_cases")
        if hasattr(message, 'from_id') and hasattr(message, 'chat_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Руда на уровень" in message.raw_text:
            a["clicks"] += 1
            self.set("kol_cases", a)
    async def bosses_fw(self,message):
        dly = self.get('dly')
        
        if self.get('as'):
            if self.get('mm'):
                if message.chat_id == 5522271758 and "🔶 Ты выбрал босса" in message.raw_text:
                    self.bb = True
                    await self.mm(message)
        if self.get('ag'):
            if self.bb:
                if message.chat_id == 5522271758 and "для атаки выбери босса" in message.raw_text:
                    self.bb = False
                    await asyncio.sleep(dly)
                    await self.mm(message)
            
        if hasattr(message, 'from_id') and hasattr(message, 'chat_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Найден" in message.raw_text:
            if "✉" in message.raw_text and "Конверт" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])
                
                a["kt"] += colvo
                self.set("kol_cases", a)
            if "🧧" in message.raw_text and "Редкий Конверт" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])
                
                a["rkt"] += colvo
                self.set("kol_cases", a)

            if "📦" in message.raw_text and "Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["k"] += colvo
                self.set("kol_cases", a)

            if "🗳" in message.raw_text and "Редкий Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["rk"] += colvo
                self.set("kol_cases", a)

            if "🕋" in message.raw_text and "Мифический Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["mif"] += colvo
                self.set("kol_cases", a)

            if "Портфель" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["pse"] += colvo
                self.set("kol_cases", a)

            if "Сумка" in message.raw_text:    
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["ssp"] += colvo
                self.set("kol_cases", a)

            if "💎" in message.raw_text and "Кристальный Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["kr"] += colvo
                self.set("kol_cases", a)

            if "🎲" in message.raw_text and "Дайс Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["dk"] += colvo
                self.set("kol_cases", a)

            if "💫" in message.raw_text:
                a["zv"] += 1
                self.set("kol_cases", a)

        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Плазма +" in message.raw_text:
            plpt = r"\d+"
            search = re.search(plpt, message.raw_text)
            colvo = int(search[0])
            
            a["plasma"] += colvo
            self.set("kol_cases", a)

    @loader.command()
    async def mm(self, message):
        '''- Включить/выключить копание'''
        self.set('mm', not self.get('mm'))
        if self.get('mm'):
            await self.client.send_message(message.chat_id, "<b><emoji document_id=5963318814958423599>⚡️</emoji><emoji document_id=5776257080658758948>⛏</emoji>Коп Вкл<emoji document_id=5776257080658758948>⛏</emoji><emoji document_id=5963318814958423599>⚡️</emoji>")
            await message.delete()
            self.set("kol_cases", {
                "kt": 0,
                "rkt": 0,
                "k": 0,
                "rk": 0,
                "mif": 0,
                "kr": 0,
                "dk": 0,
                "zv": 0,
                "ssp": 0,
                "pse": 0,
                "plasma": 0,
                "clicks": 0
            })
            self.set("time", time.time())
            await self.continue_mining()
        else:
            cases_text=""
            a = self.get("cases")
            b = self.get("kol_cases")
            timee = self.get("time")
            time_now = time.time()
            time_mine = ""
            sec = time_now - timee
            sec = sec // 1
            mint = sec // 60
            sec -= mint * 60
            hour = mint // 60
            mint -= hour * 60
            days = hour // 24
            hour -= days * 24
            time_mine += f"{int(days)} д. " if days > 0 else ""
            time_mine += f"{int(hour)} ч. " if hour > 0 else ""
            time_mine += f"{int(mint)} м. " if mint > 0 else ""
            time_mine += f"{int(sec)} с. " if sec > 0 else ""
            for i in a:
                if a[i]:
                    cases_text += f'{self.strings(i)} {str(b[i])}:'
            await self.client.send_message(message.chat_id, f"<b><emoji document_id=5963318814958423599>⚡️</emoji><emoji document_id=5776257080658758948>⛏</emoji> Коп выкл <emoji document_id=5776257080658758948>⛏</emoji><emoji document_id=5963318814958423599>⚡️</emoji>\n\nЮзербот копал {time_mine}\n\n<emoji document_id=5406631276042002796>📨</emoji> Всего копаний сделано: {b['clicks']}\n<emoji document_id=5843623986293902590>⬇️</emoji>За этот период ты выкопал <emoji document_id=5843623986293902590>⬇️</emoji>\n{cases_text}</b>")
            await message.delete()
            

    async def continue_mining(self):
        while self.get('mm'):
            await self.client.send_message(5522271758, 'коп')
            await asyncio.sleep(self.get('dly'))
    async def process_mining_result(self, result_text):
        pass

    @loader.command()
    async def emdly(self, message: Message):
        '''- Установить задержку копания [значение]'''
        args = utils.get_args_split_by(message, " ")
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        else:
            await utils.answer(message, f'<emoji document_id=5210952531676504517>❌</emoji> <b>Ошибка | {cmd}</b>\nУкажите значение, которое хотите установить')
            return
        if len(args) > 1:
            await utils.answer(message, f'<emoji document_id=5210952531676504517>❌</emoji> <b>Ошибка | {cmd}</b>\nВы указали больше одного аргумента')
            return

        zz = args[0]
        try:
            zz = float(zz)
            self.set('dly', zz)

            clicks = [100, 1000, 10000, 100000]
            times_required = [click * zz for click in clicks]

            response_text = f'<emoji document_id=5332533929020761310>✅</emoji> <b>Успешно!</b>\n<i>Задержка копания изменена на {zz} секунд</i>\n\n<emoji document_id=5974081491901091242>🕒</emoji> <b>Таким темпом:</b>\n'
            for click, time_required in zip(clicks, times_required):
                response_text += f'<emoji document_id=5843662301697150328>👉</emoji> {click} копаний за: <b>{self.format_time(time_required)}</b><emoji document_id=5776257080658758948>⛏</emoji>\n'

            await utils.answer(message, response_text)

        except ValueError:
            await utils.answer(message, f'<emoji document_id=5210952531676504517>❌</emoji> <b>Ошибка | {cmd}</b>\nУкажите число в значении!')

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return f'{int(days)} дней, {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд'

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
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n⛏ <b>Статус копания:</b> <i>{dpm}</i>\n<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}\n\n<i><emoji document_id=5452069934089641166>❓</emoji> Чтобы изменить задержку копания напишите:\n</i><code>.emdly [задержка]</code>",
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
                        'text' : 'Переключение элементов статистики',
                        'callback' : self.els,
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
                        'text' : 'Переключение элементов статистики',
                        'callback' : self.els,
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
                        'text' : 'Переключение элементов статистики',
                        'callback' : self.els,
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
                        'text' : 'Переключение элементов статистики',
                        'callback' : self.els,
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
        

    async def els(self, call: InlineCall):
        c = self.get("cases")
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                },
                {
                    'text': '🧧 Редкий Конверт',
                    'callback': self.elsrkt,
                }
            ],
            [
                {
                    'text': '📦 Кейс',
                    'callback': self.elsk,
                },
                {
                    'text': '🗳 Редкий Кейс',
                    'callback': self.elsrk,
                }
            ],
            [
                {
                    'text': '🕋 Мифический Кейс',
                    'callback': self.elsmif,
                },
                {
                    'text': '💎 Кристальный Кейс',
                    'callback': self.elskr,
                }
            ],
            [
                {
                    'text': '🎲 Дайс Кейс',
                    'callback': self.elsdk,
                },
                {
                    'text': '⭐️ Зв:',
                    'callback': self.elszv,
                }
            ],
            [
                {
                    'text': '👜 Сумка c Предметами',
                    'callback': self.elsssp,
                },
                {
                    'text': '💼 Портфель c Эскизами',
                    'callback': self.elspse,
                }
            ],
                        [
                {
                    'text': '🎆 Плазма',
                    'callback': self.elsplasma,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])

    async def elskt(self, call: InlineCall):
        c = self.get("cases")
        c["kt"] = not c["kt"]
        self.set("cases", c)
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                },
                {
                    'text': '🧧 Редкий Конверт',
                    'callback': self.elsrkt,
                }
            ],
            [
                {
                    'text': '📦 Кейс',
                    'callback': self.elsk,
                },
                {
                    'text': '🗳 Редкий Кейс',
                    'callback': self.elsrk,
                }
            ],
            [
                {
                    'text': '🕋 Мифический Кейс',
                    'callback': self.elsmif,
                },
                {
                    'text': '💎 Кристальный Кейс',
                    'callback': self.elskr,
                }
            ],
            [
                {
                    'text': '🎲 Дайс Кейс',
                    'callback': self.elsdk,
                },
                {
                    'text': '⭐️ Зв:',
                    'callback': self.elszv,
                }
            ],
            [
                {
                    'text': '👜 Сумка c Предметами',
                    'callback': self.elsssp,
                },
                {
                    'text': '💼 Портфель c Эскизами',
                    'callback': self.elspse,
                }
            ],
                        [
                {
                    'text': '🎆 Плазма',
                    'callback': self.elsplasma,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])

    async def elsrkt(self, call: InlineCall):
        c = self.get("cases")
        c["rkt"] = not c["rkt"]
        self.set("cases", c)
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                },
                {
                    'text': '🧧 Редкий Конверт',
                    'callback': self.elsrkt,
                }
            ],
            [
                {
                    'text': '📦 Кейс',
                    'callback': self.elsk,
                },
                {
                    'text': '🗳 Редкий Кейс',
                    'callback': self.elsrk,
                }
            ],
            [
                {
                    'text': '🕋 Мифический Кейс',
                    'callback': self.elsmif,
                },
                {
                    'text': '💎 Кристальный Кейс',
                    'callback': self.elskr,
                }
            ],
            [
                {
                    'text': '🎲 Дайс Кейс',
                    'callback': self.elsdk,
                },
                {
                    'text': '⭐️ Зв:',
                    'callback': self.elszv,
                }
            ],
            [
                {
                    'text': '👜 Сумка c Предметами',
                    'callback': self.elsssp,
                },
                {
                    'text': '💼 Портфель c Эскизами',
                    'callback': self.elspse,
                }
            ],
                        [
                {
                    'text': '🎆 Плазма',
                    'callback': self.elsplasma,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])

    async def elsk(self, call: InlineCall):
        c = self.get("cases")
        c["k"] = not c["k"]
        self.set("cases", c)
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                },
                {
                    'text': '🧧 Редкий Конверт',
                    'callback': self.elsrkt,
                }
            ],
            [
                {
                    'text': '📦 Кейс',
                    'callback': self.elsk,
                },
                {
                    'text': '🗳 Редкий Кейс',
                    'callback': self.elsrk,
                }
            ],
            [
                {
                    'text': '🕋 Мифический Кейс',
                    'callback': self.elsmif,
                },
                {
                    'text': '💎 Кристальный Кейс',
                    'callback': self.elskr,
                }
            ],
            [
                {
                    'text': '🎲 Дайс Кейс',
                    'callback': self.elsdk,
                },
                {
                    'text': '⭐️ Зв:',
                    'callback': self.elszv,
                }
            ],
            [
                {
                    'text': '👜 Сумка c Предметами',
                    'callback': self.elsssp,
                },
                {
                    'text': '💼 Портфель c Эскизами',
                    'callback': self.elspse,
                }
            ],
                        [
                {
                    'text': '🎆 Плазма',
                    'callback': self.elsplasma,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])

    async def elsrk(self, call: InlineCall):
        c = self.get("cases")
        c["rk"] = not c["rk"]
        self.set("cases", c)
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                },
                {
                    'text': '🧧 Редкий Конверт',
                    'callback': self.elsrkt,
                }
            ],
            [
                {
                    'text': '📦 Кейс',
                    'callback': self.elsk,
                },
                {
                    'text': '🗳 Редкий Кейс',
                    'callback': self.elsrk,
                }
            ],
            [
                {
                    'text': '🕋 Мифический Кейс',
                    'callback': self.elsmif,
                },
                {
                    'text': '💎 Кристальный Кейс',
                    'callback': self.elskr,
                }
            ],
            [
                {
                    'text': '🎲 Дайс Кейс',
                    'callback': self.elsdk,
                },
                {
                    'text': '⭐️ Зв:',
                    'callback': self.elszv,
                }
            ],
            [
                {
                    'text': '👜 Сумка c Предметами',
                    'callback': self.elsssp,
                },
                {
                    'text': '💼 Портфель c Эскизами',
                    'callback': self.elspse,
                }
            ],
                        [
                {
                    'text': '🎆 Плазма',
                    'callback': self.elsplasma,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])

    async def elsmif(self, call: InlineCall):
        c = self.get("cases")
        c["mif"] = not c["mif"]
        self.set("cases", c)
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                },
                {
                    'text': '🧧 Редкий Конверт',
                    'callback': self.elsrkt,
                }
            ],
            [
                {
                    'text': '📦 Кейс',
                    'callback': self.elsk,
                },
                {
                    'text': '🗳 Редкий Кейс',
                    'callback': self.elsrk,
                }
            ],
            [
                {
                    'text': '🕋 Мифический Кейс',
                    'callback': self.elsmif,
                },
                {
                    'text': '💎 Кристальный Кейс',
                    'callback': self.elskr,
                }
            ],
            [
                {
                    'text': '🎲 Дайс Кейс',
                    'callback': self.elsdk,
                },
                {
                    'text': '⭐️ Зв:',
                    'callback': self.elszv,
                }
            ],
            [
                {
                    'text': '👜 Сумка c Предметами',
                    'callback': self.elsssp,
                },
                {
                    'text': '💼 Портфель c Эскизами',
                    'callback': self.elspse,
                }
            ],
                        [
                {
                    'text': '🎆 Плазма',
                    'callback': self.elsplasma,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])

    async def elskr(self, call: InlineCall):
        c = self.get("cases")
        c["kr"] = not c["kr"]
        self.set("cases", c)
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                },
                {
                    'text': '🧧 Редкий Конверт',
                    'callback': self.elsrkt,
                }
            ],
            [
                {
                    'text': '📦 Кейс',
                    'callback': self.elsk,
                },
                {
                    'text': '🗳 Редкий Кейс',
                    'callback': self.elsrk,
                }
            ],
            [
                {
                    'text': '🕋 Мифический Кейс',
                    'callback': self.elsmif,
                },
                {
                    'text': '💎 Кристальный Кейс',
                    'callback': self.elskr,
                }
            ],
            [
                {
                    'text': '🎲 Дайс Кейс',
                    'callback': self.elsdk,
                },
                {
                    'text': '⭐️ Зв:',
                    'callback': self.elszv,
                }
            ],
            [
                {
                    'text': '👜 Сумка c Предметами',
                    'callback': self.elsssp,
                },
                {
                    'text': '💼 Портфель c Эскизами',
                    'callback': self.elspse,
                }
            ],
                        [
                {
                    'text': '🎆 Плазма',
                    'callback': self.elsplasma,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])

    async def elsdk(self, call: InlineCall):
        c = self.get("cases")
        c["dk"] = not c["dk"]
        self.set("cases", c)
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                },
                {
                    'text': '🧧 Редкий Конверт',
                    'callback': self.elsrkt,
                }
            ],
            [
                {
                    'text': '📦 Кейс',
                    'callback': self.elsk,
                },
                {
                    'text': '🗳 Редкий Кейс',
                    'callback': self.elsrk,
                }
            ],
            [
                {
                    'text': '🕋 Мифический Кейс',
                    'callback': self.elsmif,
                },
                {
                    'text': '💎 Кристальный Кейс',
                    'callback': self.elskr,
                }
            ],
            [
                {
                    'text': '🎲 Дайс Кейс',
                    'callback': self.elsdk,
                },
                {
                    'text': '⭐️ Зв:',
                    'callback': self.elszv,
                }
            ],
            [
                {
                    'text': '👜 Сумка c Предметами',
                    'callback': self.elsssp,
                },
                {
                    'text': '💼 Портфель c Эскизами',
                    'callback': self.elspse,
                }
            ],
                        [
                {
                    'text': '🎆 Плазма',
                    'callback': self.elsplasma,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])

    async def elszv(self, call: InlineCall):
        c = self.get("cases")
        c["zv"] = not c["zv"]
        self.set("cases", c)
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                },
                {
                    'text': '🧧 Редкий Конверт',
                    'callback': self.elsrkt,
                }
            ],
            [
                {
                    'text': '📦 Кейс',
                    'callback': self.elsk,
                },
                {
                    'text': '🗳 Редкий Кейс',
                    'callback': self.elsrk,
                }
            ],
            [
                {
                    'text': '🕋 Мифический Кейс',
                    'callback': self.elsmif,
                },
                {
                    'text': '💎 Кристальный Кейс',
                    'callback': self.elskr,
                }
            ],
            [
                {
                    'text': '🎲 Дайс Кейс',
                    'callback': self.elsdk,
                },
                {
                    'text': '⭐️ Зв:',
                    'callback': self.elszv,
                }
            ],
            [
                {
                    'text': '👜 Сумка c Предметами',
                    'callback': self.elsssp,
                },
                {
                    'text': '💼 Портфель c Эскизами',
                    'callback': self.elspse,
                }
            ],
                        [
                {
                    'text': '🎆 Плазма',
                    'callback': self.elsplasma,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])

    async def elsssp(self, call: InlineCall):
        c = self.get("cases")
        c["ssp"] = not c["ssp"]
        self.set("cases", c)
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                },
                {
                    'text': '🧧 Редкий Конверт',
                    'callback': self.elsrkt,
                }
            ],
            [
                {
                    'text': '📦 Кейс',
                    'callback': self.elsk,
                },
                {
                    'text': '🗳 Редкий Кейс',
                    'callback': self.elsrk,
                }
            ],
            [
                {
                    'text': '🕋 Мифический Кейс',
                    'callback': self.elsmif,
                },
                {
                    'text': '💎 Кристальный Кейс',
                    'callback': self.elskr,
                }
            ],
            [
                {
                    'text': '🎲 Дайс Кейс',
                    'callback': self.elsdk,
                },
                {
                    'text': '⭐️ Зв:',
                    'callback': self.elszv,
                }
            ],
            [
                {
                    'text': '👜 Сумка c Предметами',
                    'callback': self.elsssp,
                },
                {
                    'text': '💼 Портфель c Эскизами',
                    'callback': self.elspse,
                }
            ],
                        [
                {
                    'text': '🎆 Плазма',
                    'callback': self.elsplasma,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])

    async def elspse(self, call: InlineCall):
        c = self.get("cases")
        c["pse"] = not c["pse"]
        self.set("cases", c)
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                },
                {
                    'text': '🧧 Редкий Конверт',
                    'callback': self.elsrkt,
                }
            ],
            [
                {
                    'text': '📦 Кейс',
                    'callback': self.elsk,
                },
                {
                    'text': '🗳 Редкий Кейс',
                    'callback': self.elsrk,
                }
            ],
            [
                {
                    'text': '🕋 Мифический Кейс',
                    'callback': self.elsmif,
                },
                {
                    'text': '💎 Кристальный Кейс',
                    'callback': self.elskr,
                }
            ],
            [
                {
                    'text': '🎲 Дайс Кейс',
                    'callback': self.elsdk,
                },
                {
                    'text': '⭐️ Зв:',
                    'callback': self.elszv,
                }
            ],
            [
                {
                    'text': '👜 Сумка c Предметами',
                    'callback': self.elsssp,
                },
                {
                    'text': '💼 Портфель c Эскизами',
                    'callback': self.elspse,
                }
            ],
                        [
                {
                    'text': '🎆 Плазма',
                    'callback': self.elsplasma,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])

    async def elsplasma(self, call: InlineCall):
        c = self.get("cases")
        c["plasma"] = not c["plasma"]
        self.set("cases", c)
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                },
                {
                    'text': '🧧 Редкий Конверт',
                    'callback': self.elsrkt,
                }
            ],
            [
                {
                    'text': '📦 Кейс',
                    'callback': self.elsk,
                },
                {
                    'text': '🗳 Редкий Кейс',
                    'callback': self.elsrk,
                }
            ],
            [
                {
                    'text': '🕋 Мифический Кейс',
                    'callback': self.elsmif,
                },
                {
                    'text': '💎 Кристальный Кейс',
                    'callback': self.elskr,
                }
            ],
            [
                {
                    'text': '🎲 Дайс Кейс',
                    'callback': self.elsdk,
                },
                {
                    'text': '⭐️ Зв:',
                    'callback': self.elszv,
                }
            ],
            [
                {
                    'text': '👜 Сумка c Предметами',
                    'callback': self.elsssp,
                },
                {
                    'text': '💼 Портфель c Эскизами',
                    'callback': self.elspse,
                }
            ],
                        [
                {
                    'text': '🎆 Плазма',
                    'callback': self.elsplasma,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])
