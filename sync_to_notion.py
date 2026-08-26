"""
=============================================================================
NOTION PORTFOLIO SYNC ENGINE - PANDU JATI PAMUNGKAS
=============================================================================
Script ini mengotomasi pembuatan:
1. Halaman Utama Portfolio di Notion (Master Hub)
2. Database Proyek Interaktif (Board / Table / Gallery View Properties)
3. 10 Halaman Detail Studi Kasus Proyek beserta isinya ke dalam Database Notion

CARA PENGGUNAAN:
1. Buat Notion Internal Integration di https://www.notion.so/my-integrations
   - Salin "Internal Integration Secret" (contoh: secret_xxxxxx)
2. Buka workspace Notion Anda, buat sebuah Page kosong (misal: "My Portfolio Hub")
3. Klik titik tiga (...) di kanan atas page tersebut -> "Add connections" -> pilih Integration Anda.
4. Salin ID halaman tersebut dari URL Notion (32 karakter setelah nama halaman).
5. Jalankan script ini:
   python sync_to_notion.py
=============================================================================
"""

import os
import sys
import json
import urllib.request
import urllib.error

NOTION_VERSION = "2022-06-28"

def make_notion_request(endpoint, method="POST", data=None, api_key=""):
    url = f"https://api.notion.com/v1/{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION
    }
    encoded_data = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        print(f"[-] HTTP Error {e.code}: {err_msg}")
        return None
    except Exception as e:
        print(f"[-] Error: {str(e)}")
        return None

def create_notion_database(parent_page_id, api_key):
    print("[*] Creating Notion Database for Projects...")
    payload = {
        "parent": {"type": "page_id", "page_id": parent_page_id},
        "icon": {"type": "emoji", "emoji": "???"},
        "title": [{"type": "text", "text": {"content": "Projects & Portfolio Database"}}],
        "properties": {
            "Project Name": {"title": {}},
            "Category": {
                "select": {
                    "options": [
                        {"name": "AI & Computer Vision", "color": "blue"},
                        {"name": "Industrial IoT & Web ERP", "color": "purple"},
                        {"name": "Logistics & Mobile App", "color": "orange"},
                        {"name": "Full-Stack Web SaaS", "color": "green"},
                        {"name": "Quantitative Finance & Trading", "color": "yellow"},
                        {"name": "AI SaaS & Customer Support", "color": "pink"},
                        {"name": "Environmental Data Science", "color": "green"},
                        {"name": "AI Data Quality & QA", "color": "red"},
                        {"name": "Mobile Development", "color": "default"},
                        {"name": "AI Agents & Automation", "color": "gray"}
                    ]
                }
            },
            "Domain": {
                "select": {
                    "options": [
                        {"name": "Industrial AI & Safety", "color": "blue"},
                        {"name": "Industrial Operations & Maintenance", "color": "purple"},
                        {"name": "Industrial Logistics & Transportation", "color": "orange"},
                        {"name": "Hyperlocal Services Marketplace", "color": "green"},
                        {"name": "Algorithmic Trading & Commercial SaaS", "color": "yellow"},
                        {"name": "AI Customer Relationship Management", "color": "pink"},
                        {"name": "Industrial Environmental Compliance", "color": "green"},
                        {"name": "Computer Vision Data Engineering", "color": "red"},
                        {"name": "Fleet Logistics & Telemetry", "color": "default"},
                        {"name": "AI Agent Orchestration", "color": "gray"}
                    ]
                }
            },
            "Status": {
                "select": {
                    "options": [
                        {"name": "Production Ready", "color": "green"},
                        {"name": "Live Operational", "color": "green"},
                        {"name": "Production Deployment", "color": "blue"},
                        {"name": "Live MVP", "color": "yellow"},
                        {"name": "Production Commercial", "color": "purple"},
                        {"name": "Active Prototype", "color": "orange"},
                        {"name": "Pilot Verified", "color": "blue"},
                        {"name": "Production Completed", "color": "green"},
                        {"name": "Production Live", "color": "green"},
                        {"name": "Production Tooling", "color": "gray"}
                    ]
                }
            },
            "Tech Stack": {"multi_select": {}},
            "Key Metric / Impact": {"rich_text": {}},
            "GitHub Repo": {"url": {}},
            "Year": {"number": {"format": "number"}},
            "Featured": {"checkbox": {}}
        }
    }
    res = make_notion_request("databases", "POST", payload, api_key)
    if res and "id" in res:
        print(f"[+] Database created successfully with ID: {res['id']}")
        return res["id"]
    return None

