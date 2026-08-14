#!/usr/bin/env python3
"""Replace the case studies section (lines ~2687-3044) with 5 new generic cases."""

import re

FILE = "/Users/yuxinyu/Desktop/lisa/0810第二个发布的版本/index.html"

with open(FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

content = "".join(lines)

# Find the exact boundaries
# Start: <div class="scenarios reveal"> after sec-tag area
# End: the </div> that closes scenarios reveal, before </section>
start_marker = '<div class="scenarios reveal">'
end_marker = '</section>\n\n<!-- ============ DEPLOYMENT & LICENSE ============ -->'

start_idx = content.index(start_marker)
end_idx = content.index(end_marker, start_idx)

# The end_marker includes the </div> and </section>; we replace up to just before </section>
# We want to replace from start_marker to the closing </div> of scenarios reveal
# Let's find the line numbers
start_line = content[:start_idx].count("\n") + 1
end_line = content[:end_idx].count("\n") + 1

print(f"Found section: lines {start_line}-{end_line}")

NEW_CASES = '''<div class="scenarios reveal">
    <div class="section-tabs" role="tablist" aria-label="客户案例">
      <button class="section-tab active" data-tab="case-1" role="tab"><span class="sn-n">01</span>案例一 · 工业质检 DFS</button>
      <button class="section-tab" data-tab="case-2" role="tab"><span class="sn-n">02</span>案例二 · 光学电子 DFS</button>
      <button class="section-tab" data-tab="case-3" role="tab"><span class="sn-n">03</span>案例三 · 异构存储生命周期</button>
      <button class="section-tab" data-tab="case-4" role="tab"><span class="sn-n">04</span>案例四 · AI 数据平台</button>
      <button class="section-tab" data-tab="case-5" role="tab"><span class="sn-n">05</span>案例五 · AI 智能数据治理</button>
    </div>

    <!-- ============ CASE 1: 工业质检 DFS ============ -->
    <div class="section-tab-panel active" data-panel="case-1">
    <div class="case">
      <h4>工业质检数据全生命周期治理</h4>
      <div class="pains">
        <div class="lab">客户痛点</div>
        <p>多存储集群并存数据查找困难；产线多变数据规范差；需按生命周期流转降本增效。</p>
      </div>
      <div class="pains">
        <div class="lab">LiSA 方案</div>
        <p>LiSA-DFS 统一纳管，文件/对象统一检索，智能 Agent 监控数据规范，按生命周期自动分层流转至低成本存储。</p>
      </div>
      <div class="case-arch">
        <div class="ttl">方案架构</div>
        <div class="scroll-x">
          <svg viewBox="-20 0 680 380" class="flow-svg" style="max-width:720px" xmlns="http://www.w3.org/2000/svg">
            <!-- ===== ROW 1: 用户 / Admin → LiSA-DFS ===== -->
            <g class="arch-svg-node">
              <circle cx="40" cy="46" r="14" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)" stroke-width="1.3"/>
              <circle cx="40" cy="46" r="6" fill="none" stroke="var(--cyan)" stroke-width="1.3"/>
              <line x1="44" y1="50" x2="50" y2="56" stroke="var(--cyan)" stroke-width="1.3" stroke-linecap="round"/>
            </g>
            <g class="arch-svg-node">
              <circle cx="82" cy="46" r="14" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)" stroke-width="1.3"/>
              <circle cx="82" cy="46" r="6" fill="none" stroke="var(--cyan)" stroke-width="1.3"/>
              <line x1="86" y1="50" x2="92" y2="56" stroke="var(--cyan)" stroke-width="1.3" stroke-linecap="round"/>
            </g>
            <text x="60" y="74" text-anchor="middle" font-size="8" fill="#9aa3c4" font-family="JetBrains Mono">Admin / Users</text>

            <line x1="100" y1="46" x2="180" y2="46" stroke="var(--cyan)" stroke-width="1.2" stroke-dasharray="3 3" class="flow-line"/>
            <circle cx="100" cy="46" r="3" class="pulse-node" fill="var(--cyan)"/>
            <circle cx="180" cy="46" r="3" class="pulse-node" fill="var(--cyan)"/>

            <!-- LiSA-DFS Platform -->
            <rect x="190" y="20" width="450" height="160" rx="10" fill="rgba(var(--cyan-rgb),.1)" stroke="var(--cyan)" stroke-width="1.3" stroke-dasharray="4 3"/>
            <text x="415" y="42" text-anchor="middle" font-size="13" fill="#eef2ff" font-weight="700" letter-spacing="2">LiSA-DFS Platform</text>

            <!-- Module chips Row 1 -->
            <g class="arch-svg-node"><rect x="208" y="52" width="90" height="22" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="253" y="67" text-anchor="middle" font-size="8" fill="#3df0ff">Agent Management</text></g>
            <g class="arch-svg-node"><rect x="304" y="52" width="80" height="22" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="344" y="67" text-anchor="middle" font-size="8" fill="#3df0ff">Advanced Search</text></g>
            <g class="arch-svg-node"><rect x="390" y="52" width="72" height="22" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="426" y="67" text-anchor="middle" font-size="8" fill="#3df0ff">Batch Download</text></g>
            <g class="arch-svg-node"><rect x="468" y="52" width="68" height="22" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="502" y="67" text-anchor="middle" font-size="8" fill="#3df0ff">Image Compress</text></g>
            <g class="arch-svg-node"><rect x="540" y="52" width="84" height="22" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="582" y="67" text-anchor="middle" font-size="8" fill="#3df0ff">Thumbnail Browse</text></g>

            <!-- Module chips Row 2 -->
            <g class="arch-svg-node"><rect x="208" y="80" width="84" height="22" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="250" y="95" text-anchor="middle" font-size="8" fill="#3df0ff">Image Watermark</text></g>
            <g class="arch-svg-node"><rect x="298" y="80" width="72" height="22" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="334" y="95" text-anchor="middle" font-size="8" fill="#3df0ff">Tag Scanning</text></g>
            <g class="arch-svg-node"><rect x="376" y="80" width="76" height="22" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="414" y="95" text-anchor="middle" font-size="8" fill="#3df0ff">Lifecycle</text></g>
            <g class="arch-svg-node"><rect x="458" y="80" width="82" height="22" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="499" y="95" text-anchor="middle" font-size="8" fill="#3df0ff">Permission Mgmt</text></g>
            <g class="arch-svg-node"><rect x="546" y="80" width="80" height="22" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="586" y="95" text-anchor="middle" font-size="8" fill="#3df0ff">Storage Resource</text></g>

            <!-- Engines Row 3 -->
            <g class="arch-svg-node"><rect x="208" y="110" width="108" height="22" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="262" y="125" text-anchor="middle" font-size="8" fill="#8b7bff">Intelligent Label Engine</text></g>
            <g class="arch-svg-node"><rect x="322" y="110" width="92" height="22" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="368" y="125" text-anchor="middle" font-size="8" fill="#8b7bff">Monitor Engine</text></g>
            <g class="arch-svg-node"><rect x="420" y="110" width="108" height="22" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="474" y="125" text-anchor="middle" font-size="8" fill="#8b7bff">Migration Engine</text></g>
            <g class="arch-svg-node"><rect x="532" y="110" width="92" height="22" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="578" y="125" text-anchor="middle" font-size="8" fill="#8b7bff">Image Proc Engine</text></g>

            <!-- Bottom: Metadata Engine -->
            <rect x="208" y="142" width="416" height="30" rx="6" fill="rgba(139,123,255,.15)" stroke="rgba(139,123,255,.6)" stroke-width="1"/>
            <text x="416" y="161" text-anchor="middle" font-size="10" fill="#8b7bff" font-weight="700" letter-spacing="2">Metadata Engine</text>

            <!-- ===== ROW 2: Storage Pools ===== -->
            <rect x="30" y="210" width="290" height="56" rx="8" fill="rgba(245,200,122,.05)" stroke="rgba(245,200,122,.4)" stroke-dasharray="4 3"/>
            <text x="175" y="234" text-anchor="middle" font-size="10" fill="#f5c87a" font-weight="600">DXN Archive Object Pool</text>
            <text x="175" y="250" text-anchor="middle" font-size="8" fill="#9aa3c4" font-family="JetBrains Mono">低成本归档 · 海量对象存储</text>

            <rect x="350" y="210" width="290" height="56" rx="8" fill="rgba(245,200,122,.05)" stroke="rgba(245,200,122,.4)" stroke-dasharray="4 3"/>
            <text x="495" y="234" text-anchor="middle" font-size="10" fill="#f5c87a" font-weight="600">DXN High-Performance File Pool</text>
            <text x="495" y="250" text-anchor="middle" font-size="8" fill="#9aa3c4" font-family="JetBrains Mono">高性能文件 · 产线直连</text>

            <!-- Connection: LiSA → Storage Pools -->
            <path d="M415 180 L175 210" stroke="var(--cyan)" stroke-width="1.3" class="flow-line" fill="none"/>
            <path d="M415 180 L495 210" stroke="var(--cyan)" stroke-width="1.3" class="flow-line" fill="none"/>

            <!-- Lifecycle task arrow -->
            <path d="M320 238 L350 238" stroke="var(--gold)" stroke-width="1.5" fill="none" class="flow-line" stroke-dasharray="4 3"/>
            <text x="335" y="230" text-anchor="middle" font-size="8" fill="#f5c87a" font-family="JetBrains Mono">Lifecycle</text>

            <!-- ===== ROW 3: Agents → Old Equipment ===== -->
            <rect x="30" y="300" width="180" height="44" rx="8" fill="rgba(var(--cyan-rgb),.08)" stroke="var(--cyan)" stroke-dasharray="4 3"/>
            <g class="arch-svg-node">
              <circle cx="55" cy="322" r="8" fill="rgba(var(--cyan-rgb),.15)" stroke="var(--cyan)"/>
              <rect x="68" y="314" width="30" height="16" rx="2" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/>
              <rect x="104" y="314" width="30" height="16" rx="2" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/>
              <rect x="140" y="314" width="30" height="16" rx="2" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/>
            </g>
            <text x="120" y="338" text-anchor="middle" font-size="8" fill="#3df0ff">LiSA Agents</text>

            <line x1="210" y1="322" x2="280" y2="322" stroke="var(--cyan)" stroke-width="1.2" stroke-dasharray="3 3" class="flow-line"/>
            <circle cx="210" cy="322" r="3" class="pulse-node" fill="var(--cyan)"/>

            <rect x="280" y="308" width="130" height="28" rx="6" fill="rgba(245,200,122,.08)" stroke="rgba(245,200,122,.4)"/>
            <text x="345" y="326" text-anchor="middle" font-size="10" fill="#f5c87a" font-weight="600">Old Equipment CIFS</text>

            <!-- Connection: Storage → Agents -->
            <path d="M175 266 L175 300 L120 300 L120 308" stroke="var(--cyan)" stroke-width="1.1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M495 266 L495 344 L210 344 L210 322" stroke="var(--cyan)" stroke-width="1.1" class="flow-line" fill="none" stroke-dasharray="3 3"/>

            <!-- Flow particles -->
            <circle class="flow-particle"><animateMotion dur="3s" repeatCount="indefinite" path="M100 46 L180 46"/></circle>
            <circle class="flow-particle"><animateMotion dur="3s" repeatCount="indefinite" begin=".5s" path="M180 46 L190 46 L253 63"/></circle>
            <circle class="flow-particle"><animateMotion dur="4s" repeatCount="indefinite" begin="0s" path="M415 180 L175 210"/></circle>
            <circle class="flow-particle"><animateMotion dur="4s" repeatCount="indefinite" begin="1s" path="M415 180 L495 210"/></circle>
            <circle class="flow-particle"><animateMotion dur="3.5s" repeatCount="indefinite" begin="0s" path="M320 238 L350 238"/></circle>
            <circle class="flow-particle"><animateMotion dur="5s" repeatCount="indefinite" begin=".8s" path="M175 266 L175 300 L120 300 L120 308"/></circle>
            <circle class="flow-particle"><animateMotion dur="5s" repeatCount="indefinite" begin="1.5s" path="M495 266 L495 344 L210 344 L210 322"/></circle>
            <circle class="flow-particle"><animateMotion dur="3s" repeatCount="indefinite" begin="0s" path="M210 322 L280 322"/></circle>
          </svg>
        </div>
      </div>
    </div>
    </div>

    <!-- ============ CASE 2: 光学电子 DFS ============ -->
    <div class="section-tab-panel" data-panel="case-2">
    <div class="case">
      <h4>光学电子多机台数据统一管理</h4>
      <div class="pains">
        <div class="lab">客户痛点</div>
        <p>历史数据杂乱查找困难；多机台数据无法统一检索；影像文件需长期留存。</p>
      </div>
      <div class="pains">
        <div class="lab">LiSA 方案</div>
        <p>LiSA-DFS 智能标签解析元数据，汇总所有存储统一检索；定时增量迁移与健康监控。</p>
      </div>
      <div class="case-arch">
        <div class="ttl">方案架构</div>
        <div class="scroll-x">
          <svg viewBox="-20 0 640 300" class="flow-svg" style="max-width:680px" xmlns="http://www.w3.org/2000/svg">
            <!-- ===== ROW 1: Admin + Users → LiSA-DFS ===== -->
            <g class="arch-svg-node">
              <circle cx="40" cy="40" r="14" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)" stroke-width="1.3"/>
              <circle cx="40" cy="40" r="6" fill="none" stroke="var(--cyan)" stroke-width="1.3"/>
              <line x1="44" y1="44" x2="50" y2="50" stroke="var(--cyan)" stroke-width="1.3" stroke-linecap="round"/>
            </g>
            <g class="arch-svg-node">
              <circle cx="80" cy="40" r="14" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)" stroke-width="1.3"/>
              <circle cx="80" cy="40" r="6" fill="none" stroke="var(--cyan)" stroke-width="1.3"/>
              <line x1="84" y1="44" x2="90" y2="50" stroke="var(--cyan)" stroke-width="1.3" stroke-linecap="round"/>
            </g>
            <text x="60" y="68" text-anchor="middle" font-size="8" fill="#9aa3c4" font-family="JetBrains Mono">Admin / Users</text>

            <line x1="96" y1="40" x2="180" y2="40" stroke="var(--cyan)" stroke-width="1.2" stroke-dasharray="3 3" class="flow-line"/>

            <!-- LiSA-DFS -->
            <rect x="190" y="16" width="410" height="100" rx="10" fill="rgba(var(--cyan-rgb),.1)" stroke="var(--cyan)" stroke-width="1.3" stroke-dasharray="4 3"/>
            <text x="395" y="36" text-anchor="middle" font-size="12" fill="#eef2ff" font-weight="700" letter-spacing="2">LiSA-DFS</text>

            <!-- Module chips -->
            <g class="arch-svg-node"><rect x="208" y="44" width="84" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="250" y="58" text-anchor="middle" font-size="8" fill="#3df0ff">Agent Management</text></g>
            <g class="arch-svg-node"><rect x="298" y="44" width="84" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="340" y="58" text-anchor="middle" font-size="8" fill="#3df0ff">Advanced Search</text></g>
            <g class="arch-svg-node"><rect x="388" y="44" width="80" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="428" y="58" text-anchor="middle" font-size="8" fill="#3df0ff">Tag Scanning</text></g>
            <g class="arch-svg-node"><rect x="474" y="44" width="108" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="528" y="58" text-anchor="middle" font-size="8" fill="#3df0ff">Lifecycle Management</text></g>

            <g class="arch-svg-node"><rect x="208" y="70" width="100" height="20" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="258" y="84" text-anchor="middle" font-size="8" fill="#8b7bff">Metadata Engine</text></g>
            <g class="arch-svg-node"><rect x="314" y="70" width="92" height="20" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="360" y="84" text-anchor="middle" font-size="8" fill="#8b7bff">Monitor Engine</text></g>
            <g class="arch-svg-node"><rect x="412" y="70" width="92" height="20" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="458" y="84" text-anchor="middle" font-size="8" fill="#8b7bff">Migration Engine</text></g>
            <g class="arch-svg-node"><rect x="510" y="70" width="72" height="20" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="546" y="84" text-anchor="middle" font-size="8" fill="#8b7bff">Permission</text></g>

            <!-- ===== ROW 2: Storage Migration ===== -->
            <g class="arch-svg-node">
              <rect x="40" y="168" width="140" height="56" rx="8" fill="rgba(245,200,122,.06)" stroke="rgba(245,200,122,.45)" stroke-width="1"/>
              <text x="110" y="190" text-anchor="middle" font-size="10" fill="#f5c87a" font-weight="600">H3C X1000</text>
              <text x="110" y="206" text-anchor="middle" font-size="8" fill="#9aa3c4" font-family="JetBrains Mono">历史存储</text>
            </g>

            <g class="arch-svg-node">
              <rect x="460" y="168" width="140" height="56" rx="8" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)" stroke-width="1"/>
              <text x="530" y="190" text-anchor="middle" font-size="10" fill="#8b7bff" font-weight="600">NetApp FAS50</text>
              <text x="530" y="206" text-anchor="middle" font-size="8" fill="#9aa3c4" font-family="JetBrains Mono">新存储 · 长期留存</text>
            </g>

            <!-- Migration arrow -->
            <path d="M180 196 L460 196" stroke="var(--gold)" stroke-width="1.5" fill="none" class="flow-line" stroke-dasharray="6 4"/>
            <text x="320" y="188" text-anchor="middle" font-size="8" fill="#f5c87a" font-family="JetBrains Mono">定时增量迁移</text>

            <!-- LiSA → storage connections -->
            <path d="M395 116 Q250 140 110 168" stroke="var(--cyan)" stroke-width="1.2" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M395 116 Q500 140 530 168" stroke="var(--cyan)" stroke-width="1.2" class="flow-line" fill="none" stroke-dasharray="3 3"/>

            <!-- ===== Bottom: LiSA Agents ===== -->
            <rect x="200" y="246" width="240" height="36" rx="8" fill="rgba(var(--cyan-rgb),.08)" stroke="var(--cyan)" stroke-dasharray="4 3"/>
            <g class="arch-svg-node">
              <circle cx="224" cy="264" r="7" fill="rgba(var(--cyan-rgb),.15)" stroke="var(--cyan)"/>
              <rect x="238" y="256" width="24" height="14" rx="2" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/>
              <rect x="268" y="256" width="24" height="14" rx="2" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/>
              <rect x="298" y="256" width="24" height="14" rx="2" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/>
              <text x="370" y="268" text-anchor="middle" font-size="9" fill="#3df0ff">LiSA Agents</text>
            </g>

            <!-- Agent connections -->
            <path d="M110 224 Q180 240 260 246" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M530 224 Q480 240 420 246" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>

            <!-- Flow particles -->
            <circle class="flow-particle"><animateMotion dur="3s" repeatCount="indefinite" path="M96 40 L180 40"/></circle>
            <circle class="flow-particle"><animateMotion dur="3.5s" repeatCount="indefinite" begin=".5s" path="M395 116 Q250 140 110 168"/></circle>
            <circle class="flow-particle"><animateMotion dur="3.5s" repeatCount="indefinite" begin="1s" path="M395 116 Q500 140 530 168"/></circle>
            <circle class="flow-particle"><animateMotion dur="4s" repeatCount="indefinite" begin="0s" path="M180 196 L460 196"/></circle>
            <circle class="flow-particle"><animateMotion dur="4.5s" repeatCount="indefinite" begin=".5s" path="M110 224 Q180 240 260 246"/></circle>
            <circle class="flow-particle"><animateMotion dur="4.5s" repeatCount="indefinite" begin="1.5s" path="M530 224 Q480 240 420 246"/></circle>
          </svg>
        </div>
      </div>
    </div>
    </div>

    <!-- ============ CASE 3: 异构存储生命周期 ============ -->
    <div class="section-tab-panel" data-panel="case-3">
    <div class="case">
      <h4>异构平台数据生命周期统一管理</h4>
      <div class="pains">
        <div class="lab">客户痛点</div>
        <p>多品牌存储并存管理割裂；老设备数据无统一视图；需跨设备按标签快速检索。</p>
      </div>
      <div class="pains">
        <div class="lab">LiSA 方案</div>
        <p>LiSA-Lifecycle Management 统一纳管，跨厂商元数据统一视图，标签驱动快速检索。</p>
      </div>
      <div class="case-arch">
        <div class="ttl">方案架构</div>
        <div class="scroll-x">
          <svg viewBox="-20 0 680 280" class="flow-svg" style="max-width:720px" xmlns="http://www.w3.org/2000/svg">
            <!-- ===== ROW 1: Admin + Users → LiSA-Lifecycle ===== -->
            <g class="arch-svg-node">
              <circle cx="40" cy="40" r="14" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)" stroke-width="1.3"/>
              <circle cx="40" cy="40" r="6" fill="none" stroke="var(--cyan)" stroke-width="1.3"/>
              <line x1="44" y1="44" x2="50" y2="50" stroke="var(--cyan)" stroke-width="1.3" stroke-linecap="round"/>
            </g>
            <g class="arch-svg-node">
              <circle cx="80" cy="40" r="14" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)" stroke-width="1.3"/>
              <circle cx="80" cy="40" r="6" fill="none" stroke="var(--cyan)" stroke-width="1.3"/>
              <line x1="84" y1="44" x2="90" y2="50" stroke="var(--cyan)" stroke-width="1.3" stroke-linecap="round"/>
            </g>
            <text x="60" y="68" text-anchor="middle" font-size="8" fill="#9aa3c4" font-family="JetBrains Mono">Admin / Users</text>

            <line x1="96" y1="40" x2="180" y2="40" stroke="var(--cyan)" stroke-width="1.2" stroke-dasharray="3 3" class="flow-line"/>

            <!-- LiSA-Lifecycle Management -->
            <rect x="190" y="16" width="450" height="96" rx="10" fill="rgba(var(--cyan-rgb),.1)" stroke="var(--cyan)" stroke-width="1.3" stroke-dasharray="4 3"/>
            <text x="415" y="36" text-anchor="middle" font-size="12" fill="#eef2ff" font-weight="700" letter-spacing="2">LiSA-Lifecycle Management</text>

            <!-- Modules -->
            <g class="arch-svg-node"><rect x="208" y="44" width="96" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="256" y="58" text-anchor="middle" font-size="8" fill="#3df0ff">Agent Mgmt</text></g>
            <g class="arch-svg-node"><rect x="310" y="44" width="80" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="350" y="58" text-anchor="middle" font-size="8" fill="#3df0ff">Search</text></g>
            <g class="arch-svg-node"><rect x="396" y="44" width="112" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="452" y="58" text-anchor="middle" font-size="8" fill="#3df0ff">Lifecycle Mgmt</text></g>
            <g class="arch-svg-node"><rect x="514" y="44" width="116" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="572" y="58" text-anchor="middle" font-size="8" fill="#3df0ff">Permission Mgmt</text></g>

            <g class="arch-svg-node"><rect x="208" y="70" width="140" height="20" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="278" y="84" text-anchor="middle" font-size="8" fill="#8b7bff">Storage Resource Mgmt</text></g>
            <g class="arch-svg-node"><rect x="354" y="70" width="290" height="20" rx="4" fill="rgba(139,123,255,.15)" stroke="rgba(139,123,255,.6)"/><text x="499" y="84" text-anchor="middle" font-size="8" fill="#8b7bff" font-weight="600">Metadata Engine (统一跨厂商元数据视图)</text></g>

            <!-- ===== ROW 2: Storage Systems ===== -->
            <!-- NetApp A400 (old) -->
            <g class="arch-svg-node">
              <rect x="30" y="150" width="160" height="56" rx="8" fill="rgba(245,200,122,.06)" stroke="rgba(245,200,122,.45)" stroke-width="1"/>
              <text x="110" y="174" text-anchor="middle" font-size="10" fill="#f5c87a" font-weight="600">NetApp A400</text>
              <text x="110" y="192" text-anchor="middle" font-size="8" fill="#9aa3c4" font-family="JetBrains Mono">老旧存储</text>
            </g>

            <!-- Competitor VNX/Unity -->
            <g class="arch-svg-node">
              <rect x="260" y="150" width="160" height="56" rx="8" fill="rgba(245,200,122,.06)" stroke="rgba(245,200,122,.45)" stroke-width="1"/>
              <text x="340" y="174" text-anchor="middle" font-size="10" fill="#f5c87a" font-weight="600">Competitor VNX/Unity</text>
              <text x="340" y="192" text-anchor="middle" font-size="8" fill="#9aa3c4" font-family="JetBrains Mono">异构存储</text>
            </g>

            <!-- NetApp AFF A30 (new) -->
            <g class="arch-svg-node">
              <rect x="490" y="150" width="160" height="56" rx="8" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)" stroke-width="1"/>
              <text x="570" y="174" text-anchor="middle" font-size="10" fill="#8b7bff" font-weight="600">NetApp AFF A30</text>
              <text x="570" y="192" text-anchor="middle" font-size="8" fill="#9aa3c4" font-family="JetBrains Mono">新存储 · 最新1Y数据</text>
            </g>

            <!-- Migration arrow for latest 1Y -->
            <path d="M420 178 L490 178" stroke="var(--gold)" stroke-width="1.5" fill="none" class="flow-line" stroke-dasharray="6 4"/>
            <text x="455" y="170" text-anchor="middle" font-size="8" fill="#f5c87a" font-family="JetBrains Mono">最新1Y迁移</text>

            <!-- LiSA → storage connections -->
            <path d="M415 112 Q200 130 110 150" stroke="var(--cyan)" stroke-width="1.2" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M415 112 Q340 130 340 150" stroke="var(--cyan)" stroke-width="1.2" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M415 112 Q500 130 570 150" stroke="var(--cyan)" stroke-width="1.2" class="flow-line" fill="none" stroke-dasharray="3 3"/>

            <!-- ===== Bottom: LiSA Agents ===== -->
            <rect x="220" y="232" width="240" height="36" rx="8" fill="rgba(var(--cyan-rgb),.08)" stroke="var(--cyan)" stroke-dasharray="4 3"/>
            <g class="arch-svg-node">
              <circle cx="244" cy="250" r="7" fill="rgba(var(--cyan-rgb),.15)" stroke="var(--cyan)"/>
              <rect x="258" y="242" width="24" height="14" rx="2" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/>
              <rect x="288" y="242" width="24" height="14" rx="2" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/>
              <rect x="318" y="242" width="24" height="14" rx="2" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/>
              <rect x="348" y="242" width="24" height="14" rx="2" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/>
              <text x="380" y="254" text-anchor="middle" font-size="9" fill="#3df0ff">LiSA Agents</text>
            </g>

            <!-- Agent connections to storage -->
            <path d="M110 206 Q160 224 260 232" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M340 206 Q330 224 340 232" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M570 206 Q500 224 440 232" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>

            <!-- Flow particles -->
            <circle class="flow-particle"><animateMotion dur="3s" repeatCount="indefinite" path="M96 40 L180 40"/></circle>
            <circle class="flow-particle"><animateMotion dur="4s" repeatCount="indefinite" begin="0s" path="M415 112 Q200 130 110 150"/></circle>
            <circle class="flow-particle"><animateMotion dur="4s" repeatCount="indefinite" begin=".7s" path="M415 112 Q340 130 340 150"/></circle>
            <circle class="flow-particle"><animateMotion dur="4s" repeatCount="indefinite" begin="1.3s" path="M415 112 Q500 130 570 150"/></circle>
            <circle class="flow-particle"><animateMotion dur="3.5s" repeatCount="indefinite" begin="0s" path="M420 178 L490 178"/></circle>
            <circle class="flow-particle"><animateMotion dur="5s" repeatCount="indefinite" begin=".5s" path="M110 206 Q160 224 260 232"/></circle>
            <circle class="flow-particle"><animateMotion dur="5s" repeatCount="indefinite" begin="1.5s" path="M570 206 Q500 224 440 232"/></circle>
          </svg>
        </div>
      </div>
    </div>
    </div>

    <!-- ============ CASE 4: AI 数据平台 ============ -->
    <div class="section-tab-panel" data-panel="case-4">
    <div class="case">
      <h4>AI 数据平台参考架构</h4>
      <div class="pains">
        <div class="lab">客户痛点</div>
        <p>AI 训练数据规模大管理复杂；多模态数据需统一纳管；AI 流水线与存储层割裂。</p>
      </div>
      <div class="pains">
        <div class="lab">LiSA 方案</div>
        <p>AI Data Platform 整合矩阵智能框架 + 加速基础设施 + LiSA 数据管理，提供 AI Ready 数据管道。</p>
      </div>
      <div class="case-arch">
        <div class="ttl">方案架构</div>
        <div class="scroll-x">
          <svg viewBox="-30 0 720 360" class="flow-svg" style="max-width:760px" xmlns="http://www.w3.org/2000/svg">
            <!-- ===== ROW 1: Client → Agent → IAM ===== -->
            <g class="arch-svg-node">
              <rect x="30" y="20" width="72" height="30" rx="5" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="66" y="40" text-anchor="middle" font-size="8" fill="#3df0ff">Client Apps</text>
            </g>
            <g class="arch-svg-node">
              <rect x="140" y="20" width="130" height="30" rx="5" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="205" y="40" text-anchor="middle" font-size="8" fill="#3df0ff">Agent (Prompt/Response)</text>
            </g>
            <g class="arch-svg-node">
              <rect x="300" y="20" width="150" height="30" rx="5" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="375" y="40" text-anchor="middle" font-size="8" fill="#3df0ff">Identity & Access Mgmt</text>
            </g>

            <line x1="102" y1="35" x2="140" y2="35" stroke="var(--cyan)" stroke-width="1.2" stroke-dasharray="3 3" class="flow-line"/>
            <line x1="270" y1="35" x2="300" y2="35" stroke="var(--cyan)" stroke-width="1.2" stroke-dasharray="3 3" class="flow-line"/>

            <!-- ===== ROW 2: AI Data Platform ===== -->
            <!-- MatrixOne Intelligence -->
            <rect x="20" y="80" width="210" height="160" rx="8" fill="rgba(var(--cyan-rgb),.08)" stroke="var(--cyan)" stroke-width="1" stroke-dasharray="4 3"/>
            <text x="125" y="100" text-anchor="middle" font-size="10" fill="#3df0ff" font-weight="700">MatrixOne Intelligence</text>
            <g class="arch-svg-node"><rect x="36" y="108" width="180" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="126" y="122" text-anchor="middle" font-size="8" fill="#3df0ff">Multimodal Data Pipeline</text></g>
            <g class="arch-svg-node"><rect x="36" y="134" width="180" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="126" y="148" text-anchor="middle" font-size="8" fill="#3df0ff">Document Intelligences</text></g>
            <g class="arch-svg-node"><rect x="36" y="160" width="180" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="126" y="174" text-anchor="middle" font-size="8" fill="#3df0ff">Data Synthesize</text></g>
            <g class="arch-svg-node"><rect x="36" y="186" width="180" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="126" y="200" text-anchor="middle" font-size="8" fill="#3df0ff">Agentic ETL</text></g>
            <g class="arch-svg-node"><rect x="36" y="212" width="180" height="20" rx="4" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="126" y="226" text-anchor="middle" font-size="8" fill="#3df0ff">Connector</text></g>

            <!-- NeMo Models -->
            <rect x="260" y="80" width="200" height="160" rx="8" fill="rgba(139,123,255,.08)" stroke="rgba(139,123,255,.5)" stroke-width="1" stroke-dasharray="4 3"/>
            <text x="360" y="100" text-anchor="middle" font-size="10" fill="#8b7bff" font-weight="700">NeMo Models</text>
            <g class="arch-svg-node"><rect x="276" y="108" width="168" height="20" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="360" y="122" text-anchor="middle" font-size="8" fill="#8b7bff">LLM Inference</text></g>
            <g class="arch-svg-node"><rect x="276" y="134" width="168" height="20" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="360" y="148" text-anchor="middle" font-size="8" fill="#8b7bff">NeMo RL</text></g>
            <g class="arch-svg-node"><rect x="276" y="160" width="168" height="20" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="360" y="174" text-anchor="middle" font-size="8" fill="#8b7bff">cuVS Index</text></g>
            <g class="arch-svg-node"><rect x="276" y="186" width="168" height="20" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="360" y="200" text-anchor="middle" font-size="8" fill="#8b7bff">NV Embed Embedding</text></g>
            <g class="arch-svg-node"><rect x="276" y="212" width="168" height="20" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="360" y="226" text-anchor="middle" font-size="8" fill="#8b7bff">NeMo Parse</text></g>

            <!-- Accelerated Infrastructure -->
            <rect x="490" y="80" width="180" height="80" rx="8" fill="rgba(245,200,122,.06)" stroke="rgba(245,200,122,.45)" stroke-width="1" stroke-dasharray="4 3"/>
            <text x="580" y="100" text-anchor="middle" font-size="10" fill="#f5c87a" font-weight="700">Accelerated Infra</text>
            <g class="arch-svg-node"><rect x="508" y="108" width="70" height="20" rx="4" fill="rgba(245,200,122,.12)" stroke="rgba(245,200,122,.45)"/><text x="543" y="122" text-anchor="middle" font-size="8" fill="#f5c87a">GPU</text></g>
            <g class="arch-svg-node"><rect x="586" y="108" width="70" height="20" rx="4" fill="rgba(245,200,122,.12)" stroke="rgba(245,200,122,.45)"/><text x="621" y="122" text-anchor="middle" font-size="8" fill="#f5c87a">Network</text></g>
            <g class="arch-svg-node"><rect x="508" y="134" width="148" height="20" rx="4" fill="rgba(245,200,122,.12)" stroke="rgba(245,200,122,.45)"/><text x="582" y="148" text-anchor="middle" font-size="8" fill="#f5c87a">Storage</text></g>

            <!-- Row 1 → Row 2 connections -->
            <path d="M205 50 Q205 70 125 80" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M375 50 Q375 70 360 80" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M375 50 Q480 70 580 80" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>

            <!-- Intelligence → NeMo connections -->
            <line x1="230" y1="160" x2="260" y2="160" stroke="var(--cyan)" stroke-width="1.2" class="flow-line" stroke-dasharray="3 3"/>
            <!-- NeMo → Infra -->
            <line x1="460" y1="120" x2="490" y2="120" stroke="var(--cyan)" stroke-width="1.2" class="flow-line" stroke-dasharray="3 3"/>

            <!-- ===== ROW 3: Storage ===== -->
            <!-- Search & ETL row -->
            <rect x="20" y="270" width="650" height="28" rx="6" fill="rgba(var(--cyan-rgb),.06)" stroke="rgba(var(--cyan-rgb),.3)" stroke-dasharray="3 3"/>
            <g class="arch-svg-node"><rect x="34" y="274" width="120" height="20" rx="3" fill="rgba(var(--cyan-rgb),.1)" stroke="var(--cyan)"/><text x="94" y="288" text-anchor="middle" font-size="8" fill="#3df0ff">Semantic Search</text></g>
            <g class="arch-svg-node"><rect x="170" y="274" width="118" height="20" rx="3" fill="rgba(var(--cyan-rgb),.1)" stroke="var(--cyan)"/><text x="229" y="288" text-anchor="middle" font-size="8" fill="#3df0ff">Keyword Search</text></g>
            <g class="arch-svg-node"><rect x="304" y="274" width="120" height="20" rx="3" fill="rgba(var(--cyan-rgb),.1)" stroke="var(--cyan)"/><text x="364" y="288" text-anchor="middle" font-size="8" fill="#3df0ff">Agentic ETL</text></g>

            <!-- MatrixOne Storage -->
            <rect x="20" y="308" width="340" height="40" rx="8" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.55)" stroke-width="1"/>
            <text x="190" y="324" text-anchor="middle" font-size="10" fill="#8b7bff" font-weight="700">MatrixOne Storage</text>
            <text x="190" y="340" text-anchor="middle" font-size="7" fill="#9aa3c4" font-family="JetBrains Mono">Vector Data · Feature/Parquet · Object Storage · Document Metadata · Data Lakehouse</text>

            <!-- LiSA Server/Component -->
            <rect x="410" y="308" width="130" height="40" rx="8" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)" stroke-width="1"/>
            <text x="475" y="324" text-anchor="middle" font-size="9" fill="#3df0ff" font-weight="700">LiSA Server</text>
            <text x="475" y="338" text-anchor="middle" font-size="7" fill="#9aa3c4" font-family="JetBrains Mono">Component</text>

            <!-- External Object/File Storage -->
            <rect x="560" y="308" width="110" height="40" rx="8" fill="rgba(245,200,122,.08)" stroke="rgba(245,200,122,.4)" stroke-dasharray="4 3"/>
            <text x="615" y="324" text-anchor="middle" font-size="9" fill="#f5c87a" font-weight="600">External</text>
            <text x="615" y="338" text-anchor="middle" font-size="7" fill="#9aa3c4" font-family="JetBrains Mono">Object/File Storage</text>

            <!-- Metadata Monitoring API -->
            <rect x="20" y="354" width="200" height="14" rx="4" fill="rgba(139,123,255,.12)" stroke="rgba(139,123,255,.4)"/>
            <text x="120" y="364" text-anchor="middle" font-size="7" fill="#8b7bff">Metadata Monitoring API</text>

            <!-- Connections: AI Platform → Storage layer -->
            <path d="M125 240 Q125 260 190 270" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M360 240 Q360 260 360 270" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M580 160 Q580 240 475 308" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M475 308 L560 308" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>

            <!-- Flow particles -->
            <circle class="flow-particle"><animateMotion dur="3s" repeatCount="indefinite" path="M102 35 L140 35"/></circle>
            <circle class="flow-particle"><animateMotion dur="3s" repeatCount="indefinite" begin=".5s" path="M270 35 L300 35"/></circle>
            <circle class="flow-particle"><animateMotion dur="4s" repeatCount="indefinite" begin="0s" path="M205 50 Q205 70 125 80"/></circle>
            <circle class="flow-particle"><animateMotion dur="4s" repeatCount="indefinite" begin="1s" path="M375 50 Q375 70 360 80"/></circle>
            <circle class="flow-particle"><animateMotion dur="4s" repeatCount="indefinite" begin="1.5s" path="M375 50 Q480 70 580 80"/></circle>
            <circle class="flow-particle"><animateMotion dur="3.5s" repeatCount="indefinite" begin="0s" path="M230 160 L260 160"/></circle>
            <circle class="flow-particle"><animateMotion dur="3.5s" repeatCount="indefinite" begin="1s" path="M460 120 L490 120"/></circle>
            <circle class="flow-particle"><animateMotion dur="5s" repeatCount="indefinite" begin="0s" path="M125 240 Q125 260 190 270"/></circle>
            <circle class="flow-particle"><animateMotion dur="5s" repeatCount="indefinite" begin="1.5s" path="M360 240 Q360 260 360 270"/></circle>
            <circle class="flow-particle"><animateMotion dur="5s" repeatCount="indefinite" begin=".5s" path="M580 160 Q580 240 475 308"/></circle>
            <circle class="flow-particle"><animateMotion dur="3s" repeatCount="indefinite" begin="0s" path="M475 308 L560 308"/></circle>
          </svg>
        </div>
      </div>
    </div>
    </div>

    <!-- ============ CASE 5: AI 智能数据治理 ============ -->
    <div class="section-tab-panel" data-panel="case-5">
    <div class="case">
      <h4>AI 数据治理与智能 Agent</h4>
      <div class="pains">
        <div class="lab">客户痛点</div>
        <p>AI 数据生命周期管理缺失；跨存储数据无法统一治理；元数据与 AI 引擎对接困难。</p>
      </div>
      <div class="pains">
        <div class="lab">LiSA 方案</div>
        <p>统一元数据管理 + AI 数据治理 + Agent 自动化任务，对接主流 AI 框架。</p>
      </div>
      <div class="case-arch">
        <div class="ttl">方案架构</div>
        <div class="scroll-x">
          <svg viewBox="-30 0 700 340" class="flow-svg" style="max-width:740px" xmlns="http://www.w3.org/2000/svg">
            <!-- ===== ROW 1: Client Apps → Agent → AI Data Platform ===== -->
            <g class="arch-svg-node">
              <rect x="30" y="20" width="72" height="28" rx="5" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="66" y="39" text-anchor="middle" font-size="8" fill="#3df0ff">Client Apps</text>
            </g>
            <g class="arch-svg-node">
              <rect x="140" y="20" width="110" height="28" rx="5" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)"/><text x="195" y="39" text-anchor="middle" font-size="8" fill="#3df0ff">Agent</text>
            </g>
            <g class="arch-svg-node">
              <rect x="290" y="16" width="200" height="36" rx="6" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)" stroke-width="1.2"/><text x="390" y="39" text-anchor="middle" font-size="10" fill="#3df0ff" font-weight="700">AI Data Platform</text>
            </g>

            <line x1="102" y1="34" x2="140" y2="34" stroke="var(--cyan)" stroke-width="1.2" stroke-dasharray="3 3" class="flow-line"/>
            <line x1="250" y1="34" x2="290" y2="34" stroke="var(--cyan)" stroke-width="1.2" stroke-dasharray="3 3" class="flow-line"/>

            <!-- ===== ROW 2: Search / ETL → Domain Model ===== -->
            <g class="arch-svg-node">
              <rect x="30" y="80" width="110" height="24" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="85" y="96" text-anchor="middle" font-size="8" fill="#8b7bff">Semantic Search</text>
            </g>
            <g class="arch-svg-node">
              <rect x="150" y="80" width="110" height="24" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="205" y="96" text-anchor="middle" font-size="8" fill="#8b7bff">Keyword Search</text>
            </g>
            <g class="arch-svg-node">
              <rect x="270" y="80" width="118" height="24" rx="4" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.5)"/><text x="329" y="96" text-anchor="middle" font-size="8" fill="#8b7bff">Agentic ETL</text>
            </g>

            <!-- Connection to Any Domain-Specific Model -->
            <path d="M490 34 Q490 60 420 80" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M335 104 Q400 115 490 130" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>

            <g class="arch-svg-node">
              <rect x="490" y="118" width="160" height="30" rx="6" fill="rgba(var(--cyan-rgb),.1)" stroke="var(--cyan)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="570" y="137" text-anchor="middle" font-size="9" fill="#3df0ff" font-weight="600">Any Domain-Specific Model</text>
            </g>

            <!-- ===== ROW 3: MatrixOne Storage + LiSA ===== -->
            <rect x="20" y="180" width="320" height="90" rx="8" fill="rgba(139,123,255,.1)" stroke="rgba(139,123,255,.55)" stroke-width="1"/>
            <text x="180" y="200" text-anchor="middle" font-size="10" fill="#8b7bff" font-weight="700">MatrixOne Storage</text>
            <g class="arch-svg-node"><rect x="34" y="210" width="130" height="20" rx="4" fill="rgba(139,123,255,.12)" stroke="rgba(139,123,255,.5)"/><text x="99" y="224" text-anchor="middle" font-size="8" fill="#8b7bff">Metadata Management</text></g>
            <g class="arch-svg-node"><rect x="172" y="210" width="150" height="20" rx="4" fill="rgba(139,123,255,.12)" stroke="rgba(139,123,255,.5)"/><text x="247" y="224" text-anchor="middle" font-size="8" fill="#8b7bff">Data Resiliency</text></g>
            <g class="arch-svg-node"><rect x="34" y="236" width="288" height="20" rx="4" fill="rgba(139,123,255,.15)" stroke="rgba(139,123,255,.55)"/><text x="178" y="250" text-anchor="middle" font-size="8" fill="#8b7bff" font-weight="600">Vector Data · Feature Store · Object Storage · Document Metadata</text></g>

            <!-- LiSA Server/Component -->
            <rect x="380" y="180" width="130" height="90" rx="8" fill="rgba(var(--cyan-rgb),.12)" stroke="var(--cyan)" stroke-width="1"/>
            <text x="445" y="200" text-anchor="middle" font-size="9" fill="#3df0ff" font-weight="700">LiSA Server</text>
            <text x="445" y="214" text-anchor="middle" font-size="7" fill="#9aa3c4" font-family="JetBrains Mono">Component</text>
            <g class="arch-svg-node"><rect x="394" y="224" width="102" height="18" rx="3" fill="rgba(var(--cyan-rgb),.15)" stroke="var(--cyan)"/><text x="445" y="237" text-anchor="middle" font-size="7" fill="#3df0ff">Agent Mgmt</text></g>
            <g class="arch-svg-node"><rect x="394" y="246" width="102" height="18" rx="3" fill="rgba(var(--cyan-rgb),.15)" stroke="var(--cyan)"/><text x="445" y="259" text-anchor="middle" font-size="7" fill="#3df0ff">Metadata Engine</text></g>

            <!-- External Object/File Storage -->
            <rect x="540" y="180" width="130" height="90" rx="8" fill="rgba(245,200,122,.08)" stroke="rgba(245,200,122,.4)" stroke-dasharray="4 3"/>
            <text x="605" y="200" text-anchor="middle" font-size="9" fill="#f5c87a" font-weight="600">External</text>
            <text x="605" y="214" text-anchor="middle" font-size="7" fill="#9aa3c4" font-family="JetBrains Mono">Object/File Storage</text>
            <g class="arch-svg-node"><rect x="554" y="224" width="102" height="18" rx="3" fill="rgba(245,200,122,.12)" stroke="rgba(245,200,122,.4)"/><text x="605" y="237" text-anchor="middle" font-size="7" fill="#f5c87a">Legacy Systems</text></g>
            <g class="arch-svg-node"><rect x="554" y="246" width="102" height="18" rx="3" fill="rgba(245,200,122,.12)" stroke="rgba(245,200,122,.4)"/><text x="605" y="259" text-anchor="middle" font-size="7" fill="#f5c87a">Cloud Storage</text></g>

            <!-- Row 2 → Row 3 connections -->
            <path d="M85 104 Q120 140 180 180" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M205 104 Q190 140 180 180" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M329 104 Q260 140 180 180" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M570 148 Q500 165 445 180" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>
            <path d="M510 225 L540 225" stroke="var(--cyan)" stroke-width="1" class="flow-line" fill="none" stroke-dasharray="3 3"/>

            <!-- Flow particles -->
            <circle class="flow-particle"><animateMotion dur="3s" repeatCount="indefinite" path="M102 34 L140 34"/></circle>
            <circle class="flow-particle"><animateMotion dur="3s" repeatCount="indefinite" begin=".5s" path="M250 34 L290 34"/></circle>
            <circle class="flow-particle"><animateMotion dur="4s" repeatCount="indefinite" begin="0s" path="M490 34 Q490 60 420 80"/></circle>
            <circle class="flow-particle"><animateMotion dur="4s" repeatCount="indefinite" begin="1s" path="M335 104 Q400 115 490 130"/></circle>
            <circle class="flow-particle"><animateMotion dur="5s" repeatCount="indefinite" begin="0s" path="M85 104 Q120 140 180 180"/></circle>
            <circle class="flow-particle"><animateMotion dur="5s" repeatCount="indefinite" begin="1s" path="M205 104 Q190 140 180 180"/></circle>
            <circle class="flow-particle"><animateMotion dur="5s" repeatCount="indefinite" begin="2s" path="M329 104 Q260 140 180 180"/></circle>
            <circle class="flow-particle"><animateMotion dur="4s" repeatCount="indefinite" begin=".5s" path="M570 148 Q500 165 445 180"/></circle>
            <circle class="flow-particle"><animateMotion dur="3.5s" repeatCount="indefinite" begin="0s" path="M510 225 L540 225"/></circle>
          </svg>
        </div>
      </div>
    </div>
    </div>
  </div>


# Now do the replacement
old_section = content[start_idx:end_idx]
new_content = content[:start_idx] + NEW_CASES + content[end_idx:]

with open(FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

old_lines = old_section.count("\n") + 1
new_lines = NEW_CASES.count("\n") + 1

print(f"Old section: {old_lines} lines (lines {start_line}-{end_line})")
print(f"New section: {new_lines} lines")
print(f"Replacement done. {old_lines} lines replaced with {new_lines} new lines.")

# Verify
with open(FILE, "r", encoding="utf-8") as f:
    verify = f.read()

# Check for customer-specific names
forbidden = ["Flextronics", "Suna Opto", "RT Mart", "Auchan", "Tekscend", "MatrixOne", "JinPan", "iPhone", "nVidia"]
found = [w for w in forbidden if w in verify]
if found:
    print(f"WARNING: Found customer-specific names: {found}")
else:
    print("OK: No customer-specific names found.")

# Check all 5 cases present
for i in range(1, 6):
    panel = f'data-panel="case-{i}"'
    if panel in verify:
        print(f"OK: Case {i} panel found.")
    else:
        print(f"ERROR: Case {i} panel NOT found!")

# Check tabs
for i in range(1, 6):
    tab = f'data-tab="case-{i}"'
    if tab in verify:
        print(f"OK: Case {i} tab found.")
    else:
        print(f"ERROR: Case {i} tab NOT found!")

print("Verification complete.")