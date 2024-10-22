from unittest.mock import MagicMock

import pytest

from velbusaio.module import Module, VmbDali


class MockWriter:
    async def __call__(self, data):
        pass


@pytest.mark.asyncio
async def test_vmbdali_loads_and_has_channels():
    module_address = 0x12
    dali_type = 69
    module = VmbDali(
        module_address,
        dali_type,
    )
    writer = MockWriter()
    await module.initialize(writer)

    await module.load()

    assert len(module._channels) > 0
