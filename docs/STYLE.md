# Campus Fund Shorts: house style

Reverse-engineered on 2026-10-14 from 14 Shorts on the [Campus Fund YouTube channel](https://www.youtube.com/channel/UCsBjeUtTyD10A38duoiDh4w/shorts)
(also posted to Instagram [@campus.fund](https://www.instagram.com/campus.fund/)). We only had storyboards (about 1 fps), titles, descriptions
and view counts; the sandbox couldn't download the full videos because YouTube requires a PO token from datacenter IPs.
Treat timings as ±0.5 s.

**Target platform:** YouTube Shorts first. Reels use the same 9:16 master, and Instagram itself requires a login.

## The three formats on the channel

| Format | Examples (views) | Length | What it looks like |
|---|---|---|---|
| **A. Fireside / founder-visit clip** (current series, Oct 2026) | Kiran Mazumdar-Shaw "secretary" (504), "Dreaming of being a billionaire" (29), Sama law firm (21), Pranjal Sinha "Bootstrapped 7 years" (45), "Got traction? Don't open up too fast" (107) | 27–65 s | One speaker, interview-cut, punch-ins between wide and single. Hook card at the top for the first 2–4 s, magenta name lower-third, word-by-word captions, uppercase magenta "stamp" words on key phrases, a cream serif quote card mid-video (founder-visit episodes), and a navy Campus Fund end card |
| **B. Pitch clip** (FutureX / Grand Challenge) | Circuitevolve (563), Supermanager AGI (119), 12 more | 40–65 s | Founder on stage at the lectern, static or slow punch-in, plain sentence captions (small white, lower-centre). No hook card. Title = "<Startup> Pitch" |
| **C. Designed brand pieces** (2025, agency-made) | "Campus Fund 3 $100M is Live!" (1,959, best on channel), "Are you from a small city?" (911) | 43–99 s | Heavy motion design: pink gradient cards, 3D icons, maps, cutouts, an event-recap montage with giant yellow type ("OUR BOLDEST CHAPTER YET"). Hard to automate; out of scope for the pipeline except the event-recap montage |

The pipeline targets **A** (the main output) and **B** (bulk output from event footage). The Remotion `Reel` composition implements A,
and B is A with the hook, stamps and cards switched off.

## Visual spec (format A)

| Element | Spec | Remotion prop |
|---|---|---|
| Canvas | 1080×1920, 30 fps, H.264, −14 LUFS | — |
| Hook | First 2–4 s. Two variants: **box**, a white rounded card with black bold sentence-case text ("They thought she was the secretary.", "Her advice to founders who just want to be billionaires"); **stamp**, uppercase white on magenta strips, one strip per line ("BOOTSTRAPPED 7 YEARS. / THEN HE RAISED.", "WHAT MAKES A GOOD LAWYER?") | `hook: {text, style: 'box' \| 'stamp', durationMs}` |
| Name lower-third | Under the hook, top-left: magenta block with the name, white block with the role ("Kiran Mazumdar-Shaw / Founder, Biocon") | `speaker: {name, role, fromMs, durationMs}` |
| Captions | 2–4 words per page, bold sans, white with a dark outline, **active word magenta**, lower-middle (above the platform UI) | `captions` (from `tools/transcribe.py`) |
| Emphasis stamps | 1–3 per video on the key phrase ("NOT", "AVOID DISPUTES", "DON'T COMPLAIN", "GROW WITH", "CONFIDENCE"). Big uppercase on magenta, centre screen, slight tilt; captions hide while one is up | `emphasis: [{text, startMs, endMs}]` |
| Quote card | Full-screen cream card, small grey kicker, large serif line, smaller serif sub-line ("WHAT DO I WANT? / I want to be heard / Before the law. Before positions."). 1–2 s | `quoteCards: [...]` |
| End card | About 2.5 s. Campus Fund logo (white) on a navy→purple radial gradient, tagline "Powering **fearless student entrepreneurs** challenging the status quo!" | `endCard: true` |
| Optional B-roll | Exterior/office walk-through and a team group photo before the end card (Sama episode) | cut in the edit |

**Brand tokens** (`remotion/src/brand.ts`): magenta `#ED168B` and navy `#283781`, both sampled from the logo file; Montserrat 600/800/900 (captions,
hooks, stamps); Marcellus (quote cards; it is also the website's serif). Logos are in `remotion/public/brand/`.

## Editorial rules

- **Title:** `<Curiosity hook> | <Name> #Shorts`, e.g. "Bootstrapped for 7 Years: Then He Raised | Pranjal Sinha #Shorts".
- **Description:** two or three sentences of context (who, where: "Our founder Richa Bajpai sat down with… for a Campus Fund fireside chat"),
  a takeaway, a save/CTA line ("Save this for the day the grind gets loud."), then hashtags `#Shorts #Startups #StudentFounders #CampusFund`.
- **Pick moments that answer a founder question** (strategy doc: "every clip should answer a real founder question"). Pillars: Founder Magnet,
  Founder Stories, Conviction POV, Category Intelligence, Access & Process, VC/LP Trust.
- **Open on the line, not the lead-in.** The hook card paraphrases the payoff and the first spoken word starts within 0.5 s.
- **Length:** 30–60 s. The channel's best performers were 43 s.
- **Performance context:** views are low (21–1,959). The designed, emotional pieces (format C) and the first-person "small city" story
  outperform the talking heads, and the pitch clips are flat at 12–563. The quickest lever is stronger hooks and tighter cuts on format A.
