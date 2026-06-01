import streamlit as st


def load_battery_css():
    st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #f3f7f4 0%, #edf6ef 100%);
}

.main .block-container {
    max-width: 1400px;
    padding-top: 1.25rem;
    padding-bottom: 2rem;
}

.battery-topbar {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 18px;
    margin-bottom: 18px;
    padding: 4px 0 8px 0;
}

.battery-topbar-title {
    color: #111827;
    font-size: 24px;
    font-weight: 800;
    line-height: 1.2;
}

.battery-topbar-right {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 12px;
    flex-wrap: nowrap;
}

.battery-topbar-search-mini {
    min-width: 130px;
    height: 42px;
    border-radius: 999px;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    color: #9ca3af;
    font-size: 14px;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 16px;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
}

.battery-topbar-icon-wrap {
    position: relative;
    width: 40px;
    height: 40px;
    flex: 0 0 40px;
}

.battery-topbar-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
}

.battery-topbar-badge {
    position: absolute;
    top: -4px;
    right: -2px;
    min-width: 16px;
    height: 16px;
    border-radius: 999px;
    background: #ef4444;
    color: #ffffff;
    font-size: 10px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2;
    padding: 0 4px;
}

.battery-topbar-avatar {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
    flex: 0 0 42px;
}

.battery-banner-search {
    width: 100%;
    height: 52px;
    border-radius: 16px 16px 0 0;
    background: #ffffff;
    border: 1px solid #eef1ea;
    border-bottom: none;
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0 18px;
    color: #a1a1aa;
    font-size: 15px;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.03);
}

.battery-banner-search-icon {
    font-size: 16px;
    line-height: 1;
}

.battery-banner-search-text {
    font-weight: 500;
}

.battery-sidebar-wrapper {
    position: relative;
}

.battery-sidebar-checkbox {
    display: none;
}

.battery-sidebar-toggle {
    display: none;
    width: 46px;
    height: 46px;
    border-radius: 14px;
    background: #ffffff;
    border: 1px solid #d7e8da;
    color: #0f766e;
    font-size: 24px;
    font-weight: 800;
    align-items: center;
    justify-content: center;
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.06);
    margin-bottom: 12px;
    cursor: pointer;
    user-select: none;
}

.battery-sidebar-overlay {
    display: none;
}

