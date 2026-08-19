# Typed Write Granularity Mismatch In Binary Parsers

Source:
- Z.ai CVD Ledger: <https://cvd.z.ai/>
- Example public finding: GStreamer `librfb` fill-rectangle heap out-of-bounds write, CVE-2026-59691.

Source type:
- Public OSS/source-code vulnerability disclosure.

Status:
- Public pattern, use as a lead source only.

Bug class:
- Memory corruption / heap out-of-bounds write / element-size mismatch.

Core idea:
- A binary parser allocates a buffer using one unit size but writes, increments, copies, or fills using another unit size.
- This is common when formats support variable bytes-per-pixel, sample width, element width, character width, compression blocks, or negotiated protocol parameters.

Where to look:
- Image/video/audio codecs.
- Remote desktop or graphics protocols.
- Font and document parsers.
- Network protocol decoders.
- Compression/decompression loops.
- C/C++/Rust unsafe code with pointer arithmetic.

Search terms:
```text
bytespp bytes_per_pixel bpp stride pitch width height samples channels elem_size sizeof uint16 uint32 memset memcpy fill rectangle offset pointer +=
```

Concrete checks:
- Compare allocation size units against write/copy/fill units.
- Trace attacker-controlled format parameters such as bpp, depth, stride, width, height, channels, and sample width.
- Check whether pointer increments use bytes, elements, pixels, rows, or words consistently.
- Look for casts that change element size before writes.
- Check integer multiplication and rounding before buffer allocation.
- Run ASAN/UBSAN/fuzzing when a mismatch is plausible.

False-positive blockers:
- Format negotiation normalizes all variants to one internal element size before allocation and writes.
- The destination buffer is intentionally overallocated for the widest supported unit.
- Bounds checks use the same unit as the write primitive.
- The apparent mismatch is dead code or unreachable for attacker-controlled input.

PoC shape:
- Pick the smallest format variant where allocation uses a smaller unit than the write.
- Craft a payload/frame/record with attacker-controlled dimensions.
- Use ASAN or equivalent to prove out-of-bounds write, crash, or memory corruption.

Audit routing:
- Use this note during C/C++/Rust/native-code source audits of binary parsing, media processing, protocol decoding, and unsafe memory manipulation.
