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

    a = 5
    b = 8

    dut.a_in.value = a
    dut.b_in.value = b

    await Timer(1, units="ns")

    dut._log.info("a_in is %s", dut.a_in.value)
    dut._log.info("b_in is %s", dut.b_in.value)
    dut._log.info("c_out is %s", dut.c_out.value)
    assert dut.c_out.value == (a*b), f"c_out is not {a*b}!"

