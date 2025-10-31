# 🔄 HalRust Transition Guide  
### — From LLVM Dependence to Hybrid Freedom

> “Dependence is comfort. Independence is evolution. Coexistence is transition.”  
> — *The HalRust Manifesto*

---

## 🧭 1. Purpose

This guide explains how to **migrate existing Rust projects**  
from the traditional **LLVM-only toolchain** to **HalRust**,  
a hybrid compiler layer that bridges **LLVM and R3C** ecosystems.

It supports both:
- 🧠 **Hybrid Mode** — for gradual transition (LLVM + ASM)
- ⚙️ **Pure ASM Mode** — for full independence from LLVM

---

## 🧩 2. Migration Overview

| Phase | Description | Outcome |
|-------|--------------|----------|
| **Phase 0** | Existing Rust project (cargo + LLVM backend) | LLVM-only |
| **Phase 1** | Add HalRust as hybrid compiler | Dual backend (LLVM + ASM) |
| **Phase 2** | Switch to Pure ASM Mode | Fully LLVM-free build |
| **Phase 3** | Integrate with R3C | Self-hosting, beyond LLVM pipeline |

---

## ⚙️ 3. Prerequisites

| Dependency | Minimum Version | Notes |
|-------------|-----------------|--------|
| Rust | 1.75+ | Required for bootstrapping |
| LLVM | 16.x+ | Optional — only for Hybrid Mode |
| NASM | 2.16+ | Required for ASM builds |
| HalRust | Latest | https://github.com/r3c-foundation/HalRust |
| R3C (optional) | ≥ 0.3 | Needed for full LLVM-free integration |

---

## 🔧 4. Step-by-Step Migration

### **Step 1 — Clone and Install HalRust**

```bash
git clone https://github.com/r3c-foundation/HalRust.git
cd HalRust
bash scripts/build_hybrid.sh
export PATH="$PWD/target/release:$PATH"
````

Now `halrust` is available as a drop-in compiler replacement.

---

### **Step 2 — Compile Your Project Using HalRust**

#### Option A: Hybrid Mode (LLVM + ASM)

```bash
halrust build --mode hybrid --input src/main.rs
```

* Uses LLVM backend when detected
* Automatically falls back to ASM backend if LLVM missing
* Produces both `.ll` (LLVM IR) and `.asm` (NASM) outputs

#### Option B: Pure ASM Mode (No LLVM)

```bash
halrust build --mode asm --input src/main.rs
```

* 100% LLVM-Free
* Emits NASM assembly + direct binary link
* Compatible with R3C toolchain

---

### **Step 3 — Compare Outputs**

To visualize the transition between LLVM and ASM:

```bash
HALRUST_DEBUG=1 halrust build --mode hybrid src/main.rs
```

This will generate:

| File         | Path           | Description           |
| ------------ | -------------- | --------------------- |
| `output.ll`  | `/build/llvm/` | LLVM IR output        |
| `output.asm` | `/build/asm/`  | Direct ASM output     |
| `build.log`  | `/logs/`       | Hybrid diagnostic log |

Use these to verify correctness and performance.

---

### **Step 4 — Gradual LLVM Detachment**

| Stage             | Recommended Action                            |
| ----------------- | --------------------------------------------- |
| 🧠 **LLVM Stage** | Use `--mode hybrid` to ensure compatibility   |
| ⚙️ **Dual Stage** | Disable certain LLVM passes (`--skip-opt`)    |
| 🪶 **ASM Stage**  | Switch to `--mode asm` and test full R3C path |

Example:

```bash
halrust build --mode hybrid --skip-opt verify --emit-asm
```

Then verify identical behavior by comparing outputs.

---

### **Step 5 — Integrate with R3C**

Once Pure ASM Mode is stable:

```bash
export R3C_PATH=/opt/r3c
halrust build --mode asm --link-r3c $R3C_PATH
```

This enables HalRust → R3C direct compilation and linking.
Your project is now **LLVM-independent** and **R3C-compatible**.

---

## 🧱 5. Transition Timeline Example

| Week | Activity                | Deliverable                          |
| ---- | ----------------------- | ------------------------------------ |
| 1    | Test Hybrid Mode build  | Both LLVM and ASM binaries generated |
| 2    | Optimize and benchmark  | Compare build time, binary size      |
| 3    | Switch to Pure ASM Mode | Stable LLVM-free build               |
| 4    | Integrate R3C runtime   | Fully independent toolchain          |
| 5+   | Contribute feedback     | Extend HalRust transition docs       |

---

## ⚖️ 6. Expected Differences

| Category        | LLVM Backend         | HalRust ASM Backend      |
| --------------- | -------------------- | ------------------------ |
| Build Speed     | Slower (many passes) | Faster (direct emission) |
| Binary Size     | Larger               | Smaller                  |
| Debugging       | IR-based             | ASM-based                |
| Determinism     | Medium               | High                     |
| Reproducibility | Limited              | Fully reproducible       |

---

## 🧩 7. Optional: Cargo Integration

To replace Rust’s default compiler with HalRust temporarily:

```bash
cargo build --config "build.rustc='halrust'"
```

You can also use `.cargo/config.toml`:

```toml
[build]
rustc = "halrust"
```

Now all `cargo build` commands route through HalRust automatically.

---

## 🌍 8. Verification Checklist

* [ ] Hybrid Mode build success
* [ ] ASM Mode build success
* [ ] Outputs verified (`.ll` vs `.asm`)
* [ ] R3C linking test passed
* [ ] Performance benchmarked
* [ ] Code reproducibility validated

---

## 🪶 9. Philosophy of Transition

> “We don’t abandon LLVM — we evolve beyond it.”
> HalRust was created not to divide Rust, but to **liberate** it from dependency inertia.
> It is the bridge where *comfort meets freedom.*

When your code compiles with or without LLVM,
you’ve achieved **true compiler sovereignty**.

---

## 📎 10. Next Steps

* See [`build_guide.md`](build_guide.md) for platform-specific builds.
* Read [`architecture.md`](architecture.md) to understand hybrid layering.
* Visit [R3C Foundation Discussions](https://github.com/r3c-foundation/discussions) for migration help.

---

© 2025 R3C Foundation · *Beyond LLVM Initiative*
*“Transition is not rebellion — it’s evolution.”*

```

---
