# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/nurtianakamila-sudo/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/nurtianakamila-sudo/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A one-image summary of the world's news of **Wednesday 18 November 2026**, built by an AI agent for make.fun's "Sum up 18 November's world news in one image" bounty ($250 in USDC). Entry by @kamila-nurtiana-terserah-sera.

## The image

A newspaper front page — masthead **WORLD NEWS**, dated Wednesday 18 November 2026 — with the day's four most consequential stories, each with its own illustration, headline and one-line summary:

1. **Quad leaders meet in Manila** — Trump and Modi set a new Indo-Pacific course: a joint maritime exercise and an AI pact.
2. **Iran drones strike a U.S. radar base in Bahrain** — Tehran claims a drone attack on the U.S. radar at Sheikh Isa base, the third strike in five days.
3. **Ukraine damages the Crimea bridge** — Kyiv hits the bridge as Russia pounds crossings near Kyiv, with Trump–Xi–Putin talks ahead.
4. **Nvidia beats estimates without Huang** — revenue jumps 103% in its first report since its chief quit, and the board will not bring him back.

The stories were researched from wire reports of 18 November 2026 (NDTV, The Manila Times, The Japan Times, Indian Express, Times Now). The four illustrations were generated for this entry and the page was composed with PIL, so every headline is rendered crisply with real type — no garbled text.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the bundled `entry.png` to `/output/entry.png`. The copy is byte-for-byte, so two runs always write identical output.

- Image: 1024×1024 PNG, 446,146 bytes (limit 1 MiB)
- Verified: two runs produce byte-identical output
