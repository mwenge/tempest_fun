#!/usr/bin/env python3
import os
from rt11_utils import extract_files_from_disk,parse_lda_file
extract_files_from_disk("./pdp11_build/tempest_modified.rk05", "./bin/binaries/")
output_bytes = parse_lda_file("./bin/binaries/ALEXEC.LDA")

OUT_DIR="./bin/tempest"
if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

open(f"{OUT_DIR}/136002-138.np3",'wb').write(bytes(output_bytes[0x3000:0x4000]))
# Notice we have the addresses in reverse order, e.g. 136002-237 is written to 0xD000 rather
# than 0x9000.
open(f"{OUT_DIR}/136002-237.p1",'wb').write(bytes(output_bytes[0xD000:0xE000]))
open(f"{OUT_DIR}/136002-136.lm1",'wb').write(bytes(output_bytes[0xC000:0xD000]))
open(f"{OUT_DIR}/136002-235.j1",'wb').write(bytes(output_bytes[0xB000:0xC000]))
open(f"{OUT_DIR}/136002-134.f1",'wb').write(bytes(output_bytes[0xA000:0xB000]))
open(f"{OUT_DIR}/136002-133.d1",'wb').write(bytes(output_bytes[0x9000:0xA000]))

mathbox_bytes = open("src/MBOX.SAV",'rb').read()
open(f"{OUT_DIR}/136002-126.a1",'wb').write(mathbox_bytes[0x8400:0x8420])
# 136002-127.e1 contains the low 4 bits of each byte in 0x6A00:0x6B00 in MBOX.SAV
open(f"{OUT_DIR}/136002-127.e1",'wb').write(bytes([a & 0x0F for a in mathbox_bytes[0x6A00:0x6B00]]))
# 136002-128.f1 contains the high 4 bits (right-shifted) of each byte in 0x6A00:0x6B00 in MBOX.SAV
open(f"{OUT_DIR}/136002-128.f1",'wb').write(bytes([(a & 0xF0) >> 4 for a in mathbox_bytes[0x6A00:0x6B00]]))

# 136002-129.h1 contains the low 4 bits of each byte in 0x6900:0x6A00 in MBOX.SAV
open(f"{OUT_DIR}/136002-129.h1",'wb').write(bytes([a & 0x0F for a in mathbox_bytes[0x6900:0x6A00]]))
# 136002-130.j1 contains the high 4 bits (right-shifted) of each byte in 0x6900:0x6A00 in MBOX.SAV
open(f"{OUT_DIR}/136002-130.j1",'wb').write(bytes([(a & 0xF0) >> 4 for a in mathbox_bytes[0x6900:0x6A00]]))

# 136002-131.k1 contains the low 4 bits of each byte in 0x6800:0x6900 in MBOX.SAV
open(f"{OUT_DIR}/136002-131.k1",'wb').write(bytes([a & 0x0F for a in mathbox_bytes[0x6800:0x6900]]))
# 136002-132.l1 contains the high 4 bits (right-shifted) of each byte in 0x6800:0x6900 in MBOX.SAV
open(f"{OUT_DIR}/136002-132.l1",'wb').write(bytes([(a & 0xF0) >> 4 for a in mathbox_bytes[0x6800:0x6900]]))

vecgen_bytes = open("src/STATE2.SAV",'rb').read()
open(f"{OUT_DIR}/136002-125.d7",'wb').write(vecgen_bytes[0x1000:0x1100])

