import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def my_first_test(dut):
    """Try accessing the design."""

    # for cycle in range(10):
    #     dut.clk.value = 0
    #     await Timer(1, units="ns")
    #     dut.clk.value = 1
    #     await Timer(1, units="ns")

    dut.a_in.value = 2
    dut.b_in.value = 2

    await Timer(1, units="ns")

    dut._log.info("a_in is %s", dut.a_in.value)
    dut._log.info("b_in is %s", dut.b_in.value)
    dut._log.info("c_out is %s", dut.c_out.value)
    assert dut.c_out.value == 4, "c_out is not 4!"

