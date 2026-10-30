"""Builds olafthedread7-avatar.svg: an original viking portrait for the GitHub avatar.
Rune ring spells OLAF THE DREAD in Elder Futhark, drawn as strokes (no font needed)."""
import math, os

OUT = os.path.dirname(os.path.abspath(__file__))
C = 256  # canvas centre

# Elder Futhark glyphs on an 8 x 16 grid (y down). Each is a list of polylines.
GLYPHS = {
    "O": [[(0, 5), (4, 0), (8, 5)], [(0, 5), (8, 16)], [(8, 5), (0, 16)]],          # othala
    "L": [[(2, 0), (2, 16)], [(2, 0), (7, 5)]],                                        # laguz
    "A": [[(2, 0), (2, 16)], [(2, 0), (7, 4)], [(2, 5), (7, 9)]],                     # ansuz
    "F": [[(2, 0), (2, 16)], [(2, 6), (7, 1)], [(2, 11), (7, 6)]],                    # fehu
    "TH": [[(2, 0), (2, 16)], [(2, 4), (7, 8), (2, 12)]],                              # thurisaz
    "E": [[(0, 16), (0, 0), (4, 6), (8, 0), (8, 16)]],                                 # ehwaz
    "D": [[(0, 0), (0, 16), (8, 0), (8, 16), (0, 0)]],                                 # dagaz
    "R": [[(1, 0), (1, 16)], [(1, 0), (7, 4), (1, 8), (7, 16)]],                       # raido
}
PHRASE = ["O", "L", "A", "F", "•", "TH", "E", "•", "D", "R", "E", "A", "D", "✦"]


def rune_ring(radius=226, repeats=3):
    seq = PHRASE * repeats
    step = 360 / len(seq)
    out = []
    for i, g in enumerate(seq):
        ang = i * step
        top = C - radius - 8
        if g in ("•", "✦"):
            r = 1.7 if g == "•" else 2.6
            out.append(f'<circle cx="{C}" cy="{top + 8}" r="{r}" transform="rotate({ang:.2f} {C} {C})"/>')
            continue
        paths = " ".join("M" + " L".join(f"{C - 4 + x:.1f} {top + y:.1f}" for x, y in pl) for pl in GLYPHS[g])
        out.append(f'<path d="{paths}" transform="rotate({ang:.2f} {C} {C})"/>')
    return "\n    ".join(out)


def plait(x, y0, y1, w=13, h=11, tilt=1):
    """A braid: stacked slanted ellipses, alternating lean, with a dark crease."""
    out, y, i = [], y0, 0
    while y < y1:
        lean = 28 * tilt if i % 2 == 0 else -28 * tilt
        out.append(
            f'<ellipse cx="{x}" cy="{y:.1f}" rx="{w}" ry="{h / 2 + 2:.1f}" '
            f'transform="rotate({lean} {x} {y:.1f})" fill="url(#hairG)" stroke="#5c2408" stroke-width="2"/>'
        )
        y += h
        i += 1
    return "\n    ".join(out), y


def bead(x, y):
    return (f'<rect x="{x - 8}" y="{y - 2}" width="16" height="15" rx="4" fill="url(#goldG)" stroke="#6b4a12" stroke-width="2"/>'
            f'<path d="M{x - 8} {y + 5} H{x + 8}" stroke="#6b4a12" stroke-width="1.5"/>'
            f'<path d="M{x - 6} {y + 13} L{x - 9} {y + 26} M{x} {y + 13} L{x} {y + 28} M{x + 6} {y + 13} L{x + 9} {y + 26}" '
            f'stroke="#b5561f" stroke-width="3" stroke-linecap="round"/>')


def fur_trim():
    def bez(p0, p1, p2, p3, t):
        return tuple((1-t)**3*a + 3*(1-t)**2*t*b + 3*(1-t)*t**2*c + t**3*d for a, b, c, d in zip(p0, p1, p2, p3))
    out = []
    left = ((24, 540), (40, 452), (120, 410), (196, 414))
    for side in (1, -1):
        for i in range(14):
            t = 0.18 + i * 0.06
            x, y = bez(*left, t)
            if side == -1:
                x = 512 - x
            col = "#6e543d" if i % 2 else "#57412f"
            rot = -38 * side + (i % 3 - 1) * 10
            out.append(f'<ellipse cx="{x:.1f}" cy="{y + 4:.1f}" rx="17" ry="10" transform="rotate({rot} {x:.1f} {y + 4:.1f})" '
                       f'fill="{col}" stroke="#22160f" stroke-width="2"/>')
    return "\n    ".join(out)


side_l, end_l = plait(150, 236, 418, w=12)
side_r, end_r = plait(362, 236, 418, w=12, tilt=-1)
beard_l, end_bl = plait(236, 432, 480, w=11, h=10)
beard_r, end_br = plait(276, 432, 480, w=11, h=10, tilt=-1)

rivets = "".join(f'<circle cx="{x}" cy="214" r="3.4" fill="#d9e1e8" stroke="#2b333b" stroke-width="1"/>'
                 for x in range(164, 352, 21) if abs(x - 256) > 14)

