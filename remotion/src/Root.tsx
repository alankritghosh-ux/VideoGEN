import {Composition} from 'remotion';
import {Reel, reelSchemaDefaults, type ReelProps} from './Reel';

const FPS = 30;

export const RemotionRoot: React.FC = () => (
  <Composition
    id="Reel"
    component={Reel}
    width={1080}
    height={1920}
    fps={FPS}
    durationInFrames={FPS * 10}
    defaultProps={reelSchemaDefaults}
    // Length follows the clip: pass --props with durationSec from the pipeline.
    calculateMetadata={({props}: {props: ReelProps}) => ({
      durationInFrames: Math.max(1, Math.round(props.durationSec * FPS)),
    })}
  />
);
