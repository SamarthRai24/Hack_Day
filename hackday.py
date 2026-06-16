import os
import streamlit as st
import google.generativeai as genai
import json
import time
from datetime import datetime

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="VerifyAI – Truth Lens",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===============================
# PREMIUM CUSTOM CSS - HACKATHON WINNER LEVEL 🏆
# ===============================
st.markdown("""
<style>
/* ========== IMPORTS ========== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ========== ROOT VARIABLES ========== */
:root {
    --primary: #6366f1;
    --primary-light: #818cf8;
    --primary-dark: #4f46e5;
    --secondary: #06b6d4;
    --accent: #f472b6;
    --success: #10b981;
    --warning: #f59e0b;
    --danger: #ef4444;
    --bg-dark: #0a0a0f;
    --bg-card: rgba(17, 17, 27, 0.8);
    --bg-glass: rgba(255, 255, 255, 0.03);
    --border-glass: rgba(255, 255, 255, 0.08);
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --glow-primary: 0 0 40px rgba(99, 102, 241, 0.3);
    --glow-secondary: 0 0 40px rgba(6, 182, 212, 0.3);
    --glow-accent: 0 0 40px rgba(244, 114, 182, 0.3);
}

/* ========== GLOBAL STYLES ========== */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.stApp {
    background: linear-gradient(135deg, #0a0a0f 0%, #0d0d1a 25%, #111127 50%, #0d0d1a 75%, #0a0a0f 100%) !important;
    background-attachment: fixed !important;
}

/* Animated Background Orbs */
.stApp::before {
    content: '';
    position: fixed;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: 
        radial-gradient(circle at 20% 80%, rgba(99, 102, 241, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(6, 182, 212, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(244, 114, 182, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 90% 90%, rgba(16, 185, 129, 0.05) 0%, transparent 40%);
    animation: orbFloat 20s ease-in-out infinite;
    pointer-events: none;
    z-index: 0;
}

@keyframes orbFloat {
    0%, 100% { transform: translate(0, 0) rotate(0deg); }
    25% { transform: translate(2%, 2%) rotate(90deg); }
    50% { transform: translate(0, 4%) rotate(180deg); }
    75% { transform: translate(-2%, 2%) rotate(270deg); }
}

/* Grid Pattern Overlay */
.stApp::after {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        linear-gradient(rgba(99, 102, 241, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(99, 102, 241, 0.03) 1px, transparent 1px);
    background-size: 50px 50px;
    pointer-events: none;
    z-index: 0;
}

/* ========== MAIN CONTAINER ========== */
.block-container {
    padding: 2rem 3rem 4rem 3rem !important;
    max-width: 1400px !important;
    position: relative;
    z-index: 1;
}

/* ========== HERO HEADER ========== */
.hero-header {
    text-align: center;
    padding: 3rem 2rem;
    margin-bottom: 2.5rem;
    position: relative;
    overflow: hidden;
}

.hero-header::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 80%;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--primary), var(--secondary), var(--accent), transparent);
    animation: shimmer 3s ease-in-out infinite;
}

@keyframes shimmer {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 20px;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(6, 182, 212, 0.15));
    border: 1px solid rgba(99, 102, 241, 0.3);
    border-radius: 50px;
    font-size: 13px;
    font-weight: 600;
    color: var(--primary-light);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 1.5rem;
    animation: badgePulse 2s ease-in-out infinite;
}

@keyframes badgePulse {
    0%, 100% { box-shadow: 0 0 20px rgba(99, 102, 241, 0.2); }
    50% { box-shadow: 0 0 30px rgba(99, 102, 241, 0.4); }
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 800;
    background: linear-gradient(135deg, #fff 0%, #e2e8f0 25%, var(--primary-light) 50%, var(--secondary) 75%, var(--accent) 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 4s ease-in-out infinite;
    margin-bottom: 1rem;
    line-height: 1.2;
}

@keyframes gradientShift {
    0%, 100% { background-position: 0% center; }
    50% { background-position: 100% center; }
}

.hero-subtitle {
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    # font-size: 1.15rem;
    # color: var(--text-secondary);
    # max-width: 600px;
    # margin: 0 auto;
    # line-height: 1.7;
    # font-weight: 400;
    # text-align: center;
    # margin-left: auto;
    # margin-right: auto;
}

.hero-subtitle strong {
    color: var(--secondary);
    font-weight: 600;
}

/* ========== PREMIUM GLASS CARDS ========== */
.glass-card {
    background: linear-gradient(135deg, rgba(17, 17, 27, 0.9) 0%, rgba(17, 17, 27, 0.7) 100%);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--border-glass);
    border-radius: 24px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
}

.glass-card:hover {
    border-color: rgba(99, 102, 241, 0.3);
    transform: translateY(-4px);
    box-shadow: 
        0 20px 40px rgba(0, 0, 0, 0.3),
        0 0 60px rgba(99, 102, 241, 0.1);
}

/* Card Variants */
.glass-card.primary-glow {
    border-color: rgba(99, 102, 241, 0.2);
    box-shadow: inset 0 0 60px rgba(99, 102, 241, 0.05);
}

.glass-card.secondary-glow {
    border-color: rgba(6, 182, 212, 0.2);
    box-shadow: inset 0 0 60px rgba(6, 182, 212, 0.05);
}

.glass-card.success-glow {
    border-color: rgba(16, 185, 129, 0.2);
    box-shadow: inset 0 0 60px rgba(16, 185, 129, 0.05);
}

.glass-card.warning-glow {
    border-color: rgba(245, 158, 11, 0.2);
    box-shadow: inset 0 0 60px rgba(245, 158, 11, 0.05);
}

.glass-card.danger-glow {
    border-color: rgba(239, 68, 68, 0.2);
    box-shadow: inset 0 0 60px rgba(239, 68, 68, 0.05);
}

/* ========== SECTION TITLES ========== */
.section-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 1.5rem;
}

.section-icon {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    border-radius: 14px;
    font-size: 22px;
    box-shadow: 0 8px 20px rgba(99, 102, 241, 0.3);
}

.section-title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0;
}

.section-subtitle {
    font-size: 0.9rem;
    color: var(--text-muted);
    margin: 0;
}

/* ========== MEGA SCORE DISPLAY ========== */
.score-container {
    text-align: center;
    padding: 2.5rem;
    position: relative;
}

.score-ring {
    position: relative;
    width: 200px;
    height: 200px;
    margin: 0 auto 1.5rem;
}

.score-ring svg {
    transform: rotate(-90deg);
    width: 200px;
    height: 200px;
}

.score-ring-bg {
    fill: none;
    stroke: rgba(255, 255, 255, 0.05);
    stroke-width: 12;
}

.score-ring-progress {
    fill: none;
    stroke: url(#scoreGradient);
    stroke-width: 12;
    stroke-linecap: round;
    stroke-dasharray: 565.48;
    stroke-dashoffset: 565.48;
    animation: scoreProgress 2s ease-out forwards;
    filter: drop-shadow(0 0 10px rgba(99, 102, 241, 0.5));
}

@keyframes scoreProgress {
    to { stroke-dashoffset: var(--progress); }
}

.score-value-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

.score-value {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--primary-light), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
}

.score-label {
    font-size: 0.85rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: 600;
}

.score-verdict {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 24px;
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(6, 182, 212, 0.15));
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 50px;
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--success);
}

.score-verdict.medium {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(251, 191, 36, 0.15));
    border-color: rgba(245, 158, 11, 0.3);
    color: var(--warning);
}

.score-verdict.low {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(248, 113, 113, 0.15));
    border-color: rgba(239, 68, 68, 0.3);
    color: var(--danger);
}

/* ========== STATS GRID ========== */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
}

.stat-item {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--border-glass);
    border-radius: 16px;
    padding: 1.25rem;
    text-align: center;
    transition: all 0.3s ease;
}

.stat-item:hover {
    background: rgba(99, 102, 241, 0.05);
    border-color: rgba(99, 102, 241, 0.2);
    transform: translateY(-2px);
}

.stat-icon {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

.stat-value {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
}

.stat-label {
    font-size: 0.75rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 4px;
}

/* ========== SOURCE CARDS ========== */
.source-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--border-glass);
    border-radius: 16px;
    padding: 1.25rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    transition: all 0.3s ease;
}

.source-card:hover {
    background: rgba(99, 102, 241, 0.05);
    border-color: rgba(99, 102, 241, 0.2);
    transform: translateX(4px);
}

.source-icon {
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(6, 182, 212, 0.2));
    border-radius: 12px;
    font-size: 1.2rem;
    flex-shrink: 0;
}

.source-content {
    flex: 1;
    min-width: 0;
}

.source-name {
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 4px;
}

.source-url {
    font-size: 0.85rem;
    color: var(--primary-light);
    text-decoration: none;
    word-break: break-all;
    transition: color 0.2s;
}

.source-url:hover {
    color: var(--secondary);
}

.trust-badge {
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    flex-shrink: 0;
}

.trust-badge.high {
    background: rgba(16, 185, 129, 0.15);
    color: var(--success);
    border: 1px solid rgba(16, 185, 129, 0.3);
}

.trust-badge.medium {
    background: rgba(245, 158, 11, 0.15);
    color: var(--warning);
    border: 1px solid rgba(245, 158, 11, 0.3);
}

.trust-badge.low {
    background: rgba(239, 68, 68, 0.15);
    color: var(--danger);
    border: 1px solid rgba(239, 68, 68, 0.3);
}

/* ========== INSIGHT PILLS ========== */
.insight-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 20px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--border-glass);
    border-radius: 12px;
    margin: 6px;
    font-size: 0.95rem;
    color: var(--text-secondary);
    transition: all 0.3s ease;
}

.insight-pill:hover {
    background: rgba(99, 102, 241, 0.08);
    border-color: rgba(99, 102, 241, 0.3);
    color: var(--text-primary);
    transform: translateY(-2px);
}

.insight-pill-icon {
    width: 8px;
    height: 8px;
    background: var(--primary);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--primary);
}

/* ========== ALERT CARDS ========== */
.alert-card {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    padding: 1.25rem;
    background: rgba(239, 68, 68, 0.08);
    border: 1px solid rgba(239, 68, 68, 0.2);
    border-radius: 14px;
    margin-bottom: 0.75rem;
}

.alert-icon {
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(239, 68, 68, 0.15);
    border-radius: 10px;
    font-size: 1rem;
    flex-shrink: 0;
}

.alert-text {
    color: var(--text-secondary);
    font-size: 0.95rem;
    line-height: 1.5;
}

/* ========== BIAS METER ========== */
.bias-meter {
    padding: 1.5rem 0;
}

.bias-track {
    height: 12px;
    background: linear-gradient(90deg, 
        var(--success) 0%, 
        var(--success) 33%, 
        var(--warning) 33%, 
        var(--warning) 66%, 
        var(--danger) 66%, 
        var(--danger) 100%
    );
    border-radius: 6px;
    position: relative;
    margin: 1rem 0;
    overflow: hidden;
}

.bias-track::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(180deg, rgba(255,255,255,0.2) 0%, transparent 50%, rgba(0,0,0,0.2) 100%);
}

.bias-labels {
    display: flex;
    justify-content: space-between;
    font-size: 0.8rem;
    color: var(--text-muted);
}

.bias-value {
    text-align: center;
    margin-top: 1rem;
}

.bias-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 28px;
    border-radius: 50px;
    font-size: 1rem;
    font-weight: 600;
}

.bias-tag.neutral {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(6, 182, 212, 0.15));
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: var(--success);
}

.bias-tag.slight {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(251, 191, 36, 0.15));
    border: 1px solid rgba(245, 158, 11, 0.3);
    color: var(--warning);
}

.bias-tag.high {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(248, 113, 113, 0.15));
    border: 1px solid rgba(239, 68, 68, 0.3);
    color: var(--danger);
}

/* ========== PLAGIARISM DISPLAY ========== */
.plagiarism-display {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
    padding: 2rem;
}

.plagiarism-icon {
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    font-size: 2rem;
}

.plagiarism-icon.low {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(6, 182, 212, 0.2));
    box-shadow: 0 0 30px rgba(16, 185, 129, 0.3);
}

.plagiarism-icon.medium {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.2), rgba(251, 191, 36, 0.2));
    box-shadow: 0 0 30px rgba(245, 158, 11, 0.3);
}

.plagiarism-icon.high {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(248, 113, 113, 0.2));
    box-shadow: 0 0 30px rgba(239, 68, 68, 0.3);
}

.plagiarism-text {
    text-align: left;
}

.plagiarism-level {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 2rem;
    font-weight: 700;
}

.plagiarism-level.low { color: var(--success); }
.plagiarism-level.medium { color: var(--warning); }
.plagiarism-level.high { color: var(--danger); }

.plagiarism-desc {
    color: var(--text-muted);
    font-size: 0.9rem;
}

/* ========== SUMMARY BOX ========== */
.summary-box {
    position: relative;
    padding: 1.5rem;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.05), rgba(6, 182, 212, 0.05));
    border-left: 4px solid var(--primary);
    border-radius: 0 16px 16px 0;
}

.summary-box p {
    color: var(--text-secondary);
    font-size: 1.05rem;
    line-height: 1.8;
    margin: 0;
}

/* ========== INPUT STYLING ========== */
.stTextArea > div > div > textarea {
    background: rgba(17, 17, 27, 0.8) !important;
    border: 2px solid var(--border-glass) !important;
    border-radius: 16px !important;
    color: var(--text-primary) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.95rem !important;
    padding: 1.25rem !important;
    transition: all 0.3s ease !important;
}

.stTextArea > div > div > textarea:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15), var(--glow-primary) !important;
}

.stTextArea > div > div > textarea::placeholder {
    color: var(--text-muted) !important;
}

/* ========== BUTTON STYLING ========== */
.stButton > button {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
    color: white !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    padding: 1rem 2.5rem !important;
    border: none !important;
    border-radius: 14px !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3) !important;
    text-transform: none !important;
    letter-spacing: 0.5px !important;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 30px rgba(99, 102, 241, 0.5) !important;
}

.stButton > button:active {
    transform: translateY(-1px) !important;
}

/* Full Width Button */
.stButton > button[kind="primary"] {
    width: 100% !important;
}

/* ========== SIDEBAR STYLING ========== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(10, 10, 15, 0.98) 0%, rgba(13, 13, 26, 0.98) 100%) !important;
    border-right: 1px solid var(--border-glass) !important;
}

[data-testid="stSidebar"] .block-container {
    padding: 2rem 1.5rem !important;
}

/* Sidebar Input */
[data-testid="stSidebar"] .stTextInput > div > div > input {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid var(--border-glass) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    padding: 0.875rem 1rem !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.9rem !important;
}

[data-testid="stSidebar"] .stTextInput > div > div > input:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15) !important;
}

/* ========== PROGRESS BAR ========== */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent)) !important;
    border-radius: 10px !important;
    box-shadow: 0 0 20px rgba(99, 102, 241, 0.4) !important;
}

.stProgress > div > div > div {
    background: rgba(255, 255, 255, 0.05) !important;
    border-radius: 10px !important;
}

/* ========== SPINNER ========== */
.stSpinner > div {
    border-color: var(--primary) transparent transparent transparent !important;
}

/* ========== SUCCESS/ERROR/WARNING MESSAGES ========== */
.stSuccess {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(6, 182, 212, 0.1)) !important;
    border: 1px solid rgba(16, 185, 129, 0.3) !important;
    border-radius: 14px !important;
    color: var(--success) !important;
}

.stError {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(248, 113, 113, 0.1)) !important;
    border: 1px solid rgba(239, 68, 68, 0.3) !important;
    border-radius: 14px !important;
}

.stWarning {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(251, 191, 36, 0.1)) !important;
    border: 1px solid rgba(245, 158, 11, 0.3) !important;
    border-radius: 14px !important;
}

/* ========== DIVIDER ========== */
.custom-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border-glass), transparent);
    margin: 2rem 0;
}

/* ========== ANIMATIONS ========== */
.fade-in {
    animation: fadeIn 0.6s ease-out forwards;
}

.fade-in-up {
    animation: fadeInUp 0.6s ease-out forwards;
}

.fade-in-left {
    animation: fadeInLeft 0.5s ease-out forwards;
}

.scale-in {
    animation: scaleIn 0.5s ease-out forwards;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes fadeInUp {
    from { 
        opacity: 0; 
        transform: translateY(30px); 
    }
    to { 
        opacity: 1; 
        transform: translateY(0); 
    }
}

@keyframes fadeInLeft {
    from { 
        opacity: 0; 
        transform: translateX(-20px); 
    }
    to { 
        opacity: 1; 
        transform: translateX(0); 
    }
}

@keyframes scaleIn {
    from { 
        opacity: 0; 
        transform: scale(0.9); 
    }
    to { 
        opacity: 1; 
        transform: scale(1); 
    }
}

/* Stagger delays */
.delay-1 { animation-delay: 0.1s; }
.delay-2 { animation-delay: 0.2s; }
.delay-3 { animation-delay: 0.3s; }
.delay-4 { animation-delay: 0.4s; }
.delay-5 { animation-delay: 0.5s; }

/* ========== COLUMN SPACING ========== */
[data-testid="column"] {
    padding: 0 0.75rem !important;
}

/* ========== HIDE STREAMLIT BRANDING ========== */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* ========== RESPONSIVE ========== */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem 1rem 3rem 1rem !important;
    }
    
    .hero-title {
        font-size: 2rem;
    }
    
    .glass-card {
        padding: 1.25rem;
        border-radius: 18px;
    }
    
    .score-ring {
        width: 160px;
        height: 160px;
    }
    
    .score-value {
        font-size: 2.5rem;
    }
}

/* ========== FEATURE CARDS ========== */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.25rem;
    margin-top: 1rem;
}

.feature-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--border-glass);
    border-radius: 18px;
    padding: 1.75rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.feature-card::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, transparent 50%);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.feature-card:hover {
    border-color: rgba(99, 102, 241, 0.3);
    transform: translateY(-4px);
}

.feature-card:hover::after {
    opacity: 1;
}

.feature-icon {
    width: 56px;
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    border-radius: 16px;
    font-size: 1.5rem;
    margin-bottom: 1.25rem;
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.25);
}

.feature-title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.15rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
}

.feature-desc {
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.6;
}

/* ========== FOOTER ========== */
.custom-footer {
    text-align: center;
    padding: 3rem 2rem;
    margin-top: 2rem;
    border-top: 1px solid var(--border-glass);
}

.footer-brand {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--primary-light), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}

.footer-tagline {
    color: var(--text-muted);
    font-size: 0.9rem;
}

.footer-links {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 1.5rem;
}

.footer-link {
    color: var(--text-secondary);
    text-decoration: none;
    font-size: 0.9rem;
    transition: color 0.2s;
}

.footer-link:hover {
    color: var(--primary-light);
}

/* ========== LOADING ANIMATION ========== */
.loading-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 4rem 2rem;
}

.loading-spinner {
    width: 60px;
    height: 60px;
    border: 3px solid rgba(99, 102, 241, 0.1);
    border-top-color: var(--primary);
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.loading-text {
    margin-top: 1.5rem;
    color: var(--text-secondary);
    font-size: 1rem;
}

.loading-dots {
    display: inline-flex;
    gap: 4px;
}

.loading-dots span {
    width: 6px;
    height: 6px;
    background: var(--primary);
    border-radius: 50%;
    animation: bounce 1.4s ease-in-out infinite both;
}

.loading-dots span:nth-child(1) { animation-delay: -0.32s; }
.loading-dots span:nth-child(2) { animation-delay: -0.16s; }

@keyframes bounce {
    0%, 80%, 100% { transform: scale(0); }
    40% { transform: scale(1); }
}

/* ========== METRIC CARDS ========== */
.metric-row {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.metric-card {
    flex: 1;
    min-width: 150px;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--border-glass);
    border-radius: 16px;
    padding: 1.25rem;
    text-align: center;
}

.metric-value {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--primary-light), var(--secondary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.metric-label {
    font-size: 0.8rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# SIDEBAR - API KEY & INFO
# ===============================
with st.sidebar:
    # Sidebar Header
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 0 2rem;">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🔍</div>
        <div style="font-family: 'Space Grotesk', sans-serif; font-size: 1.5rem; font-weight: 700; 
                    background: linear-gradient(135deg, #818cf8, #06b6d4);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            VerifyAI
        </div>
        <div style="color: #64748b; font-size: 0.85rem;">Truth Lens</div>
    </div>
    """, unsafe_allow_html=True)
    
    # API Key Section
    st.markdown("""
    <div style="background: rgba(99, 102, 241, 0.08); border: 1px solid rgba(99, 102, 241, 0.2);
                border-radius: 14px; padding: 1.25rem; margin-bottom: 1.5rem;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 1rem;">
            <span style="font-size: 1.25rem;">🔑</span>
            <span style="font-weight: 600; color: #f8fafc;">API Configuration</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            placeholder="AIzaSy...",
            help="Your API key is stored locally and never sent to any server"
        )
    else:
        st.markdown("""
        <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.2);
                    border-radius: 12px; padding: 0.75rem; margin-bottom: 1rem;">
            <div style="font-weight: 600; color: #10b981; font-size: 0.9rem;">
                Using GEMINI_API_KEY from environment
            </div>
            <div style="color: #94a3b8; font-size: 0.8rem;">
                Set this key in Vercel / Streamlit Cloud environment variables
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Security Note
    st.markdown("""
    <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.2);
                border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
        <div style="display: flex; align-items: flex-start; gap: 10px;">
            <span style="font-size: 1.1rem;">🛡️</span>
            <div>
                <div style="font-weight: 600; color: #10b981; font-size: 0.9rem; margin-bottom: 4px;">
                    Secure & Private
                </div>
                <div style="color: #64748b; font-size: 0.8rem; line-height: 1.5;">
                    API key sirf locally use hoti hai • Kahin store nahi hoti • Page refresh pe reset
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Divider
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
    # Features Section
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <div style="font-weight: 600; color: #f8fafc; margin-bottom: 1rem; font-size: 0.9rem;">
            ✨ Key Features
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    features = [
        ("🎯", "Reliability Scoring", "AI accuracy ka real-time assessment"),
        ("🧠", "Fact Verification", "Claims ki authenticity check"),
        ("⚖️", "Bias Detection", "Tone aur bias ka analysis"),
        ("🔗", "Source Extraction", "References aur citations"),
        ("🚩", "Red Flag Alerts", "Potential issues highlight"),
        ("🧬", "Plagiarism Check", "Originality assessment")
    ]
    
    for icon, title, desc in features:
        st.markdown(f"""
        <div style="display: flex; align-items: flex-start; gap: 12px; margin-bottom: 1rem;
                    padding: 0.75rem; background: rgba(255,255,255,0.02); border-radius: 10px;
                    transition: all 0.2s;">
            <span style="font-size: 1.25rem;">{icon}</span>
            <div>
                <div style="font-weight: 500; color: #e2e8f0; font-size: 0.9rem;">{title}</div>
                <div style="color: #64748b; font-size: 0.75rem;">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Divider
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
    # Built for Hackathon Badge
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(244, 114, 182, 0.1));
                border: 1px solid rgba(99, 102, 241, 0.2); border-radius: 14px;">
        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🏆</div>
        <div style="font-weight: 600; color: #f8fafc; font-size: 0.9rem;">Built for Hackathon</div>
        <div style="color: #64748b; font-size: 0.75rem; margin-top: 4px;">Real-world trust verification</div>
    </div>
    """, unsafe_allow_html=True)

# ===============================
# GEMINI ANALYSIS FUNCTION
# ===============================
def analyze_ai_content(text, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are an AI Content Auditor and Fact-Checker. Analyze the following AI-generated content thoroughly.

STRICT RULES:
- Return ONLY valid JSON
- Do NOT add any explanations or text outside JSON
- Do NOT wrap in markdown code blocks
- Ensure all fields are filled with meaningful analysis

Required JSON format:
{{
  "summary": "A comprehensive 2-3 sentence summary of what the content claims",
  "reliability_score": <number from 0-100>,
  "reliability_reason": "Brief explanation for the score",
  "confidence_level": "High/Medium/Low",
  "factual_accuracy": "Verified/Partially Verified/Unverified/Contains Errors",
  "sources": [
    {{"name": "Source Name", "url": "https://example.com", "trust": "High/Medium/Low", "relevance": "Brief note on relevance"}}
  ],
  "tone_bias": "Neutral/Slightly Biased/Moderately Biased/Highly Biased",
  "bias_direction": "None/Left-leaning/Right-leaning/Corporate/Academic/Sensationalist",
  "quick_read": ["Key Point 1", "Key Point 2", "Key Point 3", "Key Point 4"],
  "plagiarism_risk": "Low/Medium/High",
  "originality_note": "Brief note on content originality",
  "red_flags": ["Specific issue 1", "Specific issue 2"],
  "strengths": ["Strength 1", "Strength 2"],
  "content_type": "Informational/Opinion/News/Academic/Marketing/Other",
  "reading_time": "X min read",
  "complexity_level": "Basic/Intermediate/Advanced"
}}

Content to analyze:
{text}
"""

    response = model.generate_content(prompt)
    raw = response.text.strip()
    
    # Clean JSON
    start = raw.find("{")
    end = raw.rfind("}") + 1
    
    if start == -1 or end == -1:
        raise ValueError("Gemini did not return valid JSON")
    
    clean_json = raw[start:end]
    return json.loads(clean_json)

