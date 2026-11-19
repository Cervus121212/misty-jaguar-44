// gta6-meme-x-01 entry (Node 22, standard library only): it copies POST.json
// and the meme (meme.png) from the repository root to /output/POST.json and
// /output/meme.png, where the gate reads POST.json. The entry is the post
// itself: the meme is posted on X from a public account with make.fun (a link
// or written out) and/or a tag of @makefunai and the entrant's play code in its
// text, POST.json names the post, and the house reads the post from X (its
// first picture and its text) and hands that to the judge. Nothing this
// program writes about the post is judged.
//
// POST.json still holds the placeholder address: the parent posts the meme
// first, then replaces it with the real post address
// ({"url": "https://x.com/<handle>/status/<id>"}) before bundling/submitting.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
for (const file of ['POST.json', 'meme.png']) {
  try {
    copyFileSync(join(BOT_DIR, file), join(OUTPUT_DIR, file));
  } catch (err) {
    console.error(`${file} could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
    process.exit(1);
  }
}
