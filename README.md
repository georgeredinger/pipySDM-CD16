# Python library to control a CSI SDM-CD16

The SDM-CD16 is a synchronously addressed peripheral.
C2 and C3, driven high by the datalogger, initiate a cycle. While holding C3 high, the datalogger drives C2 as a clock line and Cl as a serial data line.
The datalogger shifts out a data bit on C1 (LSB first) on the falling edge of the C2 clock.

The SDM-CD16 shifts in the C1 data bit on the rising edge of the C2 clock.
The first 8 bits clocked out represent the SDM CD16 address. If the address matches the SDM-
CD16's jumpered address, the SDM-CDI6 is enabled. If enabled, the next 16 bits are shifted
into the SDM-CD16, each bit controlling one port the first of which controls OUTPUTl.
When the 16 control bits are clocked in, C2 is held high while C3 is pulsed low then high to
latch the control bits. The datalogger then lowers both C3 and C2 to complete the cycle.




