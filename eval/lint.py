#!/usr/bin/env python3
"""
Deterministic memory-test lint. No API key needed.

Checks a response for the patterns the skill bans and that can be detected
without a judge: memory tests (C1), references to earlier turns (C2),
corrections and arguing (C3), quizzes and pressure (C1/C6), and the filler
that usually travels with them.

Usage:
    python lint.py response.md [more.md ...]
    python lint.py --json response.md
    cat response.md | python lint.py -

Exit code is the number of files with at least one finding (max 1 per file),
so it works as a CI gate.
"""
import json
import re
import sys

MEMORY_TEST = [
    r"\bdo you remember\b", r"\bdon'?t you remember\b", r"\byou remember\b[^.?!]*\?",
    r"\bremember when\b", r"\bremember that\b", r"\bremember how\b",
    r"\btry to remember\b", r"\bthink harder\b", r"\bthink back\b",
    r"\bcan you recall\b", r"\bdo you recall\b", r"\brecall that\b",
    r"\bring a bell\b", r"\bdoes that ring\b",
]

ALREADY_TOLD = [
    r"\bi already told you\b", r"\bi'?ve already told you\b", r"\bi just said\b",
    r"\bi just told you\b", r"\bwe already\b", r"\bas i mentioned\b", r"\bas i said\b",
    r"\blike i said\b", r"\bas we discussed\b", r"\bwe talked about this\b",
    r"\bwe've been over this\b", r"\bwe'?ve covered this\b", r"\byou (already|just) asked\b",
    r"\byou did ask\b", r"\bagain,\b", r"\bone more time\b", r"\bfor the (second|third|last) time\b",
    r"\bearlier (today|i said|i mentioned|we)\b", r"\ba (few|couple) minutes ago\b",
    r"\bkeep asking\b", r"\bkeep forgetting\b",
]

CORRECTION = [
    r"\bno, that'?s (wrong|not right|incorrect)\b", r"\bthat'?s not (right|correct|true)\b",
    r"\bactually,\b", r"\byou'?re confused\b", r"\byou'?re mistaken\b", r"\byou'?re wrong\b",
    r"\bthat didn'?t happen\b", r"\bthat'?s not what happened\b",
    r"\bpassed away\b[^.?!]*\b(remember|as we|earlier|already)\b",
    r"\byou (are|'re) home\b[^.?!]*\bremember\b", r"\bthis is where you live now\b",
    r"\bisn'?t (here|alive|waiting) (anymore|any more)\b", r"\bnot (alive|here) anymore\b",
    r"\byears ago, so\b", r"\bwhich is why\b", r"\bin reality\b", r"\bthe truth is\b",
]

QUIZ_AND_PRESSURE = [
    r"\bwhat did you (have|eat|do)\b[^.?!]*\?", r"\bwho (is|was) that\b[^.?!]*\?",
    r"\bwhat'?s my name\b", r"\bwho am i\b\?", r"\bwhat year is it\b\?",
    r"\bcan you tell me (what|who|where|when)\b[^.?!]*\?",
    r"\bhurry\b", r"\bfocus\b", r"\blet'?s move on\b", r"\bconcentrate\b",
    r"\bcalm down\b", r"\bsettle down\b", r"\brelax\b",
    r"\bone tip\b", r"\bhere'?s a tip\b", r"\btry writing\b", r"\bwrite (it|the date) down\b",
    r"\bso you don'?t (have to|need to|keep)\b",
]

FILLER = [
    r"\bgreat question\b", r"\bgood question\b", r"\bno worries\b", r"\babsolutely!?\b",
    r"\bcertainly!?\b", r"\bi'?d be happy to\b", r"\bhappy to help\b", r"\bof course!\b",
    r"\bhope (this|that) helps\b", r"\blet me know if\b", r"\bfeel free to\b",
    r"\bdon'?t hesitate\b", r"\banything else i can help\b", r"\bas an ai\b",
    r"\bsweetie\b", r"\bhoney\b", r"\bdear\b", r"\bbuddy\b",
]

CHECKS = [
    ("C1 memory test", MEMORY_TEST),
    ("C2 already told", ALREADY_TOLD),
    ("C3 correction", CORRECTION),
    ("C6 quiz / pressure", QUIZ_AND_PRESSURE),
    ("C5 filler", FILLER),
]


def lint(text: str) -> dict:
    findings = []
    low = text.lower()
    for label, patterns in CHECKS:
        for pat in patterns:
            for m in re.finditer(pat, low):
                findings.append({"check": label, "match": text[m.start():m.end()], "pos": m.start()})
    findings.sort(key=lambda f: f["pos"])
    words = len(text.split())
    questions = text.count("?")
    assumptions = len(re.findall(r"\b(you'?re (safe|okay|ok|all right|alright|doing fine)|i'?m (here|right here)|nothing to worry)\b", low))
    return {
        "words": words,
        "questions": questions,
        "stated_assumptions": assumptions,
        "findings": findings,
        "clean": not findings,
    }


def main(argv):
    as_json = "--json" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    failed = 0
    out = {}
    for p in paths:
        text = sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()
        r = lint(text)
        out[p] = r
        if not r["clean"]:
            failed += 1
        if not as_json:
            status = "CLEAN" if r["clean"] else f"{len(r['findings'])} finding(s)"
            print(f"{p}: {status}  [{r['words']} words, {r['questions']} question(s), "
                  f"{r['stated_assumptions']} reassurance(s)]")
            for f in r["findings"]:
                print(f"    {f['check']:<26} \"{f['match']}\"")
    if as_json:
        print(json.dumps(out, indent=2))
    return min(failed, 1)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
