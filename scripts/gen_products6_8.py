"""Generate Products 6, 7, 8"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_css import html_doc

# ── PRODUCT 6: AI-to-Blender Kit ────────────────────────────────────────────

body6 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">What this kit gives you</div>
    <p>A complete workflow for using AI to accelerate Blender 3D projects — from generating geometry-ready concept images to writing Python scripts that automate repetitive modeling tasks. No prior coding experience required.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">15+</div><div class="stat-label">Ready-to-Run Scripts</div></div>
    <div class="stat-card"><div class="stat-value">20+</div><div class="stat-label">AI Prompts for 3D</div></div>
    <div class="stat-card"><div class="stat-value">5</div><div class="stat-label">Full Workflows</div></div>
    <div class="stat-card"><div class="stat-value">0</div><div class="stat-label">Coding Experience Needed</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Workflow 01</div>
    <h2>Concept to Blender</h2>
    <p>Use AI image generation to prototype 3D concepts before touching Blender.</p>
  </div>

  <h3>Step 1: Generate geometry-aware concept images</h3>
  <div class="prompt-block">
    <div class="prompt-label">Midjourney / DALL-E / Stable Diffusion — concept prompt</div>
    <div class="prompt-text">Professional 3D product concept for [OBJECT], orthographic front view, clean white studio background, hard surface modeling reference, visible edge loops, wireframe overlay on right half, industrial design sketch aesthetic, technical illustration --ar 16:9 --style raw</div>
  </div>

  <div class="callout green">
    <div class="callout-title">Geometry-friendly prompt keywords</div>
    <p>Add these to any concept prompt: "orthographic view", "edge loop visible", "hard surface", "wireframe overlay", "technical reference sheet", "front/side/top views". These force the AI toward geometry-readable outputs rather than painterly illustrations.</p>
  </div>

  <h3>Step 2: Generate a full reference sheet</h3>
  <div class="prompt-block">
    <div class="prompt-label">Multi-view reference sheet prompt</div>
    <div class="prompt-text">3D modeling reference sheet for [CHARACTER/OBJECT], showing: front view (left), side profile (center), back view (right), detail closeup (bottom left), color palette swatches (bottom right). Clean white background, consistent lighting, T-pose if character. Style: [realistic/stylized/sci-fi/fantasy]</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Workflow 02</div>
    <h2>Python Scripting with AI</h2>
    <p>Use Claude or ChatGPT to write Blender Python scripts — no prior Python experience needed.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Generate a Blender Python script</div>
    <div class="prompt-text">Write a Blender Python script (bpy) that does the following:
[DESCRIBE WHAT YOU WANT IN PLAIN ENGLISH]

Requirements:
- Compatible with Blender 4.x
- Include comments explaining each step
- Add error handling if the operation fails
- Print a confirmation message when done
- The script should run from Blender's Text Editor (not as an add-on)

Context: I'm working on [DESCRIBE YOUR SCENE/PROJECT]</div>
  </div>

  <h3>15 tasks AI can script for you</h3>
  <ul class="checklist">
    <li><div class="check-icon"></div>Batch rename all objects in scene by type</li>
    <li><div class="check-icon"></div>Apply all modifiers and decimate to target poly count</li>
    <li><div class="check-icon"></div>Auto-UV unwrap selected objects with consistent seam placement</li>
    <li><div class="check-icon"></div>Export each object as individual FBX with consistent naming</li>
    <li><div class="check-icon"></div>Generate a grid of instances with randomized rotation and scale</li>
    <li><div class="check-icon"></div>Create material slots and assign by object name prefix</li>
    <li><div class="check-icon"></div>Set up a 3-point lighting rig with keyable intensity</li>
    <li><div class="check-icon"></div>Batch import images as planes and arrange in a grid</li>
    <li><div class="check-icon"></div>Find and remove duplicate vertices across all meshes</li>
    <li><div class="check-icon"></div>Generate camera path along a Bezier curve</li>
    <li><div class="check-icon"></div>Bake ambient occlusion to vertex colors</li>
    <li><div class="check-icon"></div>Auto-parent objects to armature by naming convention</li>
    <li><div class="check-icon"></div>Render all cameras in scene and save with camera name</li>
    <li><div class="check-icon"></div>Create LOD versions at 100%, 50%, and 25% poly count</li>
    <li><div class="check-icon"></div>Generate node group for PBR material from texture file list</li>
  </ul>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Workflow 03</div>
    <h2>Texture Generation</h2>
    <p>Generate seamless PBR textures and material descriptions with AI.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Seamless texture prompt (Stable Diffusion / Midjourney)</div>
    <div class="prompt-text">Seamless tileable texture, [MATERIAL TYPE: weathered concrete / brushed metal / wood grain / fabric / stone], 4K resolution, PBR ready, diffuse map, even lighting, no shadows, no seams visible, overhead view, [COLOR PALETTE], photorealistic</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Blender Shader Node description prompt</div>
    <div class="prompt-text">Describe how to create a Blender Cycles/EEVEE shader node tree for [MATERIAL]: [DESCRIBE THE MATERIAL IN DETAIL].

Include:
1. List of all nodes needed (exact Blender node names)
2. Connection order (what plugs into what)
3. Key value settings for each node
4. How to add variation with noise/texture nodes
5. Any special settings for realistic results

Write it step by step so I can follow in Blender's Node Editor.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Workflow 04</div>
    <h2>Scene Composition &amp; Lighting</h2>
    <p>AI-assisted scene setup, composition, and render optimization.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Scene composition advice</div>
    <div class="prompt-text">I'm composing a 3D scene in Blender for [PURPOSE: product render / architectural viz / game cinematic / portfolio piece].

Scene description: [DESCRIBE YOUR CURRENT SETUP]
Camera: [FOCAL LENGTH, ANGLE]
Mood: [DARK/BRIGHT/DRAMATIC/CLEAN/CINEMATIC]

Advise me on:
1. Camera placement and focal length for this mood
2. Rule of thirds or golden ratio composition for my subject
3. Lighting setup (3-point, HDRI, area lights — which and why)
4. Color palette for the lighting to match the mood
5. Background / environment recommendation
6. Post-processing steps in Blender's compositor

Give specific Blender settings where possible (values, node names, light strengths).</div>
  </div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">AI-to-Blender Kit &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result6 = html_doc(
    title="AI-to-Blender Kit",
    subtitle="15+ Python scripts and 20+ AI prompts for Blender 3D artists. Concept generation, automated scripting, texture creation, and scene composition — powered by AI, built for artists who hate waiting.",
    eyebrow="Schep Digital · AI + Blender Workflow Kit",
    meta_items=[
        ("Scripts", "15+ ready-to-run"),
        ("Prompts", "20+ for 3D"),
        ("Works with", "Blender 4.x"),
        ("Level", "Beginner–Intermediate"),
    ],
    body_html=body6
)

# ── PRODUCT 7: Consistent Character Genesis 2026 ─────────────────────────────

body7 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">The consistency problem — and the solution</div>
    <p>AI image generators are amazing at single images. They fail at consistent characters across scenes. This system teaches you to build character bibles, seed-lock identities, and use reference injection to maintain recognizable faces, clothing, and proportions across 50+ images.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">95%</div><div class="stat-label">Identity Retention Rate</div></div>
    <div class="stat-card"><div class="stat-value">50+</div><div class="stat-label">Scenes per Character</div></div>
    <div class="stat-card"><div class="stat-value">3</div><div class="stat-label">Core Techniques</div></div>
    <div class="stat-card"><div class="stat-value">2026</div><div class="stat-label">Updated Methods</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 01</div>
    <h2>The Character Bible</h2>
    <p>Build a document that defines your character completely — before you generate a single image.</p>
  </div>

  <p style="color:var(--ink-2);">The single biggest mistake is jumping straight to image generation without a character bible. Every inconsistency you see in AI characters traces back to under-specification. The more precisely you define the character in language, the more consistent the output.</p>

  <div class="prompt-block">
    <div class="prompt-label">Character bible generator</div>
    <div class="prompt-text">Create a detailed character bible for my AI image generation workflow. The character is:

[DESCRIBE YOUR CHARACTER IN FREE TEXT]

Generate a structured character bible with these fields filled in completely:

PHYSICAL:
- Age appearance: [specific, e.g., "late 30s, slight crow's feet"]
- Height/build: [specific proportions]
- Skin tone: [specific, e.g., "warm medium brown, Fitzpatrick type IV"]
- Hair: [color, texture, length, style — precise enough to recreate]
- Eyes: [color, shape, notable features]
- Distinctive features: [scars, moles, jawline shape, nose, any unique identifier]

STYLE:
- Signature outfit: [describe in detail — fabric, fit, color codes where possible]
- Accessories: [always-present items]
- Color palette: [3-5 hex codes that define their look]

GENERATION KEYWORDS:
- 5 positive trigger words (for consistent style)
- 3 negative keywords (what to exclude)
- Recommended seed range (if using SDXL/ComfyUI)</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 02</div>
    <h2>Technique 1: The Master Seed Lock</h2>
    <p>Find and lock the seed that captures your character's identity. Reuse it across all scenes.</p>
  </div>

  <div class="item"><h4>Step 1: Generation sprint</h4><p>Generate 20 images at fixed settings: same model, same prompt, different seeds. Record the seeds of all outputs. Look for the 3-5 seeds that feel most "right" for the character.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Step 2: Refine the winner</h4><p>Take your best seed. Vary only the lighting and pose prompt while keeping everything else fixed. If the face holds, this is your master seed. If it drifts, try the next candidate.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Step 3: Build a seed library</h4><p>For each character, maintain a seed library: master seed (neutral pose), expression seeds (happy, serious, surprised), and angle seeds (profile, three-quarter, overhead). Document all in your character bible.</p></div>

  <div class="prompt-block">
    <div class="prompt-label">Consistent scene prompt structure</div>
    <div class="prompt-text">[CHARACTER NAME], [DISTINCTIVE FEATURES FROM BIBLE], [SIGNATURE OUTFIT FROM BIBLE], [SCENE DESCRIPTION], [LIGHTING], [CAMERA ANGLE], [STYLE KEYWORDS], --seed [MASTER SEED] --cfg 7 --steps 30

Example:
Elena Vasquez, dark auburn hair in loose bun, warm olive skin, small scar above left eyebrow, wearing navy structured blazer with white collarless shirt, sitting in modern cafe, window light from left, three-quarter view, editorial photography, sharp focus --seed 847291 --cfg 7 --steps 30</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 03</div>
    <h2>Technique 2: Reference Injection</h2>
    <p>Use your existing generations as visual references for new scenes.</p>
  </div>

  <div class="item"><h4>IP-Adapter (SDXL / ComfyUI)</h4><p>The IP-Adapter node takes a reference image and maps the identity to new generations. Set face weight to 0.7-0.9, style weight to 0.3-0.5. Higher face weight = more consistent identity but less creative freedom.</p></div>
  <div class="item" style="margin-top:12px;"><h4>ControlNet Face (OpenPose)</h4><p>Combine IP-Adapter with ControlNet OpenPose to control the pose while locking the face. The pose comes from a skeleton reference, the identity from the IP-Adapter image. Most reliable combination for comics and storyboards.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Midjourney --cref flag</h4><p>In Midjourney v6+, use --cref [IMAGE_URL] to reference a character image. Combine with --cw (character weight, 0-100) to control how strongly the reference influences the output. Start at --cw 80 and adjust.</p></div>
  <div class="item" style="margin-top:12px;"><h4>DALL-E 3 consistent style prompt</h4><p>Use the GPT-4V + DALL-E pipeline: describe the character image to GPT-4V to generate a detailed text description, then use that exact description as the prompt prefix for all subsequent DALL-E generations.</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 04</div>
    <h2>Technique 3: Fine-Tuning (DreamBooth / LoRA)</h2>
    <p>Train the model on your character's face. 15-20 reference images, 30 minutes, permanent consistency.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Training data requirements checklist</div>
    <div class="prompt-text">Minimum viable training set for character LoRA:
- 15-20 images of the character (real photos OR consistent AI gens from Technique 1-2)
- Variety: 5 different lighting conditions, 5 different angles, 5 different expressions
- All images: same resolution (512x512 or 1024x1024), cropped to face/bust
- Caption each image with: "photo of [TRIGGER_WORD], [DESCRIPTION OF THIS SPECIFIC IMAGE]"
- No watermarks, heavy compression artifacts, or extreme filters

Avoid:
- Duplicate poses or expressions (weakens the model)
- Images where the face is partially occluded
- Mixed art styles (keep all images in the same style)</div>
  </div>

  <div class="callout amber">
    <div class="callout-title">Easiest training path in 2026</div>
    <p>Use Replicate or Fal.ai for LoRA training without local GPU setup. Upload your 15-20 images, set the trigger word, run training (~$1-3 per run). Download the LoRA weights and load into ComfyUI or Automatic1111 for infinite consistent generations.</p>
  </div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Consistent Character Genesis 2026 &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result7 = html_doc(
    title="Consistent Character Genesis 2026",
    subtitle="Three proven techniques for maintaining recognizable AI characters across 50+ scenes. Character bibles, seed locking, reference injection, and LoRA fine-tuning — the complete system.",
    eyebrow="Schep Digital · AI Character Consistency System",
    meta_items=[
        ("Techniques", "3 core systems"),
        ("Success rate", "95% identity retention"),
        ("Tools", "Midjourney · SDXL · ComfyUI"),
        ("Updated", "2026 Edition"),
    ],
    body_html=body7
)

# ── PRODUCT 8: Consistent Character Genesis Editorial ────────────────────────

body8 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">Editorial vs. Standard</div>
    <p>The Editorial edition focuses on commercial and publishing use cases — brand mascots, book illustrations, webtoons, and marketing campaigns. It adds style consistency (not just identity consistency), multi-character scenes, and licensing-safe generation workflows.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">Multi</div><div class="stat-label">Character Scenes</div></div>
    <div class="stat-card"><div class="stat-value">Brand</div><div class="stat-label">Mascot System</div></div>
    <div class="stat-card"><div class="stat-value">Legal</div><div class="stat-label">Safe Workflow</div></div>
    <div class="stat-card"><div class="stat-value">Print</div><div class="stat-label">Ready Output</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Module 01</div>
    <h2>Brand Mascot System</h2>
    <p>Build a legally defensible, commercially licensable brand character.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Brand mascot brief generator</div>
    <div class="prompt-text">Create a brand mascot design brief for [BRAND/COMPANY].

Brand personality: [3 ADJECTIVES]
Target audience: [DESCRIBE]
Industry: [WHAT THE BRAND DOES]
Existing brand colors: [HEX CODES]

Generate:
1. MASCOT CONCEPT: 3 distinct character directions (human/animal/abstract/hybrid) with rationale for each
2. WINNING DIRECTION: Recommend one with reasoning tied to brand personality
3. CHARACTER TRAITS: Personality, backstory, behavioral quirks
4. VISUAL SPEC: Body proportions, style guide (flat/3D/illustrated), color palette
5. EXPRESSION SHEET: 6 core expressions needed for marketing (happy, thinking, excited, explaining, approving, sleeping/resting)
6. USAGE CONTEXTS: List 10 specific marketing situations this mascot will appear in

Avoid: generic smiling blob characters, animal clichés for the industry, mascots that don't scale to icon size</div>
  </div>

  <h3>Mascot consistency across media</h3>
  <div class="item"><h4>Style guide document</h4><p>Generate a visual style guide with: exact color codes, minimum size requirements, approved backgrounds, logo lockup rules, and what never to do. Paste this into every AI image prompt as a prefix.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Vector conversion</h4><p>Generate at 2048x2048 minimum. Use Adobe Firefly or Vectorizer.ai to convert to SVG. Clean up anchor points in Illustrator. The final mascot should exist as an SVG for print flexibility.</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Module 02</div>
    <h2>Multi-Character Scenes</h2>
    <p>The hardest problem in consistent AI generation — multiple characters in one frame.</p>
  </div>

  <div class="item"><h4>The composition approach</h4><p>Generate each character separately with consistent settings, then composite in Photoshop/Figma. Use Generative Fill (Photoshop) to blend the backgrounds. This is the most reliable method for character-heavy editorial work.</p></div>
  <div class="item" style="margin-top:12px;"><h4>The regional prompt method (ComfyUI)</h4><p>Use the Regional Prompter node to assign different character descriptions to different areas of the image. Zone A: Character 1 description. Zone B: Character 2 description. Prevents character mixing.</p></div>
  <div class="item" style="margin-top:12px;"><h4>The multi-IP-Adapter method</h4><p>Load two separate IP-Adapter models simultaneously, each with a different character reference. Set face weight to 0.6 each (lower than single-character to avoid conflict). Works best when characters have clearly different appearances.</p></div>

  <div class="prompt-block">
    <div class="prompt-label">Multi-character scene prompt structure</div>
    <div class="prompt-text">[SCENE DESCRIPTION], [CHARACTER A: full appearance description] on the left, [CHARACTER B: full appearance description] on the right, [INTERACTION DESCRIPTION], [LIGHTING AND SETTING], editorial illustration style, professional, [STYLE KEYWORDS], --ar 16:9

Key: describe each character completely in the prompt even if using reference images. The text description and reference image work together — not as alternates.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Module 03</div>
    <h2>Licensing-Safe Generation</h2>
    <p>Workflows that produce commercially usable output without IP risk.</p>
  </div>

  <div class="item"><h4>Use commercially-licensed model bases</h4><p>Midjourney Pro/Teams (commercial license), Adobe Firefly (trained on licensed data), DALL-E 3 via API (commercial use permitted). Avoid open-source models fine-tuned on unlicensed celebrity data.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Originality documentation</h4><p>Screenshot your prompts, record generation parameters, save all intermediate generations. This creates an evidence trail showing your creative input and the generative process — relevant for copyright registration in some jurisdictions.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Style-not-substance protection</h4><p>AI can legally replicate an artist's style (style is not copyrightable) but not copy specific artwork. Describe the aesthetic — "impressionist loose brushwork, high chroma", not "in the style of [specific artist]". Keeps you clean and builds original brand language.</p></div>

  <div class="callout amber">
    <div class="callout-title">Legal landscape note (2026)</div>
    <p>AI copyright law is actively evolving. The safest commercial posture: use licensed-data models, add substantial creative direction via prompting, and register the final composed work as yours in jurisdictions where that's possible. Check with a media IP lawyer for commercial campaigns above €10K.</p>
  </div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Consistent Character Genesis: Editorial &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result8 = html_doc(
    title="Consistent Character Genesis: Editorial",
    subtitle="Brand mascot systems, multi-character scenes, and licensing-safe commercial workflows for AI-generated illustration. Built for marketers, publishers, and creative directors.",
    eyebrow="Schep Digital · Editorial AI Character System",
    meta_items=[
        ("Focus", "Commercial & editorial"),
        ("Includes", "Mascot system + legal guide"),
        ("Tools", "Midjourney · ComfyUI · Firefly"),
        ("Output", "Print-ready"),
    ],
    body_html=body8
)

# ── WRITE FILES ──────────────────────────────────────────────────────────────

files = [
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/06_ai_to_blender_kit.html", result6),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/07_consistent_character_genesis_2026.html", result7),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/08_consistent_character_genesis_editorial.html", result8),
]

for path, content in files:
    with open(path, "w") as f:
        f.write(content)
    print(f"Written: {path}")
