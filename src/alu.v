/*
 * Copyright (c) 2024 Andrew Dona-Couch
 * SPDX-License-Identifier: Apache-2.0
 */

`define default_netname none

module alu (
    input  wire       clk,
    input  wire       rst_n,
    input  wire       accum_source,
    input  wire       value_source,
    input  wire [3:0] opcode,
    input  wire [7:0] data_in,
    output reg [7:0] data_out
);

  reg [7:0] accum0, accum1;
  reg [7:0] status;

  wire [7:0] accum = accum_source == 0 ? accum0 : accum1;
  wire [7:0] value = value_source == 0 ? data_in :
    accum_source == 0 ? accum1 : accum0;

  wire [7:0] sum = accum + value;
  wire [7:0] diff = accum - value;
  wire [7:0] xored = accum ^ value;
  wire [7:0] neg = ~accum;
  wire [7:0] shl = accum << value;
  wire [7:0] shr = accum >> value;
  wire [7:0] anded = accum & value;
  wire [7:0] ored = accum | value;

  wire [15:0] left = accum;
  wire [15:0] right = value;
  wire [15:0] product = left * right;
  wire mul_ovf = (product[15:8] != 8'h00) & (product[15:8] != 8'hFF);

  wire [7:0] div = accum / value;
  wire [7:0] mod = accum % value;

  always @(posedge clk) begin
    if (!rst_n) begin
      accum0 <= 0;
      accum1 <= 0;
      status <= 0;
    end else begin
      case (opcode)
        // nop
        4'h0: begin
          data_out <= accum;
        end
        // load
        4'h1: begin
          data_out <= value;
          if (accum_source) accum1 <= value;
          else accum0 <= value;
          status[0] <= value == 0;
          status[1] <= value[7];
          status[2] <= 0;
        end
        // add
        4'h2: begin
          data_out <= sum;
          if (accum_source) accum1 <= sum;
          else accum0 <= sum;
          status[0] <= sum == 0;
          status[1] <= sum[7];
          status[2] <= sum < accum;
        end
        // sub
        4'h3: begin
          data_out <= diff;
          if (accum_source) accum1 <= diff;
          else accum0 <= diff;
          status[0] <= diff == 0;
          status[1] <= diff[7];
          status[2] <= diff > accum;
        end
        // zero
        4'h4: begin
          data_out <= 0;
          if (accum_source) accum1 <= 0;
          else accum0 <= 0;
          status[3:0] <= 3'b001;
        end
        // one
        4'h5: begin
          data_out <= 1;
          if (accum_source) accum1 <= 1;
          else accum0 <= 1;
          status[3:0] <= 3'b000;
        end
        // xor
        4'h6: begin
          data_out <= xored;
          if (accum_source) accum1 <= xored;
          else accum0 <= xored;
          status[0] <= xored == 0;
          status[1] <= xored[7];
          status[2] <= 0;
        end
        // not
        4'h7: begin
          data_out <= neg;
          if (accum_source) accum1 <= neg;
          else accum0 <= neg;
          status[0] <= neg == 0;
          status[1] <= neg[7];
          status[2] <= 0;
        end
        // shl
        4'h8: begin
          data_out <= shl;
          if (accum_source) accum1 <= shl;
          else accum0 <= shl;
          status[0] <= shl == 0;
          status[1] <= shl[7];
          status[2] <= accum[7];
        end
        // shr
        4'h9: begin
          data_out <= shr;
          if (accum_source) accum1 <= shr;
          else accum0 <= shr;
          status[0] <= shr == 0;
          status[1] <= shr[7];
          status[2] <= accum[0];
        end
        // and
        4'hA: begin
          data_out <= anded;
          if (accum_source) accum1 <= anded;
          else accum0 <= anded;
          status[0] <= anded == 0;
          status[1] <= anded[7];
          status[2] <= 0;
        end
        // or
        4'hB: begin
          data_out <= ored;
          if (accum_source) accum1 <= ored;
          else accum0 <= ored;
          status[0] <= ored == 0;
          status[1] <= ored[7];
          status[2] <= 0;
        end
        // mul
        4'hC: begin
          data_out <= product[7:0];
          if (accum_source) accum1 <= product[7:0];
          else accum0 <= product[7:0];
          status[0] <= product[7:0] == 0;
          status[1] <= product[7];
          status[2] <= mul_ovf;
        end
        // div
        4'hD: begin
          data_out <= div;
          if (accum_source) accum1 <= div;
          else accum0 <= div;
          status[0] <= div == 0;
          status[1] <= div[7];
          status[2] <= mod != 0;
        end
        // mod
        4'hE: begin
          data_out <= mod;
          if (accum_source) accum1 <= mod;
          else accum0 <= mod;
          status[0] <= mod == 0;
          status[1] <= mod[7];
          status[2] <= div != 0;
        end
        // status
        4'hF: begin
          data_out <= status;
        end
      endcase
    end
  end

endmodule
