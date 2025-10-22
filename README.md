# 🪶 HalRust — Half LLVM, Half Independent Rust

> “A hybrid Rust experiment that can *breathe with or without LLVM*.”

HalRust is a middle-ground compiler experiment between full LLVM dependence  
and complete independence like R3C.  
It supports both modes:

- 🧩 **LLVM-Enhanced Mode** — Use LLVM when available (for optimization and tooling)
- ⚙️ **Bare-Metal Mode** — Fall back to a lightweight direct ASM backend (no LLVM required)

Designed for developers who still rely on LLVM’s ecosystem  
but want to prepare for an independent future.
