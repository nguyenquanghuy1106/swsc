import subprocess
import sys
from pathlib import Path

import streamlit as st


def render_camera_page():
    st.title("📸 Quét rác bằng camera")

    user_id = st.session_state.get("user_id", 0)
    user_name = st.session_state.get("user_name", "Guest")

    base_dir = Path(__file__).resolve().parents[5]
    camera_file = base_dir / "SWSC_camera" / "src" / "camera_predict.py"

    if not camera_file.exists():
        st.error(f"Không tìm thấy file camera: {camera_file}")
        return

    st.info("Nhấn nút bên dưới để mở camera realtime.")

    if st.button("📸 Mở camera", use_container_width=True):
        subprocess.Popen(
            [
                sys.executable,
                str(camera_file),
                "--user_id",
                str(user_id),
                "--user_name",
                str(user_name),
            ],
            cwd=str(base_dir),
        )

        st.success("Đã mở camera. Hãy xem cửa sổ camera bên ngoài.")

    st.warning("Trong camera: P = cố định vật, S = lưu database, Q = thoát.")