# 02_simputer: "India built a tablet before the iPad" (Kiran Mazumdar-Shaw fireside)

Source: `02_simputer.mp4` (Drive folder 1V2BiCmTRP50jxOX1hmuyEHXklwtvRDX6), 67.6 s, 25 fps. Already edited with a
burned-in hook card (0-3.9 s), name tag (3.9-8.0 s) and word captions (y 1300-1395).
Output: `output/02_simputer_viral.mp4`, 47.8 s (45.2 s cut + 2.5 s end card), 1080x1920 @ 30 fps, -14.1 LUFS.

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
- Only five segments and four joins, every join on a pause: after "commercialise it.", after "computer." (before her
  "Yes."), the 0.9 s silence before "license it", and the comma after "tablets," (dropping "economies of scale / ahead
  of the curve"). Each join is a 0.16-0.20 s dissolve with a matching audio crossfade (`dissolve` in the EDL), the
  crop pans so the face lands in the same place on both sides, and every segment slowly pushes in (1.50 -> 1.60)
  instead of a static punch. The last frame holds 0.5 s so "licensed." lands before the end card.
  v1 of this edit had eleven hard jump cuts, several mid-sentence; it read as stitched.
- Burned-in captions are cropped out: every crop keeps its bottom edge above y=1295, centred on the face (MediaPipe
  BlazeFace, `work/simputer/faces.json`). Fresh house-style captions come from the Parakeet transcript re-timed onto
  the cut (`tools/remap_captions.py`). Cost: ~1.5x upscale, visibly softer than the source on a monitor, fine on a phone.
- Dropped: the "Can you imagine" lead-in and "How do you teach standardised education to millions" (a tangent).
  67.6 s -> 45.2 s.
- Old name tag ends at 7.98 s and "Simputer" starts at 8.14 s, so that segment starts at 8.00.
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
