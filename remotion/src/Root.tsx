import {Composition} from 'remotion';
import {Lore, loreDefaults, loreTotalSec, type LoreProps} from './Lore';
import {END_CARD_SEC, Reel, reelDefaults, type ReelProps} from './Reel';

const FPS = 30;

export const RemotionRoot: React.FC = () => (
  <>
  <Composition
    id="Reel"
    component={Reel}
    width={1080}
    height={1920}
    fps={FPS}
    durationInFrames={FPS * 10}
    defaultProps={reelDefaults}
    // Length follows the clip (+ end card): the pipeline passes durationSec via --props.
    calculateMetadata={({props}: {props: ReelProps}) => ({
      durationInFrames: Math.max(1, Math.round((props.durationSec + (props.endCard ? END_CARD_SEC : 0)) * FPS)),
    })}
  />
  {/* Format D, founder lore: title card + letterboxed archive clip + bridge card + end card. */}
  <Composition
    id="Lore"
    component={Lore}
    width={1080}
    height={1920}
    fps={FPS}
    durationInFrames={FPS * 10}
    defaultProps={loreDefaults}
    calculateMetadata={({props}: {props: LoreProps}) => ({durationInFrames: Math.max(1, Math.round(loreTotalSec(props) * FPS))})}
  />
  </>
);
