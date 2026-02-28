"""Utilities to save/load ML models and preprocessors.

Place this in the project and import from your notebook to persist artifacts into `models/`.

Example usage in a notebook where you have variables available:

from scripts.save_models import save_sklearn_model, save_preprocessor, save_torch_model

# sklearn
save_sklearn_model(rf_model, 'rf_v0')  # creates models/rf_v0.pkl

# preprocessor (ColumnTransformer / Pipeline)
save_preprocessor(preprocessor, 'preproc_v0')  # creates models/preproc_v0.joblib

# pytorch (recommended: save state_dict)
save_torch_model(torch_model, 'cardiov0', state_dict=True)

You can also call these functions from scripts with explicit paths.
"""
from pathlib import Path
import joblib
import torch
import typing as t

ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = ROOT / "models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)


def save_sklearn_model(model: t.Any, name: str) -> Path:
    """Save a scikit-learn estimator using joblib.

    Args:
        model: estimator (fit)
        name: base name (no extension) to use under models/
    Returns:
        Path to saved file.
    """
    out = MODELS_DIR / f"{name}.pkl"
    joblib.dump(model, out)
    return out


def save_preprocessor(preprocessor: t.Any, name: str) -> Path:
    """Save a preprocessor (e.g., ColumnTransformer / Pipeline).

    Uses .joblib extension for clarity.
    """
    out = MODELS_DIR / f"{name}.joblib"
    joblib.dump(preprocessor, out)
    return out


def save_torch_model(model: torch.nn.Module, name: str, state_dict: bool = True) -> Path:
    """Save a PyTorch model.

    Args:
        model: nn.Module instance (should be trained/loaded in the notebook session)
        name: base name under models/
        state_dict: if True, save model.state_dict(), else save entire model object

    Returns:
        Path to saved file.
    """
    if state_dict:
        out = MODELS_DIR / f"{name}_state_dict.pth"
        torch.save(model.state_dict(), out)
    else:
        out = MODELS_DIR / f"{name}_full.pth"
        # Note: saving full model may require identical class definition to reload
        torch.save(model, out)
    return out


# Convenience CLI if someone wants to run the module directly
if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser(description="Save model artifacts into models/")
    p.add_argument("--sklearn-path", type=str, help="Path to an sklearn .pkl file to copy into models/")
    p.add_argument("--preproc-path", type=str, help="Path to a preprocessor .joblib file to copy into models/")
    p.add_argument("--torch-path", type=str, help="Path to a torch .pth file to copy into models/")
    p.add_argument("--name", type=str, default=None, help="Base name to use inside models/ (if not provided, original basename is used)")
    args = p.parse_args()

    def _copy(src: str, default_ext: str) -> Path:
        srcp = Path(src)
        if not srcp.exists():
            raise SystemExit(f"File not found: {src}")
        name = args.name or srcp.stem
        dest = MODELS_DIR / f"{name}{default_ext}"
        dest.write_bytes(srcp.read_bytes())
        return dest

    if args.sklearn_path:
        dest = _copy(args.sklearn_path, ".pkl")
        print("Saved:", dest)
    if args.preproc_path:
        dest = _copy(args.preproc_path, ".joblib")
        print("Saved:", dest)
    if args.torch_path:
        dest = _copy(args.torch_path, ".pth")
        print("Saved:", dest)
