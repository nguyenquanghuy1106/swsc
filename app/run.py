from pathlib import Path
import sys

# Ensure project root is available when running this file directly with Streamlit.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.main import run_app

if __name__ == "__main__":
    run_app()