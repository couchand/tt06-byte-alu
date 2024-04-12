/*
 * Copyright (c) 2024 Andrew Dona-Couch
 * SPDX-License-Identifier: Apache-2.0
 */

`define default_netname none

module alu (
    input  wire       clk,
    input  wire       rst_n,
    input  wire [3:0] opcode,
    input  wire [7:0] data_in,
    output wire [7:0] data_out
);

  assign data_out = 50;

endmodule
