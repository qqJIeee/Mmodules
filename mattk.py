from asyncio import sleep
from .. import loader, utils
import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions

@loader.tds
class mattk(loader.Module):
    '''dev - @Kepperok'''
    strings = {
        "name" : "mattk"
    }
    def __init__(self):
        self.hmtk = False
        self.tttk = False
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "dly", 1.0,
                lambda: "куку",
                validator=loader.validators.Float()
            ),
            loader.ConfigValue(
                "autk", True,
                lambda: "Статус автоатаки",
                validator=loader.validators.Boolean()
            )
        )
    @loader.command()
    async def attk(self,message):
        '''Включить/выключить автоатаку'''
        self.config["autk"] = not self.config["autk"]
        autk = self.config["autk"]
        if autk:
            await utils.answer(message, "💢 | <b>Включена автоатака</b>")
        else:
            await utils.answer(message, "💢 | <b>Выключена автоатака</b>")
    @loader.watcher()
    async def watcher(self,message):
        dly = self.config["dly"]
        autk = self.config["autk"]
        if message.chat_id == 5522271758 and "🔶 Ты выбрал босса" in message.raw_text:
            if autk:
                self.tttk = True
                if not self.hmtk:
                    self.hmtk = True
                    if autk:
                        while self.tttk:
                            await self.client.send_message("@mine_evo_bot", "Атк")
                            await asyncio.sleep(dly)
                        else:
                            self.hmtk = False   
        if message.chat_id == 5522271758 and "для атаки выбери босса" in message.raw_text:
            self.tttk = False
