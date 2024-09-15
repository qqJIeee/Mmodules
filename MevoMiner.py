import inspect
import asyncio
from pydantic import BaseModel
from typing import Optional

from telethon.tl.types import Message, User
from telethon.errors import FloodWaitError

from .. import loader, utils
from ..inline.types import InlineCall

@loader.tds
class MevoMiner(loader.Module):
    strings = {
        "name": "MevoMiner",
    }

    async def client_ready(self, client, db):
        self.bb = False

        if not self.get('dly'):
            self.set('dly', 1.0)
        
        if not self.get('mm'):
            self.set('mm', False)
        
        if not self.get('allmines'):
            self.set('allmines', False)
        
        if not self.get('onesdelay'):
            self.set('onesdelay', False)
        
        if not self.get('dgold'):
            self.set('dgold', False)
        
        if not self.get("demerald"):
            self.set('demerald', False)
        
        if not self.get('druby'):
            self.set('druby', False)

        if not self.get('mine'):
            self.set('mine', "Gold")
        
        if not self.get("count"):
            self.set('count', 0)
        
        if not self.get('action'):
            self.set('action', "send")

        if not self.get('fwd'):
            self.set('fwd', None)

        logs = await self.client.get_entity("hikka-logs")
        logs = "-100" + str(logs.id) 
        self.set('logs', logs)

        if self.get('mm'):
            await self.continue_mining()

    async def bosses_fw(self, message):
        dly = self.get('dly')
        
        if self.get('mm'):
            if message.chat_id == 5522271758 and "🔶 Ты выбрал босса" in message.raw_text:
                self.bb = True
                await self.continue_mining()

        if self.bb:
            if message.chat_id == 5522271758 and "для атаки выбери босса" in message.raw_text:
                self.bb = False
                await asyncio.sleep(dly)
                await self.continue_mining()

    @loader.command()
    async def mm(self, message):
        '''- Включить/выключить копание'''
        self.set('mm', not self.get('mm'))
        if self.get('mm'):
            await self.client.send_message(message.chat_id, "<b>Копание включено</b>")
            await message.delete()
            await self.continue_mining()
        
        else:
            await self.client.send_message(message.chat_id, f"<b>Копание выключено</b>")
            await message.delete()
            
    async def continue_mining(self):
        while self.get('mm'):
            logs = self.get('logs')

            if self.get('allmines'):
                mines = []
                if self.get('dgold'):
                    mines.append(7168860714)
                if self.get('demerald'):
                    mines.append(7084173311)
                if self.get('druby'):
                    mines.append(7066508668)
                
                if len(mines) == 0:
                    await self.inline.bot.send_message(logs, "❌<b>Ошибка</b>\nВыберите в конфиге шахты")
                    return

                if self.get('onesdelay'):

                    count = self.get('count')
                    for mine in mines:
                        if count > 500:
                            next = "send" if action == 'forward' else 'forward'
                            self.set(action, next)

                        action = self.get('action')

                        try:
                            if action == 'send':
                                await self.client.send_message(mine, 'коп')
                            if action == 'forward':
                                forward_msg = await self.client.send_message('me', "Коп")

                                await forward_msg.forward_to(mine)
                                await forward_msg.delete()
                        except FloodWaitError as e:
                            s =  e.seconds
                            await self.inline.bot.send_message(logs, f"У вас фв молодой человек\nНачну копать через <code>{s}</code> секунд\naction - {self.get('action')}")
                            await asyncio.sleep(s + 2)

                        count += 1
                        await asyncio.sleep(self.get('dly'))
            else:
                if self.get('onesdelay'):
                    mine = self.get('mine')
                    if count > 500:
                        next = "send" if action == 'forward' else 'forward'
                        self.set(action, next)

                    action = self.get('action')

                    try:
                        if action == 'send':
                            await self.client.send_message(mine, 'коп')
                        if action == 'forward':
                            forward_msg = await self.client.send_message('me', "Коп")

                            await forward_msg.forward_to(mine)
                            await forward_msg.delete()
                            
                    except FloodWaitError as e:
                        s =  e.seconds
                        await self.inline.bot.send_message(logs, f"У вас фв молодой человек\nНачну копать через <code>{s}</code> секунд\naction - {self.get('action')}")
                        await asyncio.sleep(s + 2)
                    
                    count += 1
                    await asyncio.sleep(self.get('dly'))
                
                else:
                    await self.client.send_message(mine, 'коп')
                    await asyncio.sleep(self.get('dly'))

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

            response_text = f'<emoji document_id=5980930633298350051>✅</emoji> <b>Успешно!</b>\n<i>Задержка копания изменена на {zz} секунд</i>'

            await utils.answer(message, response_text)

        except ValueError:
            await utils.answer(message, f'<emoji document_id=5210952531676504517>❌</emoji> <b>Ошибка | {cmd}</b>\nУкажите число в значении!')

    @loader.command()
    async def emsm(self, m: Message):
        '''- Выбрать шахту для копания\ng | г - gold\n e | е - Emerald\n r | р- Ruby'''
        me = await self.client.get_me()
         
        args = utils.get_args_split_by(m, " ")
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(m)}'
        else:
            await utils.answer(m, f'<emoji document_id=5210952531676504517>❌</emoji> <b>Ошибка | {cmd}</b>\n<i>Укажите шахту, которую хотите выбрать</i>')
            return
        if len(args) > 1:
            await utils.answer(m, f'<emoji document_id=5210952531676504517>❌</emoji> <b>Ошибка | {cmd}</b>\n<i>Укажите в команде только шахту</i>')
            return
        if self.get("allmines"):
            await utils.answer(m, f'<emoji document_id=5210952531676504517>❌</emoji> <b>Ошибка | {cmd}</b>\n<i>У вас включено копание в выбранных шахтах, для того чтобы выбрать шахты с этим методом напишите команду <code>emcfg</code></i>')
            return

        mine = args[0]
        match mine:
            case 'g' | 'г':
                mine = "<emoji document_id=5380036576552178412>💛</emoji> Gold" if me.premium else "Gold"
                self.set('mine', 7168860714)

            case 'e' | 'е':
                mine = "<emoji document_id=5379866611811375909>💚</emoji> Emerald" if me.premium else "Emerald"
                self.set('mine', 7084173311)

            case "r" | 'р':
                mine = "<emoji document_id=5382255988017483709>❤️</emoji> Ruby" if me.premium else "Ruby"
                self.set('mine', 7066508668)

        await utils.answer(m, f'<emoji document_id=5980930633298350051>✅</emoji> <b>Успешно!</b>\n<i>Шахта изменена на <code>{mine}</code></i>')

    class Attributes(BaseModel):
        mine: str
        
        onesdelay: Optional[str]
        allmines: Optional[str]

        ruby: Optional[str]
        emerald: Optional[str]
        gold: Optional[str]

    async def get_attributes(self):
        me = await self.client.get_me()

        ruby_text = "• <emoji document_id=5382255988017483709>❤️</emoji> Ruby\n" if me.premium else "• Ruby\n"
        emerald_text = "• <emoji document_id=5379866611811375909>💚</emoji> Emerald\n" if me.premium else "• Emerald\n"
        gold_text = "• <emoji document_id=5380036576552178412>💛</emoji> Gold\n" if me.premium else "• Gold\n"
       
        ruby = ruby_text if self.get("druby") else ''
        emerald = emerald_text if self.get('demerald') else ''
        gold = gold_text if self.get('dgold') else ''

        mine = self.get('mine')

        onesdelay = "▫️<i>Копать методом при котором не дает фв с задержкой 1</i> <u>(на старых аккаунтах, насчёт новых хз)</u>\n" if self.get("onesdelay") else ''
        allmines = f"▫️<i>Копать во всех выбранных шахтах</i>\n{gold}{emerald}{ruby}" if self.get('allmines') else ''

        return self.Attributes(mine=mine, onesdelay=onesdelay, allmines=allmines, gold=gold, emerald=emerald, ruby=ruby)

    def main_markup(self):
        return [
                [
                    {
                        'text' : '⏱ Задержка копания ',
                        'callback' : self.mdlym,
                    },
                    {
                        'text' : '➕ Дополнительно',
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

    @loader.command()
    async def emcfg(self,message):
        '''- Конфиг модуля MevoMiner'''
        attributes = await self.get_attributes()
        
        if self.get('mm'):
            dpm = 'Включено'
        else:
            dpm = 'Выключено'
        
        await self.inline.form(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n<emoji document_id=5776257080658758948>⛏</emoji> <b>Статус копания:</b> <i>{dpm}</i>\n<b>Выбранная шахта:</b> <i>{attributes.mine}</i>\n<b>➕ Дополнительные параметры:</b>\n{attributes.onesdelay}{attributes.allmines}",
            message=message,
            reply_markup=self.main_markup()
        )

    async def mdlym(self, call: InlineCall):
        attributes = await self.get_attributes()
        
        if self.get('mm'):
            dpm = 'Включено'
        else:
            dpm = 'Выключено'
        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n<emoji document_id=5776257080658758948>⛏</emoji> <b>Статус копания:</b> <i>{dpm}</i>\n<b>Выбранная шахта:</b> <i>{attributes.mine}</i>\n<b>➕ Дополнительные параметры:</b>\n{attributes.onesdelay}{attributes.allmines}\n\n<i><emoji document_id=5452069934089641166>❓</emoji> Чтобы изменить задержку копания напишите:\n</i><code>.emdly [задержка]</code>",
            reply_markup=self.main_markup()
        )

    async def iback(self, call: InlineCall):
        attributes = await self.get_attributes()
        
        if self.get('mm'):
            dpm = 'Включено'
        else:
            dpm = 'Выключено'

        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n<emoji document_id=5776257080658758948>⛏</emoji> <b>Статус копания:</b> <i>{dpm}</i>\n🚧 <b>Выбранная шахта:</b> <i>{attributes.mine}</i>\n<b>➕ Дополнительные параметры:</b>\n{attributes.onesdelay}{attributes.allmines}",
            reply_markup=self.main_markup()
        )

    def additional_markup(self):
        return [
                [
                    {
                        "text": "Копать методом с задержкой 1",
                        'callback': self.dmo,
                    },
                ],
                [
                    {
                        "text": "Копать во всех выбранных шахтах",
                        'callback': self.am,
                    },
                ],
                [
                    {
                        'text': "🚧 Выбрать шахты",
                        'callback': self.sm,
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

    def mines_markup(self):
        return [
            [
                {
                    'text': "Gold",
                    'callback': self.sg,
                },
                {
                    'text': "Emerald",
                    'callback': self.se,
                },
                {
                    'text': "Ruby",
                    'callback': self.sr,
                },
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ibackd,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ]

    async def idd(self, call: InlineCall):
        attributes = await self.get_attributes()
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{attributes.onesdelay}{attributes.allmines}',
            reply_markup=self.additional_markup()
        )

    async def dmo(self, call: InlineCall):
        self.set('onesdelay', not self.get('onesdelay'))
        attributes = await self.get_attributes()
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{attributes.onesdelay}{attributes.allmines}',
            reply_markup=self.additional_markup()
        )

    async def am(self, call: InlineCall):
        self.set('allmines', not self.get('allmines'))
        attributes = await self.get_attributes()
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{attributes.onesdelay}{attributes.allmines}',
            reply_markup=self.additional_markup()
        )

    async def ibackd(self, call: InlineCall):
        attributes = await self.get_attributes()
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{attributes.onesdelay}{attributes.allmines}',
            reply_markup=self.additional_markup()
        )

    async def sm(self, call: InlineCall):
        attributes = await self.get_attributes()

        await call.edit(
            text=f"🚧 <b>Шахты</b>\n{attributes.gold}{attributes.emerald}{attributes.ruby}",
            reply_markup=self.mines_markup()
        )

    async def sg(self, call: InlineCall):
        self.set('dgold', not self.get('dgold'))
        attributes = await self.get_attributes()

        await call.edit(
            text=f"🚧 <b>Шахты</b>\n{attributes.gold}{attributes.emerald}{attributes.ruby}",
            reply_markup=self.mines_markup()
        )

    async def se(self, call: InlineCall):
        self.set('demerald', not self.get('demerald'))
        attributes = await self.get_attributes()

        await call.edit(
            text=f"🚧 <b>Шахты</b>\n{attributes.gold}{attributes.emerald}{attributes.ruby}",
            reply_markup=self.mines_markup()
        )
    
    async def sr(self, call: InlineCall):
        self.set('druby', not self.get('druby'))
        attributes = await self.get_attributes()

        await call.edit(
            text=f"🚧 <b>Шахты</b>\n{attributes.gold}{attributes.emerald}{attributes.ruby}",
            reply_markup=self.mines_markup()
        )