if __name__ == "__main__":
    import nadtcp
    import logging
    import asyncio

    logging.basicConfig(level=logging.DEBUG)

    _LOGGER = logging.getLogger(__name__)

    loop = asyncio.get_event_loop()


    def state_changed(state):
        pass

    client = nadtcp.NADC338Client('192.168.1.121', loop, state_changed_cb=state_changed)

    async def test():
        asyncio.ensure_future(client.run_loop())
        while True:
            client.exec_command('Main', '?')
            await asyncio.sleep(5)

    loop.run_until_complete(test())

    loop.run_forever()
