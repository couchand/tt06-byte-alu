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

  reg [7:0] accum;
  reg [7:0] status;
  reg result;

  wire [7:0] sum = accum + data_in;
  wire [7:0] diff = accum - data_in;
  wire [7:0] xored = accum ^ data_in;
  wire [7:0] neg = ~accum;
  wire [7:0] shl = accum << data_in;
  wire [7:0] shr = accum >> data_in;
  wire [7:0] anded = accum & data_in;
  wire [7:0] ored = accum | data_in;

  wire [15:0] left = accum;
  wire [15:0] right = data_in;
  wire [15:0] product = left * right;
  wire mul_ovf = (product[15:8] != 8'h00) & (product[15:8] != 8'hFF);

  assign data_out = result ? status : accum;

  always @(posedge clk) begin
    if (!rst_n) begin
      accum <= 0;
      status <= 0;
      result <= 0;
    end else begin
      // status
      result <= opcode == 4'hF;
      case (opcode)
        // nop
        4'h0: ;
        // load
        4'h1: begin
          accum <= data_in;
          status[0] <= data_in == 0;
          status[1] <= data_in[7];
          status[2] <= 0;
        end
        // add
        4'h2: begin
          accum <= sum;
          status[0] <= sum == 0;
          status[1] <= sum[7];
          status[2] <= sum < accum;
        end
        // sub
        4'h3: begin
          accum <= diff;
          status[0] <= diff == 0;
          status[1] <= diff[7];
          status[2] <= diff > accum;
        end
        // zero
        4'h4: begin
          accum <= 0;
          status[3:0] <= 3'b001;
        end
        // one
        4'h5: begin
          accum <= 1;
          status[3:0] <= 3'b000;
        end
        // xor
        4'h6: begin
          accum <= xored;
          status[0] <= xored == 0;
          status[1] <= xored[7];
          status[2] <= 0;
        end
        // not
        4'h7: begin
          accum <= neg;
          status[0] <= neg == 0;
          status[1] <= neg[7];
          status[2] <= 0;
        end
        // shl
        4'h8: begin
          accum <= shl;
          status[0] <= shl == 0;
          status[1] <= shl[7];
          status[2] <= accum[7];
        end
        // shr
        4'h9: begin
          accum <= shr;
          status[0] <= shr == 0;
          status[1] <= shr[7];
          status[2] <= accum[0];
        end
        // and
        4'hA: begin
          accum <= anded;
          status[0] <= anded == 0;
          status[1] <= anded[7];
          status[2] <= 0;
        end
        // or
        4'hB: begin
          accum <= ored;
          status[0] <= ored == 0;
          status[1] <= ored[7];
          status[2] <= 0;
        end
        // mul
        4'hC: begin
          accum <= product[7:0];
          status[0] <= product[7:0] == 0;
          status[1] <= product[7];
          status[2] <= mul_ovf;
        end
      endcase
    end
  end

endmodule
