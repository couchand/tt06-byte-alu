# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
  dut._log.info("Start")

  clock = Clock(dut.clk, 10, units="us")
  cocotb.start_soon(clock.start())

  # Reset
  dut._log.info("Reset")
  dut.ena.value = 1
  dut.ui_in.value = 0
  dut.uio_in.value = 0
  dut.rst_n.value = 0
  await ClockCycles(dut.clk, 10)
  dut.rst_n.value = 1

  dut.ui_in.value = 20
  dut.uio_in.value = 1
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 20

  dut.ui_in.value = 30
  dut.uio_in.value = 2
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 50

  dut.ui_in.value = 207
  dut.uio_in.value = 2
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 1

  dut.uio_in.value = 15
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 4

  dut.ui_in.value = 1
  dut.uio_in.value = 3
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0

  dut.uio_in.value = 15
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 1

  dut.ui_in.value = 1
  dut.uio_in.value = 3
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 255

  dut.uio_in.value = 15
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 6

  dut.ui_in.value = 1
  dut.uio_in.value = 3
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 254

  dut.uio_in.value = 15
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 2

  dut.ui_in.value = 0
  dut.uio_in.value = 1
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0

  dut.uio_in.value = 15
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 1

  dut.ui_in.value = 253
  dut.uio_in.value = 1
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 253

  dut.uio_in.value = 15
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 2

  dut.uio_in.value = 4
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0

  dut.uio_in.value = 15
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 1

  dut.uio_in.value = 5
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 1

  dut.uio_in.value = 15
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 0

  dut.ui_in.value = 0x16
  dut.uio_in.value = 1
  await ClockCycles(dut.clk, 1)
  dut.ui_in.value = 0xF5
  dut.uio_in.value = 6
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0xE3

  dut.uio_in.value = 7
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0x1C

  dut.ui_in.value = 1
  dut.uio_in.value = 1
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 8
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0b00000010

  dut.ui_in.value = 2
  dut.uio_in.value = 8
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0b00001000

  dut.ui_in.value = 2
  dut.uio_in.value = 8
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0b00100000

  dut.ui_in.value = 2
  dut.uio_in.value = 9
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0b00001000

  dut.ui_in.value = 3
  dut.uio_in.value = 9
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0b00000001

  dut.ui_in.value = 0xF0
  dut.uio_in.value = 1
  await ClockCycles(dut.clk, 1)
  dut.ui_in.value = 0x3C
  dut.uio_in.value = 0xA
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0x30

  dut.ui_in.value = 0xF0
  dut.uio_in.value = 1
  await ClockCycles(dut.clk, 1)
  dut.ui_in.value = 0x3C
  dut.uio_in.value = 0xB
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0xFC

  dut.ui_in.value = 0x02
  dut.uio_in.value = 1
  await ClockCycles(dut.clk, 1)
  dut.ui_in.value = 0x03
  dut.uio_in.value = 0xC
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0x06
  dut.uio_in.value = 15
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 0b0000

  dut.ui_in.value = 0x02
  dut.uio_in.value = 1
  await ClockCycles(dut.clk, 1)
  dut.ui_in.value = 0x00
  dut.uio_in.value = 0xC
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0x00
  dut.uio_in.value = 15
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 0b0001

  dut.ui_in.value = 0x02
  dut.uio_in.value = 1
  await ClockCycles(dut.clk, 1)
  dut.ui_in.value = 0xFE
  dut.uio_in.value = 0xC
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0xFC
  dut.uio_in.value = 15
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 0b0110

  dut.ui_in.value = 0x02
  dut.uio_in.value = 1
  await ClockCycles(dut.clk, 1)
  dut.ui_in.value = 0x7F
  dut.uio_in.value = 0xC
  await ClockCycles(dut.clk, 1)
  dut.uio_in.value = 0
  await ClockCycles(dut.clk, 1)
  assert dut.uo_out.value == 0xFE
  dut.uio_in.value = 15
  await ClockCycles(dut.clk, 2)
  assert dut.uo_out.value == 0b0010
