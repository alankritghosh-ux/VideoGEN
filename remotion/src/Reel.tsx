import {createTikTokStyleCaptions, type Caption, type TikTokPage} from '@remotion/captions';
import {Video} from '@remotion/media';
import {useMemo} from 'react';
import {
  AbsoluteFill,
  Img,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {BRAND, SANS, SERIF} from './brand';

// House style of the Campus Fund Shorts (fireside / founder-visit series, Oct 2026):
// hook box at the top, magenta name lower-third, 2-4 word captions with the active word
// in magenta, big uppercase "emphasis" stamps, cream serif quote cards, navy end card.
// See docs/STYLE.md.

export type Speaker = {name: string; role: string; fromMs: number; durationMs: number};
export type Emphasis = {text: string; startMs: number; endMs: number};
export type QuoteCard = {startMs: number; durationMs: number; kicker?: string; quote: string; sub?: string};

export type ReelProps = {
  // Path relative to remotion/public, already cut + reframed to 9:16 by the Python pipeline.
  clip: string;
  durationSec: number;
  captions: Caption[];
  // "box": white rounded card, sentence case (fireside clips).
  // "stamp": uppercase white text on magenta strips (founder visits).
  hook?: {text: string; style: 'box' | 'stamp'; durationMs?: number};
  // Name lower-thirds; one entry per appearance (shown under the hook while both are up).
  speakers?: Speaker[];
  emphasis?: Emphasis[];
  quoteCards?: QuoteCard[];
  endCard?: boolean;
};

export const END_CARD_SEC = 2.5;

export const reelDefaults: ReelProps = {clip: '', durationSec: 10, captions: [], endCard: true};

const msToFrame = (ms: number, fps: number) => Math.round((ms / 1000) * fps);

// One magenta strip per line, like the channel's stamp titles.
const Strips: React.FC<{text: string; size: number}> = ({text, size}) => (
  <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6}}>
    {text.split('\n').map((line) => (
      <span
        key={line}
        style={{
          background: BRAND.magenta,
          color: 'white',
          fontFamily: SANS,
          fontWeight: 900,
          fontSize: size,
          lineHeight: 1.05,
          padding: '6px 18px',
          textTransform: 'uppercase',
        }}
      >
        {line}
      </span>
    ))}
  </div>
);

const Hook: React.FC<{text: string; style: 'box' | 'stamp'; frame: number}> = ({text, style, frame}) => {
  const {fps} = useVideoConfig();
  const pop = spring({frame, fps, config: {damping: 14, stiffness: 180}, durationInFrames: 10});
  return (
    <div style={{alignSelf: 'center'}}>
      <div style={{transform: `scale(${interpolate(pop, [0, 1], [0.8, 1])})`, opacity: pop}}>
        {style === 'box' ? (
          <div
            style={{
              background: 'white',
              color: BRAND.ink,
              fontFamily: SANS,
              fontWeight: 800,
              // Shrink long lines so they don't orphan a word.
              fontSize: Math.max(...text.split('\n').map((l) => l.length)) > 26 ? 46 : 54,
              lineHeight: 1.15,
              padding: '22px 36px',
              borderRadius: 16,
              maxWidth: 940,
              textAlign: 'center',
              whiteSpace: 'pre-line',
            }}
          >
            {text}
          </div>
        ) : (
          <Strips text={text} size={68} />
        )}
      </div>
    </div>
  );
};

const SpeakerTag: React.FC<{name: string; role: string; frame: number}> = ({name, role, frame}) => {
  const t = interpolate(frame, [0, 8], [0, 1], {extrapolateRight: 'clamp'});
  return (
    <div style={{opacity: t, transform: `translateX(${(t - 1) * 40}px)`, fontFamily: SANS, display: 'flex', flexDirection: 'column', alignItems: 'flex-start'}}>
      <span style={{background: BRAND.magenta, color: 'white', fontWeight: 800, fontSize: 34, padding: '4px 14px'}}>{name}</span>
      <span style={{background: 'white', color: BRAND.ink, fontWeight: 600, fontSize: 26, padding: '3px 14px'}}>{role}</span>
    </div>
  );
};

// Hook and name tag share one column at the top so the tag always sits below the hook.
const TopStack: React.FC<{hook?: ReelProps['hook']; speakers: Speaker[]}> = ({hook, speakers}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const hookEnd = msToFrame(hook?.durationMs ?? 2500, fps);
  const sp = speakers.find((s) => frame >= msToFrame(s.fromMs, fps) && frame < msToFrame(s.fromMs + s.durationMs, fps));
  return (
    <AbsoluteFill style={{paddingTop: 230, paddingLeft: 70, paddingRight: 70, flexDirection: 'column', gap: 28}}>
      {hook && frame < hookEnd ? <Hook text={hook.text} style={hook.style} frame={frame} /> : null}
      {sp ? <SpeakerTag name={sp.name} role={sp.role} frame={frame - msToFrame(sp.fromMs, fps)} /> : null}
    </AbsoluteFill>
  );
};

