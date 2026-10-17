# Sourcing raw clips for founder-lore reels (format D)

Tested from the cloud sandbox on 2026-10-17. "Works" means the sandbox fetched real bytes, not just a 200 on the homepage.

## What works from the sandbox

| Source | How | Rights | Notes |
|---|---|---|---|
| **NASA Image and Video Library** | `https://images-api.nasa.gov/search?q=<query>&media_type=video`, then the item's `collection.json` lists `~orig/~large/~medium/~small.mp4`. Pull only the minutes you need: `ffmpeg -ss <s> -t <len> -i "<url>" -c copy out.mp4` (range requests work) | **Public domain** (NASA-produced; credit "NASA") | Musk at the Demo-2 press conference (30 May 2020), Crew-2, the in-flight abort presser, Bridenstine's SpaceX HQ visit, launch footage. `~orig` is 7.7 GB for an hour; `~medium` is 720p and enough for a letterboxed window |
| **Internet Archive** | `https://archive.org/advancedsearch.php?q=<q>+AND+mediatype:movies&fl[]=identifier&fl[]=licenseurl&output=json`, then `https://archive.org/metadata/<id>` for the file list and `https://archive.org/download/<id>/<file>` (about 5 MB/s) | Mixed: check `licenseurl`; many items are uploads of copyrighted keynotes (usable only as short quoted clips) | Jobs: SIGGRAPH '95 keynote (`siggraph95keynote-stevejobs`, VHS digitised by IA), WWDC 1998 (`open-kynt`), Macworld Tokyo 1999, Apple Expo Paris 2000, "Celebrating Steve". Narayana Murthy: "Chai with Manjula". **Skip the TV News Archive items** (CNBC, Bloomberg, RT, CNN): stream-only and not ours to use |
| **Wikimedia Commons** | `https://commons.wikimedia.org/w/api.php?action=query&list=search&srnamespace=6&srsearch=<q>&format=json` with a `User-Agent` header (the API returns nothing without one), then `prop=imageinfo&iiprop=url|extmetadata` for the licence | Per file: PD, CC-BY, CC-BY-SA; reject NC | Stills for Ken Burns shots. Jobs: 1984 Gotfryd portrait (PD, Library of Congress, 3340×4918), 1972 Homestead yearbook (PD), WWDC07 (CC-BY-SA 2.0), 2010 headshot (CC-BY-SA 3.0). Few videos |
| **Openverse** | `https://api.openverse.org/v1/images/?q=<q>&license=by,by-sa,pdm,cc0` | CC / PD, filterable | Aggregates Commons + Flickr + museums; good for finding CC stills across sources |
| **Flickr API** | `https://www.flickr.com/services/rest/` (needs a free API key, `license=4,5,9,10` for BY/BY-SA/CC0/PD) | CC, filterable | SpaceX's own Flickr is CC0 / public domain: launch and pad photos |
| **Library of Congress** | `https://www.loc.gov/search/?q=<q>&fo=json` | Mostly PD | Historical portraits and newsreels (pre-1990 founders: Ford, Edison, Disney) |
| **Dailymotion** | `yt-dlp "<url>"` works without cookies | Copyrighted; quoted clips only | Thin on founder content |
| **Google Drive (our own footage)** | The Drive connector in this session lists the fireside folder (`1V2BiCmTRP50jxOX1hmuyEHXklwtvRDX6`: `02_simputer.mp4`, `05_space.mp4`, ...). For files shared **"anyone with the link"**, `gdown <file-id> -O input/<name>.mp4` fetches them straight into `input/` (tested: `05_space.mp4`, 131 MB, about 27 MB/s) | Ours | The cleanest route for anything the user downloads at home: drop it in the Drive folder, share by link, say the file name |

## What does not work from the sandbox

| Source | Symptom | Workaround |
|---|---|---|
| **YouTube** via `yt-dlp` | "Sign in to confirm you're not a bot" (datacenter IP; PO-token flow) | (a) Export a `cookies.txt` from a logged-in browser and put it at `input/cookies.txt` (gitignored); `yt-dlp --cookies input/cookies.txt <url>` usually passes. (b) Run the `bgutil-ytdlp-pot-provider` plugin plus its Node token server; the project itself now says PO tokens no longer pass the check in most cases, so treat it as best-effort. (c) Download at home and share via Drive. See the [yt-dlp PO Token Guide](https://github.com/yt-dlp/yt-dlp/wiki/PO-Token-Guide) |
| **Vimeo** via `yt-dlp` | "The web client only works when logged-in" | Cookies, as above |
| **C-SPAN** | 403 at the edge | None from here; user-side download |
| **Pexels / Pixabay** stock APIs | 401 / 400 without an API key | Free keys; put them in the environment's secrets. Only useful for B-roll (rockets, cities), not founders |
| **Getty, Storyblocks, Videvo** | Pages load; licensed stock, paid | Buy per clip if a piece needs a specific archive shot |

## Rights, in practice

1. Public domain first (NASA, LoC, PD Commons files). 2. CC-BY / CC-BY-SA with on-screen credit. 3. Our own footage.
4. Short quoted clips (≤ 15 s, founder's own words, with our title and bridge line as commentary). 5. Never: TV-network
recordings, documentary excerpts, unlicensed music. Full rules in `docs/STYLE.md`, format D.

## A working recipe

```bash
# 1. Find it
curl -s 'https://images-api.nasa.gov/search?q=elon%20musk&media_type=video' | python3 -m json.tool | grep -E 'nasa_id|title'
# 2. Pull only the window you need (times from the SRT if NASA ships one; Demo-2's was empty, so transcribe instead)
ffmpeg -ss 240 -t 120 -i "https://images-assets.nasa.gov/video/<id>/<id>~medium.mp4" -c copy input/archive/<name>.mp4
# 3. Word timings
python tools/transcribe.py input/archive/<name>.mp4 --out work/archive/<name>
# 4. Cut (letterboxed), re-time captions onto the cut, render Lore
python tools/assemble.py edits/<x>/edl.json work/<x>/cut.mp4
python tools/edl_captions.py edits/<x>/edl.json work/<x>/cut.mp4.timeline.json work/archive/<name>.whisper.json work/<x>/cut.captions.json
```

Pulled so far (gitignored, `input/archive/`): NASA Demo-2 post-launch presser (first 25 min at 360p, Musk's two minutes at 720p),
Jobs SIGGRAPH '95 keynote (archive.org, 640×360, 26 min; the Pixar "twenty years climbing the wall of the castle" passage is at
23:49, "the first computer-animated feature" close at 25:19).
