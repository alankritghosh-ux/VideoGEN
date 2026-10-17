# 06_musk_18years: "18 years for one launch" (format D pilot, founder lore)

Source: NASA TV, Demo-2 post-launch news conference, Kennedy Space Center, 30 May 2020. **Public domain.**
`input/archive/nasa_demo2/demo2_musk_medium.mp4` = minutes 4:00–6:00 of the `~medium.mp4` (720p) from
`images-api.nasa.gov` (search "elon musk", media_type=video, item "NASA's SpaceX Demonstration Mission 2 Postlaunch News Conference").
Output: `output/06_musk_18years.mp4`, 42.5 s (36.8 s cut + 3.2 s bridge card + 2.5 s end card), 1080x1920 @ 30 fps, -14 LUFS.

Rebuild:
    ffmpeg -ss 240 -t 120 -i "https://images-assets.nasa.gov/video/NASA%E2%80%99s%20SpaceX%20Demonstration%20Mission%202%20Postlaunch%20News%20Conference/NASA%E2%80%99s%20SpaceX%20Demonstration%20Mission%202%20Postlaunch%20News%20Conference~medium.mp4" -c copy input/archive/nasa_demo2/demo2_musk_medium.mp4
    python tools/transcribe.py input/archive/nasa_demo2/demo2_musk_medium.mp4 --out work/archive/musk
    python tools/assemble.py edits/06_musk_18years/edl.json work/musk/cut.mp4
    python tools/edl_captions.py edits/06_musk_18years/edl.json work/musk/cut.mp4.timeline.json work/archive/musk.whisper.json work/musk/cut.captions.json
    # paste cut.captions.json into props.json "captions"; durationSec and bigWords follow cut.mp4.timeline.json
    cp work/musk/cut.mp4 remotion/public/clips/06_musk_cut.mp4
    cd remotion && npx remotion render src/index.ts Lore ../work/musk/render.mp4 --props=../edits/06_musk_18years/props.json --crf=16
    ffmpeg -i work/musk/render.mp4 -c:v libx264 -crf 18 -preset slow -af loudnorm=I=-14:TP=-1:LRA=11 -c:a aac -b:a 192k -ar 48000 -movflags +faststart output/06_musk_18years.mp4

The three beats:
1. Doubt (0–10 s): black title card "18 YEARS / for one launch" with his voice under it ("getting astronauts back to orbit after
   almost a decade"), reveal on "I'm really quite overcome with emotion this day. It's kinda hard to talk, frankly."
2. Dream line (10–15 s): "It's been eighteen years working towards this goal." then the natural pause held with the big word
   EIGHTEEN YEARS. over his face, then "It's hard to believe that's happened."
3. Bigger than life (15–37 s): "right on the heart of anyone who has any spirit of exploration", "a craft made by humans, for humans",
   "something humanity should be excited about and proud of". Bridge card: "He was 30 when SpaceX started. The first three rockets
   failed. Sound familiar?" then the end card.

No music (we hold no licence for a track yet; the piece runs dry, which the genre tolerates). Add one under `input/music/`
and mix at about -22 LUFS when we have it.

Suggested title: 18 Years for One Launch | Elon Musk #Shorts
Suggested description:
  May 30, 2020. Minutes after Crew Dragon put astronauts back in orbit from US soil, Elon Musk sat down at the Kennedy Space Center
  press conference and could barely talk. Eighteen years of work for one launch.
  He was 30 when SpaceX started, and the first three rockets failed. If you are building something nobody believes in yet, this one is for you.
  Footage: NASA TV (public domain).
  #Shorts #Startups #StudentFounders #CampusFund #FounderStories #SpaceX
