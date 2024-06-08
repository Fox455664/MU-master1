import sys
from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        super().__init__(session_string=str(config.STRING_SESSION))
        self.one = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        await super().start()
        LOGGER(__name__).info("Getting Assistants Info...")
        # بدء العميل الأول
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("FTTUTT0")
                await self.one.join_chat("FTTUTY")
            except Exception as e:
                LOGGER(__name__).error(f"Error joining chats: {e}")
            assistants.append(1)
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            self.one.mention = get_me.mention
            assistantids.append(get_me.id)
            self.one.name = get_me.first_name
            if get_me.last_name:
                self.one.name += " " + get_me.last_name
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, f"تم تنصيب المساعد على سورس سمير."
                )
            except Exception as e:
                LOGGER(__name__).error(f"Failed to send message: {e}")
                sys.exit()

        # بدء العميل الثاني
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("FTTUTT0")
                await self.two.join_chat("FTTUTY")
            except Exception as e:
                LOGGER(__name__).error(f"Error joining chats: {e}")
            assistants.append(2)
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            self.two.mention = get_me.mention
            assistantids.append(get_me.id)
            self.two.name = get_me.first_name
            if get_me.last_name:
                self.two.name += " " + get_me.last_name
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, f"تم تنصيب المساعد الثاني على سورس سمير."
                )
            except Exception as e:
                LOGGER(__name__).error(f"Failed to send message: {e}")
                sys.exit()

        # بدء العميل الثالث
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("FTTUTT0")
                await self.three.join_chat("FTTUTY")
            except Exception as e:
                LOGGER(__name__).error(f"Error joining chats: {e}")
            assistants.append(3)
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            self.three.mention = get_me.mention
            assistantids.append(get_me.id)
            self.three.name = get_me.first_name
            if get_me.last_name:
                self.three.name += " " + get_me.last_name
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, f"تم تنصيب المساعد الثالث على سورس سمير."
                )
            except Exception as e:
                LOGGER(__name__).error(f"Failed to send message: {e}")
                sys.exit()

        # بدء العميل الرابع
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("FTTUTT0")
                await self.four.join_chat("FTTUTY")
            except Exception as e:
                LOGGER(__name__).error(f"Error joining chats: {e}")
            assistants.append(4)
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            self.four.mention = get_me.mention
            assistantids.append(get_me.id)
            self.four.name = get_me.first_name
            if get_me.last_name:
                self.four.name += " " + get_me.last_name
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, f"تم تنصيب المساعد الرابع على سورس سمير."
                )
            except Exception as e:
                LOGGER(__name__).error(f"Failed to send message: {e}")
                sys.exit()

        # بدء العميل الخامس
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("FTTUTT0")
                await self.five.join_chat("FTTUTY")
            except Exception as e:
                LOGGER(__name__).error(f"Error joining chats: {e}")
            assistants.append(5)
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            self.five.mention = get_me.mention
            assistantids.append(get_me.id)
            self.five.name = get_me.first_name
            if get_me.last_name:
                self.five.name += " " + get_me.last_name
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, f"تم تنصيب المساعد الخامس على سورس سمير."
                )
            except Exception as e:
                LOGGER(__name__).error(f"Failed to send message: {e}")
                sys.exit()

        LOGGER(__name__).info("All Assistants Started Successfully.")
