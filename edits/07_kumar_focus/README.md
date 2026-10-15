# 07_kumar_focus: "The only thing I optimise" (Kumar Vembu, Campus Fund fireside, 1 Sept 2025)

Source: Drive folder 1eAfYloWtKzXI_yKfY6dWdb0eksRIEG2j, clips `C5790.MP4` (host question, 10 s) and `C5793.MP4` (34 s), both 16:9 4K.
Delivery copy: `output/07_kumar_focus_reel_29mb.mp4` (two-pass x264, sized for the 30 MB chat limit; the crf 18 master is the file above).
Output: `output/07_kumar_focus_reel.mp4`, 33.7 s (31.1 s cut + 2.5 s end card), 1080x1920 @ 30 fps, -13.5 LUFS.

Rebuild (needs the two raw clips in `input/drive/raw/`): same recipe as `edits/06_cashmere/README.md` with
    C5790: crop=1215:2160:315:0   (Kumar, camera left, listening while the host asks)
    C5790: crop=1215:2160:2465:0  (Shifa Garg, camera right, for "right? So what's your advice?")
    C5793: crop=1215:2160:929:0   (Kumar medium, keeps the audience member in the right foreground out of frame)
then assemble edl_a / edl_a2 / edl_b, concat, `python edits/07_kumar_focus/build_props.py`, Remotion render, loudnorm.

Edit notes:
- Opener is the host's question over Kumar listening ("the roots should be stronger for you to become a larger tree"), with the hook card on top,
  then a short cut to Shifa Garg (Campus Fund) for "right? So what's your advice?" with her lower-third.
- Kumar's credit reads "Co-founder Zoho, Founder GoFrugal" (lower-third and hook).
- C5793 with the "uh"s and the 4 s pause before "for me" removed; ends on "that is the only thing I optimise." and drops the trailing
  "that means everything else I do" which the camera cut off.
- ASR fix: "optimism" -> "optimise".
- Hook (box): "He co-founded Zoho, then built GoFrugal. He optimises for one thing." Stamps: DON'T JUGGLE / WILLING TO PAY / KEEP USING IT.
- "Optimised for success, whatever it takes" (C5786 0:03 to 0:10) is the host's reaction to Amit, not Kumar's line, and a wide three-shot; not used.
- Picture: C5793 is slightly soft on Kumar (the lens was on the foreground). Fine on a phone, visible on a monitor.

Suggested title: The Only Sign Your Product Is Working | Kumar Vembu #Shorts
Suggested description:
  Don't juggle multiple balls. Kumar Vembu, co-founder of Zoho and founder of GoFrugal, on the one thing he optimises for: customers adopting the product,
  paying for it, and continuing to use it. Everything else follows.
  From our Campus Fund fireside chat with student founders.
  Save this for the next time a new feature looks more exciting than the customer.
  #Shorts #Startups #StudentFounders #CampusFund #ProductMarketFit #SaaS