# ===============================
# MAIN HEADER
# ===============================
st.markdown("""
<div class="hero-header fade-in">
    <div class="hero-badge">
        <span>🤖</span>
        <span>AI Content Verification Platform</span>
    </div>
    <h1 class="hero-title">VerifyAI – Truth Lens</h1>
    <p class="hero-subtitle">
        AI-generated content ki <strong>reliability</strong>, <strong>accuracy</strong> aur <strong>trust</strong> 
        verify karein advanced Gemini-powered analysis se
    </p>
</div>
""", unsafe_allow_html=True)

# ===============================
# FEATURES SHOWCASE (Before Input)
# ===============================
st.markdown("""
<div class="glass-card fade-in-up" style="margin-bottom: 2rem;">
    <div class="section-header">
        <div class="section-icon">⚡</div>
        <div>
            <h3 class="section-title">Powerful Analysis Features</h3>
            <p class="section-subtitle">Comprehensive AI content verification in seconds</p>
        </div>
    </div>
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Reliability Score</div>
            <div class="feature-desc">0-100 accuracy rating with detailed reasoning</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔬</div>
            <div class="feature-title">Fact Analysis</div>
            <div class="feature-desc">Claims verification with source matching</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎭</div>
            <div class="feature-title">Bias Detection</div>
            <div class="feature-desc">Identify tone, bias direction & sentiment</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📝</div>
            <div class="feature-title">Smart Summary</div>
            <div class="feature-desc">Quick insights & key takeaways</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===============================
# INPUT SECTION
# ===============================
st.markdown("""
<div class="glass-card primary-glow fade-in-up delay-1">
    <div class="section-header">
        <div class="section-icon">📝</div>
        <div>
            <h3 class="section-title">Content Input</h3>
            <p class="section-subtitle">Paste any AI-generated text for comprehensive analysis</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

ai_text = st.text_area(
    "AI Content",
    height=200,
    placeholder="🤖 Yahan AI ka generated content paste karein...\n\nExample: ChatGPT, Claude, Gemini ya kisi bhi AI tool ka output paste kar sakte ho.\n\nHum analyze karenge:\n• Reliability & accuracy\n• Bias & tone\n• Sources & citations\n• Potential red flags",
    label_visibility="collapsed"
)

# Character count
if ai_text:
    char_count = len(ai_text)
    word_count = len(ai_text.split())
    st.markdown(f"""
    <div style="display: flex; gap: 1.5rem; margin-top: 0.5rem; padding: 0.75rem 1rem;
                background: rgba(99, 102, 241, 0.05); border-radius: 10px;">
        <span style="color: #64748b; font-size: 0.85rem;">
            📊 <strong style="color: #818cf8;">{char_count:,}</strong> characters
        </span>
        <span style="color: #64748b; font-size: 0.85rem;">
            📝 <strong style="color: #06b6d4;">{word_count:,}</strong> words
        </span>
        <span style="color: #64748b; font-size: 0.85rem;">
            ⏱️ ~<strong style="color: #10b981;">{max(1, word_count // 200)}</strong> min read
        </span>
    </div>
    """, unsafe_allow_html=True)

# Analyze Button
st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_clicked = st.button("🚀 Analyze Content", use_container_width=True, type="primary")

# ===============================
# ANALYSIS LOGIC
# ===============================
if analyze_clicked:
    if not api_key:
        st.markdown("""
        <div class="glass-card danger-glow fade-in" style="text-align: center; padding: 2rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🔐</div>
            <div style="font-size: 1.25rem; font-weight: 600; color: #f8fafc; margin-bottom: 0.5rem;">
                API Key Required
            </div>
            <div style="color: #94a3b8;">
                Sidebar mein Gemini API key enter karein to continue
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    elif not ai_text.strip():
        st.markdown("""
        <div class="glass-card warning-glow fade-in" style="text-align: center; padding: 2rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📄</div>
            <div style="font-size: 1.25rem; font-weight: 600; color: #f8fafc; margin-bottom: 0.5rem;">
                Content Required
            </div>
            <div style="color: #94a3b8;">
                Analysis ke liye pehle AI content paste karein
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    else:
        # Loading Animation
        with st.spinner(""):
            st.markdown("""
            <div class="glass-card fade-in" style="text-align: center; padding: 3rem;">
                <div class="loading-spinner" style="margin: 0 auto 1.5rem;"></div>
                <div style="font-size: 1.1rem; color: #f8fafc; margin-bottom: 0.5rem;">
                    🔍 Analyzing Content...
                </div>
                <div style="color: #64748b; font-size: 0.9rem;">
                    Gemini AI deep analysis kar raha hai
                </div>
                <div style="margin-top: 1.5rem; display: flex; justify-content: center; gap: 2rem;">
                    <span style="color: #818cf8; font-size: 0.85rem;">✓ Fact checking</span>
                    <span style="color: #06b6d4; font-size: 0.85rem;">✓ Bias detection</span>
                    <span style="color: #f472b6; font-size: 0.85rem;">✓ Source analysis</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            time.sleep(1)
            
            try:
                data = analyze_ai_content(ai_text, api_key)
                
                # ===============================
                # RESULTS DASHBOARD
                # ===============================
                st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
                
                st.markdown("""
                <div style="text-align: center; margin-bottom: 2rem;" class="fade-in">
                    <div class="hero-badge" style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(6, 182, 212, 0.15));
                                                   border-color: rgba(16, 185, 129, 0.3);">
                        <span>✅</span>
                        <span>Analysis Complete</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Main Results Grid
                col1, col2 = st.columns([1, 1.5])
                
                # ===============================
                # SCORE SECTION (Left Column)
                # ===============================
                with col1:
                    score = data.get("reliability_score", 50)
                    progress_offset = 565.48 - (565.48 * score / 100)
                    
                    # Determine score color
                    if score >= 70:
                        score_class = "high"
                        verdict_text = "Highly Reliable"
                        verdict_icon = "✅"
                    elif score >= 40:
                        score_class = "medium"
                        verdict_text = "Moderately Reliable"
                        verdict_icon = "⚠️"
                    else:
                        score_class = "low"
                        verdict_text = "Low Reliability"
                        verdict_icon = "❌"
                    
                    st.markdown(f"""
                    <div class="glass-card success-glow fade-in-up">
                        <div class="score-container">
                            <div class="score-ring">
                                <svg viewBox="0 0 200 200">
                                    <defs>
                                        <linearGradient id="scoreGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:#6366f1"/>
                                            <stop offset="50%" style="stop-color:#06b6d4"/>
                                            <stop offset="100%" style="stop-color:#10b981"/>
                                        </linearGradient>
                                    </defs>
                                    <circle class="score-ring-bg" cx="100" cy="100" r="90"/>
                                    <circle class="score-ring-progress" cx="100" cy="100" r="90" 
                                            style="--progress: {progress_offset};"/>
                                </svg>
                                <div class="score-value-container">
                                    <div class="score-value">{score}</div>
                                    <div class="score-label">Score</div>
                                </div>
                            </div>
                            <div class="score-verdict {score_class}">
                                {verdict_icon} {verdict_text}
                            </div>
                            <p style="color: #94a3b8; margin-top: 1rem; font-size: 0.9rem; line-height: 1.6;">
                                {data.get("reliability_reason", "Analysis complete")}
                            </p>
                        </div>
                        
                        <div class="stats-grid">
                            <div class="stat-item">
                                <div class="stat-icon">🎯</div>
                                <div class="stat-value">{data.get("confidence_level", "Medium")}</div>
                                <div class="stat-label">Confidence</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-icon">📖</div>
                                <div class="stat-value">{data.get("reading_time", "2 min")}</div>
                                <div class="stat-label">Read Time</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-icon">📊</div>
                                <div class="stat-value">{data.get("complexity_level", "Intermediate")}</div>
                                <div class="stat-label">Complexity</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-icon">📁</div>
                                <div class="stat-value">{data.get("content_type", "Info")}</div>
                                <div class="stat-label">Type</div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # ===============================
                # SUMMARY & QUICK READ (Right Column)
                # ===============================
                with col2:
                    # Summary
                    st.markdown(f"""
                    <div class="glass-card primary-glow fade-in-up delay-1">
                        <div class="section-header">
                            <div class="section-icon">🧠</div>
                            <div>
                                <h3 class="section-title">Fact-Check Summary</h3>
                                <p class="section-subtitle">{data.get("factual_accuracy", "Analysis complete")}</p>
                            </div>
                        </div>
                        <div class="summary-box">
                            <p>{data.get("summary", "No summary available")}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Quick Read Points
                    quick_read = data.get("quick_read", [])
                    if quick_read:
                        pills_html = "".join([f'<div class="insight-pill"><span class="insight-pill-icon"></span>{point}</div>' for point in quick_read])
                        st.markdown(f"""
                        <div class="glass-card secondary-glow fade-in-up delay-2">
                            <div class="section-header">
                                <div class="section-icon" style="background: linear-gradient(135deg, #06b6d4, #0891b2);">📌</div>
                                <div>
                                    <h3 class="section-title">Quick Insights</h3>
                                    <p class="section-subtitle">Key takeaways at a glance</p>
                                </div>
                            </div>
                            <div style="display: flex; flex-wrap: wrap; margin: -6px;">
                                {pills_html}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # ===============================
                # SECOND ROW - BIAS & PLAGIARISM
                # ===============================
                col1, col2 = st.columns(2)
                
                with col1:
                    # Bias Detection
                    tone_bias = data.get("tone_bias", "Neutral")
                    bias_direction = data.get("bias_direction", "None")
                    
                    if "Neutral" in tone_bias:
                        bias_class = "neutral"
                        bias_icon = "✅"
                    elif "Slight" in tone_bias:
                        bias_class = "slight"
                        bias_icon = "⚠️"
                    else:
                        bias_class = "high"
                        bias_icon = "🚨"
                    
                    st.markdown(f"""
                    <div class="glass-card fade-in-up delay-3">
                        <div class="section-header">
                            <div class="section-icon" style="background: linear-gradient(135deg, #f472b6, #ec4899);">⚖️</div>
                            <div>
                                <h3 class="section-title">Bias & Tone Analysis</h3>
                                <p class="section-subtitle">Content objectivity assessment</p>
                            </div>
                        </div>
                        <div class="bias-meter">
                            <div class="bias-track"></div>
                            <div class="bias-labels">
                                <span>Neutral</span>
                                <span>Slight Bias</span>
                                <span>High Bias</span>
                            </div>
                        </div>
                        <div class="bias-value">
                            <div class="bias-tag {bias_class}">
                                {bias_icon} {tone_bias}
                            </div>
                            <p style="color: #64748b; margin-top: 1rem; font-size: 0.9rem;">
                                Direction: <strong style="color: #94a3b8;">{bias_direction}</strong>
                            </p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    # Plagiarism Risk
                    plagiarism = data.get("plagiarism_risk", "Low")
                    originality = data.get("originality_note", "Content appears original")
                    
                    plag_class = plagiarism.lower()
                    if plagiarism == "Low":
                        plag_icon = "✅"
                        plag_desc = "Content appears to be original"
                    elif plagiarism == "Medium":
                        plag_icon = "⚠️"
                        plag_desc = "Some common patterns detected"
                    else:
                        plag_icon = "🚨"
                        plag_desc = "High similarity to existing content"
                    
                    st.markdown(f"""
                    <div class="glass-card fade-in-up delay-3">
                        <div class="section-header">
                            <div class="section-icon" style="background: linear-gradient(135deg, #10b981, #059669);">🧬</div>
                            <div>
                                <h3 class="section-title">Plagiarism Assessment</h3>
                                <p class="section-subtitle">Content originality check</p>
                            </div>
                        </div>
                        <div class="plagiarism-display">
                            <div class="plagiarism-icon {plag_class}">
                                {plag_icon}
                            </div>
                            <div class="plagiarism-text">
                                <div class="plagiarism-level {plag_class}">{plagiarism} Risk</div>
                                <div class="plagiarism-desc">{plag_desc}</div>
                            </div>
                        </div>
                        <p style="color: #64748b; font-size: 0.9rem; text-align: center; margin-top: 1rem;">
                            {originality}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # ===============================
                # STRENGTHS & RED FLAGS
                # ===============================
                col1, col2 = st.columns(2)
                
                with col1:
                    # Strengths
                    strengths = data.get("strengths", [])
                    if strengths:
                        strengths_html = "".join([f"""
                        <div style="display: flex; align-items: flex-start; gap: 12px; padding: 1rem;
                                    background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.2);
                                    border-radius: 12px; margin-bottom: 0.75rem;">
                            <span style="font-size: 1.25rem;">💪</span>
                            <span style="color: #94a3b8; font-size: 0.95rem; line-height: 1.5;">{s}</span>
                        </div>
                        """ for s in strengths])
                        
                        st.markdown(f"""
                        <div class="glass-card success-glow fade-in-up delay-5">
                            <div class="section-header">
                                <div class="section-icon" style="background: linear-gradient(135deg, #10b981, #059669);">💪</div>
                                <div>
                                    <h3 class="section-title">Content Strengths</h3>
                                    <p class="section-subtitle">Positive aspects identified</p>
                                </div>
                            </div>
                            {strengths_html}
                        </div>
                        """, unsafe_allow_html=True)
                
                with col2:
                    # Red Flags
                    red_flags = data.get("red_flags", [])
                    if red_flags:
                        flags_html = "".join([f"""
                        <div class="alert-card">
                            <div class="alert-icon">⚠️</div>
                            <div class="alert-text">{flag}</div>
                        </div>
                        """ for flag in red_flags])
                        
                        st.markdown(f"""
                        <div class="glass-card danger-glow fade-in-up delay-5">
                            <div class="section-header">
                                <div class="section-icon" style="background: linear-gradient(135deg, #ef4444, #dc2626);">🚩</div>
                                <div>
                                    <h3 class="section-title">Red Flags Detected</h3>
                                    <p class="section-subtitle">Potential issues to review</p>
                                </div>
                            </div>
                            {flags_html}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div class="glass-card success-glow fade-in-up delay-5">
                            <div style="text-align: center; padding: 2rem;">
                                <div style="font-size: 3rem; margin-bottom: 1rem;">✨</div>
                                <div style="font-size: 1.1rem; font-weight: 600; color: #10b981;">No Red Flags!</div>
                                <div style="color: #64748b; margin-top: 0.5rem;">Content appears clean</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Success Message
                st.markdown("""
                <div style="text-align: center; margin-top: 2rem; padding: 1.5rem;
                            background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(6, 182, 212, 0.1));
                            border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 16px;">
                    <span style="font-size: 1.5rem;">✅</span>
                    <span style="color: #10b981; font-weight: 600; margin-left: 10px;">
                        Comprehensive Analysis Complete!
                    </span>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.markdown(f"""
                <div class="glass-card danger-glow fade-in" style="text-align: center; padding: 2rem;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">❌</div>
                    <div style="font-size: 1.25rem; font-weight: 600; color: #ef4444; margin-bottom: 0.5rem;">
                        Analysis Error
                    </div>
                    <div style="color: #94a3b8; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem;
                                background: rgba(0,0,0,0.3); padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        {str(e)}
                    </div>
                </div>
                """, unsafe_allow_html=True)

# ===============================
# FOOTER
# ===============================
st.markdown("""
<div class="custom-footer fade-in">
    <div class="footer-brand">VerifyAI – Truth Lens</div>
    <div class="footer-tagline">Built with ❤️ for Hackathon 2025</div>
    <div style="margin-top: 1.5rem; display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
        <span style="padding: 6px 16px; background: rgba(99, 102, 241, 0.1); border: 1px solid rgba(99, 102, 241, 0.2);
                     border-radius: 20px; font-size: 0.8rem; color: #818cf8;">🐍 Python</span>
        <span style="padding: 6px 16px; background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.2);
                     border-radius: 20px; font-size: 0.8rem; color: #f87171;">🎈 Streamlit</span>
        <span style="padding: 6px 16px; background: rgba(6, 182, 212, 0.1); border: 1px solid rgba(6, 182, 212, 0.2);
                     border-radius: 20px; font-size: 0.8rem; color: #22d3ee;">🤖 Gemini AI</span>
    </div>
</div>
""", unsafe_allow_html=True)