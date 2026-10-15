# 06_cashmere: "10x more cashmere than goats" (Amit Gautam, Campus Fund fireside, 1 Sept 2025)

Source: Drive folder 1eAfYloWtKzXI_yKfY6dWdb0eksRIEG2j, clips `C5744.MP4` (105 s, 16:9 4K) and `C5776.MP4` (28 s, portrait 4K).
Output: `output/06_cashmere_reel.mp4`, 54.7 s (delivery copy `output/06_cashmere_reel_29mb.mp4`, two-pass x264 sized for the 30 MB chat limit) (52.1 s cut + 2.5 s end card), 1080x1920 @ 30 fps, -14.2 LUFS.

Rebuild (needs the two raw clips in `input/drive/raw/`):
    ffmpeg -ss 14 -to 102 -i input/drive/raw/C5744.MP4 -vf "crop=1215:2160:1428:0,scale=1080:1920:flags=lanczos,curves=m='0/0 0.2/0.12 0.5/0.5 0.8/0.86 1/1',eq=saturation=1.45:contrast=1.03,fps=30,format=yuv420p" -c:v libx264 -crf 14 -c:a aac -b:a 320k work/cashmere/precut.mp4
    ffmpeg -i input/drive/raw/C5776.MP4 -vf "scale=1080:1920:flags=lanczos,curves=m='0/0 0.2/0.12 0.5/0.5 0.8/0.86 1/1',eq=saturation=1.45:contrast=1.03,fps=30,format=yuv420p" -c:v libx264 -crf 14 -c:a aac -b:a 320k work/cashmere/precut_5776.mp4
    # edl.json / edl_b.json carry source times; subtract src_offset (14 s for C5744) before assemble.py
    python tools/assemble.py work/cashmere/edl_precut.json work/cashmere/cut_a.mp4
    python tools/assemble.py work/cashmere/edl_b_precut.json work/cashmere/cut_b.mp4
    ffmpeg -f concat -safe 0 -i work/cashmere/concat.txt -c copy work/cashmere/cut.mp4
    cp work/cashmere/cut.mp4 remotion/public/clips/06_cashmere_cut.mp4
    python edits/06_cashmere/build_props.py
    cd remotion && npx remotion render src/index.ts Reel ../work/cashmere/render.mp4 --props=../edits/06_cashmere/props.json --crf=16
    ffmpeg -i work/cashmere/render.mp4 -c:v libx264 -crf 18 -preset slow -af "arnndn=m=models/rnnnoise/std.rnnn,loudnorm=I=-14:TP=-1:LRA=11" -c:a aac -b:a 192k -movflags +faststart output/06_cashmere_reel.mp4

Edit notes:
- Cold open on the payoff (up to ten times more cashmere claimed than there are cashmere goats), then the setup
  (textile looks simple, eight to nine transformation steps), the organic cotton 5x claim, and "the key idea was we created what we call".
- C5744 pans to an audience listener from 1:26 to 1:43, exactly under the fibre-coin line, so the ending is C5776 instead:
  "a digital twin of the physical material at point of origin... even after seven years no one has been able to launch that."
- Source is flat/log-like; graded with a mild S-curve and +45% saturation. The 16:9 clip is cropped to the speaker (x=1428 of 3840).
- ASR fixes in build_props.py: "quotes" -> "goats", "full overs" -> "pullovers", "and finished" -> "in finished", "then" -> "than".
- Hook (box): "Shops sell 10x more cashmere than goats can produce." Stamps: 10X MORE / FRAUD AND CORRUPTION / 7 YEARS. NO ONE ELSE.

Suggested title: 10x More Cashmere Is Sold Than Goats Can Make | Amit Gautam #Shorts
Suggested description:
  Five times more organic cotton, ten times more cashmere: the fashion supply chain claims far more than farms produce.
  Amit Gautam, founder of TextileGenesis, on the fraud problem he left McKinsey to fix, and the fibre coin that tracks every kilo from origin.
  From our Campus Fund fireside chat with student founders.
  Save this for the next time someone tells you a market is "simple".
  #Shorts #Startups #StudentFounders #CampusFund #Sustainability #Fashion
