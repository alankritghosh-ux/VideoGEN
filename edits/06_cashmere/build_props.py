"""Remap word timings through the two EDLs (C5744 then C5776) into Remotion captions + props. Run after assemble.py."""
import json
E = 'edits/06_cashmere'
# per-source-time overrides (word start -> text), '' drops the word
OVR_A = {50.87: 'in', 52.41: 'than', 70.13: 'than', 71.33: 'goats.', 68.73: 'pullovers.', 69.05: '', 73.91: 'Now,', 17.45: '', 27.85: ''}
OVR_B = {0.41: 'a digital', 3.13: 'at point', 5.75: 'digital'}
SOURCES = [(f'{E}/edl.json', 'input/drive/tx/C5744.whisper.json', OVR_A), (f'{E}/edl_b.json', 'input/drive/tx/C5776.whisper.json', OVR_B)]
caps, t, marks = [], 0.0, {}
for k, (edl_path, tx, ovr) in enumerate(SOURCES):
    edl = json.load(open(edl_path))
    words = [w for s in json.load(open(tx))['segments'] for w in s['words']]
    for s in edl['segments']:
        for w in words:
            mid = (w['start'] + w['end']) / 2
            if s['in'] <= mid <= s['out']:
                text = ovr.get(round(w['start'], 2), w['word'])
                if text == '':
                    continue
                a = max(w['start'], s['in']) - s['in'] + t
                b = min(w['end'], s['out']) - s['in'] + t
                caps.append({'text': (' ' if caps else '') + text, 'startMs': round(a * 1000), 'endMs': round(b * 1000),
                             'timestampMs': round(a * 1000), 'confidence': None})
                marks[(k, round(w['start'], 2))] = round(a * 1000)
        t += s['out'] - s['in']
at = lambda k, src: marks[(k, src)]
props = {
    'clip': 'clips/06_cashmere_cut.mp4', 'durationSec': round(t, 3), 'captions': caps,
    'hook': {'text': 'Shops sell 10x more cashmere\nthan goats can produce.', 'style': 'box', 'durationMs': 3400},
    'speakers': [{'name': 'Amit Gautam', 'role': 'Founder, TextileGenesis', 'fromMs': 400, 'durationMs': 3000},
                 {'name': 'Amit Gautam', 'role': 'Founder, TextileGenesis', 'fromMs': at(0, 82.89), 'durationMs': 2600}],
    'emphasis': [{'text': '10X MORE', 'startMs': at(0, 64.09), 'endMs': at(0, 64.09) + 1500},
                 {'text': 'FRAUD AND\nCORRUPTION', 'startMs': at(0, 43.03), 'endMs': at(0, 43.03) + 1100},
                 {'text': '7 YEARS.\nNO ONE ELSE.', 'startMs': at(1, 9.09), 'endMs': at(1, 9.09) + 1900}],
    'quoteCards': [], 'endCard': True}
json.dump(props, open(f'{E}/props.json', 'w'), indent=1)
print(f'{t:.2f}s, {len(caps)} words;', ''.join(c['text'] for c in caps))