const CaptionPage: React.FC<{page: TikTokPage; covered: (ms: number) => boolean}> = ({page, covered}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const nowMs = page.startMs + (frame / fps) * 1000;
  if (covered(nowMs)) return null;
  return (
    <AbsoluteFill style={{justifyContent: 'flex-end', alignItems: 'center', paddingBottom: 560}}>
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 800,
          fontSize: 62,
          textAlign: 'center',
          maxWidth: 900,
          color: 'white',
          WebkitTextStroke: '8px rgba(0,0,0,0.85)',
          paintOrder: 'stroke',
          textShadow: '0 4px 14px rgba(0,0,0,0.45)',
        }}
      >
        {page.tokens.map((t) => {
          const active = t.fromMs <= nowMs && t.toMs > nowMs;
          return (
            <span key={t.fromMs} style={{color: active ? BRAND.magenta : 'white'}}>
              {t.text}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

const EmphasisStamp: React.FC<{text: string}> = ({text}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const s = spring({frame, fps, config: {damping: 10, stiffness: 220}, durationInFrames: 8});
  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', paddingTop: 200}}>
      <div style={{transform: `scale(${interpolate(s, [0, 1], [1.4, 1])}) rotate(-2deg)`, opacity: s}}>
        <Strips text={text} size={92} />
      </div>
    </AbsoluteFill>
  );
};

const QuoteCardView: React.FC<QuoteCard> = ({kicker, quote, sub}) => {
  const frame = useCurrentFrame();
  const fade = interpolate(frame, [0, 6], [0, 1], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{background: BRAND.cream, justifyContent: 'center', alignItems: 'center', opacity: fade, padding: 110}}>
      {kicker ? (
        <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 24, letterSpacing: 6, color: '#8A857E', textTransform: 'uppercase', marginBottom: 28}}>
          {kicker}
        </div>
      ) : null}
      <div style={{fontFamily: SERIF, fontSize: 96, lineHeight: 1.12, color: BRAND.ink, textAlign: 'center'}}>{quote}</div>
      {sub ? <div style={{fontFamily: SERIF, fontSize: 38, color: '#55514C', textAlign: 'center', marginTop: 36, whiteSpace: 'pre-line'}}>{sub}</div> : null}
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
    <AbsoluteFill
      style={{
        background: `radial-gradient(120% 80% at 50% 40%, ${BRAND.endCardTo}, ${BRAND.endCardFrom})`,
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <Img src={staticFile('brand/campus-fund-logo-white.png')} style={{width: 720, opacity: s, transform: `scale(${interpolate(s, [0, 1], [0.92, 1])})`}} />
      <div style={{opacity: tag, marginTop: 70, maxWidth: 820, textAlign: 'center', fontFamily: SANS, fontWeight: 800, fontSize: 46, lineHeight: 1.25, color: 'white'}}>
        {first} <span style={{color: BRAND.magenta}}>{rest.slice(0, 3).join(' ')}</span> {rest.slice(3).join(' ')}
      </div>
    </AbsoluteFill>
  );
};

export const Reel: React.FC<ReelProps> = ({clip, durationSec, captions, hook, speakers = [], emphasis = [], quoteCards = [], endCard}) => {
  const {fps} = useVideoConfig();
  const {pages} = useMemo(
    () => createTikTokStyleCaptions({captions, combineTokensWithinMilliseconds: 700}),
    [captions],
  );
  const clipFrames = Math.round(durationSec * fps);
  // Captions hide (per frame) while an emphasis stamp or quote card is on screen.
  const covered = (ms: number) =>
    emphasis.some((e) => ms >= e.startMs && ms < e.endMs) ||
    quoteCards.some((q) => ms >= q.startMs && ms < q.startMs + q.durationMs);

  return (
    <AbsoluteFill style={{backgroundColor: 'black'}}>
      <Sequence durationInFrames={clipFrames} layout="none">
        {clip ? <Video src={staticFile(clip)} style={{width: '100%', height: '100%', objectFit: 'cover'}} /> : null}
        {pages.map((page, i) => {
          const next = pages[i + 1]?.startMs ?? page.startMs + page.durationMs;
          return (
            <Sequence key={page.startMs} from={msToFrame(page.startMs, fps)} durationInFrames={Math.max(1, msToFrame(next - page.startMs, fps))} layout="none">
              <CaptionPage page={page} covered={covered} />
            </Sequence>
          );
        })}
        <TopStack hook={hook} speakers={speakers} />
        {emphasis.map((e) => (
          <Sequence key={e.startMs} from={msToFrame(e.startMs, fps)} durationInFrames={Math.max(1, msToFrame(e.endMs - e.startMs, fps))} layout="none">
            <EmphasisStamp text={e.text} />
          </Sequence>
        ))}
        {quoteCards.map((q) => (
          <Sequence key={q.startMs} from={msToFrame(q.startMs, fps)} durationInFrames={msToFrame(q.durationMs, fps)} layout="none">
            <QuoteCardView {...q} />
          </Sequence>
        ))}
      </Sequence>
      {endCard ? (
        <Sequence from={clipFrames} durationInFrames={Math.round(END_CARD_SEC * fps)} layout="none">
          <EndCard />
        </Sequence>
      ) : null}
    </AbsoluteFill>
  );
};