beard_strands = "".join(
    f'<path d="M{x} {y0} C{x + dx * 0.4} {y0 + 40}, {x + dx} {y0 + 80}, {x + dx * 1.2} {y0 + 118}" '
    f'stroke="#7f2f0c" stroke-width="2.6" fill="none" stroke-linecap="round" opacity="0.75"/>'
    for x, y0, dx in [(200, 330, -6), (218, 336, -3), (238, 340, -1), (256, 342, 0), (274, 340, 1),
                      (294, 336, 3), (312, 330, 6), (188, 318, -10), (324, 318, 10)])

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <title>OlafTheDread7</title>
  <defs>
    <radialGradient id="bgG" cx="50%" cy="42%" r="62%">
      <stop offset="0" stop-color="#22466e"/><stop offset="0.55" stop-color="#11243b"/><stop offset="1" stop-color="#070d17"/>
    </radialGradient>
    <linearGradient id="auroraG" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#2be3a6" stop-opacity="0"/><stop offset="0.35" stop-color="#2be3a6" stop-opacity="0.55"/>
      <stop offset="0.7" stop-color="#3fa7ff" stop-opacity="0.45"/><stop offset="1" stop-color="#8a5cff" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="steelG" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#eef3f7"/><stop offset="0.35" stop-color="#a9b6c2"/><stop offset="0.75" stop-color="#5f6d7b"/><stop offset="1" stop-color="#36404a"/>
    </linearGradient>
    <linearGradient id="brimG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#7d8a97"/><stop offset="1" stop-color="#3a444e"/>
    </linearGradient>
    <linearGradient id="hornG" x1="0" y1="1" x2="0.6" y2="0">
      <stop offset="0" stop-color="#9c8152"/><stop offset="0.5" stop-color="#e9dbb6"/><stop offset="1" stop-color="#fff8e6"/>
    </linearGradient>
    <linearGradient id="skinG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#b9785a"/><stop offset="1" stop-color="#e2a989"/>
    </linearGradient>
    <linearGradient id="hairG" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f08a3c"/><stop offset="1" stop-color="#a53f12"/>
    </linearGradient>
    <linearGradient id="beardG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ee8640"/><stop offset="0.6" stop-color="#c2531b"/><stop offset="1" stop-color="#8e3510"/>
    </linearGradient>
    <linearGradient id="goldG" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ffe9a3"/><stop offset="0.5" stop-color="#d9a637"/><stop offset="1" stop-color="#8f6514"/>
    </linearGradient>
    <linearGradient id="furG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#5b4331"/><stop offset="1" stop-color="#241812"/>
    </linearGradient>
    <filter id="glow" x="-80%" y="-200%" width="260%" height="500%">
      <feGaussianBlur stdDeviation="4.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="soft"><feGaussianBlur stdDeviation="14"/></filter>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="7" flood-color="#000" flood-opacity="0.55"/>
    </filter>
  </defs>

  <rect width="512" height="512" fill="url(#bgG)"/>

  <!-- aurora behind the head -->
  <path d="M-20 190 C 90 90, 200 150, 270 110 S 430 40, 540 120 L 540 175 C 430 105, 360 175, 270 165 S 90 155, -20 245 Z"
        fill="url(#auroraG)" filter="url(#soft)"/>

  <!-- stars -->
  <g fill="#e8f1ff">
    <circle cx="92" cy="128" r="1.6" opacity=".8"/><circle cx="420" cy="150" r="1.4" opacity=".7"/>
    <circle cx="380" cy="92" r="1.1" opacity=".6"/><circle cx="130" cy="92" r="1" opacity=".5"/>
    <circle cx="448" cy="236" r="1.2" opacity=".5"/><circle cx="64" cy="250" r="1.2" opacity=".5"/>
  </g>

  <!-- rune ring: OLAF THE DREAD -->
  <circle cx="256" cy="256" r="244" fill="none" stroke="#d4a94c" stroke-width="2" opacity=".55"/>
  <circle cx="256" cy="256" r="207" fill="none" stroke="#d4a94c" stroke-width="1.2" opacity=".35"/>
  <g stroke="#e3b95a" stroke-width="2" fill="#e3b95a" stroke-linecap="round" stroke-linejoin="round" opacity=".9">
    {rune_ring()}
  </g>

  <g filter="url(#shadow)">
    <!-- fur mantle -->
    <path d="M24 540 C 40 452, 120 410, 196 414 L 256 462 L 316 414 C 392 410, 472 452, 488 540 Z" fill="url(#furG)"/>
    {fur_trim()}

    <!-- side braids (the dreads) -->
    {side_l}
    {bead(150, end_l)}
    {side_r}
    {bead(362, end_r)}

    <!-- horns -->
    <path d="M168 176 C 122 176, 86 146, 88 80 C 106 122, 132 138, 172 140 Z" fill="url(#hornG)" stroke="#5a4a2e" stroke-width="2.5"/>
    <path d="M344 176 C 390 176, 426 146, 424 80 C 406 122, 380 138, 340 140 Z" fill="url(#hornG)" stroke="#5a4a2e" stroke-width="2.5"/>
    <path d="M150 172 C 146 160, 146 150, 152 140 M134 168 C 128 156, 129 146, 136 136
             M362 172 C 366 160, 366 150, 360 140 M378 168 C 384 156, 383 146, 376 136"
          stroke="#7a6438" stroke-width="3" fill="none" stroke-linecap="round"/>

    <!-- face -->
    <path d="M170 214 L342 214 C 346 262, 338 304, 318 330 L194 330 C 174 304, 166 262, 170 214 Z" fill="url(#skinG)"/>
    <!-- war paint band -->
    <path d="M168 240 L 344 236 L 340 268 L 322 262 L 306 272 L 288 264 L 256 270 L 224 264 L 206 272 L 190 262 L 172 268 Z"
          fill="#17335c" opacity=".92"/>
    <!-- eye sockets + glowing eyes -->
    <ellipse cx="214" cy="252" rx="22" ry="9" fill="#06101f"/>
    <ellipse cx="298" cy="252" rx="22" ry="9" fill="#06101f"/>
    <g filter="url(#glow)" fill="#a8f0ff">
      <path d="M198 253 Q 214 245 230 251 Q 214 258 198 253 Z"/>
      <path d="M314 253 Q 298 245 282 251 Q 298 258 314 253 Z"/>
    </g>
    <circle cx="216" cy="251.5" r="2.4" fill="#ffffff"/><circle cx="296" cy="251.5" r="2.4" fill="#ffffff"/>
    <!-- brows, angry -->
    <path d="M186 232 L 238 242 L 236 249 L 184 239 Z" fill="#8e3510"/>
    <path d="M326 232 L 274 242 L 276 249 L 328 239 Z" fill="#8e3510"/>
    <!-- cheek scar -->
    <path d="M318 278 L 330 300 M321 283 l6 -2 M325 291 l6 -2" stroke="#8a4a35" stroke-width="2.4" stroke-linecap="round"/>

    <!-- beard -->
    <path d="M170 266 C 156 330, 166 398, 206 440 L 232 458 L 256 468 L 280 458 L 306 440 C 346 398, 356 330, 342 266
             C 332 300, 300 322, 256 322 C 212 322, 180 300, 170 266 Z" fill="url(#beardG)"/>
    {beard_strands}
    <!-- mouth -->
    <path d="M232 334 Q 256 344 280 334 Q 256 338 232 334 Z" fill="#3a1206"/>
    <!-- mustache -->
    <path d="M256 296 C 228 288, 198 298, 174 330 C 168 346, 180 356, 190 346 C 208 324, 234 318, 256 314
             C 278 318, 304 324, 322 346 C 332 356, 344 346, 338 330 C 314 298, 284 288, 256 296 Z"
          fill="#d96a28" stroke="#7f2f0c" stroke-width="2"/>
    <!-- nose tip below the nasal guard -->
    <path d="M244 292 Q 256 304 268 292" stroke="#9b5a3e" stroke-width="3" fill="none" stroke-linecap="round"/>

    <!-- beard braids -->
    {beard_l}
    {beard_r}
    {bead(236, end_bl)}
    {bead(276, end_br)}

    <!-- helmet dome -->
    <path d="M152 212 C 150 124, 200 90, 256 90 C 312 90, 362 124, 360 212 Z" fill="url(#steelG)" stroke="#2b333b" stroke-width="3"/>
    <path d="M249 92 L 263 92 L 266 210 L 246 210 Z" fill="#c8d2dc" stroke="#2b333b" stroke-width="2"/>
    <path d="M180 132 C 200 108, 226 100, 246 98" stroke="#ffffff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".55"/>
    <!-- brim + rivets -->
    <rect x="146" y="202" width="220" height="24" rx="8" fill="url(#brimG)" stroke="#232a31" stroke-width="2.5"/>
    {rivets}
    <!-- spectacle guard around the eyes, with nasal -->
    <path d="M176 222 C 176 252, 196 268, 216 268 C 232 268, 244 258, 246 246 L 246 222 Z" fill="none" stroke="#56626e" stroke-width="7"/>
    <path d="M336 222 C 336 252, 316 268, 296 268 C 280 268, 268 258, 266 246 L 266 222 Z" fill="none" stroke="#56626e" stroke-width="7"/>
    <path d="M244 220 L 268 220 L 264 290 Q 256 298 248 290 Z" fill="url(#steelG)" stroke="#2b333b" stroke-width="2.5"/>

    <!-- cloak brooch -->
    <circle cx="150" cy="452" r="22" fill="url(#goldG)" stroke="#5e420e" stroke-width="3"/>
    <path d="M150 436 L 162 452 L 150 468 L 138 452 Z M150 444 L 156 452 L 150 460 L 144 452 Z" fill="none" stroke="#5e420e" stroke-width="2.5"/>
  </g>
</svg>
'''

with open(os.path.join(OUT, "olafthedread7-avatar.svg"), "w") as f:
    f.write(svg)
print("wrote svg")
