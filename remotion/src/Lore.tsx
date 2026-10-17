import {createTikTokStyleCaptions, type Caption, type TikTokPage} from '@remotion/captions';
import {Video} from '@remotion/media';
import '@fontsource/ibm-plex-mono/500.css';
import {useMemo} from 'react';
import {AbsoluteFill, Img, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {BRAND, SANS, SERIF} from './brand';

// Format D, "founder lore" (docs/STYLE.md): an archive clip letterboxed by tools/assemble.py
// (`"letterbox": true`), a black title card over the opening, a mono date/place stamp, serif
// captions under the archive window with the active word in magenta, "big word" cards for the
// key phrase, a source credit, a cream bridge card for student founders, then the end card.

const MONO = "'IBM Plex Mono', 'Courier New', monospace";
export const END_CARD_SEC = 2.5;

export type Timed = {text: string; startMs: number; endMs: number};
export type LoreProps = {
  clip: string; // relative to remotion/public, 1080x1920, already letterboxed
  durationSec: number;
  captions: Caption[]; // from tools/transcribe.py, times relative to the cut
  window: {top: number; height: number}; // where the archive picture sits, px
  title?: {big: string; sub?: string; durationMs: number}; // black card over the opening
  stamps?: Timed[]; // "MAY 30, 2020 · KENNEDY SPACE CENTER"
  bigWords?: Timed[]; // key phrase alone over the window; captions hide
  credit?: string; // "Footage: NASA (public domain)"
  bridge?: {kicker?: string; text: string; durationMs: number}; // after the clip
  endCard?: boolean;
};

export const loreDefaults: LoreProps = {
  clip: '',
  durationSec: 10,
  captions: [],
  window: {top: 541, height: 608},
  endCard: true,
};

export const loreTotalSec = (p: LoreProps) =>
  p.durationSec + (p.bridge ? p.bridge.durationMs / 1000 : 0) + (p.endCard ? END_CARD_SEC : 0);

const msToFrame = (ms: number, fps: number) => Math.round((ms / 1000) * fps);

const TitleCard: React.FC<{big: string; sub?: string; frames: number}> = ({big, sub, frames}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const rise = spring({frame, fps, config: {damping: 200}, durationInFrames: 20});
  const out = interpolate(frame, [frames - 10, frames], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const subIn = interpolate(frame, [12, 24], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{background: 'black', justifyContent: 'center', alignItems: 'center', opacity: out, padding: 90}}>
      <div
        style={{
          fontFamily: SERIF,
          fontSize: 160,
          lineHeight: 1,
          color: BRAND.cream,
          textAlign: 'center',
          whiteSpace: 'pre-line',
          opacity: rise,
          transform: `translateY(${(1 - rise) * 30}px)`,
        }}
      >
        {big}
      </div>
      {sub ? (
        <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 40, color: 'rgba(242,239,234,0.75)', marginTop: 40, textAlign: 'center', opacity: subIn, whiteSpace: 'pre-line'}}>
          {sub}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};

const Stamp: React.FC<{text: string; top: number}> = ({text, top}) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [0, 10], [0, 1], {extrapolateRight: 'clamp'});
  return (
    <div style={{position: 'absolute', top: top + 24, left: 40, fontFamily: MONO, fontWeight: 500, fontSize: 26, letterSpacing: 4, color: `rgba(255,255,255,${0.7 * t})`, textTransform: 'uppercase'}}>
      {text}
    </div>
  );
};

const CaptionPage: React.FC<{page: TikTokPage; top: number; hidden: (ms: number) => boolean}> = ({page, top, hidden}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const nowMs = page.startMs + (frame / fps) * 1000;
  if (hidden(nowMs)) return null;
  return (
    <div style={{position: 'absolute', top, left: 70, right: 70, textAlign: 'center', fontFamily: SERIF, fontSize: 58, lineHeight: 1.25, color: BRAND.cream, textShadow: '0 2px 12px rgba(0,0,0,0.6)'}}>
      {page.tokens.map((tok) => {
        const active = tok.fromMs <= nowMs && tok.toMs > nowMs;
        return (
          <span key={tok.fromMs} style={{color: active ? BRAND.magenta : BRAND.cream}}>
            {tok.text}
          </span>
        );
      })}
    </div>
  );
};

const BigWord: React.FC<{text: string; frames: number}> = ({text, frames}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const s = spring({frame, fps, config: {damping: 200}, durationInFrames: 14});
  const out = interpolate(frame, [frames - 6, frames], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{background: `rgba(0,0,0,${0.6 * s * out})`, justifyContent: 'center', alignItems: 'center', padding: 80}}>
      <div style={{fontFamily: SERIF, fontSize: 110, lineHeight: 1.08, color: BRAND.cream, textAlign: 'center', whiteSpace: 'pre-line', opacity: s * out, transform: `scale(${interpolate(s, [0, 1], [1.04, 1])})`}}>
        {text}
      </div>
      <div style={{width: 110, height: 4, background: BRAND.magenta, marginTop: 40, opacity: s * out}} />
    </AbsoluteFill>
  );
};

