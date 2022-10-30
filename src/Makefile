# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

TOPLEVEL_LANG ?= vhdl
SIM ?= ghdl

PWD=$(shell pwd)

# # Matrix parameters
# DATA_WIDTH ?= 32
# A_ROWS ?= 10
# B_COLUMNS ?= 4
# A_COLUMNS_B_ROWS ?= 6

ifeq ($(TOPLEVEL_LANG),verilog)
	# VERILOG_SOURCES = $(PWD)/../hdl/matrix_multiplier.sv

	# TODO: Test converted verilog because that is what OpenLane accepts

else ifeq ($(TOPLEVEL_LANG),vhdl)
	VHDL_SOURCES = $(PWD)/simple_multiplier.vhd

	ifneq ($(filter $(SIM),ghdl questa modelsim riviera activehdl),)
		# ghdl, questa, and aldec all use SIM_ARGS with '-g' for setting generics
		# SIM_ARGS += -gDATA_WIDTH=$(DATA_WIDTH) -gA_ROWS=$(A_ROWS) -gB_COLUMNS=$(B_COLUMNS) -gA_COLUMNS_B_ROWS=$(A_COLUMNS_B_ROWS)
	else ifneq ($(filter $(SIM),ius xcelium),)
		# SIM_ARGS += -generic "matrix_multiplier:DATA_WIDTH=>$(DATA_WIDTH)" -generic "matrix_multiplier:A_ROWS=>$(A_ROWS)" -generic "matrix_multiplier:B_COLUMNS=>$(B_COLUMNS)" -generic "matrix_multiplier:A_COLUMNS_B_ROWS=>$(A_COLUMNS_B_ROWS)"
	endif

	ifeq ($(SIM),ghdl)
		EXTRA_ARGS += --std=08
		SIM_ARGS += --wave=wave.ghw
	else ifneq ($(filter $(SIM),questa modelsim riviera activehdl),)
		COMPILE_ARGS += -2008
	endif
else
	$(error A valid value (verilog or vhdl) was not provided for TOPLEVEL_LANG=$(TOPLEVEL_LANG))
endif

# Fix the seed to ensure deterministic tests
export RANDOM_SEED := 123456789

TOPLEVEL    := simple_multiplier
MODULE      := test_simple_mult

include $(shell cocotb-config --makefiles)/Makefile.sim


# Profiling

DOT_BINARY ?= dot

test_profile.pstat: sim

callgraph.svg: test_profile.pstat
	$(shell cocotb-config --python-bin) -m gprof2dot -f pstats ./$< | $(DOT_BINARY) -Tsvg -o $@

.PHONY: profile
profile:
	COCOTB_ENABLE_PROFILING=1 $(MAKE) callgraph.svg
