import asyncio
import re
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
from asyncio import sleep
from .. import loader, utils
import inspect


@loader.tds
class maboost(loader.Module):
    '''Модуль для автоматической активации бустеров в боте MineEvo'''
    strings = {
        "name": "maboost"
    }


    async def client_ready(self):
        
        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "Forab",
            "Группа для работы модуля Autoboosts",
            silent=True,
            archive=True,
            _folder="hikka",
        )

        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="EVO",
            )
        )



    @loader.command()
    async def mab(self, message):
        '''- Включает автоматическую активацию множителей руды\n[Тип (Д, Р, Гр, Гд)] [Множитель]  [Количество]'''
        args = utils.get_args_split_by(message, " ")
        mnoz = None
        quantity = None
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        if not args:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВведите аргументы</b>\n<i>Например: </i><code>Д 1.5 3</code>")
        if len(args) == 1:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВы ввели только тип бустера</b>")
        if len(args) == 2:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nВы не указали количество бустеров</b>")
        if len(args) == 3:
            type = args[0]
            type = type.lower()
            typer = ""
            emj = ""
            if type == 'д':
                typer = "Деньги"
            if type == 'р':
                typer = "Руда"
            if type == "гр":
                typer = "Глобальная Руда"
            if type == "гд":
                typer = "Глобальные Деньги"
            if type not in ["д", "р", "гр", "гд"]:
                await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nТакого типа бустеров не существует или не поддерживается</b>\n<i>Типы бустеров: </i><code>Д</code> <code>Р</code> <code>Гр</code> <code>Гд</code>")
            if type in ["д", "р", "гр", "гд"]:
                try:
                    mnoz = float(args[1])
                except ValueError:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nМножитель должен быть числом</b>")
                if mnoz:
                    try:
                        quantity = int(args[2])
                    except ValueError:
                        await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nКоличество должно быть числом</b>")
                if quantity:
                    if type in ["д", "р"]:
                        await utils.answer(message, f"<emoji document_id=5456140674028019486>⚡️</emoji> | <b>Включена автоматическая активация бустера:\nТип: <code>{typer}</code>\nМножитель: <code>{mnoz}</code>\nКоличество бустеров:</b> <code>{quantity}</code>")
                    if type in ["гд", "гр"] and mnoz == 2.0:
                        await utils.answer(message, f"<emoji document_id=5447410659077661506>🌐</emoji> | <b>Включена автоматическая активация бустера:\nТип: <code>{typer}</code>\nМножитель: <code>{mnoz}</code>\nКоличество бустеров:</b> <code>{quantity}</code>")
                    if type == 'д':
                        if mnoz == 1.5:
                            while quantity > 0:
                                async with self.client.conversation('Forab', exclusive=False) as d:
                                    await d.send_message('Буст Д 1.5')
                                    try:
                                        e = await asyncio.wait_for(d.get_response(), timeout=2)
                                        if e:
                                            quantity -= 1
                                            await asyncio.sleep(605)                       
                                    except asyncio.TimeoutError:
                                        continue 

                        if mnoz == 2.0:
                            while quantity > 0:
                                async with self.client.conversation('Forab', exclusive=False) as d:
                                    await d.send_message('Буст Д 2')
                                    try:
                                        e = await asyncio.wait_for(d.get_response(), timeout=2)
                                        if e:
                                            quantity -= 1
                                            await asyncio.sleep(1205)
                                    except asyncio.TimeoutError:
                                        continue

                        if mnoz == 2.5:
                            while quantity > 0:
                                async with self.client.conversation('Forab', exclusive=False) as d:
                                    await d.send_message('Буст Д 2.5')
                                    try:
                                        e = await asyncio.wait_for(d.get_response(), timeout=2)
                                        if e:
                                            quantity -= 1
                                            await asyncio.sleep(1805)
                                    except asyncio.TimeoutError:
                                        continue

                        if mnoz == 3.0:
                            while quantity > 0:
                                async with self.client.conversation('Forab', exclusive=False) as d:
                                    await d.send_message('Буст Д 3')
                                    try:
                                        e = await asyncio.wait_for(d.get_response(), timeout=2)
                                        if e:
                                            quantity -= 1
                                            await asyncio.sleep(2405)
                                    except asyncio.TimeoutError:
                                        continue


                    if type == "р":
                        if mnoz == 1.5:
                            while quantity > 0:
                                async with self.client.conversation('Forab', exclusive=False) as d:
                                    await d.send_message('Буст Р 1.5')
                                    try:
                                        e = await asyncio.wait_for(d.get_response(), timeout=2)
                                        if e:
                                            quantity -= 1
                                            await asyncio.sleep(605)                       
                                    except asyncio.TimeoutError:
                                        continue 

                        if mnoz == 2.0:
                            while quantity > 0:
                                async with self.client.conversation('Forab', exclusive=False) as d:
                                    await d.send_message('Буст Р 2')
                                    try:
                                        e = await asyncio.wait_for(d.get_response(), timeout=2)
                                        if e:
                                            quantity -= 1
                                            await asyncio.sleep(1205)
                                    except asyncio.TimeoutError:
                                        continue

                        if mnoz == 2.5:
                            while quantity > 0:
                                async with self.client.conversation('Forab', exclusive=False) as d:
                                    await d.send_message('Буст Р 2.5')
                                    try:
                                        e = await asyncio.wait_for(d.get_response(), timeout=2)
                                        if e:
                                            quantity -= 1
                                            await asyncio.sleep(1805)
                                    except asyncio.TimeoutError:
                                        continue

                        if mnoz == 3.0:
                            while quantity > 0:
                                async with self.client.conversation('Forab', exclusive=False) as d:
                                    await d.send_message('Буст Р 3')
                                    try:
                                        e = await asyncio.wait_for(d.get_response(), timeout=2)
                                        if e:
                                            quantity -= 1
                                            await asyncio.sleep(2405)
                                    except asyncio.TimeoutError:
                                        continue


                    if type == "гд":
                        if mnoz != 2.0:
                            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nМножитель глобальных бустеров может быть только 2</b>")
                        if mnoz == 2.0:
                            while quantity > 0:
                                async with self.client.conversation('Forab', exclusive=False) as d:
                                    await d.send_message('Буст Гд 2')
                                    try:
                                        e = await asyncio.wait_for(d.get_response(), timeout=2)
                                        if e:
                                            quantity -= 1
                                            await asyncio.sleep(3605)
                                    except asyncio.TimeoutError:
                                        continue

                    if type == "гр":
                        if mnoz != 2.0:
                            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nМножитель глобальных бустеров может быть только 2</b>")
                        if mnoz == 2.0:
                            while quantity > 0:
                                async with self.client.conversation('Forab', exclusive=False) as d:
                                    await d.send_message('Буст Гр 2')
                                    try:
                                        e = await asyncio.wait_for(d.get_response(), timeout=2)
                                        if e:
                                            quantity -= 1
                                            await asyncio.sleep(3605)
                                    except asyncio.TimeoutError:
                                        continue