const BridgeCard: React.FC<{kicker?: string; text: string}> = ({kicker, text}) => {
  const frame = useCurrentFrame();
  const fade = interpolate(frame, [0, 8], [0, 1], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{background: BRAND.cream, justifyContent: 'center', alignItems: 'center', opacity: fade, padding: 110}}>
      {kicker ? (
        <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 24, letterSpacing: 6, color: '#8A857E', textTransform: 'uppercase', marginBottom: 32}}>{kicker}</div>
      ) : null}
      <div style={{fontFamily: SERIF, fontSize: 84, lineHeight: 1.15, color: BRAND.ink, textAlign: 'center', whiteSpace: 'pre-line'}}>{text}</div>
      <div style={{width: 90, height: 4, background: BRAND.magenta, marginTop: 44}} />
    </AbsoluteFill>
  );
};

const EndCard: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const s = spring({frame, fps, config: {damping: 200}, durationInFrames: 15});
  const tag = interpolate(frame, [12, 24], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const [first, ...rest] = BRAND.tagline.split(' ');
  return (
    <AbsoluteFill style={{background: `radial-gradient(120% 80% at 50% 40%, ${BRAND.endCardTo}, ${BRAND.endCardFrom})`, justifyContent: 'center', alignItems: 'center'}}>
      <Img src={staticFile('brand/campus-fund-logo-white.png')} style={{width: 720, opacity: s, transform: `scale(${interpolate(s, [0, 1], [0.92, 1])})`}} />
      <div style={{opacity: tag, marginTop: 70, maxWidth: 820, textAlign: 'center', fontFamily: SANS, fontWeight: 800, fontSize: 46, lineHeight: 1.25, color: 'white'}}>
        {first} <span style={{color: BRAND.magenta}}>{rest.slice(0, 3).join(' ')}</span> {rest.slice(3).join(' ')}
      </div>
    </AbsoluteFill>
  );
};

export const Lore: React.FC<LoreProps> = ({clip, durationSec, captions, window, title, stamps = [], bigWords = [], credit, bridge, endCard}) => {
  const {fps} = useVideoConfig();
  const {pages} = useMemo(() => createTikTokStyleCaptions({captions, combineTokensWithinMilliseconds: 900}), [captions]);
  const clipFrames = Math.round(durationSec * fps);
  const bridgeFrames = bridge ? msToFrame(bridge.durationMs, fps) : 0;
  const titleMs = title?.durationMs ?? 0;
  const hidden = (ms: number) => ms < titleMs || bigWords.some((b) => ms >= b.startMs && ms < b.endMs);
  const captionTop = window.top + window.height + 44;

  return (
    <AbsoluteFill style={{backgroundColor: 'black'}}>
      <Sequence durationInFrames={clipFrames} layout="none">
        {clip ? <Video src={staticFile(clip)} style={{width: '100%', height: '100%', objectFit: 'cover'}} /> : null}
        {stamps.map((s) => (
          <Sequence key={s.startMs} from={msToFrame(s.startMs, fps)} durationInFrames={Math.max(1, msToFrame(s.endMs - s.startMs, fps))} layout="none">
            <Stamp text={s.text} top={window.top} />
          </Sequence>
        ))}
        {pages.map((page, i) => {
          const next = pages[i + 1]?.startMs ?? page.startMs + page.durationMs;
          return (
            <Sequence key={page.startMs} from={msToFrame(page.startMs, fps)} durationInFrames={Math.max(1, msToFrame(next - page.startMs, fps))} layout="none">
              <CaptionPage page={page} top={captionTop} hidden={hidden} />
            </Sequence>
          );
        })}
        {credit ? (
          <div style={{position: 'absolute', top: 1470, left: 0, right: 0, textAlign: 'center', fontFamily: MONO, fontSize: 22, letterSpacing: 2, color: 'rgba(255,255,255,0.5)'}}>{credit}</div>
        ) : null}
        {bigWords.map((b) => (
          <Sequence key={b.startMs} from={msToFrame(b.startMs, fps)} durationInFrames={Math.max(1, msToFrame(b.endMs - b.startMs, fps))} layout="none">
            <BigWord text={b.text} frames={msToFrame(b.endMs - b.startMs, fps)} />
          </Sequence>
        ))}
        {title ? (
          <Sequence durationInFrames={msToFrame(title.durationMs, fps)} layout="none">
            <TitleCard big={title.big} sub={title.sub} frames={msToFrame(title.durationMs, fps)} />
          </Sequence>
        ) : null}
      </Sequence>
      {bridge ? (
        <Sequence from={clipFrames} durationInFrames={bridgeFrames} layout="none">
          <BridgeCard kicker={bridge.kicker} text={bridge.text} />
        </Sequence>
      ) : null}
      {endCard ? (
        <Sequence from={clipFrames + bridgeFrames} durationInFrames={Math.round(END_CARD_SEC * fps)} layout="none">
          <EndCard />
        </Sequence>
      ) : null}
    </AbsoluteFill>
  );
};
