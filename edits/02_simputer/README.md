# 02_simputer: "India built a tablet before the iPad" (Kiran Mazumdar-Shaw fireside)

Source: `02_simputer.mp4` (Drive folder 1V2BiCmTRP50jxOX1hmuyEHXklwtvRDX6), 67.6 s, 25 fps. Already edited with a
burned-in hook card (0-3.9 s), name tag (3.9-8.0 s) and word captions (y 1300-1395).
Output: `output/02_simputer_viral.mp4`, 48.8 s (46.2 s cut + 2.5 s end card), 1080x1920 @ 30 fps, -14.1 LUFS.

Rebuild:
    python tools/transcribe.py input/02_simputer.mp4 --out work/simputer/tr
    python tools/assemble.py edits/02_simputer/edl.json work/simputer/cut.mp4
    python tools/remap_captions.py work/simputer/tr.captions.json work/simputer/cut.mp4.timeline.json \
        edits/02_simputer/captions.json --fix edits/02_simputer/caption_fixes.json
    cp work/simputer/cut.mp4 remotion/public/clips/02_simputer_cut.mp4
    cd remotion && npx remotion render src/index.ts Reel ../work/simputer/render.mp4 --props=../edits/02_simputer/props.json --crf=16
    ffmpeg -i work/simputer/render.mp4 -c:v libx264 -crf 18 -preset slow -af loudnorm=I=-14:TP=-1:LRA=11 -c:a aac -b:a 192k -movflags +faststart output/02_simputer_viral.mp4

Changes vs the original:
- Cold open on the claim ("this predated the iPad... the Palm Pilot... everything you can think of. But we missed the
  boat. Why? Because they didn't know how to commercialise it."), then what the Simputer was, what happened (40,000
  units, too late, iPad took over) and the lesson (a million-unit government order).
- Five spoken segments and four joins, every join on a pause: after "commercialise it.", after "computer." (before
  her "Yes."), the 0.9 s silence before "license it", and the comma after "tablets," (dropping "economies of scale /
  ahead of the curve"). Joins are hard cuts with a snap punch-in (`punch_from`, 0.25 s ease), alternating wide
  (1.50) and tight (1.62) like the channel's own edits. No dissolves: a dissolve between two near-identical shots of
  one person double-exposes her face; v2/v3 of this edit did that and read as scrappy. v1 had eleven jump cuts.
- Two of the source's punch-ins land on a segment's last word (38.16 "it.", 16.84 "compu-ter."). Those joins are
  bridged with a reaction shot of Richa listening (`video_in` from the 53.0-55.04 cutaway, 0.57-0.64 s) under
  Kiran's audio, which is how an editor hides a jump: Kiran -> Richa -> Kiran on a punch-in.
- The crop follows the face: `cx_keys` are MediaPipe face positions (`work/simputer/faces.json`) smoothed within each
  of the source's own shots, with a one-frame re-centre step on the source's punch-in cuts (29.92, 35.72, 53.0,
  55.04). Every segment slowly drifts (about 5%) so nothing is static.
- The last frame holds 0.6 s so "licensed." (the source stops dead on it) lands, and the end card fades in over
  10 frames (Reel change).
- Burned-in captions are cropped out: every crop keeps its bottom edge above y=1295, centred on the face (MediaPipe
  BlazeFace, `work/simputer/faces.json`). Fresh house-style captions come from the Parakeet transcript re-timed onto
  the cut (`tools/remap_captions.py`). Cost: ~1.5x upscale, visibly softer than the source on a monitor, fine on a phone.
- Dropped: the "Can you imagine" lead-in and "How do you teach standardised education to millions" (a tangent).
  67.6 s -> 45.2 s.
- Old name tag ends at 7.98 s and "Simputer" starts at 8.14 s, so that segment starts at 8.08 (input seeking can land a frame early; at 8.00 the tag ghosted through the dissolve).
- Hook box "India built a tablet in 2000, before the iPad. So what went wrong?", name lower-third, stamps
  MISSED THE BOAT and TOO LATE, end card.
- Motion-interpolated 25->30 fps (`minterpolate` mci) was tried and rejected: it smears her hands. Frames are duplicated.

Suggested title: India Built a Tablet Before the iPad. Then Lost It | Kiran Mazumdar-Shaw #Shorts
Suggested description:
  The Simputer was the world's first handheld, multilingual, GPRS-connected computer, built in India in 2000.
  Kiran Mazumdar-Shaw on why it never took off: nobody knew how to commercialise it, and by the time a private
  company made 40,000 units, the iPad had taken the market. One government order could have changed that.
  From our Campus Fund fireside chat at Biocon with founder Richa Bajpai.
  Save this for the next time someone tells you the product is the hard part.
  #Shorts #Startups #StudentFounders #CampusFund #Simputer #MakeInIndia

Caption pages never straddle a join: `pageBreaksMs` in props.json (the join times from the timeline) forces a new
page there (Reel prop added for this edit).
