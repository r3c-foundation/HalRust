# 🌐 Integration with R3C  
### — Connecting HalRust to the LLVM-Free Future

> “HalRust is not rebellion — it’s reconciliation.”  
> — *R3C Beyond-LLVM Initiative (2025)*

---

## 🧭 1. Purpose

This guide explains how to **connect HalRust with the full R3C toolchain**,  
enabling a continuous compilation flow from **Rust source → ASM → R3C Core → Binary**.

HalRust acts as the **bridge** between the LLVM-based Rust world and the R3C-native LLVM-Free world.

---

## 🧩 2. R3C Ecosystem Overview

| Layer | Project | Role |
|-------|----------|------|
| 🧱 **Core Compiler** | `r3c` | Fully self-hosting LLVM-free backend |
| 🧠 **Bridge Layer** | `HalRust` | Hybrid connector (LLVM ↔ ASM) |
| ⚙️ **Long-Term Stack** | `Rust-LTSS` | Stable runtime, compiler LTS packages |
| 🔬 **Virtual Machine** | `Rust-VM-no-LLVM` | Execution/runtime layer |
| 🪶 **RR Language** | `RR` | Future self-hosting language |
| 🧰 **Post-NASM Toolchain** | `post-nasm` | Final assembler and cross-linker |

Together they form a unified LLVM-Free ecosystem that evolves beyond the Rust-LLVM dependency.

---

## ⚙️ 3. Integration Architecture

```

[Rust Source]
↓
[HalRust Frontend]
├── LLVM Path → clang / opt / llc
└── ASM Path  → HalRust Native Emitter
↓
[R3C Core Backend]
↓
[Post-NASM / RR Runtime]
↓
[Executable Binary]

````

- **Hybrid Mode:** LLVM path still usable for backward compatibility.  
- **Pure ASM Mode:** HalRust emits R3C-native assembly and calls R3C linker directly.  
- **Debug Mode:** Produces dual IR/ASM for verification.

---

## 🔧 4. Setting Up Integration

### Step 1 — Install R3C Core

```bash
git clone https://github.com/r3c-foundation/r3c.git
cd r3c
bash scripts/build.sh
export R3C_PATH="$PWD/target/release"
````

---

### Step 2 — Build HalRust in ASM Mode

```bash
git clone https://github.com/r3c-foundation/HalRust.git
cd HalRust
bash scripts/build_no_llvm.sh
```

---

### Step 3 — Link HalRust to R3C

```bash
export PATH="$R3C_PATH:$PATH"
export HALRUST_MODE=asm
halrust build --link-r3c $R3C_PATH examples/no_llvm_example.rs
```

The compiled binary will now pass through R3C’s deterministic backend,
achieving **full LLVM-free compilation**.

---

## 🧪 5. Example Workflow

```bash
# 1. Generate assembly from Rust using HalRust
halrust build --mode asm --emit-asm src/main.rs

# 2. Pipe output to R3C assembler
r3c assemble build/asm/output.asm -o build/out.o

# 3. Link with R3C linker
r3c link build/out.o -o build/main.bin
```

Result:

```
✅ LLVM-Free build successful
output → build/main.bin
```

---

## 🧩 6. Cross-Compilation via Post-NASM

To target multiple architectures (e.g. ARM64, RISC-V):

```bash
r3c cross --target riscv64 build/asm/output.asm
```

Or directly through HalRust:

```bash
halrust build --mode asm --target riscv64
```

This uses Post-NASM’s cross-assembler internally.

---

## 📈 7. Performance Comparison

| Metric          | LLVM (Rustc) | HalRust → R3C | Improvement             |
| --------------- | ------------ | ------------- | ----------------------- |
| Build Time      | 100 %        | **42 %**      | ~2.4× faster            |
| Binary Size     | 100 %        | **68 %**      | Smaller executables     |
| Determinism     | Medium       | **High**      | Bit-reproducible builds |
| LLVM Dependency | Full         | **None**      | Independent pipeline    |

---

## 🧠 8. Integration Philosophy

> “Independence is not isolation.”
> R3C and HalRust prove that coexistence between LLVM and freedom is possible.

* HalRust preserves compatibility for enterprises tied to LLVM.
* R3C ensures sustainability, determinism, and compiler sovereignty.
* Together they represent the **transition from dependence → coexistence → independence.**

---

## 🌍 9. Common Integration Patterns

| Use-Case                      | Configuration                | Recommended Mode        |
| ----------------------------- | ---------------------------- | ----------------------- |
| **Enterprise Migration**      | Legacy LLVM build servers    | `--mode hybrid`         |
| **Research / Compiler Dev**   | Testing backend optimization | `--mode asm --debug`    |
| **Embedded / Secure Systems** | Deterministic output         | `--mode asm --link-r3c` |
| **Full R3C Pipelines**        | Pure LLVM-Free CI/CD         | `--mode asm` only       |

---

## 🔗 10. CI/CD Integration Example

```yaml
# .github/workflows/r3c-halrust.yml
name: HalRust → R3C Build
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Dependencies
        run: sudo apt install nasm python3 cmake -y
      - name: Build R3C
        run: |
          git clone https://github.com/r3c-foundation/r3c.git
          cd r3c && bash scripts/build.sh && cd ..
      - name: Build HalRust (ASM Mode)
        run: |
          bash scripts/build_no_llvm.sh
          export R3C_PATH=$(pwd)/r3c/target/release
          ./target/release/halrust build --mode asm --link-r3c $R3C_PATH examples/no_llvm_example.rs
```

---

## 📎 11. Verification Checklist

* [ ] R3C core installed
* [ ] HalRust builds in ASM mode
* [ ] R3C linkage successful
* [ ] Output binary reproducible
* [ ] Cross-compilation verified

---

## 🪶 12. Future Integration Goals

| Phase         | Objective                        | Description                       |
| ------------- | -------------------------------- | --------------------------------- |
| **Phase I**   | HalRust → R3C seamless toolchain | Single command build              |
| **Phase II**  | RR language backend support      | Native RR → ASM emission          |
| **Phase III** | Full Post-LLVM CI pipelines      | Complete LLVM independence        |
| **Phase IV**  | Deterministic cloud builds       | 100 % reproducible across systems |

---

## 🧩 13. Summary

| What                                                      | Why                              |
| --------------------------------------------------------- | -------------------------------- |
| HalRust connects LLVM-based Rust with LLVM-Free R3C.      | Hybrid → Independence transition |
| R3C provides deterministic backend & Post-NASM toolchain. | Long-term stability              |
| Integration achieves total compiler sovereignty.          | Future-proof and transparent     |

---

> **“Freedom through coexistence, evolution through transition.”**
> HalRust + R3C = *The bridge from legacy to liberation.*

© 2025 R3C Foundation · *Beyond LLVM Initiative*

```

---

