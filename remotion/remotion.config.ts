import {Config} from '@remotion/cli/config';
import {existsSync} from 'node:fs';

// remotion.media (Remotion's own Chrome download) is blocked in cloud sessions;
// use the preinstalled Playwright headless shell when present.
const headlessShell = '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell';
if (existsSync(headlessShell)) {
  Config.setBrowserExecutable(headlessShell);
}
Config.setConcurrency(4);
Config.setVideoImageFormat('jpeg');
