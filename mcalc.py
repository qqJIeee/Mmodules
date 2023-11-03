import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
from asyncio import sleep
from .. import loader, utils
import inspect



@loader.tds
class mcalc(loader.Module):
    '''dev - @Kepperok'''

    strings = {
        "name" : "mcalc",
    }
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
            await utils.answer(message, f'🔄 <b>Произвожу подсчет</b>.\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> ?')
            await asyncio.sleep(0.4)
            await utils.answer(message, f'🔄 <b>Произвожу подсчет</b>..\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> ?')
            n = needed - current
            if n > 2:        
                f = current * 5000
                d = (needed - 1) * 5000
                b = (f + d) / 2 * (needed - current)
            if n == 1:
                b = needed * 5000
            if n == 2:
                b = needed * 5000 + (current + 1) * 5000
            await asyncio.sleep(0.4)    
            await utils.answer(message, f'🔄 <b>Произвожу подсчет</b>...\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> ?')
            await asyncio.sleep(0.4)
            await utils.answer(message, f'<b>✅ Успешно!</b>\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> <code>{b}</code>')

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
            n = needed - current
            form = needed - 1
            mop = 1 + 0.1 * needed
            mel = 10 + 5 * needed
            if n > 2:
                f = current * 10000
                d = (needed - 1) * 10000
                fs = current * 10
                ds = (needed - 1) * 10
                mdlp = (f + d) / 2 * (needed - current)
                mdls = (fs + ds) / 2 * (needed - current)
            if n == 1:
                mdlp = needed * 10000
                mdls = needed * 10
            if n == 2:
                mdlp = needed * 10000 + (current + 1) * 10000 
                mdls = needed * 10 + (current + 1) * 10
            await utils.answer(message, f'🔄 <b>Произвожу подсчет</b>.\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> ?\n🔩 | <b>Нужно скрапа: ?\n🍀 | <b>Удача/Эффективность: ?\n🧱 | Руда/Плазма</b>: ?')
            await asyncio.sleep(0.4)
            await utils.answer(message, f'🔄 <b>Произвожу подсчет</b>..\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> ?\n🔩 | <b>Нужно скрапа: ?\n🍀 | <b>Удача/Эффективность: ?\n🧱 | Руда/Плазма</b>: ?')
            await asyncio.sleep(0.4)    
            await utils.answer(message, f'🔄 <b>Произвожу подсчет</b>...\n\n💥 <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> ?\n🔩 | <b>Нужно скрапа: ?\n🍀 | <b>Удача/Эффективность: ?\n🧱 | Руда/Плазма</b>: ?')
            await asyncio.sleep(0.4)
            await utils.answer(message, f'<b>✅ Успешно!</b>\n\n⚙️ | <u><b>Текущий Уровень</u>:</b> <code>{current}</code>\n💫 | <u><b>Конечный</u>:</b> <code>{needed}</code>\n\n🎆 | <b>Нужно плазмы:</b> <code>{mdlp}</code>\n🔩 | <b>Нужно скрапа: <code>{mdls}</code></b>\n🍀 | <b>Удача/Эффективность: <code>{mel}%</code>\n🧱 | Руда/Плазма</b>: <code>{mop}x</code>')






        