def add_project_to_database(database_id, project, api_key):
    print(f"[*] Adding project: {project['name']}...")
    
    # Parse tech stack tags
    tech_tags = [{"name": tag.strip()[:100]} for tag in project["tech_stack"].split(",") if tag.strip()]
    
    payload = {
        "parent": {"database_id": database_id},
        "icon": {"type": "emoji", "emoji": project.get("emoji", "??")},
        "properties": {
            "Project Name": {
                "title": [{"type": "text", "text": {"content": project["name"]}}]
            },
            "Category": {
                "select": {"name": project["category"]}
            },
            "Domain": {
                "select": {"name": project["domain"]}
            },
            "Status": {
                "select": {"name": project["status"]}
            },
            "Tech Stack": {
                "multi_select": tech_tags[:10]  # Notion limit
            },
            "Key Metric / Impact": {
                "rich_text": [{"type": "text", "text": {"content": project["metric"]}}]
            },
            "GitHub Repo": {
                "url": project["github"] if project["github"].startswith("http") else None
            },
            "Year": {
                "number": project["year"]
            },
            "Featured": {
                "checkbox": project.get("featured", False)
            }
        },
        "children": [
            {
                "object": "block",
                "type": "callout",
                "callout": {
                    "rich_text": [{"type": "text", "text": {"content": f"Summary: {project['summary']}"}}],
                    "icon": {"emoji": "??"}
                }
            },
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": "Studi Kasus & Detail Arsitektur"}}]
                }
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": f"Lihat dokumentasi lengkap di file lokal projects/{project['file']}"}}]
                }
            }
        ]
    }
    
    res = make_notion_request("pages", "POST", payload, api_key)
    if res and "id" in res:
        print(f"[+] Page added for: {project['name']}")
        return res["id"]
    return None

