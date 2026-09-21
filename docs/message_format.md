# Message format

Binary format for market data sent from the packet generator to the FPGA.
One message per UDP packet.

UDP destination port: TBD

## Conventions

- Big-endian (most significant byte first)
- All integers unsigned
- Prices are integers x 10,000 (4 decimal places), e.g. 187.25 is stored as 1872500
- Text is ASCII, padded with spaces on the right

## Add order (type 'A')

26 bytes total.

| Offset | Width | Field    | Type    | Notes                     |
|--------|-------|----------|---------|---------------------------|
| 0      | 1     | type     | ASCII   | 'A'                       |
| 1      | 8     | order_id | uint64  | unique per order          |
| 9      | 1     | side     | ASCII   | 'B' buy, 'S' sell         |
| 10     | 4     | qty      | uint32  | number of shares          |
| 14     | 8     | symbol   | ASCII   | space-padded, e.g. "AAPL    " |
| 22     | 4     | price    | uint32  | x 10,000                  |

## Limits

- qty: max 4,294,967,295
- price: max 429,496.7295 (some very high-priced stocks, e.g. BRK.A, can exceed this)

## Example

Buy 100 AAPL at 187.25, order ID 1:

41 00 00 00 00 00 00 00 01 42 00 00 00 64 41 41 50 4c 20 20 20 20 00 1c 92 74

## Changes

- v1: add order only