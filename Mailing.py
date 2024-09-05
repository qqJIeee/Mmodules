import asyncio
import inspect 

from telethon.tl.types import Message, ChatAdminRights
from telethon import functions, errors

from ..inline.types import InlineCall
from .. import loader, utils 

class Mailing(loader.Module):
    '''Модуль для рассылки'''
    strings = {
        "name" : "Mailing"
    }

    async def client_ready(self):
        if self.get('ms') == None:
            self.set('ms', [])

        if self.get('ii') == None:
            self.set('ii', [])

    @loader.command()
    async def magr(self,message):
        '''- Добавить/удалить текущую группу в список'''
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        args = utils.get_args_raw(message)
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        if not args:
            if message.chat_id not in self.get('ii'): 
                self.get('ii').append(message.chat_id)
                await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> |<b> Группа <code>{message.chat_id}</code> добавлена в список</b> ")
                return
            else:
                self.get('ii').remove(message.chat_id)
                await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> |<b> Группа <code>{message.chat_id}</code> удалена из список</b> ")
                return
        else:
            if args[1:].isdigit():
                if int(args) not in self.get('ii'):
                    if args[0] == '-':
                        try:
                            l = await self.client.get_entity(int(args))
                            if l:
                                self.get('ii').append(int(args))
                                await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> |<b> Группа <code>{args}</code> добавлена в список</b> ")
                                return
                        except errors.PeerIdInvalidError:
                            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Ошибка | <code>{cmd}</code>\nГруппы с ID <code>{args}</code> не существует</b>')
                        except errors.ChatIdInvalidError:
                            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Ошибка | <code>{cmd}</code>\nГруппы с ID <code>{args}</code> не существует</b>')
                        except ValueError:
                            await utils.answer(message, f'<emoji document_id=5877477244938489129>🚫</emoji> <b>Ошибка | <code>{cmd}</code>\nГруппы с ID <code>{args}</code> не существует</b>')
                    else:
                        await utils.answer(message, f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Ошибка | <code>{cmd}</code>\nID групп начинается с '-100'</b>")
                else:
                    self.get('ii').remove(int(args))
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> |<b> Группа <code>{args}</code> удалена из списка</b> ")
                    return
            else:
                await utils.answer(message, f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Ошибка | <code>{cmd}</code>\nID поддерживает только числа</b>")

    @loader.command()
    async def masend(self,message):
        '''- [Название] отправить указанную рассылку'''
        args = utils.get_args_raw(message)
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        if args:
            if args in self.get('ms'):
                await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> |<b> Рассылка сообщения <code>{args}</code> отправлена</b> ")
                for i in self.get('ii'):
                    await self.client.send_message(i, f"{self.get(f'{args}')}")
            else:
                await utils.answer(message, f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Ошибка | <code>{cmd}</code>\nТакого сообщения не существует</b>")
        else:
            await utils.answer(message, f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Ошибка | <code>{cmd}</code>\nУкажите сообщение</b>")


    @loader.command()
    async def maclearg(self,message):
        '''- Убрать все группы из списка'''
        await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> |<b> Список групп очищен</b> ")
        self.set('ii', [])


    @loader.command()
    async def matx(self,message):
        ''' < ответ на сообщение > - [Название] Добавить сообщение для рассылки'''
        args = utils.get_args_raw(message)
        oo = await message.get_reply_message()
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        if args:
            if oo:
                if args in self.get('ms'):
                    self.set(f'{args}', f'{oo.text}')
                    self.get('ms').remove(args)
                    self.get('ms').append(args)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> |<b> Сообщение <code>{args}</code> обновлено</b> ")
                else:
                    self.set(f'{args}', f'{oo.text}')
                    self.get('ms').append(args)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> |<b> Сообщение добавленао в список как <code>{args}</code></b> ")
            else:
                await utils.answer(message, f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Ошибка | <code>{cmd}</code>\nОтветьте на сообщение которое хотите добавить</b>")
        else:
            await utils.answer(message, f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Ошибка | <code>{cmd}</code>\nУкажите название сообщения</b>")
    @loader.command()
    async def macheckt(self,message):
        '''- Посмотреть сообщения которые отправляются в группы'''
        m = '<emoji document_id=5213307977640979750>💬</emoji> | <b>Сообщения:</b>\n\n'
        if self.get('ms') == []:
            await utils.answer(message, f"<emoji document_id=5213307977640979750>💬</emoji> | <b>Ваш список сообщения пуст</b>")
        else:
            for k in self.get('ms'):
                m += f"{k} - {self.get(f'{k}')}\n\n"
            await utils.answer(message, m)
    @loader.command()
    async def macheckg(self,message):
        '''- Посмотреть группы в которые отправляются сообщения '''
        m = '<emoji document_id=5936283232780684228>👥</emoji> | <b>Группы в которые отправляются сообщения:</b>\n'
        if self.get('ii') == []:
            await utils.answer(message, f"<emoji document_id=5936283232780684228>👥</emoji> | <b>Ваш список групп пуст</b>")
        else:
            for k in self.get('ii'):
                w = await self.client.get_entity(k)
                m += f'{k} | {(w.title)}\n'
            await utils.answer(message, m)
    
    @loader.command()
    async def maremovet(self,message):
        '''- [Название] Удалить указанное сообщение из списка'''
        args = utils.get_args_raw(message)
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        if args:
            if args in self.get('ms'):
                self.get('ms').remove(args)
                self.set(f'{args}', None)
                await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> |<b> Сообщение <code>{args}</code> удалено из списка</b> ")
            else:
                await utils.answer(message, f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Ошибка | <code>{cmd}</code>\nДанного сообщения не существует</b>")
        else:
            await utils.answer(message, f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Ошибка | <code>{cmd}</code>\nУкажите название сообщения</b>")


    @loader.command()
    async def macleart(self,message):
        '''- Убрать все сообщения из списка '''
        await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji> |<b> Список сообщений очищен</b> ")
        self.set('ms', [])        