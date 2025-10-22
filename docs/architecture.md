# 🧭 HalRust Architecture  
> **Bridge between LLVM-based Rust and the LLVM-free R3C ecosystem.**

---

## 1️⃣ Overview
**HalRust** (*Half-LLVM Rust*) is a transitional compiler layer connecting  
the **official Rust toolchain (LLVM-dependent)** with the **R3C LLVM-free ecosystem.**

It lets developers keep using the LLVM backend for optimization when needed,  
while enabling a fallback to direct ASM emission for lightweight or independent builds.

---

## 2️⃣ Layered Ecosystem Diagram
```text
┌────────────────────────────┐
│  Rust (LLVM-based)         │
│  └─ rustc, cargo, LLVM IR  │
└────────────┬───────────────┘
             │
             ▼
      🪶 HalRust  ←  Bridge Layer
             │
      (LLVM optional backend)
      (Direct ASM fallback)
             │
             ▼
┌────────────────────────────┐
│  R3C (LLVM-free compiler)  │
│  └─ C++ → Rust → ASM       │
└────────────────────────────┘




3️⃣ Functional Roles




Layer
Role
Description




Rust (official)
Primary language frontend
Full LLVM toolchain, maximum optimization


HalRust (bridge)
Transitional hybrid compiler
Uses LLVM or internal ASM backend


R3C (independent)
Fully LLVM-free self-hosting compiler
Direct C++ → Rust → ASM transpilation





4️⃣ Technical Components




Module
Description




hal_core.rs
Core layer handling IR translation and mode detection


hal_codegen.rs
Optional LLVM adapter module


hal_direct_asm.rs
Direct ASM backend emitter


backend/llvm_adapter/
Interfaces existing Rust/LLVM optimization pipeline


backend/asm_emitter/
Lightweight R3C-style emitter for direct builds


scripts/build_hybrid.sh
Hybrid mode build script


scripts/build_no_llvm.sh
Pure ASM fallback build script





5️⃣ Build Modes




Mode
Backend
Target




🧩 Hybrid Mode
LLVM when available, auto-ASM fallback
Developer systems with LLVM installed


⚙️ Pure ASM Mode
Internal ASM emitter only
Environments without LLVM/Clang


🔬 Inspect Mode
Shows LLVM IR vs. ASM output side-by-side
Debugging, optimization comparison





6️⃣ Ecosystem Integration


HalRust acts as a translator between ecosystems:




Project
Role
Layer




Rust
Base compiler (LLVM)
Source Frontend


HalRust
Transitional bridge
LLVM↔ASM Adapter


R3C
LLVM-free compiler
Independent Core


Rust-Industrial-stable-library-with-no-LLVM
Runtime & std layer
Industrial Stability


Rust-Virtual-Machine-no-LLVM
Execution backend
VM Layer





7️⃣ Philosophy




“Dependence is comfort.

Independence is evolution.

Coexistence is transition.”




HalRust is not anti-LLVM —

it recognizes LLVM’s power but offers freedom of choice.

This project ensures the transition from dependence to independence is smooth, compatible, and developer-friendly.



8️⃣ Future Direction




🌐 Rust ↔ R3C IR compatibility layer (shared intermediate spec)


🧩 Auto-mode detection (llvm-present → hybrid, llvm-missing → pure ASM)


🪶 Unified toolchain connecting R3C and standard Rust seamlessly







HalRust — Because even independence deserves a safe bridge.





---


