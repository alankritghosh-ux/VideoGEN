"""Remap word timings through the two EDLs (C5790 host question, then C5793) into Remotion captions + props."""
import json
E = 'edits/07_kumar_focus'
OVR_A = {}
OVR_B = {31.22: 'optimise.', 2.15: '', 2.23: ''}  # ASR "optimism" -> optimise; drop the "you know" inside "juggle multiple balls"
SOURCES = [(f'{E}/edl_a.json', 'input/drive/tx/C5790.whisper.json', OVR_A), (f'{E}/edl_a2.json', 'input/drive/tx/C5790.whisper.json', OVR_A),
           (f'{E}/edl_b.json', 'input/drive/tx/C5793.whisper.json', OVR_B)]
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
    'clip': 'clips/07_kumar_focus_cut.mp4', 'durationSec': round(t, 3), 'captions': caps,
    'hook': {'text': 'He co-founded Zoho, then built GoFrugal.\nHe optimises for one thing.', 'style': 'box', 'durationMs': 3600},
    'speakers': [{'name': 'Kumar Vembu', 'role': 'Co-founder Zoho, Founder GoFrugal', 'fromMs': 400, 'durationMs': 3200},
                 {'name': 'Shifa Garg', 'role': 'Campus Fund', 'fromMs': at(1, 6.17), 'durationMs': 2300},
                 {'name': 'Kumar Vembu', 'role': 'Co-founder Zoho, Founder GoFrugal', 'fromMs': at(2, 13.57), 'durationMs': 2600}],
    'emphasis': [{'text': "DON'T JUGGLE", 'startMs': at(2, 1.75), 'endMs': at(2, 1.75) + 1400},
                 {'text': 'WILLING\nTO PAY', 'startMs': at(2, 19.09), 'endMs': at(2, 19.09) + 1500},
                 {'text': 'KEEP\nUSING IT', 'startMs': at(2, 23.49), 'endMs': at(2, 23.49) + 1500}],
    'quoteCards': [], 'endCard': True}
json.dump(props, open(f'{E}/props.json', 'w'), indent=1)
print(f'{t:.2f}s, {len(caps)} words;', ''.join(c['text'] for c in caps))
