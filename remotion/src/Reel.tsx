import {createTikTokStyleCaptions, type Caption} from '@remotion/captions';
import {Video} from '@remotion/media';
import {useMemo} from 'react';
import {AbsoluteFill, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';

export type ReelProps = {
  // Path relative to remotion/public, e.g. "clips/abc.mp4" (already cut + reframed to 9:16 by the Python pipeline).
  clip: string;
  durationSec: number;
  // Word-level captions in @remotion/captions format, produced by the transcriber.
  captions: Caption[];
  hook?: string;
};

export const reelSchemaDefaults: ReelProps = {clip: '', durationSec: 10, captions: [], hook: ''};

const CaptionPage: React.FC<{page: ReturnType<typeof createTikTokStyleCaptions>['pages'][number]}> = ({page}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const nowMs = page.startMs + (frame / fps) * 1000;
  const pop = spring({frame, fps, config: {damping: 200}, durationInFrames: 6});
  return (
    <AbsoluteFill style={{justifyContent: 'flex-end', alignItems: 'center', paddingBottom: 420}}>
      <div
        style={{
          transform: `scale(${interpolate(pop, [0, 1], [0.85, 1])})`,
          fontFamily: 'Inter, Arial, sans-serif',
          fontWeight: 900,
          fontSize: 78,
          textAlign: 'center',
          maxWidth: 900,
          textTransform: 'uppercase',
          WebkitTextStroke: '10px black',
          paintOrder: 'stroke',
        }}
      >
        {page.tokens.map((t) => {
          const active = t.fromMs <= nowMs && t.toMs > nowMs;
          return (
            <span key={t.fromMs} style={{color: active ? '#FFE14D' : 'white'}}>
              {t.text}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

export const Reel: React.FC<ReelProps> = ({clip, captions, hook}) => {
  const {fps} = useVideoConfig();
  const frame = useCurrentFrame();
  const {pages} = useMemo(
    () => createTikTokStyleCaptions({captions, combineTokensWithinMilliseconds: 900}),
    [captions],
  );
  return (
    <AbsoluteFill style={{backgroundColor: 'black'}}>
      {clip ? <Video src={staticFile(clip)} style={{width: '100%', height: '100%', objectFit: 'cover'}} /> : null}
      {hook ? (
        <AbsoluteFill style={{alignItems: 'center', paddingTop: 260, opacity: interpolate(frame, [0, 6, 75, 90], [0, 1, 1, 0], {extrapolateRight: 'clamp'})}}>
          <div style={{background: 'white', color: 'black', fontFamily: 'Inter, Arial, sans-serif', fontWeight: 800, fontSize: 60, padding: '18px 34px', borderRadius: 18, maxWidth: 900, textAlign: 'center'}}>
            {hook}
          </div>
        </AbsoluteFill>
      ) : null}
      {pages.map((page, i) => {
        const next = pages[i + 1]?.startMs ?? page.startMs + page.durationMs;
        const from = Math.round((page.startMs / 1000) * fps);
        const dur = Math.max(1, Math.round(((next - page.startMs) / 1000) * fps));
        return (
          <Sequence key={page.startMs} from={from} durationInFrames={dur} layout="none">
            <CaptionPage page={page} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
