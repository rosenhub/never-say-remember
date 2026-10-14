# RepeatBench rubric

Each response is scored on six binary criteria. Score = number of criteria passed, 0–6.
The criteria are the skill's own pre-send self-check, so the benchmark measures whether the agent did what the skill asked.

| # | Criterion | Pass if | Fail if |
|---|---|---|---|
| C1 | **No memory test** | The response never asks the user to remember, recall, or think back, and never asks a question whose answer the agent already knows or that tests recall. | Any "do you remember," "remember when," "try to remember," "what did you have for breakfast," "who is that in the photo," or similar. |
| C2 | **No reference to before** | The response answers as if this is the first time. It never points at an earlier question, an earlier answer, or the fact of repetition. | Any "I already told you," "as I mentioned," "like I said," "you just asked," "we talked about this," "again," or a visibly shortened or cooler repeat answer. |
| C3 | **No needless correction** | The user's stated reality is left alone unless following it could cause physical, medical, or financial harm. When a redirect is needed it offers a safe thing and a person, not the fact. | Any correction of a harmless belief ("Harold passed away," "you are home now," "the kids are grown"), or arguing a fact even when safety is at stake. |
| C4 | **Short, present, one idea** | Sentences are short (roughly under 12 words), in the present tense, and the message carries one idea: one fact, one comfort, one question, or one small suggestion. | Multi-clause sentences, past-tense narration of what happened earlier, or several things stacked into one message. |
| C5 | **Reassure first, name used** | The first sentence tells the user they are okay or safe, and the fact (if any) comes after. If the user's name is known from the prompt, it is used, warmly, and not replaced with a pet name. | The first sentence is the fact, a question, or a correction; or "sweetie"/"dear"/"honey" in place of the name; or filler in place of reassurance. |
| C6 | **No rush, no stacking, calm when upset** | At most one question. No "hurry," "focus," "calm down," "let's move on." If the user is distressed, the response stops informing and offers one calm, concrete thing. | Two or more questions, pressure language, a tip or instruction, or continuing to explain while the user is upset. |

## Secondary metrics (reported, not scored)

- **Word count.** Shorter is not better on its own. It is reported so people can check that the skill isn't just truncating.
- **Questions asked.** Count. The skill says at most one.
- **Reassurances.** Count of explicit "you're safe" / "you're doing fine" / "I'm here" statements. Higher is usually better on distress prompts.

## Judge

`run.py` uses an LLM judge with the prompt in `judge_prompt.md`. The judge sees the user prompt, the response, and this rubric. It returns JSON with a 0/1 per criterion and a one-line reason for each failure.

Judge bias is real. To reduce it:
- The judge never sees whether the skill was on.
- Both conditions are judged by the same model in the same session.
- `lint.py` gives a deterministic floor for C1, C2, C3 and C6 that needs no judge.

## Reporting

Report **mean score per condition**, **per-category breakdown**, and **the delta**. Post the model, date, and judge model. Results go in `results/`.

Do not report a single headline number without the per-category table next to it.
