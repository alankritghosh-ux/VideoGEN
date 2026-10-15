"""Remap C5744 word timings through the EDL into Remotion captions + props. Run after assemble.py."""
import json, sys
E = 'edits/06_cashmere'
edl = json.load(open(f'{E}/edl.json'))
words = [w for s in json.load(open('input/drive/tx/C5744.whisper.json'))['segments'] for w in s['words']]
# per-source-time overrides (start time -> text), '' drops the word
OVR = {50.87: 'in', 52.41: 'than', 70.13: 'than', 71.33: 'goats.', 68.73: 'pullovers.', 69.05: '', 73.91: 'Now,', 17.45: '', 27.85: '', 91.51: '', 86.31: '', 98.04: ''}
caps, t = [], 0.0
for s in edl['segments']:
    for w in words:
        mid = (w['start'] + w['end']) / 2
        if s['in'] <= mid <= s['out']:
            text = OVR.get(round(w['start'], 2), w['word'])
            if text == '':
                continue
            a = max(w['start'], s['in']) - s['in'] + t
            b = min(w['end'], s['out']) - s['in'] + t
            caps.append({'text': (' ' if caps else '') + text, 'startMs': round(a * 1000), 'endMs': round(b * 1000),
                         'timestampMs': round(a * 1000), 'confidence': None})
    t += s['out'] - s['in']
def at(src):  # source time -> timeline ms
    tt = 0.0
    for s in edl['segments']:
        if s['in'] <= src <= s['out']:
            return round((src - s['in'] + tt) * 1000)
        tt += s['out'] - s['in']
    raise SystemExit(f'{src} not in cut')
props = {
    'clip': 'clips/06_cashmere_cut.mp4', 'durationSec': round(t, 3), 'captions': caps,
    'hook': {'text': 'Shops sell 10x more cashmere\nthan goats can produce.', 'style': 'box', 'durationMs': 3400},
    'speakers': [{'name': 'Amit Gautam', 'role': 'Founder, TextileGenesis', 'fromMs': 400, 'durationMs': 3000},
                 {'name': 'Amit Gautam', 'role': 'Founder, TextileGenesis', 'fromMs': at(82.9), 'durationMs': 2600}],
    'emphasis': [{'text': '10X MORE', 'startMs': at(64.09), 'endMs': at(65.6)},
                 {'text': 'FRAUD AND\nCORRUPTION', 'startMs': at(43.03), 'endMs': at(44.1)},
                 {'text': 'ONE KILO.\nONE COIN.', 'startMs': at(99.24), 'endMs': at(100.7)}],
    'quoteCards': [], 'endCard': True}
json.dump(props, open(f'{E}/props.json', 'w'), indent=1)
print(f'{t:.2f}s, {len(caps)} words;', ' '.join(c['text'] for c in caps))
