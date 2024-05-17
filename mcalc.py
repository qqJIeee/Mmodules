import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
from asyncio import sleep
from .. import loader, utils
import inspect
import locale
from typing import Union 

numbers = {
    "0" : "B",
    "3" : "T",
    "6" : "Qa",
    "9" : "Qi",
    "12" : "Sx",
    '15' : "Sp",
    '18' : "O",
    "21" : "N",
    "24" : "D",
    "27" : "Aa",
    "30" : "Bb",
    "33" : "Cc",
    "36" : "Dd",
    "39" : "Ee",
    "42" : "Ff",
    "45" : "Gg",
    "48" : "Hh",
    "51" : "Ii",
    '54' : "Jj",
    "57" : "Kk",
    "60" : "Ll",
    "63" : "Mm",
    "66" : "Nn",
    "69" : "Oo",
    "72" : "Pp",
    "75" : "Qq",
    "78" : "Rr",
    "81" : "Ss",
    "84" : "Tt",
    "87" : "Uu",
    '90' : "Vv",
    "93" : "Ww",
    "96" : "Xx",
    "99" : "Yy",
    "102" : "Zz"
    }

@loader.tds
class mcalc(loader.Module):
    '''Модуль для подсчета ресурсов на улучшения в боте @@mine_evo_bot'''

    strings = {"name" : "mcalc"}
    
    @loader.command()
    async def bcl(self, message: Message):
        '''[Ваш уровень бура] [Конечный бура]'''
        args = utils.get_args_split_by(message, " ")
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        if not args:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВведите текущий и конечный уровень бура</b>")
        if len(args) == 1:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВведите конечный уровень бура</b>")
        if len(args) > 2:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВы ввели слишком много аргументов</b>")
        if "0" in args:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nУровень бура не может быть равен нулю</b>")
        if len(args) == 2 and "0" not in args:
            current = int(args[0])
            needed = int(args[1])
            if current > needed:
                current, needed = needed, current
            try:
                await utils.answer(message, f'🔄 <b>Произвожу подсчет</b>.\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> ?\n🧱 | <b>Добыча руды</b>: <code>?/10 мин</code>')
                await asyncio.sleep(0.4)
                await utils.answer(message, f'🔄 <b>Произвожу подсчет</b>..\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> ?\n🧱 | <b>Добыча руды</b>: <code>?/10 мин</code>')
                n = needed - current
                if n > 2:        
                    f = current * 5000
                    d = (needed - 1) * 5000
                    b = (f + d) / 2 * (needed - current)
                if n == 1:
                    b = current * 5000
                if n == 2:
                    b = current * 5000 + (current + 1) * 5000
                i = 1 * 2**(needed-1)
                i = str(i)
                v = str(i)[1:]
                v = len(v)
                t = v % 3
                n = i[0:t+1]
                v = v - v % 3 
                try:
                    w = numbers[str(v)]
                    n = n + w
                except KeyError:
                    n = n + "?"
                await asyncio.sleep(0.4)    
                await utils.answer(message, f'🔄 <b>Произвожу подсчет</b>...\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> ?\n🧱 | <b>Добыча руды</b>: <code>?/10 мин</code>')
                await asyncio.sleep(0.4)
                await utils.answer(message, f'<b>✅ Успешно!</b>\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> <code>{b}</code>\n🧱 | <b>Добыча руды</b>: <code>{n}/10 мин</code>')
            except OverflowError:
                await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВы указали слишком большой уровень бура</b>")
    
    
    @loader.command()
    async def mcl(self,message: Message):
        '''[Ваш уровень модуля] [Конечный модуля]'''
        args = utils.get_args_split_by(message, " ")
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        if not args:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВведите текущий и конечный уровень модуля</b>")
        if len(args) == 1:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВведите конечный уровень модуля</b>")
        if len(args) > 2:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВы ввели слишком много аргументов</b>")
        if "0" in args:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nУровень модуля не может быть равен нулю</b>")
        if len(args) == 2 and "0" not in args:
            current = int(args[0])
            needed = int(args[1])
            if current > needed:
                current, needed = needed, current
            try:
                n = needed - current
                form = needed - 1
                mop = 1 + 0.1 * needed
                mel = 10 + 5 * (needed - 1)
                if needed >= 9:
                    mel = 50
                if n > 2:
                    f = current * 10000
                    d = (needed - 1) * 10000
                    fs = current * 10
                    ds = (needed - 1) * 10
                    mdlp = (f + d) / 2 * (needed - current)
                    mdls = (fs + ds) / 2 * (needed - current)
                if n == 1:
                    mdlp = current * 10000
                    mdls = current * 10
                if n == 2:
                    mdlp = current * 10000 + (current + 1) * 10000 
                    mdls = current * 10 + (current + 1) * 10
                await utils.answer(message, f'🔄 <b>Произвожу подсчет</b>.\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> ?\n🔩 | <b>Нужно скрапа: ?\n🍀 | <b>Удача/Эффективность: ?\n🧱 | Руда/Плазма</b>: ?')
                await asyncio.sleep(0.4)
                await utils.answer(message, f'🔄 <b>Произвожу подсчет</b>..\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> ?\n🔩 | <b>Нужно скрапа: ?\n🍀 | <b>Удача/Эффективность: ?\n🧱 | Руда/Плазма</b>: ?')
                await asyncio.sleep(0.4)    
                await utils.answer(message, f'🔄 <b>Произвожу подсчет</b>...\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> ?\n🔩 | <b>Нужно скрапа: ?\n🍀 | <b>Удача/Эффективность: ?\n🧱 | Руда/Плазма</b>: ?')
                await asyncio.sleep(0.4)
                await utils.answer(message, f'<b>✅ Успешно!</b>\n\n⚙️ | <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 | <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> <code>{mdlp}</code>\n🔩 | <b>Нужно скрапа: <code>{mdls}</code></b>\n🍀 | <b>Удача/Эффективность: <code>{mel}%</code>\n🧱 | Руда/Плазма</b>: <code>{mop}x</code>')
            except OverflowError:
                await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВы указали слишком большой уровень модуля</b>")





        
