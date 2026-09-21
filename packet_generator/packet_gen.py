# v1: market data hardcoded (not randomly generated),

import struct

messages = [
    {"type": "A", "order_id": 1, "side": "B", "qty": 100, "symbol": "AAPL", "price": 1872500},
    {"type": "A", "order_id": 2, "side": "S", "qty": 50,  "symbol": "MSFT", "price": 4153000},
]

# for price used 4dp (e.g. 1872500 would be £187.2500)

def encode_message(msg):
    return struct.pack(
        ">1sQ1sI8sI",
        msg["type"].encode(),              # 1 byte as minimal types
        msg["order_id"],                   # 8 bytes to allow a lot of orders
        msg["side"].encode(),              # 1 byte as only need "b" or "s"
        msg["qty"],                        # 4 bytes allows up to 4.29 billion quantity
        msg["symbol"].encode().ljust(8),   # 8 bytes (make symbol 8 bytes, and pad the right with 0)
        msg["price"],                      # 4 bytes (can hold prices up to : 429,496.7295)
    )

for msg in messages:
    payload = encode_message(msg)
    print(len(b), b.hex(" "))