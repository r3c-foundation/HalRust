#!/usr/bin/env python3
"""
🪶 HalRust Docs Auto Initializer
Automatically creates the full documentation directory tree and placeholder .md files.
"""

import os

# Documentation structure definition
structure = {
    "00_INTRODUCTION": [
        "overview.md",
        "design_goals.md",
        "philosophy.md"
    ],
    "01_ARCHITECTURE": [
        "architecture_diagram.md",
        "compiler_flow.md",
        "llvm_path.md",
        "asm_path.md",
        "dual_mode.md"
    ],
    "02_BUILD_SYSTEM": [
        "setup.md",
        "build_hybrid.md",
        "build_no_llvm.md",
        "ci_cd_pipeline.md"
    ],
    "03_COMPONENTS": [
        "hal_core.md",
        "hal_codegen.md",
        "hal_direct_asm.md",
        "llvm_adapter.md",
        "asm_emitter.md"
    ],
    "04_GUIDES": [
        "hybrid_mode_guide.md",
        "pure_asm_guide.md",
        "debug_mode_guide.md",
        "transition_from_rustc.md",
        "migration_to_r3c.md"
    ],
    "05_ECOSYSTEM": [
        "relation_to_r3c.md",
        "relation_to_ltss.md",
        "cpppm_integration.md",
        "rust_vm_no_llvm.md"
    ],
    "06_PHILOSOPHY_AND_MANIFESTOS": [
        "coexistence_manifesto.md",
        "independence_statement.md",
        "future_of_rust.md",
        "beyond_llvm_thesis.md"
    ],
    "07_API_REFERENCE": [
        "halrust_cli.md",
        "config_options.md",
        "llvm_hooks.md",
        "asm_emitter_api.md"
    ],
    "08_EXAMPLES": [
        "example_hybrid_project.md",
        "example_no_llvm_project.md",
        "performance_comparison.md",
        "debugging_samples.md"
    ],
    "09_APPENDIX": [
        "glossary.md",
        "versioning_policy.md",
        "license_notice.md",
        "contributors.md"
    ]
}

# Markdown placeholder content
template = """# {title}

_(This document is auto-generated as part of the HalRust Docs Portal.)_

Describe the content of **{title}** here.

---

🪶 HalRust — Hybrid Adaptive Layered Rust  
"LLVM and Freedom can coexist."
"""

def main():
    root = "docs"
    os.makedirs(root, exist_ok=True)
    count = 0

    for folder, files in structure.items():
        folder_path = os.path.join(root, folder)
        os.makedirs(folder_path, exist_ok=True)
        for f in files:
            f_path = os.path.join(folder_path, f)
            if not os.path.exists(f_path):
                with open(f_path, "w", encoding="utf-8") as md:
                    md.write(template.format(title=f.replace(".md", "").replace("_", " ").title()))
                count += 1

    print(f"✅ HalRust documentation tree initialized: {count} markdown files created.")
    print("📘 Next steps:")
    print("  1. Run: pip install mkdocs-material")
    print("  2. Run: mkdocs serve")
    print("  3. Visit http://127.0.0.1:8000 to preview your docs.")

if __name__ == "__main__":
    main()
