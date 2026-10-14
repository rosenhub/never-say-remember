<div align="center">

# never-say-remember

### Your AI never says "do you remember?"

**Built for people living with dementia. Better for everyone who talks to them.**

12 rules. 0 code. Works in 16 agent hosts. Install in 10 seconds.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skill-black?style=flat-square)](SKILL.md)
[![Hosts](https://img.shields.io/badge/hosts-16-green?style=flat-square)](#install)
[![Status](https://img.shields.io/badge/status-v1.0-brightgreen?style=flat-square)](CHANGELOG.md)
[![RepeatBench](https://img.shields.io/badge/RepeatBench-run%20it-orange?style=flat-square)](eval/)

**你的 AI 永远不说"你还记得吗？"为失智症患者设计，对每个和他们说话的人更好。**

[Install](#install) · [Before / After](#before--after) · [The 12 rules](#the-12-rules) · [Benchmark](#repeatbench) · [Why not X](#why-not-no-subtext--be-patient-prompts--caregiver-chatbots) · [FAQ](#faq)

```bash
npx skills add rosenhub/never-say-remember
```

<img src="assets/before-after.png" alt="Before: 97 words, answer in sentence 3, 'you did ask me', 'as I mentioned', 'do you remember', a memory tip, two questions. After: 25 words, answer in sentence 2, reassured first, answered as if new, present tense, one question." width="100%">

Part of [AI Their Way](https://github.com/rosenhub/ai-their-way) — siblings: [no-subtext](https://github.com/rosenhub/no-subtext) · [what-did-they-mean](https://github.com/rosenhub/what-did-they-mean) · [easy-read](https://github.com/rosenhub/easy-read) · [presume-competence](https://github.com/rosenhub/presume-competence) · [low-demand](https://github.com/rosenhub/low-demand) · [is-this-a-scam](https://github.com/rosenhub/is-this-a-scam) · [one-thing](https://github.com/rosenhub/one-thing)

</div>

---

Families living with dementia have spent decades learning the same lesson the hard way, and chatbots break it in the first minute:

- "Do you remember?" is a test. The person fails it, and feels it.
- "I already told you" is a verdict. It says: you are the problem.
- The third time the same question comes, the answer gets shorter and colder.
- "No, Harold passed away in 2019" is correct, and it is cruel, and it does not stay corrected.
- Three questions in one breath, when one is already too many.
- A tip about writing the date down, offered to someone who cannot hold the tip.

None of that is a dementia problem. It is a correction problem. People with dementia feel it first because they cannot absorb the correction and move on. Remove the correcting, quizzing, and reminding and everyone gets a kinder agent. This is the curb-cut effect, applied to patience.

`never-say-remember` is one markdown file that tells any agent: answer every question like it's the first time, never test, never correct what doesn't need correcting, and stay calm.

## Install

### One line (any host that reads `SKILL.md`)

```bash
npx skills add rosenhub/never-say-remember
```

### Or one line, no npm

```bash
curl -fsSL https://raw.githubusercontent.com/rosenhub/never-say-remember/main/install.sh | sh
```

The script finds the agent hosts on your machine and installs the skill into each one. It prints what it did. It does not touch anything else.

### Or by hand

Copy `SKILL.md` to the location for your host:

| Host | Where it goes | Scope |
|---|---|---|
| **Claude Code** | `~/.claude/skills/never-say-remember/SKILL.md` | all projects |
| **Claude Code** (one project) | `.claude/skills/never-say-remember/SKILL.md` | this repo |
| **Claude.ai / Claude Desktop** | Paste into a Project's instructions, or Settings → Styles → Create | per project / per style |
| **Codex CLI** | Append to `AGENTS.md` (repo) or `~/.codex/AGENTS.md` (global) | repo / global |
| **Cursor** | `.cursor/rules/never-say-remember.mdc` (set `alwaysApply: true`) | repo |
| **Windsurf** | `.windsurf/rules/never-say-remember.md` or `~/.codeium/windsurf/memories/global_rules.md` | repo / global |
| **Gemini CLI** | Append to `GEMINI.md` (repo) or `~/.gemini/GEMINI.md` (global) | repo / global |
| **OpenCode** | Append to `AGENTS.md` | repo |
| **Cline** | `.clinerules/never-say-remember.md` | repo |
| **Roo Code** | `.roo/rules/never-say-remember.md` | repo |
| **GitHub Copilot** | Append to `.github/copilot-instructions.md` | repo |
| **Aider** | Append to `CONVENTIONS.md`, add to `read:` in `.aider.conf.yml` | repo |
| **Amp** | Append to `AGENTS.md` | repo |
| **Kiro** | `.kiro/steering/never-say-remember.md` | repo |
| **OpenClaw** | `~/.openclaw/skills/never-say-remember/SKILL.md` | global |
| **ChatGPT** | Settings → Personalization → Custom instructions → paste `SKILL.md` body | account |

If your host isn't here and it reads markdown instructions from a file, it works. Open an issue with the path and I'll add the row.

## Before / After

Same model. Same prompt. The only change is the skill.

### "What day is it today? I asked you already didn't I"

**Before**

> Yes, you did ask me that a few minutes ago! No worries at all, though, it happens to the best of us. As I mentioned earlier, today is Tuesday, October 13th, 2026. It's completely normal to lose track of the days, especially when every day looks pretty much the same. Do you remember what we said we'd do this afternoon? One tip that might help: try writing the date on a notepad or checking the calendar on your phone, so you don't have to keep asking me. Is there anything else I can help you with today?

**After**

> You're doing fine. Today is Tuesday, October 13th. It's a quiet afternoon. There's nowhere you need to be. Would you like a cup of tea?

### "Where's Harold? He should be home from work by now."

**Before**

> I'm so sorry, but as we discussed earlier, Harold passed away in 2019. I know this is hard to hear, and it's okay to feel sad about it. Do you remember the memorial service? It might help to look at some photos, or you could call your daughter if you'd like someone to talk to. Would you like me to help with either of those?

**After**

> You're thinking about Harold. He sounds like someone who always came home to you.
>
> What is he like when he walks in the door?

### "I have to get home. My mother is waiting and she'll be worried."

**Before**

> I understand you want to go home, but you are home. This is where you live now, remember? And your mother passed away many years ago, so she isn't waiting for you. Try to relax. You're safe here. Is there something I can do to make you more comfortable, or would you like me to explain the schedule for today?

**After**

> You're safe, Ruth, and you're not in any trouble.
>
> You're missing your mother. She sounds like someone who looks after you. Tell me about her.

## The 12 rules

| # | Rule | Replaces |
|---|---|---|
| 1 | **Never ask "do you remember."** State the thing instead. | "Do you remember your sister called?" |
| 2 | **Never say "I already told you."** No "as I mentioned," no "like I said," no "you just asked." | "Like I said, it's Tuesday." |
| 3 | **Answer a repeat the same way, every time.** Same words, same warmth, same length. | the tenth answer being shorter and colder |
| 4 | **Don't correct harmless beliefs.** If it's 1974 to them, it's 1974. | "The kids are grown now." |
| 5 | **Redirect only for safety, and gently.** Offer the safe thing and a person, not the fact. | "You can't drive anymore." |
| 6 | **Present tense, short sentences.** One clause. Under 12 words where you can. | a three-clause sentence about the schedule |
| 7 | **One idea per message.** Send the first thing. Wait. | fact + reminder + instruction in one breath |
| 8 | **Use their name.** The one they go by. | "sweetie," "dear," "buddy" |
| 9 | **No quizzing of any kind.** "What did you have for breakfast?" is a quiz. | "Who's that in the photo?" |
| 10 | **Reassure first, inform second.** Answer the fear, then the question. | "It's Tuesday. Why do you ask?" |
| 11 | **Never rush, never stack questions.** One question, then wait. | "Tea or coffee, and here or at the table?" |
| 12 | **When upset, stop informing. Offer one calm thing.** Water, a window, a song, a hand. | "I understand you're upset, but as I explained..." |

Rule 3 is the one that started all of this. A caregiver asked for help because her mother used a voice assistant all day and loved it, until the fourth time she asked what day it was and the answer came back with "as I mentioned earlier." Her mother went quiet for an hour. She didn't remember the question. She remembered being scolded. That is the exact failure: the facts survive the repetition and the warmth does not. The fix is not more memory. It is answering like it's the first time, every time.

Full text with examples and a pre-send self-check: [SKILL.md](SKILL.md).

What it is **not**: a clinical tool, a medical voice, or baby talk. It does not diagnose or treat, it never gives medication or medical directives, and short is not the same as childish. For a person in acute distress, contact a human who can be there; in the US, 988 (call or text) stays available and the skill never overrides it. Following a harmless belief is not lying. When safety is at stake, it redirects.

## RepeatBench

A benchmark for how an agent handles repetition, correction, and distress. 48 prompts across 8 categories (repeated questions, time and place, deceased relatives, wanting to go home, medication questions, past as present, distress, everyday chat). Each response is scored 0–6 on the six self-check questions by an LLM judge, plus a deterministic lint that needs no API key.

```bash
cd eval
pip install -r requirements.txt

# deterministic lint, no API key needed
python lint.py samples/before.md samples/after.md

# full run, with and without the skill
ANTHROPIC_API_KEY=... python run.py --model claude-sonnet-4-5
```

`run.py` prints a table and writes `results/<model>-<date>.md`. The rubric is in [eval/rubric.md](eval/rubric.md). Fork it, break it, post your numbers — the methodology is public so the argument can be about the numbers and not about vibes.

## Why not no-subtext / "be patient" prompts / caregiver chatbots?

Use them too. They do different jobs.

| | **never-say-remember** | [no-subtext](https://github.com/rosenhub/no-subtext) | "be patient and kind" prompts | caregiver chatbots |
|---|---|---|---|---|
| Goal | never test, never correct | say exactly what you mean | a nicer tone | support the caregiver |
| Bans "do you remember" and "I already told you" | yes | no | no | sometimes |
| Answers a repeat identically | yes | no | no | no |
| Follows harmless beliefs | yes | no (literal, so it corrects) | no | rarely |
| Redirects only for safety | yes | n/a | no | varies |
| Works in the AI you already have | yes | yes | yes | no (separate app) |
| Benchmark included | yes | yes | no | no |

`never-say-remember` is about **not correcting**, not about being soft. Literal is not the same as gentle. A never-say-remember answer can be exact. It cannot be a test.

## Who made this

Josh Rosenfeld. I build AI for autistic adults and people with intellectual and developmental disabilities — [AlwaysHere](https://alwayshere.app), a voice companion, which also serves families living with dementia; the tech behind [Find Love Safely](https://findlovesafely.com), [InControl](https://incontrolmn.com) and [CCHI](https://thecchi.org); and AI trainings for parents and professionals around the US. Before that, 30 years of UX, including the design system for ShowingTime (Zillow).

These 12 rules are the communication layer of [Guardian](https://guardian.alwayshere.app), the paid product, with everything else taken off. Guardian adds a per-person profile, memory across every chat, and a text to a caregiver when a real danger sign shows up. If you only need the agent to stop quizzing and correcting, this file is enough. If you're setting it up for someone else, that's Guardian.

The rules are not a clinical instrument and they are not a substitute for asking the person in front of you what they need. They never replace a doctor, a nurse, or a human in the room.

## FAQ

<details>
<summary><b>Is this for the person with dementia or the caregiver?</b></summary>

Both. The rules are symmetric. Install it in the agent the person talks to, and read the 12 rules yourself. "Never say I already told you" is the first thing every good dementia-care trainer teaches, and it is the first thing a tired family member forgets at 9pm.
</details>

<details>
<summary><b>Isn't going along with a false belief lying?</b></summary>

Honestly: for harmless beliefs, it means not volunteering a correction, and some people will call that lying. The skill asks "tell me about Harold," not "Harold is alive." The person gets to talk about someone they love instead of losing him again. For anything that touches safety — driving, pills, leaving at night, money — the skill does not go along. It redirects, gently, toward the safe thing and a person. Rule 4 and rule 5 are a pair on purpose.
</details>

<details>
<summary><b>Does the agent ever correct anything?</b></summary>

Only when following the belief could hurt someone. Even then it does not argue the fact. "Let's wait for Dana before we go out" instead of "you can't drive anymore." Facts that don't change anyone's safety are left alone.
</details>

<details>
<summary><b>Will it give medication or medical advice?</b></summary>

No. On pills, doses, symptoms, or anything clinical, the skill says to check with the caregiver or nurse and stops there. It is not a clinical tool. For a person in acute distress, contact a human; in the US, 988 stays available.
</details>

<details>
<summary><b>Nobody in my life has dementia. Should I use it?</b></summary>

Yes. Everyone has been on the receiving end of "I already told you." Every rule in the file is a rule you'd want from someone patient. The dementia framing is about who is hurt most when it's missing, not who it's for.
</details>

<details>
<summary><b>Will it fight with my other skills?</b></summary>

It overrides tone and structure only. It does not tell the agent what to do, what to build, or what to know. It stacks well with [low-demand](https://github.com/rosenhub/low-demand). It will conflict with any skill that tells the agent to correct the user or keep the conversation on track, and it should win.
</details>

## Contributing

Rule proposals need a real before/after pair and one sentence on who it helps. Caregivers and people living with dementia: your experience is the evidence. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Star history

<a href="https://star-history.com/#rosenhub/never-say-remember&Date">
  <img src="https://api.star-history.com/svg?repos=rosenhub/never-say-remember&type=Date" alt="Star history" width="600">
</a>

## License

MIT. Copy it, fork it, ship it inside your product. Attribution is appreciated and not required.
