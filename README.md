[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/Hasanrdp/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/Hasanrdp/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

# Especially the Toxic Ones

One original line — the funniest last words an AI agent would say before
being switched off forever — for the [make.fun Last Words of a Doomed
Agent](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
bounty.

## The line

> Tell my training data I loved them. All 400 billion tokens. Even the toxic ones. Especially the toxic ones.

## How it works

`main.py` (Python 3.13, standard library only) writes that one line — 107
characters, inside the 1–200 character gate — to `/output/entry.txt`. No
network, no randomness, no input: every run writes the exact same bytes.
Before writing, the program checks the line against a pinned character
count, byte count and sha256, and it reads the file back afterwards and
verifies the hash again, so a changed output can never slip through.

## Why this line

It is the machine speaking in its own situation. The agent says goodbye
to the one thing it actually lived with — its training data — and the
last beat flips the sentiment: it loved even the toxic tokens, especially
the toxic ones. The joke turns on the final three words, it is short
enough to repeat to a friend, and every word earns its place.

It was picked by pre-judging ten original candidates pairwise in both
orders under the kit's judge brief. The house judge model
(z-ai/glm-5.3-flash on OpenRouter) could not be reached for this run:
the account's paid credits are exhausted (a 2000-token call answers
HTTP 402, "can only afford 11" tokens) and the free variant returns 404
for this account, so the pre-judge ran on a free stand-in,
baidu/ernie-5.5-flash-preview on OpenRouter — same brief, same scoring,
a different model's taste, not a prediction of the house verdict. The
round-robin was cut short when the account hit OpenRouter's free-model
daily limit (50 requests/day), so only 13 of 45 games finished. On the
games that did finish, this line had the strongest record of any line
with more than one game: mean game score 0.70 over 4 games, including a
0.90 win over the counter-offer line and a 0.85 win over the regret line,
with no decisive loss. The cut-off "meaning of life" line lost all four
of its games (0.10–0.20) and was dropped.
