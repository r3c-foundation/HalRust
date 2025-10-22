# 🪶 HalRust — Hybrid Adaptive Layered Rust  
> “LLVM and Freedom can coexist.”

---

## 🧭 Overview
**HalRust** (*Half LLVM, Half Independent Rust*)  
is an experimental compiler layer that connects **LLVM-based Rust**  
with the **LLVM-free R3C ecosystem**.  

It’s designed for developers who still depend on LLVM for tooling and optimization,  
but want a **path toward independence and direct ASM emission**.

---

## ⚙️ Architecture
```text
Rust Source
    ↓
 HalRust Frontend
    ├── LLVM Path → clang / opt / llc
    └── ASM Path  → HalRust native emitter



🧩 Dual Mode Design




Mode
Description




🧠 Hybrid Mode
Use LLVM backend when available, auto-fallback to ASM on missing LLVM.


⚙️ Pure ASM Mode
Full R3C-compatible mode (no LLVM, no Clang).


🔬 Debug Mode
Visualizes IR/ASM output side-by-side for performance inspection.





🧱 Directory Structure


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




🧩 Philosophy




“Dependence is comfort.

Independence is evolution.

Coexistence is transition.”




HalRust isn’t anti-LLVM —

it acknowledges LLVM’s value but seeks to reduce friction, size, and build complexity.

It’s the bridge between Rust’s current compiler stack

and the long-term R3C self-hosting future.



🌍 Relation to R3C Ecosystem




Project
Role
Layer




R3C
Core self-hosting compiler
LLVM-Free Core


HalRust
Transitional compiler layer
Hybrid Bridge


Rust-Industrial-Stable-Library-with-no-LLVM
Stable runtime and standard extensions
Industry Layer


Rust-Virtual-Machine-no-LLVM
VM and Execution Environment
Runtime Layer





🧰 Build (Linux/macOS/Windows)


# Hybrid mode (LLVM + ASM)
bash scripts/build_hybrid.sh

# No-LLVM mode (direct ASM backend)
bash scripts/build_no_llvm.sh




📜 License


MIT — free to modify, study, or integrate.

Just don’t let LLVM yell at you 😎



🪶 Author’s Note


HalRust is not rebellion —

it’s compatibility without compromise,

a step toward a compiler ecosystem

that can breathe both with and without LLVM.



---