def main():
    print("=" * 60)
    print(" NOTION PORTFOLIO SYNC - PANDU JATI PAMUNGKAS")
    print("=" * 60)
    
    api_key = os.environ.get("NOTION_API_KEY")
    parent_page_id = os.environ.get("NOTION_PAGE_ID")
    
    if not api_key:
        api_key = input("Masukkan NOTION_API_KEY (secret_...): ").strip()
    if not parent_page_id:
        parent_page_id = input("Masukkan NOTION_PAGE_ID (32 char ID): ").strip()
        
    if not api_key or not parent_page_id:
        print("[-] API Key dan Page ID dibutuhkan untuk eksekusi API.")
        return
        
    # Clean Page ID
    parent_page_id = parent_page_id.replace("-", "")
    
    db_id = create_notion_database(parent_page_id, api_key)
    if not db_id:
        print("[-] Gagal membuat database di Notion. Pastikan Integration sudah di-connect ke page target.")
        return
        
    projects = [
        {
            "name": "AI K3 Electrical Room Monitoring & Safety Alert",
            "emoji": "???",
            "category": "AI & Computer Vision",
            "domain": "Industrial AI & Safety",
            "status": "Production Ready",
            "tech_stack": "Python, FastAPI, YOLO11, SFace, ByteTrack, SQLite, Baileys WhatsApp",
            "metric": "Ensemble PPE, 128-D face biometrics, fall detection (38? spine), 32 automated unit tests",
            "github": "https://github.com/Pandujatip/ai-electrical-room-monitor",
            "year": 2026,
            "featured": True,
            "summary": "Smart CCTV video analytics system for electrical rooms with PPE compliance, smoking/fall alerts, and instant WhatsApp notifications with snapshots.",
            "file": "01_ai_electrical_room_monitor.md"
        },
        {
            "name": "PLIRM34 Web Aplikasi - Maintenance Management",
            "emoji": "?",
            "category": "Industrial IoT & Web ERP",
            "domain": "Industrial Operations & Maintenance",
            "status": "Live Operational",
            "tech_stack": "Python, Vanilla JS, SQLite, Spec-Driven Dev, RBAC",
            "metric": "Digitalized inspection for Raw Mill 3-4, dynamic Carbon Brush wear trending, threshold alarms for MV transformers",
            "github": "https://github.com/Pandujatip/PLIRM34-WEB-APLIKASI",
            "year": 2026,
            "featured": True,
            "summary": "Operational web platform for Raw Mill 3-4 electrical & instrumentation maintenance, spare-part management, and automated audit logging.",
            "file": "02_plirm34_web_aplikasi.md"
        },
        {
            "name": "SIGXPORT Reborn - Logistics & Port Management",
            "emoji": "??",
            "category": "Logistics & Mobile App",
            "domain": "Industrial Logistics & Transportation",
            "status": "Production Deployment",
            "tech_stack": "Node.js, Express, PostgreSQL, Kotlin Compose, PWA, PM2",
            "metric": "Real-time queue monitoring per loading point, ship telemetry, automated cron sync with legacy DB, Play Store AAB pipeline",
            "github": "https://github.com/Pandujatip/sigxport-web-reborn",
            "year": 2026,
            "featured": True,
            "summary": "Parallel dashboard, PWA, and native Android app for cement export dispatching, loading point queues, and third-party integration API.",
            "file": "03_sigxport_reborn.md"
        },
        {
            "name": "Berdikari Care / Saling Bantu Marketplace",
            "emoji": "??",
            "category": "Full-Stack Web SaaS",
            "domain": "Hyperlocal Services Marketplace",
            "status": "Live MVP",
            "tech_stack": "React 18, TypeScript, Vite, Node.js, Express, Prisma, DOKU",
            "metric": "3-role platform (Consumer/Mitra/Admin), automated escrow ledger, in-app masked chat, partner verification with PDF/images",
            "github": "https://github.com/Pandujatip/saling-bantu",
            "year": 2026,
            "featured": True,
            "summary": "Hyperlocal service marketplace MVP for Tuban regency covering home repairs, cleaning, laundry, vehicle maintenance with escrow payment flow.",
            "file": "04_berdikari_care_marketplace.md"
        },
        {
            "name": "Robot Financial Freedom - Algorithmic Crypto Bot",
            "emoji": "??",
            "category": "Quantitative Finance & Trading",
            "domain": "Algorithmic Trading & Commercial SaaS",
            "status": "Production Commercial",
            "tech_stack": "Python, CCXT, Binance API, Web Dashboard, PowerShell",
            "metric": "Auto-scanning 40+ USDT pairs, EMA/RSI momentum filter, dual engine (paper & live), commercial license key system",
            "github": "https://github.com/Pandujatip/publik-robot-financial-freedom",
            "year": 2026,
            "featured": True,
            "summary": "Automated crypto trading bot with real-time web telemetry, risk management (SL/TP/trailing), and proprietary licensed customer distribution.",
            "file": "05_robot_financial_freedom.md"
        },
        {
            "name": "AI Omnichannel CRM for Indonesian SMEs",
            "emoji": "??",
            "category": "AI SaaS & Customer Support",
            "domain": "AI Customer Relationship Management",
            "status": "Active Prototype",
            "tech_stack": "Next.js, React, TypeScript, Supabase, PostgreSQL RLS, Midtrans",
            "metric": "Unified WhatsApp + Instagram inbox, LLM auto-reply with strict business guardrails, multi-tenant workspace with RLS",
            "github": "https://github.com/Pandujatip",
            "year": 2026,
            "featured": False,
            "summary": "AI-powered omnichannel CRM unifying WhatsApp and Instagram messages with automated smart responses, product catalogue, and billing.",
            "file": "06_ai_omnichannel_crm.md"
        },
        {
            "name": "EP 343EP1 Pilot - Industrial Emission Analytics",
            "emoji": "??",
            "category": "Environmental Data Science",
            "domain": "Industrial Environmental Compliance",
            "status": "Pilot Verified",
            "tech_stack": "Python, DuckDB, Pandas, Scikit-learn, SQLAlchemy, OpenPyXL",
            "metric": "Real-time Electrostatic Precipitator emission tracking at Raw Mill Tuban 3 aligned with BNSP PPPU certification standards",
            "github": "https://github.com/Pandujatip",
            "year": 2026,
            "featured": False,
            "summary": "Data science and analytics pipeline for industrial emission monitoring and compliance of electrostatic precipitator systems.",
            "file": "07_ep_343ep1_pilot.md"
        },
        {
            "name": "Independent CVAT & Annotation QA Pipeline",
            "emoji": "???",
            "category": "AI Data Quality & QA",
            "domain": "Computer Vision Data Engineering",
            "status": "Production Completed",
            "tech_stack": "CVAT, YOLOv7 ONNX, Nuclio Serverless, Precision/Recall/F1",
            "metric": "End-to-end dataset curation, structured error taxonomy, IoU >= 0.50 automated evaluation",
            "github": "https://github.com/Pandujatip",
            "year": 2026,
            "featured": True,
            "summary": "Self-hosted CVAT computer vision annotation and QA pipeline with Nuclio serverless auto-labeling and rigorous error categorization.",
            "file": "08_cvat_annotation_qa_pipeline.md"
        },
        {
            "name": "GPS Truck SIG Mobile APK",
            "emoji": "??",
            "category": "Mobile Development",
            "domain": "Fleet Logistics & Telemetry",
            "status": "Production Live",
            "tech_stack": "Android Java, WebView, Gradle Portable, ProGuard",
            "metric": "Hardware sensor bindings (GPS, camera), ProGuard-optimized build, portable zero-dependency Windows build script",
            "github": "https://github.com/Pandujatip",
            "year": 2026,
            "featured": False,
            "summary": "Native Android tracking wrapper application with hardware permission bindings for cement logistics fleet drivers.",
            "file": "09_gpstruck_sig_apk.md"
        },
        {
            "name": "OpenClaw Infrastructure & AI Agent Bootstrap",
            "emoji": "??",
            "category": "AI Agents & Automation",
            "domain": "AI Agent Orchestration",
            "status": "Production Tooling",
            "tech_stack": "PowerShell, OpenAI Codex, ClawHub Skills",
            "metric": "Automated zero-token-leak provisioning for autonomous web agents with isolated browser profiles and host control",
            "github": "https://github.com/Pandujatip/openclaw-bootstrap",
            "year": 2026,
            "featured": False,
            "summary": "Reproducible infrastructure setup for deploying autonomous AI agents with headless/non-headless browser automation and skill orchestration.",
            "file": "10_openclaw_bootstrap_agent.md"
        }
    ]
    
    for p in projects:
        add_project_to_database(db_id, p, api_key)
        
    print("
" + "=" * 60)
    print(" [?] SEMUA PROYEK BERHASIL DI-SYNC KE NOTION DATABASE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
