# ⚙️ HalRust Build Guide  
### — Building the Hybrid Adaptive Layered Rust Compiler

HalRust is designed to **coexist** with both LLVM and ASM backends.  
You can build it in either **Hybrid Mode** (LLVM + ASM) or **Pure ASM Mode** (LLVM-free, fully R3C-compatible).

---

## 🧭 1. Requirements

| Dependency | Minimum Version | Purpose |
|-------------|-----------------|----------|
| **Rust Toolchain** | 1.75+ | Base Rust compiler for bootstrapping |
| **CMake** | 3.18+ | Cross-platform build management |
| **Python** | 3.8+ | Used for build scripts and documentation generation |
| **LLVM** *(optional)* | 16.x or later | Required for Hybrid Mode only |
| **NASM** | 2.16+ | Required for direct ASM emission |
| **Git** | Latest | Source retrieval and submodule management |

---

## ⚙️ 2. Directory Overview

```

HalRust/
├── scripts/
│    ├── build_hybrid.sh     # Hybrid (LLVM + ASM)
│    ├── build_no_llvm.sh    # Pure ASM (LLVM-free)
│    └── detect_llvm.ps1     # Windows detection script
├── src/
│    ├── hal_core.rs
│    ├── hal_codegen.rs
│    └── hal_direct_asm.rs
├── backend/
│    ├── llvm_adapter/
│    └── asm_emitter/
└── CMakeLists.txt

````

---

## 🧩 3. Build Modes

| Mode | Description | Command |
|------|--------------|----------|
| 🧠 **Hybrid Mode** | Uses LLVM backend when available; falls back to ASM otherwise. | `bash scripts/build_hybrid.sh` |
| ⚙️ **Pure ASM Mode** | Fully LLVM-free mode, emits NASM-compatible assembly. | `bash scripts/build_no_llvm.sh` |
| 🧪 **Debug Mode** | Displays LLVM IR and ASM output side-by-side for comparison. | `HALRUST_DEBUG=1 bash scripts/build_hybrid.sh` |

---

## 🧰 4. Building on Linux / macOS

```bash
# Clone repository
git clone https://github.com/r3c-foundation/HalRust.git
cd HalRust

# Ensure dependencies
rustup update
sudo apt install cmake nasm python3 -y

# Hybrid build (uses LLVM if found)
bash scripts/build_hybrid.sh

# LLVM-free build
bash scripts/build_no_llvm.sh
````

If LLVM is missing, `build_hybrid.sh` will automatically fallback to Pure ASM Mode.

---

## 🪟 5. Building on Windows (PowerShell)

```powershell
git clone https://github.com/r3c-foundation/HalRust.git
cd HalRust

# Detect LLVM environment
.\scripts\detect_llvm.ps1

# Hybrid build (LLVM + ASM)
bash scripts/build_hybrid.sh

# No-LLVM build (direct ASM)
bash scripts/build_no_llvm.sh
```

You can also build directly with CMake (for advanced setups):

```powershell
mkdir build
cd build
cmake .. -DENABLE_LLVM=ON
cmake --build . --config Release
```

---

## 🔍 6. Expected Outputs

| Output       | Path               | Description                         |
| ------------ | ------------------ | ----------------------------------- |
| `halrust`    | `/target/release/` | Main binary (Hybrid or ASM backend) |
| `output.asm` | `/build/asm/`      | Generated NASM-compatible assembly  |
| `output.ll`  | `/build/llvm/`     | LLVM IR (if Hybrid Mode enabled)    |
| `build.log`  | `/logs/`           | Compilation log for debugging       |

When running in debug mode, both `output.ll` and `output.asm` are created for visual comparison.

---

## 🧪 7. Example Usage

```bash
# Hybrid build + run
bash scripts/build_hybrid.sh
./target/release/halrust examples/hybrid_example.rs

# Pure ASM build
bash scripts/build_no_llvm.sh
./target/release/halrust examples/no_llvm_example.rs
```

---

## 🧩 8. Troubleshooting

| Issue                          | Cause                             | Fix                                    |
| ------------------------------ | --------------------------------- | -------------------------------------- |
| LLVM not found                 | LLVM not installed or not in PATH | Install LLVM (`sudo apt install llvm`) |
| NASM missing                   | Required for ASM emission         | `sudo apt install nasm`                |
| Build script permission denied | Shell script not executable       | `chmod +x scripts/*.sh`                |
| Python errors                  | Old Python version                | Update to ≥3.8                         |

---

## 🌍 9. Integrating with R3C

To connect HalRust with the full R3C toolchain:

```bash
export R3C_PATH=/opt/r3c
./halrust --emit-asm --link-r3c $R3C_PATH
```

This enables full interoperability with the **R3C LLVM-Free pipeline**.

---

## 🪶 10. Next Steps

* Read [`transition_guide.md`](transition_guide.md) to migrate existing Rust projects to HalRust.
* Explore [`architecture.md`](architecture.md) for backend structure and data flow.
* Join the R3C Beyond-LLVM discussions at [GitHub Discussions → R3C Foundation](https://github.com/r3c-foundation).

---

© 2025 R3C Foundation · *Beyond LLVM Initiative*
*“LLVM and Freedom can coexist.”*

```

---
