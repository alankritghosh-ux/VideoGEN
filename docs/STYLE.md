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
| Name lower-third | Under the hook, top-left: magenta block with the name, white block with the role ("Kiran Mazumdar-Shaw / Founder, Biocon") | `speakers: [{name, role, fromMs, durationMs}]` |
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

## Format D: Founder lore (archive edit)

Added 2026-10-17. The "founder documentary" genre that media houses and funds post (Founders Podcast clips, a16z, Colin & Samir,
Hormozi's team): archive footage of an A-list founder, one beat of their story, cut to the register of **working towards a dream,
a goal, something bigger than life**. It is the emotional format the channel lacks; the strategy doc says designed, emotional pieces
outperform the talking heads. Campus Fund's twist is the **bridge line**: every piece lands on student founders.

### The three beats (35–50 s)

| Beat | Length | What happens | Graphics |
|---|---|---|---|
| **1. The doubt** | 0–8 s | Cold open on the low point or the boldest claim, in the founder's own voice if a clip exists, else over a Ken Burns still. First spoken word within 0.5 s of the title card ending. | Title card over black for 1.5–2.5 s with the stake in numbers ("18 YEARS / for this moment"), then the archive window and a date/place stamp |
| **2. The dream line** | 8–30 s | The sentence where they state the goal or the dream. Dead air cut, no music swell under the key line, a 0.4 s silence beat before it. | Serif captions under the window; the key phrase alone as a **big word** card over the window (captions hide) |
| **3. The proof + bridge** | 30–45 s | One line of hindsight (what happened next), then the Campus Fund bridge line to student founders | Bridge card (cream, serif), then the standard end card |

One founder, **one** beat. It is not a biography. If the story needs two clips it is two reels.

### Visual spec

| Element | Spec | Remotion prop (`Lore`) |
|---|---|---|
| Canvas | 1080×1920, 30 fps, H.264, −14 LUFS | — |
| Archive window | Source kept at its own aspect (4:3 or 16:9), fitted to 1080 wide, vertically centred at about 44% of the frame height. Fill above and below with the same frame blurred and darkened. Grain, slight vignette, and for colour sources a 15% desaturation so mismatched tapes read as one film. Done in ffmpeg by `tools/assemble.py` (`"letterbox": true` in the EDL); the master is 1080×1920 before Remotion sees it | `clip`, `window: {top, height}` (px, so captions can sit under it) |
| Title card | Black, 1.5–2.5 s. Big number or stake in Marcellus serif (160 px) with a one-line Montserrat sub-line | `title: {big, sub, durationMs}` |
| Date / place stamp | Top-left of the window, IBM Plex Mono 26 px, uppercase, letter-spaced, 70% white: "MAY 30, 2020 · KENNEDY SPACE CENTER" | `stamps: [{text, startMs, endMs}]` |
| Captions | Marcellus serif, 58 px, cream, centred, 2–4 words per page, **active word magenta**, placed in the fill just under the window | `captions` from `tools/transcribe.py` |
| Big word | The key phrase alone, Marcellus 110 px cream, centred over the window on a 60% black scrim, 1–2.5 s, captions hide | `bigWords: [{text, startMs, endMs}]` |
| Still with Ken Burns | For founders with no usable footage: a public-domain or CC photo, slow push 1.00→1.08 over the shot | cut in by the assembler (`"still": "path.jpg"` segment) |
| Source credit | Bottom of the fill, Plex Mono 22 px, 50% white: "Footage: NASA (public domain)" | `credit` |
| Bridge card | Cream card, grey kicker "FOR STUDENT FOUNDERS", serif line, 2–3 s | `bridge: {kicker, text, durationMs}` |
| End card | Standard Campus Fund end card, 2.5 s | `endCard: true` |

Same brand tokens as format A (magenta, navy, cream, Marcellus, Montserrat). The format reads as the same channel, only slower and
quieter. No hook box, no name lower-third, no emphasis stamps: the title card and the stamp do their jobs.

### Audio

- Founder's voice is the lead. Denoise tape hiss lightly (`arnndn`), never to the point of warble.
- Music: slow piano or ambient pad, about −22 LUFS under speech, ducked to silence for the 0.4 s before the dream line, swell under beat 3.
  Only use tracks we hold a licence for (the repo ships none; put them in `input/music/`, gitignored). Without a track, the piece
  runs dry; that is acceptable for the pilot and common in the genre.
- Final: `loudnorm=I=-14:TP=-1:LRA=11`.

### Editorial rules

- **Title:** `<The stake in numbers or the dream line> | <Founder> #Shorts`, e.g. "18 Years for One Launch | Elon Musk #Shorts".
- **Description:** when and where the footage is from, the story in two sentences, the bridge line, a source credit line
  ("Footage: NASA, public domain"), then `#Shorts #Startups #StudentFounders #CampusFund #FounderStories`.
- **Bridge line** is mandatory and specific: "He was 30 and had already failed twice. Sound familiar?" Not "Follow for more".
- Quote accurately. If a famous line is apocryphal (most "Walt Disney" quotes), don't use it.

### Rights rules (in order of preference)

1. **Public domain**: NASA (`images-api.nasa.gov`), US government, Library of Congress, pre-1930 material, photos explicitly PD on
   Wikimedia Commons. No restriction; credit anyway.
2. **Creative Commons**: Commons, Flickr, Openverse, archive.org items with a `licenseurl`. CC-BY and CC-BY-SA are fine with the
   on-screen credit; **CC-NC is not** (a fund's brand channel is commercial use).
3. **Our own footage**: Campus Fund firesides and founder visits (Drive). Use freely.
4. **Quoted clips** of public keynotes and interviews: ≤ 15 s, the founder's own words, with our commentary (title, bridge). This is
   how the whole genre operates and platforms mostly tolerate it, but it is a judgement call for a brand account: prefer 1–3,
   keep clips short, credit the source, and expect an occasional Content ID claim on the music or the clip.
5. **Never**: TV-network recordings (CNBC, Bloomberg, CNN, archive.org's TV News Archive), film and documentary excerpts,
   music we don't hold a licence for.

See `docs/SOURCING.md` for what the sandbox can actually fetch.

### Shortlist: ten founders, one line each

| Founder | The beat | Asset and rights |
|---|---|---|
| **Elon Musk** | Demo-2 post-launch presser, 30 May 2020: "It's been 18 years working towards this goal... I'm really quite overcome with emotion." | NASA TV recording, **public domain**. Pulled; pilot |
| **Steve Jobs** | SIGGRAPH 1995 keynote: Pixar's ten-year road from a hardware company nobody wanted to the first computer-animated feature | archive.org `siggraph95keynote-stevejobs` (VHS). Quoted clip. Pulled |
| **Steve Jobs** | 2005 Stanford commencement, "stay hungry, stay foolish" | Stanford copyright, YouTube only. Quoted clip; needs a user-side download |
| **Kiran Mazumdar-Shaw** | Started Biocon in a garage in 1978 with ₹10,000, 25 years old, no bank would lend to a woman in biotech | Our fireside footage (Drive folder `1V2BiCmTRP50jxOX1hmuyEHXklwtvRDX6`), **ours** |
| **Narayana Murthy** | 1981: Infosys founded with ₹10,000 borrowed from Sudha Murthy; the first computer took a year to import | archive.org "Chai with Manjula" interview (check licence); else stills + text quote |
| **Dhirubhai Ambani** | "Think big, think fast, think ahead. Ideas are no one's monopoly." Yarn trader to Reliance | No PD footage. Stills (Commons, check each licence) + text quote card |
| **Ratan Tata** | "I don't believe in taking right decisions. I take decisions and then make them right." Nano, JLR, the 2008 bet | TV interviews only (not usable). Stills + text quote |
| **Jeff Bezos** | 1997 shareholder letter, "It's all about the long term"; the 1999 interview where he's laughed at | Letter is quotable text; 1999 interview is CNBC (not usable). Stills + text; NASA-shot Blue Origin event footage is PD |
| **Jensen Huang** | "I wish upon you ample doses of pain and suffering" (Stanford GSB, 2024); 30 years to the overnight success | Stanford copyright, YouTube only. Quoted clip; user-side download |
| **Jack Ma** | 1999, the Hupan apartment: "We will make it because we are young and we never give up." | Alibaba's own footage ("Crocodile in the Yangtze"); quoted clip only with a user-side download. Alternative: Davos 2015 text quote |

Pilot: **Elon Musk / Demo-2**, because the footage is public domain and the moment is exactly the theme.