.battery-sidebar {
    background: linear-gradient(180deg, #0f766e 0%, #115e59 100%);
    border-radius: 24px;
    padding: 22px 16px;
    min-height: 760px;
    box-shadow: 0 14px 30px rgba(15, 118, 110, 0.16);
}

.battery-logo {
    color: #ffffff;
    font-size: 26px;
    font-weight: 800;
    margin-bottom: 22px;
    line-height: 1.2;
}

.battery-menu {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.battery-menu-item {
    background: rgba(255, 255, 255, 0.08);
    color: #ffffff;
    border-radius: 14px;
    padding: 12px 14px;
    font-size: 15px;
    font-weight: 600;
}

.battery-menu-item.active {
    background: rgba(255, 255, 255, 0.18);
    border: 1px solid rgba(255, 255, 255, 0.12);
}

.battery-hero-banner {
    background: linear-gradient(180deg, #eef8e9 0%, #e8f5df 100%);
    border-radius: 0 0 24px 24px;
    padding: 0;
    margin-bottom: 22px;
    display: flex;
    align-items: stretch;
    justify-content: space-between;
    gap: 0;
    min-height: 300px;
    overflow: hidden;
    border: 1px solid #e3eddc;
    box-shadow: 0 10px 26px rgba(88, 120, 90, 0.08);
}

.battery-hero-left {
    flex: 1.05;
    min-width: 0;
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.battery-hero-right {
    flex: 1;
    min-width: 0;
    min-height: 300px;
    display: flex;
    align-items: stretch;
    justify-content: stretch;
}

.battery-hero-big-title {
    font-size: 38px;
    line-height: 1.25;
    font-weight: 800;
    color: #263238;
    margin-bottom: 16px;
}

.battery-hero-big-desc {
    font-size: 17px;
    line-height: 1.75;
    color: #44525c;
    margin-bottom: 20px;
}

.battery-hero-actions {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
}

.battery-hero-btn {
    padding: 12px 22px;
    border-radius: 14px;
    font-size: 16px;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
}

.battery-hero-btn.primary {
    background: #49a254;
    color: #ffffff;
    box-shadow: 0 8px 18px rgba(73, 162, 84, 0.22);
}

.battery-hero-btn.secondary {
    background: #ffffff;
    color: #5c7c5d;
    border: 1px solid #d7e5d2;
}

.battery-hero-banner-image {
    width: 100%;
    height: 100%;
    min-height: 300px;
    object-fit: cover;
    display: block;
}

.battery-hero-banner-missing {
    width: 100%;
    min-height: 300px;
    background: #f3f4f6;
    border-left: 1px dashed #cbd5e1;
    color: #64748b;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 700;
    text-align: center;
    padding: 20px;
}

.battery-section-title {
    color: #102a1f;
    font-size: 28px;
    font-weight: 800;
    margin: 8px 0 16px 0;
}

.battery-card {
    background: #ffffff;
    border-radius: 22px;
    padding: 16px 16px 14px 16px;
    border: 1px solid #d7e8da;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
    margin-bottom: 10px;
    min-height: 330px;
    display: flex;
    flex-direction: column;
}

.battery-card-head {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 10px;
    margin-bottom: 10px;
}

.battery-card-title {
    color: #1f2937;
    font-size: 18px;
    font-weight: 800;
    line-height: 1.2;
}

.battery-card-badge {
    min-width: 32px;
    height: 32px;
    padding: 0 10px;
    border-radius: 10px;
    background: #9fb6c4;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 800;
}

.battery-card-image-wrap {
    width: 100%;
    height: 150px;
    border-radius: 14px;
    overflow: hidden;
    background: #f3f7f1;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.battery-card-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.battery-card-image-fallback {
    background: #eef6f0;
}

.battery-card-emoji {
    font-size: 44px;
}

.battery-card-years {
    color: #2b2b2b;
    font-size: 15px;
    font-weight: 800;
    line-height: 1.4;
    margin-bottom: 10px;
}

.battery-progress {
    width: 100%;
    height: 8px;
    background: #dfe8dd;
    border-radius: 999px;
    overflow: hidden;
    margin-bottom: 12px;
}

.battery-progress-fill {
    height: 100%;
    border-radius: 999px;
}

.battery-card-desc {
    color: #52606d;
    font-size: 14px;
    line-height: 1.5;
    min-height: 42px;
}

.battery-card-button-row {
    display: flex;
    justify-content: flex-end;
    margin-top: auto;
    padding-top: 10px;
}

.battery-card-detail-btn {
    min-width: 88px;
    height: 34px;
    padding: 0 14px;
    border-radius: 8px;
    border: 1px solid #d7dce2;
    background: #f3f4f6;
    color: #3f3f46;
    font-size: 14px;
    font-weight: 600;
    cursor: not-allowed;
}

.battery-info-box {
    background: #ffffff;
    border-radius: 22px;
    padding: 20px 18px;
    border: 1px solid #d7e8da;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.05);
    min-height: 220px;
}

.battery-info-title {
    color: #0f172a;
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 12px;
}

.battery-list {
    padding-left: 18px;
    margin: 0;
}

.battery-list li {
    color: #334155;
    font-size: 15px;
    line-height: 1.65;
    margin-bottom: 8px;
}

.battery-action-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin-top: 6px;
}

.battery-action-card {
    background: #ffffff;
    border: 1px solid #d7e8da;
    border-radius: 18px;
    padding: 14px 16px;
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05);
    display: flex;
    align-items: center;
    justify-content: center;
}

.battery-action-btn {
    width: 100%;
    height: 46px;
    border: none;
    border-radius: 999px;
    color: #ffffff;
    font-size: 16px;
    font-weight: 700;
    cursor: not-allowed;
}

.battery-action-btn.red {
    background: linear-gradient(90deg, #6ec7ea 0%, #5aa3d6 100%);
}

.battery-action-btn.green {
    background: linear-gradient(90deg, #6fbe68 0%, #43a047 100%);
}

.battery-action-btn.blue {
    background: linear-gradient(90deg, #7db8dc 0%, #5aa3d6 100%);
}

.battery-note {
    color: #64748b;
    font-size: 13px;
    margin-top: 8px;
}

.battery-space-16 {
    height: 16px;
}

div[data-testid="stButton"] > button {
    border-radius: 14px;
    font-weight: 700;
    padding: 0.74rem 1rem;
    border: none;
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.08);
}

@media (max-width: 1200px) {
    .battery-hero-big-title {
        font-size: 32px;
    }

    .battery-hero-big-desc {
        font-size: 15px;
    }
}

@media (max-width: 1100px) {
    .battery-topbar {
        flex-direction: column;
        align-items: flex-start;
    }

    .battery-topbar-right {
        width: 100%;
        justify-content: flex-start;
        flex-wrap: wrap;
    }

    .battery-banner-search {
        height: 48px;
        font-size: 14px;
    }

    .battery-hero-banner {
        flex-direction: column;
        align-items: stretch;
        min-height: unset;
    }

    .battery-hero-left {
        padding: 24px;
    }

    .battery-hero-right {
        width: 100%;
        min-height: 220px;
    }

    .battery-hero-banner-image,
    .battery-hero-banner-missing {
        min-height: 220px;
    }

    .battery-action-grid {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 768px) {
    .battery-sidebar-wrapper {
        position: relative;
    }

    .battery-sidebar-toggle {
        display: inline-flex;
        position: relative;
        z-index: 997;
    }

    .battery-sidebar-checkbox:checked + .battery-sidebar-toggle {
        opacity: 0;
        pointer-events: none;
    }

    .battery-sidebar-checkbox:checked ~ .battery-sidebar-overlay {
        display: block;
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.35);
        z-index: 998;
    }

    .battery-sidebar {
        position: fixed;
        top: 0;
        left: -280px;
        width: 260px;
        height: 100vh;
        min-height: 100vh;
        border-radius: 0 20px 20px 0;
        z-index: 999;
        transition: left 0.28s ease;
        overflow-y: auto;
        padding-top: 24px;
    }

    .battery-sidebar-checkbox:checked ~ .battery-sidebar {
        left: 0;
    }
}
                .battery-ai-link {
    text-decoration: none !important;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer !important;
}

.battery-ai-link:hover {
    color: #ffffff;
    text-decoration: none !important;
    filter: brightness(1.05);
}
</style>
""", unsafe_allow_html=True)