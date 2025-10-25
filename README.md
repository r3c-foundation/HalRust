# 🪶 HalRust — Hybrid Adaptive Layered Rust
### “LLVM and Freedom can coexist.”

> *The bridge between Rust’s LLVM roots and its LLVM-free future.*  
> *HalRust connects the past and the future — without choosing sides.*

---

## 🧭 Overview

**HalRust (Half LLVM, Half Independent Rust)**  
is an **experimental hybrid compiler layer** that links  
LLVM-based Rust with the LLVM-free **R3C** ecosystem.

It is designed for developers and organizations who  
still depend on LLVM tooling and optimizations —  
but seek a clear path toward independence and **direct ASM emission**.

---

## ⚙️ Architecture

```text
[Rust Source]
   ↓
[HalRust Frontend]
   ├── LLVM Path → clang / opt / llc
   └── ASM Path  → HalRust Native Emitter
````

---

## 🧩 Dual Mode Design

| Mode                 | Description                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| 🧠 **Hybrid Mode**   | Uses LLVM backend when available; auto-fallback to ASM when missing.         |
| ⚙️ **Pure ASM Mode** | Fully LLVM-free mode, 100% R3C-compatible.                                   |
| 🔬 **Debug Mode**    | Visualizes LLVM IR and ASM output side-by-side for comparison and profiling. |

---

## 🧱 Directory Structure

```text
HalRust/
 ├── src/
 │    ├── hal_core.rs
 │    ├── hal_codegen.rs        # optional LLVM path
 │    ├── hal_direct_asm.rs     # direct emitter
 ├── backend/
 │    ├── llvm_adapter/
 │    └── asm_emitter/
 ├── scripts/
 │    ├── build_hybrid.sh
 │    ├── build_no_llvm.sh
 │    └── detect_llvm.ps1
 ├── examples/
 │    ├── hybrid_example.rs
 │    └── no_llvm_example.rs
 └── CMakeLists.txt
```

---

## 🧩 Philosophy

> **“Dependence is comfort.
> Independence is evolution.
> Coexistence is transition.”**

HalRust isn’t anti-LLVM —
it acknowledges LLVM’s strength and ecosystem value.
But it seeks **to reduce friction, build time, and dependency inertia**,
offering a practical bridge between LLVM comfort and R3C independence.

---

## 🌍 Relation to R3C Ecosystem

| Project                                                                                        | Role                                 | Layer          |
| ---------------------------------------------------------------------------------------------- | ------------------------------------ | -------------- |
| [**R3C**](https://github.com/r3c-foundation/r3c)                                               | Core self-hosting compiler           | LLVM-Free Core |
| **HalRust**                                                                                    | Transitional compiler layer          | Hybrid Bridge  |
| [**Rust-Industrial-Stable-Library-with-no-LLVM**](https://github.com/r3c-foundation/Rust-ltss) | Stable runtime & standard extensions | Industry Layer |
| **Rust-Virtual-Machine-no-LLVM**                                                               | VM & execution environment           | Runtime Layer  |

---

## 🧰 Build (Linux / macOS / Windows)

```bash
# Hybrid mode (LLVM + ASM)
bash scripts/build_hybrid.sh

# No-LLVM mode (direct ASM backend)
bash scripts/build_no_llvm.sh
```

Windows PowerShell:

```powershell
.\scripts\detect_llvm.ps1
```

---

## 📜 License

MIT — free to modify, study, or integrate.

> Just don’t let LLVM yell at you 😎

---

## 🪶 Author’s Note

> **HalRust is not rebellion —**
> it’s *compatibility without compromise*.
> A transition layer between comfort and freedom,
> bridging LLVM’s legacy with R3C’s destiny.

---

**© 2025 R3C Foundation**
Part of the *Beyond-LLVM Initiative*
[https://github.com/r3c-foundation](https://github.com/r3c-foundation)

````

---

## 📜 `MANIFESTO.md` — *LLVM과 자유의 공존선언문 (Manifesto of Coexistence)*

```markdown
# 🪶 The HalRust Manifesto  
### — LLVM과 자유의 공존선언문 —

> “Dependence is comfort.  
> Independence is evolution.  
> Coexistence is transition.”

---

## I. The Reality

Rust was born modern,  
but it breathes through LLVM — a legacy machine of C and C++.

LLVM is not evil.  
It is *a monument of compiler engineering*,  
but also *a labyrinth of dependencies*.

To move forward, Rust needs not rejection — but **transition**.

---

## II. The Bridge

**HalRust** exists between two worlds:  
the *LLVM-anchored past* and the *R3C-driven future*.

It does not declare war.  
It builds a **bridge** —  
a hybrid, adaptive layer where both can coexist.

---

## III. The Philosophy

| Principle | Meaning |
|------------|----------|
| 🧠 **Hybrid Freedom** | Use LLVM when it helps; drop it when it hurts. |
| ⚙️ **Pragmatic Transition** | No ideological purity — only functionality. |
| 🪶 **Layered Adaptation** | Each system should evolve at its own pace. |

---

## IV. The Path Forward

1. Let Rust learn to build without fear of breaking LLVM.  
2. Let developers choose when and how to detach.  
3. Let compilers coexist — not compete — in harmony.  
4. Let **R3C** define independence through **transparency**, not isolation.

---

## V. The Future

When Rust breathes both ways —  
through LLVM *and* without it —  
we will have achieved the true meaning of sustainability.

> “LLVM and Freedom can coexist.”  
>  
> **HalRust — the bridge between comfort and evolution.**

---

🧩 *R3C Foundation · Beyond LLVM Initiative (2025)*
````



