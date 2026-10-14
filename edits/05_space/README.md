# 05_space: "Pharma lab in space" (Kiran Mazumdar-Shaw fireside)

Source: `05_space.mp4` (Drive folder 1V2BiCmTRP50jxOX1hmuyEHXklwtvRDX6), 63 s. It was already edited with burned-in captions.
Output: `output/05_space_viral.mp4`, 42.4 s (39.8 s cut + 2.6 s end card), 1080x1920 @ 30 fps, -14.6 LUFS.

Rebuild:
    python tools/assemble.py edits/05_space/edl.json work/space/cut.mp4
    cp work/space/cut.mp4 remotion/public/clips/05_space_cut.mp4
    cd remotion && npx remotion render src/index.ts Reel ../work/space/render.mp4 --props=../edits/05_space/props.json --crf=16
    ffmpeg -i work/space/render.mp4 -c:v libx264 -crf 18 -preset slow -af loudnorm=I=-14:TP=-1:LRA=11 -c:a aac -b:a 192k -movflags +faststart output/05_space_viral.mp4

Changes vs the original:
- Cold open on the payoff line ("don't get driven by a cool idea that it'll remain in space") instead of the setup.
- Cold open -> founder transition: Kiran's video ends on the frame before the original edit's cutaway, the founder reaction shot carries the tail of "space." with an easing punch-in, and the founder starts on a clean caption. The hook and her name tag end exactly at the shot change.
- Fixed the original's swapped name tags (Kiran was labelled "Campus Fund founder" and vice versa). The punch-in crops the old tags out.
- Removed "my my my question to you", the "uh"s and the audience "Nice.". The cut went from 63 s to 39.8 s.
- Punch-in zooms alternate on every cut, and there are 2 emphasis stamps (VERY DIFFICULT MODEL, DON'T STAY IN A COCOON) plus the end card.

Suggested title: Making Medicine in Space? Kiran Mazumdar-Shaw's Reality Check #Shorts
Suggested description:
  A founder pitched satellites the size of a suitcase that manufacture biologics in orbit. Kiran Mazumdar-Shaw's reply:
  figure out the science, then build it on Earth, and don't stay in a cocoon with a cool idea.
  From our Campus Fund fireside chat at Biocon with founder Richa Bajpai.
  Save this for the next time you fall in love with an idea.
  #Shorts #Startups #StudentFounders #CampusFund #SpaceTech #Biotech
