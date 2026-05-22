from __future__ import annotations

import importlib
import platform
import sys


def package_version(name: str) -> str:
    try:
        module = importlib.import_module(name)
    except Exception as exc:
        return f"not available ({exc.__class__.__name__}: {exc})"
    return getattr(module, "__version__", "installed, version unknown")


def main() -> None:
    print("YOLO Learning Lab environment check")
    print("=" * 40)
    print(f"Python: {sys.version.split()[0]}")
    print(f"Executable: {sys.executable}")
    print(f"Platform: {platform.platform()}")
    print()

    for package in ["ultralytics", "torch", "cv2", "yaml", "numpy", "matplotlib"]:
        print(f"{package}: {package_version(package)}")

    print()
    try:
        import torch

        print(f"Torch CUDA available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"CUDA device count: {torch.cuda.device_count()}")
            print(f"CUDA device 0: {torch.cuda.get_device_name(0)}")
    except Exception as exc:
        print(f"Could not inspect torch CUDA: {exc}")

    print()
    try:
        from ultralytics import YOLO

        print("Ultralytics YOLO import: OK")
        print(f"YOLO class: {YOLO.__name__}")
    except Exception as exc:
        print(f"Ultralytics YOLO import failed: {exc}")


if __name__ == "__main__":
    main()

