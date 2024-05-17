from asyncio import sleep
from .. import loader, utils
import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions, TelegramClient, errors, events
import inspect
from random import randint
import re


cases = {
    "1": ["✉"],
    "2": ["✉", "🧧"],
    "3": ["✉", "🧧", "📦"],
    "4": ["✉", "🧧", "📦", "🗳"]
}

class mtrade(loader.Module):

    @loader.command()
    async def ts(self, m: Message):
        '''- Включить/выключить автопринятие трейдов'''
        self.set('trade', not self.get('trade', False))
        text = 'Автопринятие трейдов включено' if self.get('trade') else "Автопринятие трейдов выключено"
        await utils.answer(m, text)

    @loader.watcher()
    async def trade_handler(self, m: Message):

        if "Трейд" in m.raw_text and "игрока" in m.raw_text:
            if self.get('trade') and m.chat_id == -1002101809770:
                pattern_from = "Трейдер отдаст свои:\n(.*?) шт."
                find_from = re.search(pattern_from, m.raw_text, re.DOTALL)
                
                pattern_me = "Взамен на твои:\n(.*?) шт."
                find_me = re.search(pattern_me, m.raw_text, re.DOTALL)

                find_from_text = find_from.group(1).split(' ')
                case_from = find_from_text[0]
                quantity_from = int(find_from_text[1])

                find_me_text = find_me.group(1).split(' ')
                case_me = find_me_text[0]
                quantity_me = int(find_me_text[1])

                pattern_nick = "игрока\n(.*?):"
                nickname = re.search(pattern_nick, m.raw_text, re.DOTALL)
                
                d = quantity_from - quantity_me if quantity_from > quantity_me else quantity_me - quantity_from 

                if nickname:
                    if nickname.group(1) not in self.get('traders', []):
                        if d == 1 and case_from == case_me and case_from in self.get('cases'):
                            click = await m.click(0)
                            print(click)
                            if click:
                                traders = self.get('traders', [])
                                if nickname.group(1) not in traders:
                                    traders.append(nickname.group(1))
                                self.set('traders', traders)
            

    @loader.command()
    async def sc(self, m: Message):
        '''- Установить вид кейсов\n1 - только кт\2 - кт и ркт\nи т.д. Максимум рк'''
        args = utils.get_args_raw(m)
        self.set("cases", cases.get(args))
        await utils.answer(m, f"<b>Установлены кейсы:</b>\n{' '.join(self.get('cases'))}")

    @loader.command()
    async def clear(self, m: Message):
        '''- Очистить список тех, с кем трейдились'''
        self.set('traders', [])

    @loader.command()
    async def tsh(self, m: Message):
        '''- Показать список тех, с кем трейдились'''
        await utils.answer(m, '\n'.join(self.get('traders', [])))