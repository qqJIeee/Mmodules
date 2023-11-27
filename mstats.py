from asyncio import sleep
from .. import loader, utils
from ..inline.types import InlineCall
import asyncio
import re
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
import datetime
import time


@loader.tds
class mstats(loader.Module):
    '''Модуль для статистики в боте MineEvo'''
    strings = {
        "name" : "mstats"
    }
    async def client_ready(self):
        if self.get('timee') == None:
            self.set('timee', time.time())
        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "mstats",
            "Группа для работы модуля mstats",
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
    async def stn(self,message: Message):
        '''- Установить свой ник'''
        async with self.client.conversation("mstats", exclusive=False) as prof:
            await asyncio.sleep(1)
            await prof.send_message("Проф")
            try:
                res = await asyncio.wait_for(prof.get_response(), timeout=2)
                pattern = "Профиль пользователя  (.*?):"
                match = re.search(pattern, res.raw_text, re.DOTALL)
                if match:
                    im = str(match.group(1))
                    self.set("im",im)
                    await utils.answer(message, f"✅ <b>| Успешно!\n👉 | Ник <code>{im}</code> успешно установлен")
            except asyncio.TimeoutError:
                await utils.answer(message, "🚫 <b>| Ошибка!\n👉 | Попробуйте еще раз</b>")
                
    @loader.command()
    async def drest(self,message):
        '''- Сбросить дб и время'''
        self.set("kt1",0)
        self.set("rkt1",0)
        self.set("k1",0)
        self.set("rk1",0)
        self.set("mif1",0)
        self.set('ps', 0)
        self.set("ss1", 0)
        self.set("kr1",0)
        self.set("zv1",0)
        self.set('es', 0)
        self.set("p",0)
        self.set("pb",0)
        self.set("sb",0)
        self.set("mb",0)
        self.set("klks",0)
        self.set('bss',0)
        self.set("ktt",0)
        self.set("rkb",0)
        self.set("kb",0)
        self.set("bskld",0)
        self.set("mmb",0)
        self.set("kk",0)
        self.set("pthx",0)
        self.set('ktt',0)
        self.set('rkk',0)
        self.set("miff",0)
        self.set("kkr",0)
        self.set('pst', 0)
        self.set('sst', 0)
        self.set("zvv",0)
        self.set("bdmg",0)
        self.set("bkdmg",0)
        self.set("ppthx",0)
        self.set("boostsss",0)
        self.set("rkkt",0)
        self.set("bskn",0)
        self.set('crd', 0)
        self.set('dk', 0)
        self.set('dkkt', 0)
        timee = time.time()
        self.set("timee",timee)
        await utils.answer(message, "Данные в базе данных сброшены")
    @loader.watcher()
    async def watcher(self, message):
        kt1 = self.get("kt1",0)
        rkt1 = self.get("rkt1",0)
        k1 = self.get("k1",0)
        rk1 = self.get("rk1",0)
        mif1 = self.get("mif1",0)
        ps = self.get('ps', 0)
        ss1 = self.get('ss1', 0)
        kr1 = self.get("kr1",0)
        dk = self.get('dk', 0)
        zv1 = self.get("zv1",0)
        p = self.get("p",0)
        pb = self.get("pb",0)
        mb = self.get("mb",0)
        sb = self.get("sb",0)
        klks = self.get("klks",0)
        bss = self.get("bss",0)
        kb = self.get("kb",0)
        rkb = self.get("rkb",0)
        ktt = self.get("ktt",0)
        rkk = self.get("rkk",0)
        rkkt = self.get("rkkt",0)
        bskld = self.get("bskld",0)
        mmb = self.get("mmb",0)
        es = self.get('es', 0)
        es = self.get('es')
        pthx = self.get("pthx",0)
        kk = self.get("kk",0)
        miff = self.get("miff",0)
        kkr = self.get("kkr",0)
        pst = self.get('pst', 0)
        sst = self.get('sst', 0)
        dkkt = self.get('dkkt', 0)
        zvv = self.get("zvv",0)
        bdmg = self.get("bdmg",0)
        bkdmg = self.get("bkdmg",0)
        ppthx = self.get("ppthx",0)
        boostsss = self.get("boostsss",0)
        dayp = self.get("dayp",0)
        daypp = self.get("daypp",0)
        skp = self.get("skp",0)
        mbp = self.get("mbp",0)
        bssd = self.get("bssd",0)
        bskldd = self.get("bskldd",0)
        bskn = self.get("bskn",0)
        ktd1 = self.get("ktd1",0)
        rktd1 = self.get("rktd1", 0)
        kd1 = self.get("kd1", 0)
        rkd1 = self.get("rkd1", 0)
        mifd1 = self.get("mifd1",0)
        psd = self.get('psd', 0)
        ssd = self.get('ssd', 0)
        krd1 = self.get("krd1",0)
        dkd = self.get('dkd', 0)
        zvd1 = self.get("zvd1", 0)
        shdp = self.get("shdp", 0)
        bsknd = self.get("bsknd",0)
        bspd = self.get("bspd",0)
        klksd = self.get("klksd", 0)
        esd = self.get('esd', 0)
        boostd = self.get("boostd", 0)
        bskbd = self.get("bskbd", 0)
        bsrkbd = self.get("bsrkbd", 0)
        bsmifbd = self.get("bsmifbd", 0)
        bddmg = self.get("bddmg", 0)
        bkddmg = self.get("bkddmg", 0)
        kttd = self.get("kttd", 0)
        rkttd = self.get("rkttd", 0)
        kkd = self.get("kkd", 0)
        rkkd = self.get("rkkd", 0)
        miffd = self.get("miffd", 0)
        kkrd = self.get("kkrd", 0)
        pstd = self.get('pstd', 0)
        sstd = self.get('sstd', 0)
        dkktd = self.get('dkktd',0)
        zvvd = self.get("zvvd", 0)
        pthxd = self.get("pthxd", 0)
        ppthxd = self.get("ppthxd", 0)
        crd = self.get('crd', 0)
        crdd = self.get('crdd', 0)
        dk = self.get('dk', 0)
        dkd = self.get('dkd', 0)
        dkkt = self.get('dkkt', 0)
        dkktd = self.get('dkktd', 0)
        now = datetime.datetime.now()
        if now.hour == 0 and now.minute == 0: 
            self.set("dayp",0)
            self.set("daypp",0)
            self.set("skp",0)
            self.set("mbp",0)
            self.set("bssd",0)
            self.set("bskldd",0)
            self.set("ktd1", 0)
            self.set("rktd1", 0)
            self.set("kd1", 0)
            self.set("rkd1", 0)
            self.set("mifd1", 0)
            self.set('psd', 0)
            self.set('ssd', 0)
            self.set("krd1", 0)
            self.set("zvd1", 0)
            self.set("shdp", 0)
            self.set("bsknd", 0)
            self.set("bspd", 0)
            self.set("klksd", 0)
            self.set("boostd", 0)
            self.set("bskbd", 0)
            self.set("bsrkbd", 0)
            self.set("bsmifbd", 0)
            self.set("bddmg", 0)
            self.set("bkddmg", 0)
            self.set("kttd", 0)
            self.set('esd', 0)
            self.set("rkttd", 0)
            self.set("kkd", 0)
            self.set("rkkd", 0)
            self.set("miffd", 0)
            self.set('pstd', 0)
            self.set('sstd', 0)
            self.set("kkrd", 0)
            self.set("zvvd", 0)
            self.set("pthxd", 0)
            self.set("ppthxd", 0)
            self.set('crdd',0)
            self.set('dkd', 0)
            self.set('dkktd', 0)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Найден" in message.raw_text:
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "✉" in message.raw_text and "Конверт" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])
                
                kt1 += 1
                ktd1 += 1
                self.set("ktd1", ktd1)
                self.set("kt1",kt1)
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🧧" in message.raw_text and "Редкий Конверт" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])
                
                rkt1 += colvo
                rktd1 += colvo
                self.set("rktd1", rktd1)
                self.set("rkt1",rkt1)
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "📦" in message.raw_text and "Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                k1 += 1
                kd1 += 1
                self.set("kd1", kd1)
                self.set("k1",k1)
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🗳" in message.raw_text and "Редкий Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                rk1 += 1
                rkd1 += 1
                self.set("rkd1", rkd1)
                self.set("rk1",rk1)
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🕋" in message.raw_text and "Мифический Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                mif1 += 1
                mifd1 += 1
                self.set("mifd1", mifd1)
                self.set("mif1", mif1)
            
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Портфель" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                ps += colvo
                psd += colvo
                self.set('ps', ps)
                self.set('psd', psd)

            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Сумка" in message.raw_text:    
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                ss1 += colvo
                ssd += colvo
                self.set('ss1', ss1)
                self.set('ssd', ssd)
            
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💎" in message.raw_text and "Кристальный Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                kr1 += colvo
                krd1 += colvo
                self.set("krd1", krd1)
                self.set("kr1",kr1)
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🎲" in message.raw_text and "Дайс Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                dk += colvo
                dkd += colvo
                self.set('dk', dk)
                self.set('dkd', dkd)
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🌌" in message.raw_text and "Звёздный Кейс" in message.raw_text or hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💫" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                zv1 += colvo
                zvd1 += colvo
                self.set("zvd1", zvd1)
                self.set("zv1",zv1)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Плазма +" in message.raw_text:
            plpt = r"\d+"
            search = re.search(plpt, message.raw_text)
            colvo = int(search[0])

            p += colvo
            shdp += colvo
            dayp += colvo 
            self.set("shdp", shdp)
            self.set("p",p)
            self.set("dayp",dayp)

        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "нанес(ла)" in message.raw_text:
            bskn += 1
            bsknd += 1
            self.set("bsknd", bsknd)
            self.set("bskn",bskn)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Медаль" in message.raw_text:
            pattern = "Медаль +(.*?)</b>"
            match = re.search(pattern, message.text, re.DOTALL)
            if match:
                mbm = int(match.group(1))
                mb += mbm
                mbp += mbm
                self.set("mbp",mbp)
                self.set("mb",mb)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Скрап" in message.raw_text:
            pattern = "Скрап +(.*?)</b>"
            match = re.search(pattern, message.text, re.DOTALL)
            if match:
                sbm = int(match.group(1))
                sb += sbm
                skp += sbm
                self.set("sb",sb)
                self.set("skp",skp)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "✨ Твоя награда:" in message.raw_text:
            pattern = "Плазма +(.*?)</b>"
            match = re.search(pattern, message.text, re.DOTALL)
            if match:
                pbm = match.group(1)
                pbb = pbm.split()[0].lstrip('+')
                pbb = int(pbb)
                pb += pbb
                dayp += pbb
                bspd += pbb
                self.set("bspd", bspd)
                self.set("pb",pb)
                self.set("dayp",dayp)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Руда на уровень" in message.raw_text:
            klks += 1
            klksd += 1
            self.set("klksd", klksd)
            self.set("klks",klks)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "✨ Твоя награда:" in message.raw_text:
            bss += 1
            bssd += 1
            self.set("bssd",bssd)
            self.set("bss",bss)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🗳 | Редкий Кейс +" in message.raw_text:
            rkkb = message.text.index("<b>Редкий Кейс ") + len("<b>Редкий Кейс ")
            rkkkb = message.text.index("</b>", rkkb)
            rkkbrc = message.text[rkkb:rkkkb]
            rkb += int(rkkbrc)
            bsrkbd += int(rkkbrc)
            self.set("bsrkbd", bsrkbd)
            self.set("rkb",rkb)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Эссенция +" in message.raw_text:
            espt = "Эссенция +(.*?)"
            match = re.search(espt, message.raw_text, re.DOTALL)
            colvo = int(match.group(1))

            es += colvo
            esd += colvo
            self.set('es', es)
            self.set('esd', esd)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "📦 | Кейс +" in message.raw_text:
            pattern = "<b>Кейс +(.*?)</b>"
            match = re.search(pattern, message.text, re.DOTALL)
            if match:
                kbm = int(match.group(1))
                kb += kbm
                bskbd += kbm
                self.set("bskbd", bskbd)
                self.set("kb",kb)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🕋 | Мифический Кейс +" in message.raw_text:
            mmmb = message.text.index("<b>Мифический Кейс ") + len("<b>Мифический Кейс ")
            mmmmb = message.text.index("</b>", mmmb)
            mmmbrc = message.text[mmmb:mmmmb]
            mmb += int(mmmbrc)
            bsmifbd += int(mmmbrc)
            self.set("bsmifbd", bsmifbd)
            self.set("mmb",mmb)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💳" in message.text and 'перечислил(а) тебе ' in message.text:
            jj = message.text.index('перечислил(а) тебе ') + len('перечислил(а) тебе ')
            jjj = message.text.index( 'кредитов')
            j = message.text[jj:jjj]
            crd += int(j)
            crdd += int(j)
            self.set('crd',crd)
            self.set('crdd', crdd)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Награда и статистика отображена в лс с ботом" in message.raw_text:
            bskld += 1
            bskldd += 1
            self.set("bskldd",bskldd)
            self.set("bskld",bskld)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🎆" in message.raw_text and "ты поблагодарил(а) игрока" in message.raw_text:
            l = message.raw_text.split(' ', maxsplit=3)[2]
            l = l.replace(',', '')
            if l == self.get('im'):
                ptthx = message.text.index("+") + len("+")
                pttthx = message.text.index("</b")
                ptttthx = message.text[ptthx:pttthx]
                pttttthx = ptttthx.replace(",","")
                pthx += int(pttttthx)
                dayp += int(pttttthx)
                pthxd += int(pttttthx)
                self.set("pthxd", pthxd)
                self.set("pthx",pthx)
                self.set("dayp",dayp)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🎆" in message.raw_text and "поблагодарил(а) тебя" in message.raw_text:
            pptthx = message.text.index("+") + len("+")
            ppttthx = message.text.index("</b>")
            pptttthx = message.text[pptthx:ppttthx]
            ppttttthx = pptttthx.replace(",","")
            ppthx += int(ppttttthx)
            dayp += int(ppttttthx)
            ppthxd += int(ppttttthx)
            self.set("ppthxd", ppthxd)
            self.set("ppthx",ppthx)
            self.set("dayp",dayp)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.text and "📦" in message.text:
            kkc = message.text.index("📦 Кейс</b>  <i>") + len("📦 Кейс</b>  <i>")
            kkkc = message.text.index("шт.", kkc)
            kkcr = message.text[kkc:kkkc]
            kk += int(kkcr)
            kkd += int(kkcr)
            self.set("kkd", kkd)
            self.set("kk",kk)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.text and "✉" in message.text:
            ktc = message.text.index("<b>✉ Конверт</b>  <i>") + len("<b>✉ Конверт</b>  <i>")
            kttc = message.text.index("шт.</i>", ktc)
            ktcr = message.text[ktc:kttc]
            ktcr = int(ktcr)
            ktt += ktcr
            kttd += ktcr
            self.set("kttd", kttd)
            self.set("ktt",ktt)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.text and "🗳" in message.text:
            rkc = message.text.index("🗳 Редкий Кейс</b>  <i>") + len("🗳 Редкий Кейс</b>  <i>")
            rrkc = message.text.index("шт.")
            rkcr = message.text[rkc:rrkc]
            rkk += int(rkcr)
            rkkd += int(rkcr)
            self.set("rkkd", rkkd)
            self.set("rkk",rkk)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.text and "🧧" in message.text:
            rkktc = message.text.index("🧧 Редкий Конверт</b>  <i>") + len("🧧 Редкий Конверт</b>  <i>")
            rkkktc = message.text.index("шт.", rkktc)
            rkktcr = message.text[rkktc:rkkktc]
            rkkt += int(rkktcr)
            rkttd += int(rkktcr)
            self.set("rkttd", rkttd)
            self.set("rkkt",rkkt)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.text and "🕋" in message.text:
            miffc = message.text.index("🕋 Мифический Кейс</b>  <i>") + len("🕋 Мифический Кейс</b>  <i>")
            mifffc = message.text.index("шт.", miffc)
            miffcr = message.text[miffc:mifffc]
            miff += int(miffcr)
            miffd += int(miffcr)
            self.set("miffd", miffd)
            self.set("miff",miff)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.text and "💼" in message.text:
            pspt = r"\d+"
            search = re.search(pspt, message.raw_text)
            colvo = int(search[0])

            pst += colvo
            pstd += colvo
            self.set('pst', pst)
            self.set('psdt', pstd)

        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.text and "👜" in message.text:
            sspt = r"\d+"
            search = re.search(sspt, message.raw_text)
            colvo = int(search[0])

            sst += colvo
            sstd += colvo
            self.set('sst', sst)
            self.set('ssdt', sstd)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.text and "💎" in message.text:
            kkrc = message.text.index("💎 Кристальный Кейс</b>  <i>") + len("💎 Кристальный Кейс</b>  <i>")
            kkkrc = message.text.index("шт.", kkrc)
            kkrcr = message.text[kkrc:kkkrc]
            kkr += int(kkrcr)
            kkrd += int(kkrcr)
            self.set("kkrd", kkrd)
            self.set("kkr",kkr)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.text and "🎲" in message.text:
            dkkrc = message.text.index('<b>🎲 Дайс Кейс</b>  <i>') + len("<b>🎲 Дайс Кейс</b>  <i>")
            dkkkrc = message.text.index('  шт.</i>')
            dkkrcr = message.text[dkkrc:dkkkrc]
            dkkt += int(dkkrcr)
            dkktd += int(dkkrcr)
            self.set('dkkt', dkkt)
            self.set('dkktd', dkktd)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.text and "🌌" in message.text:
            zvvc = message.text.index('<b>🌌 Звёздный Кейс</b>  <i>') + len("<b>🌌 Звёздный Кейс</b>  <i>")
            zvvvc = message.text.index('  шт.</i>')
            zvcr = message.text[zvvc:zvvvc]
            zvv += int(zvcr)
            zvvd += int(zvcr)
            self.set('zvv', zvv)
            self.set('zvvd', zvvd)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "🗡" in message.raw_text and "нанес(ла) удар" in message.raw_text:
            dpt = "<b>-(.*?) оз"
            search = re.search(dpt, message.text, re.DOTALL)
            ddmgr = search.group(1)

            bdmg += int(ddmgr)
            bddmg += int(ddmgr)
            self.set("bddmg", bddmg)
            self.set("bdmg",bdmg)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💢" in message.raw_text and "нанес(ла) крит. удар" in message.raw_text:
            kdpt = "<b>-(.*?) оз"
            search = re.search(kdpt, message.text, re.DOTALL)
            kddmgr = search.group(1)

            bkdmg += int(kddmgr)
            bkddmg += int(kddmgr)
            self.set("bkddmg", bkddmg)
            self.set("bkdmg",bkdmg)
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер:" in message.raw_text:
            boostsss += 1
            boostd += 1
            self.set("boostd", boostd)
            self.set("boostsss",boostsss)
    @loader.command()
    async def ansst(self, message):
        '''- Стата'''
        timee = self.get("timee",0)
        timeee = time.time()
        fly = timeee - timee
        mmmm = fly // 60
        mmmmm = mmmm
        mmmm = mmmm % 60
        mmmm = round(mmmm)
        ss = fly % 60
        ss = round(ss)
        hhhh = fly // 3600
        hhhhh = hhhh
        hhhh = hhhh % 24
        hhhh = round(hhhh)
        dddd = fly // 86400
        ddddd = dddd
        dddd = dddd % 7
        dddd = round(dddd)
        wwww = fly // 604800
        wwwww = wwww
        wwww = wwww % 4.285
        wwww = round(wwww)
        mmmmth = fly // 2592000
        mmmmmth = mmmmth
        mmmmth = mmmmth % 12
        mmmmth = round(mmmmth)
        y = fly // 31536000
        im = self.get("im","")
        p = self.get("p",0)
        kt1 = self.get("kt1",0)
        rkt1 = self.get("rkt1",0)
        k1 = self.get("k1",0)
        rk1 = self.get("rk1",0)
        mif1 = self.get("mif1",0)
        ps = self.get('ps', 0)
        ss1 = self.get('ss1', 0)
        kr1 = self.get("kr1",0)
        dk = self.get('dk', 0)
        zv1 = self.get("zv1",0)
        pb = self.get("pb",0)
        mb = self.get("mb",0)
        sb = self.get("sb",0)
        klks = self.get("klks",0)
        bss = self.get("bss",0)
        kb = self.get("kb",0)
        rkb = self.get("rkb",0)
        ktt = self.get("ktt",0)
        rkkt = self.get("rkkt",0)
        kk = self.get("kk",0)
        rkk = self.get("rkk",0)
        bskld = self.get("bskld",0)
        mmb = self.get("mmb",0)
        es = self.get('es', 0)
        pthx = self.get("pthx",0)
        miff = self.get("miff",0)
        kkr = self.get("kkr",0)
        pst = self.get('pst', 0)
        sst = self.get('sst', 0)
        dkkt = self.get('dkkt', 0)
        zvv = self.get("zvv",0)
        bdmg = self.get("bdmg",0)
        bkdmg = self.get("bkdmg",0)
        ppthx = self.get("ppthx",0)
        boostsss = self.get("boostsss",0)
        mbp = self.get("mbp",0)
        bskn = self.get("bskn",0)
        crd = self.get('crd', 0)
        fpp = p + pb + pthx + ppthx 
        shcs = kt1 + rkt1 + k1 + rk1 + mif1 + kr1 + zv1
        bdmg = bdmg + bkdmg
        bsst = str(bss)
        bssr = " "
        bbb = bsst[-1]
        bbbb = 0
        bssit = int(bss) 
        klkst = str(klks)
        klkr = " "
        kkk = klkst[-1]
        kkkk = 0
        klkit = int(klks)
        if bssit > 10:
            bbbb = bsst[-2]
        if bbb in ["1"]:
            bssr = "босса"
        if bbb in ["2", "3", "4", "5", "6", "7", "9", "8", "0"]:
            bssr = "боссов"
        if bbb in ["1"] and bbbb in ["1"]:
            bssr = "боссов"
        if klkit > 10:
            kkkk = klkst[-2]
        if kkk in ["1"]:
            klkr = "клик"
        if kkk in ["2","3", "4"]:
            klkr = "клика"
        if kkk in ["5", "6", "7", "8", "9", "0"]:
            klkr = "кликов"
        if kkkk in ["1"] and kkk in ["1"]:
            klkr = "кликов"
        if mmmmm < 1:
            await self.client.send_message(
                message.peer_id,
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока <code>{im}</code></b>за <i>{ss}с.:</i>\n\n<b><emoji document_id=5019364941228933739>🧱</emoji> | В шахте :</b>\n\n👆 | <b>За <code>{klks}</code> {klkr}\n\n<b>✉️ | Конверт : <code>{kt1}</code>\n🧧 | Редкий Конверт : <code>{rkt1}</code>\n📦 | Кейс : <code>{k1}</code>\n🗳 | Редкий Кейс : <code>{rk1}</code>\n🕋 | Мифический Кейс : <code>{mif1}</code>\n💼 | Портфель с Эскизами : <code>{ps}</code>\n👜 | Сумка с Предметами : <code>{ss1}</code>\n💎 | Кристальный Кейс : <code>{kr1}</code>\n🎲 | Дайс Кейс : <code>{dk}</code>\n🌌 | Звёздный Кейс : <code>{zv1}</code></b> \n<i>Всего кейсов с шахты:</i> <code>{shcs}</code>\n\n<b><emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{p}</code>\n<emoji document_id=5456140674028019486>⚡️</emoji> | Бусты : <code>{boostsss}</code></b>\n\n<emoji document_id=5465137208878969279>😵</emoji> | <b>С <code>{bss}</code> {bssr} | Добиты тобой : <code>{bskld}</code>\n\n🌀 | Эссенция : <code>{es}</code>\n🔩 | Скрап : <code>{sb}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{pb}</code>\n🎖 | Медали : <code>{mb}</code>\n📦 | Кейсы : <code>{kb}</code>\n🗳 | Редкие Кейсы : <code>{rkb}</code>\n🕋 | Мифические Кейсы : <code>{mmb}</code>\n🩸 | Всего нанесено урона : <code>{bdmg}</code>\n💢 | Критического урона: <code>{bkdmg}</code>\n<emoji document_id=5463277406435422003>🗡</emoji> | Нанесено ударов : <code>{bskn}</code></b>\n\n<emoji document_id=5215440433198413312>🎁</emoji> | <b>Трейды :\n\n✉️ | Конверты : <code>{ktt}</code>\n🧧 | Редкие Конверты : <code>{rkkt}</code>\n📦 | Кейсы : <code>{kk}</code>\n🗳 | Редкий Кейс : <code>{rkk}</code>\n🕋 | Мифический Кейс : <code>{miff}</code>\n💼 | Портфель с Эскизами : <code>{pst}</code>\n👜 | Сумка с Предметами : <code>{sst}</code>\n💎 | Кристальный Кейс : <code>{kkr}</code>\n🎲 | Дайс Кейс : <code>{dkkt}</code>\n🌌 | Звёздный Кейс : <code>{zvv}</code></b>\n\n<b><emoji document_id=5033104253846029290>📚</emoji> | Прочее :\n\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодаришь ты : <code>{pthx}</code>\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодарят тебя : <code>{ppthx}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма за всё время: <code>{fpp}</code>\n💳 | Перечисленные кредиты: </b><code>{crd}</code>")

        if message.out:
            await message.delete()
                        
        if hhhhh < 1 and mmmmm > 1:
            await self.client.send_message(
                message.peer_id,
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока <code>{im}</code></b>за <i>{mmmm}мин.{ss}с.:</i>\n\n<b><emoji document_id=5019364941228933739>🧱</emoji> | В шахте :</b>\n\n👆 | <b>За <code>{klks}</code> {klkr}\n\n<b>✉️ | Конверт : <code>{kt1}</code>\n🧧 | Редкий Конверт : <code>{rkt1}</code>\n📦 | Кейс : <code>{k1}</code>\n🗳 | Редкий Кейс : <code>{rk1}</code>\n🕋 | Мифический Кейс : <code>{mif1}</code>\n💼 | Портфель с Эскизами : <code>{ps}</code>\n👜 | Сумка с Предметами : <code>{ss1}</code>\n💎 | Кристальный Кейс : <code>{kr1}</code>\n🎲 | Дайс Кейс : <code>{dk}</code>\n🌌 | Звёздный Кейс : <code>{zv1}</code></b> \n<i>Всего кейсов с шахты:</i> <code>{shcs}</code>\n\n<b><emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{p}</code>\n<emoji document_id=5456140674028019486>⚡️</emoji> | Бусты : <code>{boostsss}</code></b>\n\n<emoji document_id=5465137208878969279>😵</emoji> | <b>С <code>{bss}</code> {bssr} | Добиты тобой : <code>{bskld}</code>\n\n🌀 | Эссенция : <code>{es}</code>\n🔩 | Скрап : <code>{sb}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{pb}</code>\n🎖 | Медали : <code>{mb}</code>\n📦 | Кейсы : <code>{kb}</code>\n🗳 | Редкие Кейсы : <code>{rkb}</code>\n🕋 | Мифические Кейсы : <code>{mmb}</code>\n🩸 | Всего нанесено урона : <code>{bdmg}</code>\n💢 | Критического урона: <code>{bkdmg}</code>\n<emoji document_id=5463277406435422003>🗡</emoji> | Нанесено ударов : <code>{bskn}</code></b>\n\n<emoji document_id=5215440433198413312>🎁</emoji> | <b>Трейды :\n\n✉️ | Конверты : <code>{ktt}</code>\n🧧 | Редкие Конверты : <code>{rkkt}</code>\n📦 | Кейсы : <code>{kk}</code>\n🗳 | Редкий Кейс : <code>{rkk}</code>\n🕋 | Мифический Кейс : <code>{miff}</code>\n💼 | Портфель с Эскизами : <code>{pst}</code>\n👜 | Сумка с Предметами : <code>{sst}</code>\n💎 | Кристальный Кейс : <code>{kkr}</code>\n🎲 | Дайс Кейс : <code>{dkkt}</code>\n🌌 | Звёздный Кейс : <code>{zvv}</code></b>\n\n<b><emoji document_id=5033104253846029290>📚</emoji> | Прочее :\n\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодаришь ты : <code>{pthx}</code>\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодарят тебя : <code>{ppthx}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма за всё время: <code>{fpp}</code>\n💳 | Перечисленные кредиты: </b><code>{crd}</code>")

        if message.out:
            await message.delete()
                        
        if ddddd < 1 and hhhhh > 0:
            await self.client.send_message(
                message.peer_id,
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока <code>{im}</code></b>за <i>{hhhh}ч.{mmmm}мин.{ss}с.:</i>\n\n<b><emoji document_id=5019364941228933739>🧱</emoji> | В шахте :</b>\n\n👆 | <b>За <code>{klks}</code> {klkr}\n\n<b>✉️ | Конверт : <code>{kt1}</code>\n🧧 | Редкий Конверт : <code>{rkt1}</code>\n📦 | Кейс : <code>{k1}</code>\n🗳 | Редкий Кейс : <code>{rk1}</code>\n🕋 | Мифический Кейс : <code>{mif1}</code>\n💼 | Портфель с Эскизами : <code>{ps}</code>\n👜 | Сумка с Предметами : <code>{ss1}</code>\n💎 | Кристальный Кейс : <code>{kr1}</code>\n🎲 | Дайс Кейс : <code>{dk}</code>\n🌌 | Звёздный Кейс : <code>{zv1}</code></b> \n<i>Всего кейсов с шахты:</i> <code>{shcs}</code>\n\n<b><emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{p}</code>\n<emoji document_id=5456140674028019486>⚡️</emoji> | Бусты : <code>{boostsss}</code></b>\n\n<emoji document_id=5465137208878969279>😵</emoji> | <b>С <code>{bss}</code> {bssr} | Добиты тобой : <code>{bskld}</code>\n\n🌀 | Эссенция : <code>{es}</code>\n🔩 | Скрап : <code>{sb}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{pb}</code>\n🎖 | Медали : <code>{mb}</code>\n📦 | Кейсы : <code>{kb}</code>\n🗳 | Редкие Кейсы : <code>{rkb}</code>\n🕋 | Мифические Кейсы : <code>{mmb}</code>\n🩸 | Всего нанесено урона : <code>{bdmg}</code>\n💢 | Критического урона: <code>{bkdmg}</code>\n<emoji document_id=5463277406435422003>🗡</emoji> | Нанесено ударов : <code>{bskn}</code></b>\n\n<emoji document_id=5215440433198413312>🎁</emoji> | <b>Трейды :\n\n✉️ | Конверты : <code>{ktt}</code>\n🧧 | Редкие Конверты : <code>{rkkt}</code>\n📦 | Кейсы : <code>{kk}</code>\n🗳 | Редкий Кейс : <code>{rkk}</code>\n🕋 | Мифический Кейс : <code>{miff}</code>\n💼 | Портфель с Эскизами : <code>{pst}</code>\n👜 | Сумка с Предметами : <code>{sst}</code>\n💎 | Кристальный Кейс : <code>{kkr}</code>\n🎲 | Дайс Кейс : <code>{dkkt}</code>\n🌌 | Звёздный Кейс : <code>{zvv}</code></b>\n\n<b><emoji document_id=5033104253846029290>📚</emoji> | Прочее :\n\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодаришь ты : <code>{pthx}</code>\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодарят тебя : <code>{ppthx}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма за всё время: <code>{fpp}</code>\n💳 | Перечисленные кредиты: </b><code>{crd}</code>")

        if message.out:
            await message.delete()
                        
        if wwwww < 1 and ddddd > 0:
            await self.client.send_message(
                message.peer_id,
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока <code>{im}</code></b>за <i>{dddd}д.{hhhh}ч.{mmmm}мин.{ss}с.:</i>\n\n<b><emoji document_id=5019364941228933739>🧱</emoji> | В шахте :</b>\n\n👆 | <b>За <code>{klks}</code> {klkr}\n\n<b>✉️ | Конверт : <code>{kt1}</code>\n🧧 | Редкий Конверт : <code>{rkt1}</code>\n📦 | Кейс : <code>{k1}</code>\n🗳 | Редкий Кейс : <code>{rk1}</code>\n🕋 | Мифический Кейс : <code>{mif1}</code>\n💼 | Портфель с Эскизами : <code>{ps}</code>\n👜 | Сумка с Предметами : <code>{ss1}</code>\n💎 | Кристальный Кейс : <code>{kr1}</code>\n🎲 | Дайс Кейс : <code>{dk}</code>\n🌌 | Звёздный Кейс : <code>{zv1}</code></b> \n<i>Всего кейсов с шахты:</i> <code>{shcs}</code>\n\n<b><emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{p}</code>\n<emoji document_id=5456140674028019486>⚡️</emoji> | Бусты : <code>{boostsss}</code></b>\n\n<emoji document_id=5465137208878969279>😵</emoji> | <b>С <code>{bss}</code> {bssr} | Добиты тобой : <code>{bskld}</code>\n\n🌀 | Эссенция : <code>{es}</code>\n🔩 | Скрап : <code>{sb}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{pb}</code>\n🎖 | Медали : <code>{mb}</code>\n📦 | Кейсы : <code>{kb}</code>\n🗳 | Редкие Кейсы : <code>{rkb}</code>\n🕋 | Мифические Кейсы : <code>{mmb}</code>\n🩸 | Всего нанесено урона : <code>{bdmg}</code>\n💢 | Критического урона: <code>{bkdmg}</code>\n<emoji document_id=5463277406435422003>🗡</emoji> | Нанесено ударов : <code>{bskn}</code></b>\n\n<emoji document_id=5215440433198413312>🎁</emoji> | <b>Трейды :\n\n✉️ | Конверты : <code>{ktt}</code>\n🧧 | Редкие Конверты : <code>{rkkt}</code>\n📦 | Кейсы : <code>{kk}</code>\n🗳 | Редкий Кейс : <code>{rkk}</code>\n🕋 | Мифический Кейс : <code>{miff}</code>\n💼 | Портфель с Эскизами : <code>{pst}</code>\n👜 | Сумка с Предметами : <code>{sst}</code>\n💎 | Кристальный Кейс : <code>{kkr}</code>\n🎲 | Дайс Кейс : <code>{dkkt}</code>\n🌌 | Звёздный Кейс : <code>{zvv}</code></b>\n\n<b><emoji document_id=5033104253846029290>📚</emoji> | Прочее :\n\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодаришь ты : <code>{pthx}</code>\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодарят тебя : <code>{ppthx}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма за всё время: <code>{fpp}</code>\n💳 | Перечисленные кредиты: </b><code>{crd}</code>")

        if message.out:
            await message.delete()
                        
        if mmmmmth < 1 and wwwww > 0:
            await self.client.send_message(
                message.peer_id,
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока <code>{im}</code></b>за <i>{wwww}нед.{dddd}д.{hhhh}ч.{mmmm}мин.{ss}с.:</i>\n\n<b><emoji document_id=5019364941228933739>🧱</emoji> | В шахте :</b>\n\n👆 | <b>За <code>{klks}</code> {klkr}\n\n<b>✉️ | Конверт : <code>{kt1}</code>\n🧧 | Редкий Конверт : <code>{rkt1}</code>\n📦 | Кейс : <code>{k1}</code>\n🗳 | Редкий Кейс : <code>{rk1}</code>\n🕋 | Мифический Кейс : <code>{mif1}</code>\n💼 | Портфель с Эскизами : <code>{ps}</code>\n👜 | Сумка с Предметами : <code>{ss1}</code>\n💎 | Кристальный Кейс : <code>{kr1}</code>\n🎲 | Дайс Кейс : <code>{dk}</code>\n🌌 | Звёздный Кейс : <code>{zv1}</code></b> \n<i>Всего кейсов с шахты:</i> <code>{shcs}</code>\n\n<b><emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{p}</code>\n<emoji document_id=5456140674028019486>⚡️</emoji> | Бусты : <code>{boostsss}</code></b>\n\n<emoji document_id=5465137208878969279>😵</emoji> | <b>С <code>{bss}</code> {bssr} | Добиты тобой : <code>{bskld}</code>\n\n🌀 | Эссенция : <code>{es}</code>\n🔩 | Скрап : <code>{sb}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{pb}</code>\n🎖 | Медали : <code>{mb}</code>\n📦 | Кейсы : <code>{kb}</code>\n🗳 | Редкие Кейсы : <code>{rkb}</code>\n🕋 | Мифические Кейсы : <code>{mmb}</code>\n🩸 | Всего нанесено урона : <code>{bdmg}</code>\n💢 | Критического урона: <code>{bkdmg}</code>\n<emoji document_id=5463277406435422003>🗡</emoji> | Нанесено ударов : <code>{bskn}</code></b>\n\n<emoji document_id=5215440433198413312>🎁</emoji> | <b>Трейды :\n\n✉️ | Конверты : <code>{ktt}</code>\n🧧 | Редкие Конверты : <code>{rkkt}</code>\n📦 | Кейсы : <code>{kk}</code>\n🗳 | Редкий Кейс : <code>{rkk}</code>\n🕋 | Мифический Кейс : <code>{miff}</code>\n💼 | Портфель с Эскизами : <code>{pst}</code>\n👜 | Сумка с Предметами : <code>{sst}</code>\n💎 | Кристальный Кейс : <code>{kkr}</code>\n🎲 | Дайс Кейс : <code>{dkkt}</code>\n🌌 | Звёздный Кейс : <code>{zvv}</code></b>\n\n<b><emoji document_id=5033104253846029290>📚</emoji> | Прочее :\n\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодаришь ты : <code>{pthx}</code>\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодарят тебя : <code>{ppthx}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма за всё время: <code>{fpp}</code>\n💳 | Перечисленные кредиты: </b><code>{crd}</code>")

        if message.out:
            await message.delete()

        if y < 1 and mmmmmth > 0:
            await self.client.send_message(
                message.peer_id,
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока <code>{im}</code></b>за <i>{mmmmth}мес.{wwww}нед.{dddd}д.{hhhh}ч.{mmmm}мин.{ss}с.:</i>\n\n<b><emoji document_id=5019364941228933739>🧱</emoji> | В шахте :</b>\n\n👆 | <b>За <code>{klks}</code> {klkr}\n\n<b>✉️ | Конверт : <code>{kt1}</code>\n🧧 | Редкий Конверт : <code>{rkt1}</code>\n📦 | Кейс : <code>{k1}</code>\n🗳 | Редкий Кейс : <code>{rk1}</code>\n🕋 | Мифический Кейс : <code>{mif1}</code>\n💼 | Портфель с Эскизами : <code>{ps}</code>\n👜 | Сумка с Предметами : <code>{ss1}</code>\n💎 | Кристальный Кейс : <code>{kr1}</code>\n🎲 | Дайс Кейс : <code>{dk}</code>\n🌌 | Звёздный Кейс : <code>{zv1}</code></b> \n<i>Всего кейсов с шахты:</i> <code>{shcs}</code>\n\n<b><emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{p}</code>\n<emoji document_id=5456140674028019486>⚡️</emoji> | Бусты : <code>{boostsss}</code></b>\n\n<emoji document_id=5465137208878969279>😵</emoji> | <b>С <code>{bss}</code> {bssr} | Добиты тобой : <code>{bskld}</code>\n\n🌀 | Эссенция : <code>{es}</code>\n🔩 | Скрап : <code>{sb}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{pb}</code>\n🎖 | Медали : <code>{mb}</code>\n📦 | Кейсы : <code>{kb}</code>\n🗳 | Редкие Кейсы : <code>{rkb}</code>\n🕋 | Мифические Кейсы : <code>{mmb}</code>\n🩸 | Всего нанесено урона : <code>{bdmg}</code>\n💢 | Критического урона: <code>{bkdmg}</code>\n<emoji document_id=5463277406435422003>🗡</emoji> | Нанесено ударов : <code>{bskn}</code></b>\n\n<emoji document_id=5215440433198413312>🎁</emoji> | <b>Трейды :\n\n✉️ | Конверты : <code>{ktt}</code>\n🧧 | Редкие Конверты : <code>{rkkt}</code>\n📦 | Кейсы : <code>{kk}</code>\n🗳 | Редкий Кейс : <code>{rkk}</code>\n🕋 | Мифический Кейс : <code>{miff}</code>\n💼 | Портфель с Эскизами : <code>{pst}</code>\n👜 | Сумка с Предметами : <code>{sst}</code>\n💎 | Кристальный Кейс : <code>{kkr}</code>\n🎲 | Дайс Кейс : <code>{dkkt}</code>\n🌌 | Звёздный Кейс : <code>{zvv}</code></b>\n\n<b><emoji document_id=5033104253846029290>📚</emoji> | Прочее :\n\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодаришь ты : <code>{pthx}</code>\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодарят тебя : <code>{ppthx}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма за всё время: <code>{fpp}</code>\n💳 | Перечисленные кредиты: </b><code>{crd}</code>")

        if message.out:
            await message.delete()
        
        if y > 0:
            await self.client.send_message(
                message.peer_id,
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока <code>{im}</code></b>за <i>{y}г.{mmmmth}мес.{wwww}нед.{dddd}д.{hhhh}ч.{mmmm}мин.{ss}с.:</i>\n\n<b><emoji document_id=5019364941228933739>🧱</emoji> | В шахте :</b>\n\n👆 | <b>За <code>{klks}</code> {klkr}\n\n<b>✉️ | Конверт : <code>{kt1}</code>\n🧧 | Редкий Конверт : <code>{rkt1}</code>\n📦 | Кейс : <code>{k1}</code>\n🗳 | Редкий Кейс : <code>{rk1}</code>\n🕋 | Мифический Кейс : <code>{mif1}</code>\n💼 | Портфель с Эскизами : <code>{ps}</code>\n👜 | Сумка с Предметами : <code>{ss1}</code>\n💎 | Кристальный Кейс : <code>{kr1}</code>\n🎲 | Дайс Кейс : <code>{dk}</code>\n🌌 | Звёздный Кейс : <code>{zv1}</code></b> \n<i>Всего кейсов с шахты:</i> <code>{shcs}</code>\n\n<b><emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{p}</code>\n<emoji document_id=5456140674028019486>⚡️</emoji> | Бусты : <code>{boostsss}</code></b>\n\n<emoji document_id=5465137208878969279>😵</emoji> | <b>С <code>{bss}</code> {bssr} | Добиты тобой : <code>{bskld}</code>\n\n🌀 | Эссенция : <code>{es}</code>\n🔩 | Скрап : <code>{sb}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{pb}</code>\n🎖 | Медали : <code>{mb}</code>\n📦 | Кейсы : <code>{kb}</code>\n🗳 | Редкие Кейсы : <code>{rkb}</code>\n🕋 | Мифические Кейсы : <code>{mmb}</code>\n🩸 | Всего нанесено урона : <code>{bdmg}</code>\n💢 | Критического урона: <code>{bkdmg}</code>\n<emoji document_id=5463277406435422003>🗡</emoji> | Нанесено ударов : <code>{bskn}</code></b>\n\n<emoji document_id=5215440433198413312>🎁</emoji> | <b>Трейды :\n\n✉️ | Конверты : <code>{ktt}</code>\n🧧 | Редкие Конверты : <code>{rkkt}</code>\n📦 | Кейсы : <code>{kk}</code>\n🗳 | Редкий Кейс : <code>{rkk}</code>\n🕋 | Мифический Кейс : <code>{miff}</code>\n💼 | Портфель с Эскизами : <code>{pst}</code>\n👜 | Сумка с Предметами : <code>{sst}</code>\n💎 | Кристальный Кейс : <code>{kkr}</code>\n🎲 | Дайс Кейс : <code>{dkkt}</code>\n🌌 | Звёздный Кейс : <code>{zvv}</code></b>\n\n<b><emoji document_id=5033104253846029290>📚</emoji> | Прочее :\n\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодаришь ты : <code>{pthx}</code>\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодарят тебя : <code>{ppthx}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма за всё время: <code>{fpp}</code>\n💳 | Перечисленные кредиты: </b><code>{crd}</code>")

        if message.out:
            await message.delete()
    @loader.command()
    async def anstt(self,message):
        '''- Стата за сегодня'''
        im = self.get('im',None)
        dayp = self.get("dayp",0)
        skp = self.get("skp",0)
        mbp = self.get("mbp",0)
        bskldd = self.get("bskldd",0)
        bssd = self.get("bssd",0)
        bskn = self.get("bskn",0)
        ktd1 = self.get("ktd1",0)
        rktd1 = self.get("rktd1", 0)
        kd1 = self.get("kd1", 0)
        rkd1 = self.get("rkd1", 0)
        mifd1 = self.get("mifd1",0)
        psd = self.get('psd', 0)
        ssd = self.get('ssd', 0)
        krd1 = self.get("krd1",0)
        dkd = self.get('dkd', 0)
        shdp = self.get("shdp", 0)
        bsknd = self.get("bsknd",0)
        bspd = self.get("bspd",0)
        zvd1 = self.get("zvd1", 0)
        klksd = self.get("klksd", 0)
        boostd = self.get("boostd", 0)
        bskbd = self.get("bskbd", 0)
        bsrkbd = self.get("bsrkbd", 0)
        esd = self.get('esd', 0)
        bsmifbd = self.get("bsmifbd", 0)
        bddmg = self.get("bddmg", 0)
        bkddmg = self.get("bkddmg", 0)
        kttd = self.get("kttd", 0)
        rkttd = self.get("rkttd", 0)
        kkd = self.get("kkd", 0)
        rkkd = self.get("rkkd", 0)
        miffd = self.get("miffd", 0)
        kkrd = self.get("kkrd", 0)
        pstd = self.get('pstd', 0)
        sstd = self.get('sstd', 0)
        dkktd = self.get('dkktd',0)
        zvvd = self.get("zvvd", 0)
        ppthxd = self.get("ppthxd", 0)
        pthxd = self.get("pthxd", 0)
        bssd = self.get("bssd", 0)
        crdd = self.get('crdd', 0)
        fppd = shdp + bspd + ppthxd + pthxd 
        bddmg = bddmg + bkddmg
        shcsd = ktd1 + rktd1 + rkd1 + kd1 + mifd1 + krd1 + zvd1
        bsst = str(bssd)
        bssr = " "
        bbb = bsst[-1]
        bbbb = 0
        bssit = int(bssd) 
        klkst = str(klksd)
        klkr = " "
        kkk = klkst[-1]
        kkkk = 0
        klkit = int(klksd)
        if bssit > 10:
            bbbb = bsst[-2]
        if bbb in ["1"]:
            bssr = "босса"
        if bbb in ["2", "3", "4", "5", "6", "7", "9", "8", "0"]:
            bssr = "боссов"
        if bbb in ["1"] and bbbb in ["1"]:
            bssr = "боссов"
        if klkit > 10:
            kkkk = klkst[-2]
        if kkk in ["1"]:
            klkr = "клик"
        if kkk in ["2","3", "4"]:
            klkr = "клика"
        if kkk in ["5", "6", "7", "8", "9", "0"]:
            klkr = "кликов"
        if kkkk in ["1"] and kkk in ["1"]:
            klkr = "кликов"
        await self.client.send_message(
            message.peer_id,
            f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока <code>{im}</code> за сегодня</b>\n\n<b><emoji document_id=5019364941228933739>🧱</emoji> | В шахте :\n\n👆 | За <code>{klksd}</code> {klkr}\n\n✉️ | Конверт : <code>{ktd1}</code>\n🧧 | Редкий Конверт : <code>{rktd1}</code>\n📦 | Кейс : <code>{kd1}</code>\n🗳 | Редкий Кейс : <code>{rkd1}</code>\n🕋 | Мифический Кейс : <code>{mifd1}</code>\n💼 | Портфель с Эскизами : <code>{psd}</code>\n👜 | Сумка с Предметами : <code>{ssd}</code>\n💎 | Кристальный Кейс : <code>{krd1}</code>\n🎲 | Дайс Кейс : <code>{dkd}</code>\n🌌 | Звёздный Кейс :</b> <code>{zvd1}</code>\n<i>Всего кейсов с шахты:</i> <code>{shcsd}</code></b>\n\n<b><emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{shdp}</code>\n<emoji document_id=5456140674028019486>⚡️</emoji> | Бусты : <code>{boostd}</code></b>\n\n<emoji document_id=5465137208878969279>😵</emoji> | <b>С <code>{bssd}</code> {bssr} | Добиты тобой : <code>{bskldd}</code>\n\n🌀 | Эссенция : <code>{esd}</code>\n🔩 | Скрап : <code>{skp}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{bspd}</code>\n🎖 | Медали : <code>{mbp}</code>\n📦 | Кейсы : <code>{bskbd}</code>\n🗳 | Редкие Кейсы : <code>{bsrkbd}</code>\n🕋 | Мифические Кейсы : <code>{bsmifbd}</code>\n🩸 | Всего нанесено урона : <code>{bddmg}</code>\n💢 | Критического урона: <code>{bkddmg}</code>\n<emoji document_id=5463277406435422003>🗡</emoji> | Нанесено ударов : </b><code>{bsknd}</code>\n\n<emoji document_id=5215440433198413312>🎁</emoji> | <b>Трейды :\n\n✉️ | Конверты : <code>{kttd}</code>\n🧧 | Редкие Конверты : <code>{rkttd}</code>\n📦 | Кейсы : <code>{kkd}</code>\n🗳 | Редкий Кейс : <code>{rkkd}</code>\n🕋 | Мифический Кейс : <code>{miffd}</code>\n💼 | Портфель с Эскизами : <code>{pstd}</code>\n👜 | Сумка с Предметами : <code>{sstd}</code>\n💎 | Кристальный Кейс : <code>{kkrd}</code>\n🎲 | Дайс Кейс : <code>{dkktd}</code>\n🌌 | Звёздный Кейс : </b><code>{zvvd}</code>\n\n<b><emoji document_id=5033104253846029290>📚</emoji> | Прочее :\n\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодаришь ты : <code>{pthxd}</code>\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодарят тебя : <code>{ppthxd}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма за сегодня: <code>{fppd}</code>\n💳 | Перечисленные кредиты: </b><code>{crdd}</code>")
        
        await message.delete()
            
        

    @loader.command()
    async def inst(self, message): 
        '''Инлайн стата'''
        im = self.get('im',None)
        await self.inline.form(
            text=f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>",
            message=message,
            reply_markup=[
                [
                    {
                        "text" : f"☀️ За сегодня",
                        "callback" : self.stdy,
                    },
                
                
                
                    {
                        "text" : f"⏳ За все время",
                        "callback" : self.sall,
                    },
                ],
                [
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    }
                ]
            ]
        )
    async def iback(self,call: InlineCall):
        im = self.get('im', None)
        await call.edit(
            text=f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>",
            reply_markup=[
                [
                    {
                        "text" : f"☀️ За сегодня",
                        "callback" : self.stdy,
                    },
                
                
                
                
                    {
                        "text" : f"⏳ За все время",
                        "callback" : self.sall,
                    },
                ],
                [
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    }
                ]
            ]
        )
    async def ibackl(self,call: InlineCall):
        timee = self.get("timee",0)
        timeee = time.time()
        fly = timeee - timee
        mmmm = fly // 60
        mmmmm = mmmm
        mmmm = mmmm % 60
        mmmm = round(mmmm)
        ss = fly % 60
        ss = round(ss)
        hhhh = fly // 3600
        hhhhh = hhhh
        hhhh = hhhh % 24
        hhhh = round(hhhh)
        dddd = fly // 86400
        ddddd = dddd
        dddd = dddd % 7
        dddd = round(dddd)
        wwww = fly // 604800
        wwwww = wwww
        wwww = wwww % 4.285
        wwww = round(wwww)
        mmmmth = fly // 2592000
        mmmmmth = mmmmth
        mmmmth = mmmmth % 12
        mmmmth = round(mmmmth)
        y = fly // 31536000
        im = self.get("im","")
        if mmmmm < 1:
            await call.edit(
                text=f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )
        if hhhhh < 1 and mmmmm > 1:
            await call.edit(
                text=f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{mmmm}мин.{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )           

                        
        if ddddd < 1 and hhhhh > 0:
            await call.edit(
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{hhhh}ч.{mmmm}мин.{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )                        
        if wwwww < 1 and ddddd > 0:
            await call.edit(
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{dddd}д.{hhhh}ч.{mmmm}мин.{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )

                        
        if mmmmmth < 1 and wwwww > 0:
            await call.edit(
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{wwww}нед.{dddd}д.{hhhh}ч.{mmmm}мин.{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )

        if y < 1 and mmmmmth > 0:
            await call.edit(
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{mmmmth}мес.{wwww}нед.{dddd}д.{hhhh}ч.{mmmm}мин.{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )
        
        if y > 0:
            await call.edit(
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{y}г.{mmmmth}мес.{wwww}нед.{dddd}д.{hhhh}ч.{mmmm}мин.{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )
    async def ibackd(self,call: InlineCall):
        im = self.get("im", None)
        await call.edit(
            text=f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im} за сегодня</b>:",
            reply_markup=[
                [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.ishtd,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibssd,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrdd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianfd,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    }
                ]
            ]
        )
    async def stdy(self, call: InlineCall):
        im = self.get("im", None)
        await call.edit(
            text=f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im} за сегодня</b>:",
            reply_markup=[
                [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.ishtd,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibssd,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrdd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianfd,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    }
                ]
            ]
        )
    async def sall(self, call: InlineCall):
        timee = self.get("timee",0)
        timeee = time.time()
        fly = timeee - timee
        mmmm = fly // 60
        mmmmm = mmmm
        mmmm = mmmm % 60
        mmmm = round(mmmm)
        ss = fly % 60
        ss = round(ss)
        hhhh = fly // 3600
        hhhhh = hhhh
        hhhh = hhhh % 24
        hhhh = round(hhhh)
        dddd = fly // 86400
        ddddd = dddd
        dddd = dddd % 7
        dddd = round(dddd)
        wwww = fly // 604800
        wwwww = wwww
        wwww = wwww % 4.285
        wwww = round(wwww)
        mmmmth = fly // 2592000
        mmmmmth = mmmmth
        mmmmth = mmmmth % 12
        mmmmth = round(mmmmth)
        y = fly // 31536000
        im = self.get("im","")
        if mmmmm < 1:
            await call.edit(
                text=f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )
        if hhhhh < 1 and mmmmm > 1:
            await call.edit(
                text=f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{mmmm}мин.{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )           

                        
        if ddddd < 1 and hhhhh > 0:
            await call.edit(
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{hhhh}ч.{mmmm}мин.{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )                        
        if wwwww < 1 and ddddd > 0:
            await call.edit(
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{dddd}д.{hhhh}ч.{mmmm}мин.{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )

                        
        if mmmmmth < 1 and wwwww > 0:
            await call.edit(
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{wwww}нед.{dddd}д.{hhhh}ч.{mmmm}мин.{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )

        if y < 1 and mmmmmth > 0:
            await call.edit(
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{mmmmth}мес.{wwww}нед.{dddd}д.{hhhh}ч.{mmmm}мин.{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )
        
        if y > 0:
            await call.edit(
                f"<b><emoji document_id=5231200819986047254>📊</emoji> | Статистика игрока {im}</b>за <i>{y}г.{mmmmth}мес.{wwww}нед.{dddd}д.{hhhh}ч.{mmmm}мин.{ss}с.:</i>",
                reply_markup=[
                     [
                    {
                        "text" : "🧱 Шахта",
                        "callback" : self.isht,
                    },
                
                
                    {
                        "text" : "☠️ Боссы",
                        "callback" : self.ibss,
                    },
                
                
                    {
                        "text" : "🎁 Трейды",
                        "callback" : self.itrd,
                    }
                ],
                [
                    {
                        "text" : "📚 Прочее",
                        "callback" : self.ianf,
                    }
                ],
                [
                    {
                        "text" : "♻️ Сбросить статистику",
                        "callback" : self.idrest,
                    }
                ],
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.iback,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close",
                    },
                ],
            ]
        )
    async def ishtd(self,call: InlineCall):
        ktd1 = self.get("ktd1",0)
        rktd1 = self.get("rktd1", 0)
        kd1 = self.get("kd1", 0)
        rkd1 = self.get("rkd1", 0)
        mifd1 = self.get("mifd1",0)
        psd = self.get('psd', 0)
        ssd = self.get('ssd', 0)
        krd1 = self.get("krd1",0)
        dkd = self.get('dkd', 0)
        shdp = self.get("shdp", 0)
        zvd1 = self.get("zvd1", 0)
        klksd = self.get("klksd", 0)
        boostd = self.get("boostd", 0)
        shcsd = ktd1 + rktd1 + rkd1 + kd1 + mifd1 + krd1 + zvd1
        klkst = str(klksd)
        klkr = " "
        kkk = klkst[-1]
        kkkk = 0
        klkit = int(klksd)
        if klkit > 10:
            kkkk = klkst[-2]
        if kkk in ["1"]:
            klkr = "клик"
        if kkk in ["2","3", "4"]:
            klkr = "клика"
        if kkk in ["5", "6", "7", "8", "9", "0"]:
            klkr = "кликов"
        if kkkk in ["1"] and kkk in ["1"]:
            klkr = "кликов"
        await call.edit(
            text=f"<b><emoji document_id=5019364941228933739>🧱</emoji> | В шахте :\n\n👆 | За <code>{klksd}</code> {klkr}\n\n✉️ | Конверт : <code>{ktd1}</code>\n🧧 | Редкий Конверт : <code>{rktd1}</code>\n📦 | Кейс : <code>{kd1}</code>\n🗳 | Редкий Кейс : <code>{rkd1}</code>\n🕋 | Мифический Кейс : <code>{mifd1}</code>\n💼 | Портфель с Эскизами : <code>{psd}</code>\n👜 | Сумка с Предметами : <code>{ssd}</code>\n💎 | Кристальный Кейс : <code>{krd1}</code>\n🎲 | Дайс Кейс : <code>{dkd}</code>\n🌌 | Звёздный Кейс :</b> <code>{zvd1}</code>\n<i>Всего кейсов с шахты:</i> <code>{shcsd}</code>\n\n<b><emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{shdp}</code>\n<emoji document_id=5456140674028019486>⚡️</emoji> | Бусты : <code>{boostd}</code></b>",
            reply_markup=[
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.ibackd, 
                    }
                ]
            ]      
        )
    async def isht(self,call: InlineCall):
        p = self.get("p",0)
        kt1 = self.get("kt1",0)
        rkt1 = self.get("rkt1",0)
        k1 = self.get("k1",0)
        rk1 = self.get("rk1",0)
        mif1 = self.get("mif1",0)
        ps = self.get('ps', 0)
        ss1 = self.get('ss1', 0)
        kr1 = self.get("kr1",0)
        dk = self.get('dk', 0)
        zv1 = self.get("zv1",0)
        klks = self.get("klks",0)
        shcs = kt1 + rkt1 + k1 + rk1 + mif1 + kr1 + zv1
        klkst = str(klks)
        klkr = " "
        kkk = klkst[-1]
        kkkk = 0
        klkit = int(klks)
        boostsss = self.get("boostsss",0)
        if klkit > 10:
            kkkk = klkst[-2]
        if kkk in ["1"]:
            klkr = "клик"
        if kkk in ["2","3", "4"]:
            klkr = "клика"
        if kkk in ["5", "6", "7", "8", "9", "0"]:
            klkr = "кликов"
        if kkkk in ["1"] and kkk in ["1"]:
            klkr = "кликов"
        await call.edit(
            text=f"<b><emoji document_id=5019364941228933739>🧱</emoji> | В шахте :</b>\n\n👆 | <b>За <code>{klks}</code> {klkr}\n\n✉️ | Конверт : <code>{kt1}</code>\n🧧 | Редкий Конверт : <code>{rkt1}</code>\n📦 | Кейс : <code>{k1}</code>\n🗳 | Редкий Кейс : <code>{rk1}</code>\n🕋 | Мифический Кейс : <code>{mif1}</code>\n💼 | Портфель с Эскизами : <code>{ps}</code>\n👜 | Сумка с Предметами : <code>{ss1}</code>\n💎 | Кристальный Кейс : <code>{kr1}</code>\n🎲 | Дайс Кейс : <code>{dk}</code>\n🌌 | Звёздный Кейс : <code>{zv1}</code></b>\n\n<b><emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{p}</code>\n<emoji document_id=5456140674028019486>⚡️</emoji> | Бусты : <code>{boostsss}</code></b>",
            reply_markup=[
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.ibackl, 
                    }
                ]
            ]      
        )
    async def ibssd(self,call: InlineCall):
        skp = self.get("skp",0)
        mbp = self.get("mbp",0)
        bskldd = self.get("bskldd",0)
        bssd = self.get("bssd",0)
        bskn = self.get("bskn",0)
        bsknd = self.get("bsknd",0)
        bspd = self.get("bspd",0)
        boostd = self.get("boostd", 0)
        bskbd = self.get("bskbd", 0)
        bsrkbd = self.get("bsrkbd", 0)
        esd = self.get('esd', 0)
        bsmifbd = self.get("bsmifbd", 0)
        bddmg = self.get("bddmg", 0)
        bkddmg = self.get("bkddmg", 0)
        bssd = self.get("bssd", 0)
        bddmg = bddmg + bkddmg
        bsst = str(bssd)
        bssr = " "
        bbb = bsst[-1]
        bbbb = 0
        bssit = int(bssd) 
        if bssit > 10:
            bbbb = bsst[-2]
        if bbb in ["1"]:
            bssr = "босса"
        if bbb in ["2", "3", "4", "5", "6", "7", "9", "8", "0"]:
            bssr = "боссов"
        if bbb in ["1"] and bbbb in ["1"]:
            bssr = "боссов"
        await call.edit(
            text=f"<emoji document_id=5465137208878969279>😵</emoji> | <b>С <code>{bssd}</code> {bssr} | Добиты тобой : <code>{bskldd}</code>\n\n🌀 | Эссенция : <code>{esd}</code>\n🔩 | Скрап : <code>{skp}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{bspd}</code>\n🎖 | Медали : <code>{mbp}</code>\n📦 | Кейсы : <code>{bskbd}</code>\n🗳 | Редкие Кейсы : <code>{bsrkbd}</code>\n🕋 | Мифические Кейсы : <code>{bsmifbd}</code>\n🩸 | Всего нанесено урона : <code>{bddmg}</code>\n💢 | Критического урона: <code>{bkddmg}</code>\n<emoji document_id=5463277406435422003>🗡</emoji> | Нанесено ударов : </b><code>{bsknd}</code>",
            reply_markup=[
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.ibackd, 
                    }
                ]
            ]      
        )
        
    async def ibss(self,call: InlineCall):
        pb = self.get("pb",0)
        mb = self.get("mb",0)
        sb = self.get("sb",0)
        bss = self.get("bss",0)
        kb = self.get("kb",0)
        rkb = self.get("rkb",0)
        ktt = self.get("ktt",0)
        bskld = self.get("bskld",0)
        mmb = self.get("mmb",0)
        es = self.get('es', 0)
        bdmg = self.get("bdmg",0)
        bkdmg = self.get("bkdmg",0)
        mbp = self.get("mbp",0)
        bskn = self.get("bskn",0)
        bdmg = bdmg + bkdmg
        bsst = str(bss)
        bssr = " "
        bbb = bsst[-1]
        bbbb = 0
        bssit = int(bss) 
        if bssit > 10:
            bbbb = bsst[-2]
        if bbb in ["1"]:
            bssr = "босса"
        if bbb in ["2", "3", "4", "5", "6", "7", "9", "8", "0"]:
            bssr = "боссов"
        if bbb in ["1"] and bbbb in ["1"]:
            bssr = "боссов"
        await call.edit(
            text=f"<emoji document_id=5465137208878969279>😵</emoji> | <b>С <code>{bss}</code> {bssr} | Добиты тобой : <code>{bskld}</code>\n\n🌀 | Эссенция : <code>{es}</code>\n🔩 | Скрап : <code>{sb}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма : <code>{pb}</code>\n🎖 | Медали : <code>{mb}</code>\n📦 | Кейсы : <code>{kb}</code>\n🗳 | Редкие Кейсы : <code>{rkb}</code>\n🕋 | Мифические Кейсы : <code>{mmb}</code>\n🩸 | Всего нанесено урона : <code>{bdmg}</code>\n💢 | Критического урона: <code>{bkdmg}</code>\n<emoji document_id=5463277406435422003>🗡</emoji> | Нанесено ударов : <code>{bskn}</code></b>",
            reply_markup=[
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.ibackl, 
                    }
                ]
            ]  
        )
    async def itrdd(self,call: InlineCall):
        kttd = self.get("kttd", 0)
        rkttd = self.get("rkttd", 0)
        kkd = self.get("kkd", 0)
        rkkd = self.get("rkkd", 0)
        miffd = self.get("miffd", 0)
        kkrd = self.get("kkrd", 0)
        pstd = self.get('pstd', 0)
        sstd = self.get('sstd', 0)
        dkktd = self.get('dkktd',0)
        zvvd = self.get("zvvd", 0)
        await call.edit(
            text=f"<emoji document_id=5215440433198413312>🎁</emoji> | <b>Трейды :\n\n✉️ | Конверты : <code>{kttd}</code>\n🧧 | Редкие Конверты : <code>{rkttd}</code>\n📦 | Кейсы : <code>{kkd}</code>\n🗳 | Редкий Кейс : <code>{rkkd}</code>\n🕋 | Мифический Кейс : <code>{miffd}</code>\n💼 | Портфель с Эскизами : <code>{pstd}</code>\n👜 | Сумка с Предметами : <code>{sstd}</code>\n💎 | Кристальный Кейс : <code>{kkrd}</code>\n🎲 | Дайс Кейс : <code>{dkktd}</code>\n🌌 | Звёздный Кейс : </b><code>{zvvd}</code>",
            reply_markup=[
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.ibackd, 
                    }
                ]
            ]      
        )
    async def itrd(self,call: InlineCall):
        ktt = self.get("ktt",0)
        rkkt = self.get("rkkt",0)
        kk = self.get("kk",0)
        rkk = self.get("rkk",0)
        miff = self.get("miff",0)
        kkr = self.get("kkr",0)
        pst = self.get('pst', 0)
        sst = self.get('sst', 0)
        dkkt = self.get('dkkt', 0)
        zvv = self.get("zvv",0)
        await call.edit(
            text=f"<emoji document_id=5215440433198413312>🎁</emoji> | <b>Трейды :\n\n✉️ | Конверты : <code>{ktt}</code>\n🧧 | Редкие Конверты : <code>{rkkt}</code>\n📦 | Кейсы : <code>{kk}</code>\n🗳 | Редкий Кейс : <code>{rkk}</code>\n🕋 | Мифический Кейс : <code>{miff}</code>\n💼 | Портфель с Эскизами : <code>{pst}</code>\n👜 | Сумка с Предметами : <code>{sst}</code>\n💎 | Кристальный Кейс : <code>{kkr}</code>\n🎲 | Дайс Кейс : <code>{dkkt}</code>\n🌌 | Звёздный Кейс : <code>{zvv}</code></b>",
            reply_markup=[
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.ibackl, 
                    }
                ]
            ]
        )
    async def ianfd(self,call: InlineCall):
        shdp = self.get('shdp')
        bspd = self.get('bspd')
        pthxd = self.get("pthxd",0)
        ppthxd = self.get("ppthxd",0)
        fppd = shdp + bspd + ppthxd + pthxd 
        crdd = self.get('crdd', 0)
        await call.edit(
            text=f"<b><emoji document_id=5033104253846029290>📚</emoji> | Прочее :\n\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодаришь ты : <code>{pthxd}</code>\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодарят тебя : <code>{ppthxd}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма за сегодня: <code>{fppd}</code>\n💳 | Перечисленные кредиты: </b><code>{crdd}</code>",
            reply_markup=[
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.ibackd, 
                    }
                ]
            ]   
        )
    async def ianf(self,call: InlineCall):
        p = self.get('p')
        pb = self.get('pb')
        pthx = self.get("pthx",0)
        ppthx = self.get("ppthx",0)
        crd = self.get('crd', 0)
        fpp = p + pb + pthx + ppthx 
        await call.edit(
            text=f"<b><emoji document_id=5033104253846029290>📚</emoji> | Прочее :\n\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодаришь ты : <code>{pthx}</code>\n<emoji document_id=5447410659077661506>🌐</emoji> | Плазмы с 'thx' когда благодарят тебя : <code>{ppthx}</code>\n<emoji document_id=5431783411981228752>🎆</emoji> | Плазма за всё время: <code>{fpp}</code>\n💳 | Перечисленные кредиты: </b><code>{crd}</code>",
            reply_markup=[
                [
                    {
                        'text' : "🔙 Назад",
                        'callback' : self.ibackl, 
                    }
                ]
            ]  
        )
    async def idrest(self,call: InlineCall):
        self.set("kt1",0)
        self.set("rkt1",0)
        self.set("k1",0)
        self.set("rk1",0)
        self.set("mif1",0)
        self.set('ps', 0)
        self.set('ss1', 0)
        self.set("kr1",0)
        self.set("zv1",0)
        self.set("p",0)
        self.set("pb",0)
        self.set("sb",0)
        self.set("mb",0)
        self.set("klks",0)
        self.set('bss',0)
        self.set("ktt",0)
        self.set("rkb",0)
        self.set("kb",0)
        self.set("bskld",0)
        self.set("mmb",0)
        self.set("kk",0)
        self.set("pthx",0)
        self.set('ktt',0)
        self.set('rkk',0)
        self.set("miff",0)
        self.set("kkr",0)
        self.set('pst', 0)
        self.set('sst', 0)
        self.set("zvv",0)
        self.set("bdmg",0)
        self.set("bkdmg",0)
        self.set("ppthx",0)
        self.set("boostsss",0)
        self.set("rkkt",0)
        self.set('crd',0)
        self.set('dk', 0)
        self.set('dkkt', 0)
        im = self.get('im', "")
        timee = time.time()
        self.set("timee",timee)
        await call.edit(
                text=f"<b>✅ Статистика успешно сброшена</b>",
                reply_markup=[
                [
                    {
                        "text" : "🔙 Вернуться",
                        "callback" : self.sall,
                    },
                    {
                        "text" : "🔻 Закрыть",
                        "action" : "close"
                    }
                ]
                ]
        )
