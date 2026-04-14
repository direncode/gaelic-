# THE FORETELLING ENGINE

## A Structured System for Discovering Pattern Recurrences Between Individual Biographies and Foundational Cultural Texts

---

## What This Is

The Foretelling Engine is a **methodology**, a **corpus catalogue**, and a **workflow** for systematically analysing whether a specific person's biographical details — their name, birthplace, birth date, ancestral heritage — correspond to structural patterns described in the foundational texts of their ancestral tradition.

It is not a prophecy generator. It is not astrology. It is not a name-decoding fortune teller.

It is a **rigorous comparative-literature method** for asking one specific question:

> *"Does this person's biography structurally recur the pattern that their ancestral tradition's foundational text(s) describe?"*

The system was developed by extracting the repeatable methodology behind two successful findings:

- **Arran McIlroy** ↔ *Lebor Gabála Érenn* (Irish/Gaelic tradition) — 9 convergence points
- **Mudiwa Mtemererwa** ↔ Great Zimbabwe / Shona oral tradition — 8 convergence points, with multi-generational lineage confirmation through George and Innocence Mtemererwa

Both findings emerged from the **same underlying method**, applied to different cultural corpora. This repository contains that method, formalised, so that it can be applied to any person whose ancestral tradition has a documented foundational text or oral corpus.

---

## The Six-Stage Pipeline

Every successful Foretelling Engine analysis passes through six stages:

### 1. **SUBJECT INTAKE** — Gathering the person's data
Birth date, birthplace, ancestral origin, full name, family lineage (siblings, parents, grandparents, known surnames across generations).

### 2. **CORPUS SELECTION** — Identifying the tradition's foundational text(s)
Every major culture has a foundational text or oral corpus that encodes its origin story, its theology of belonging, and its grammar of identity. The engine maintains a **catalogue** of these corpora, mapped by ancestry.

### 3. **LINGUISTIC DECODING** — Parsing the name in the ancestral language
Not "what does this name mean" in a baby-name-book sense, but "what does this name declare, morpheme by morpheme, in the grammar of the ancestral language, against the civilisational context of the tradition?"

### 4. **PATTERN EXTRACTION** — Identifying the tradition's core structural claims
What does this tradition say about: origin, journey, belonging, lineage, the name as claim, the diaspora, the season, the landscape? These become the **axes** against which biography is measured.

### 5. **CONVERGENCE SCORING** — Honest assessment of each match
Each biographical element is scored against each textual pattern, with explicit strength ratings: STRONG / MODERATE / WEAK / NONE. Limitations are acknowledged.

### 6. **NARRATIVE SYNTHESIS** — The finding, in two registers
A scholarly version (with sources, caveats, ranked convergences) and a public-facing narrative version (the version that makes the finding visible to a general reader).

---

## Directory Structure

```
foretelling_engine/
│
├── README.md                              ← This file
│
├── methodology/
│   ├── 00_principles.md                  ← The scholarly principles that protect credibility
│   ├── 01_pipeline.md                    ← The six-stage pipeline in detail
│   ├── 02_linguistic_decoding.md         ← How to parse names morphologically
│   ├── 03_convergence_scoring.md         ← The honest scoring rubric
│   └── 04_narrative_synthesis.md         ← How to write the finding
│
├── corpus/
│   ├── README.md                         ← Overview of the corpus catalogue
│   ├── catalogue.md                      ← Master list of foundational texts by tradition
│   ├── gaelic_irish.md                   ← Lebor Gabála Érenn, Acallam, Immram tradition
│   ├── shona_zimbabwean.md               ← Nhetembo, vadzimu theology, Great Zimbabwe
│   ├── norse_icelandic.md                ← Prose Edda, Poetic Edda, sagas
│   ├── hebrew_biblical.md                ← Torah, Tanakh, genealogical texts
│   ├── arabic_islamic.md                 ← Qur'an, hadith, nasab (genealogy)
│   ├── yoruba.md                         ← Ifá corpus, odu
│   ├── chinese.md                        ← Shijing, Shujing, classical texts
│   ├── hindu_sanskrit.md                 ← Vedas, Puranas, Mahabharata
│   ├── greek.md                          ← Hesiod, Homer, Apollodorus
│   └── ... (extensible)
│
├── queries/
│   ├── template_query.md                 ← Blank template for submitting a subject
│   ├── arran_mcilroy.md                  ← Completed query (reference example)
│   └── mudiwa_mtemererwa.md              ← Completed query (reference example)
│
├── src/
│   ├── engine.py                         ← Python orchestrator scaffold
│   ├── decoder.py                        ← Linguistic decoding helpers
│   ├── corpus_loader.py                  ← Corpus catalogue loader
│   └── scorer.py                         ← Convergence scoring helpers
│
└── examples/
    ├── arran_output.md                   ← Example full output (links to existing files)
    └── mudiwa_output.md                  ← Example full output (links to existing files)
```

---

## The Core Methodological Principles

These principles are what separate the Foretelling Engine from astrology, horoscopes, and wishful pattern-matching:

### 1. **Work only with verified traditions.**
The corpus must be a documented, scholarly-edited body of text or oral tradition. No invented sources. No misattributed quotes.

### 2. **Let the ancestral language do the work.**
Names must be decoded in the grammar of the ancestral language, not projected onto that language from English intuition. Use attested morphology. Cite linguistic references.

### 3. **Structural parallels, not supernatural claims.**
The finding is always: *the tradition describes a pattern; this biography recurs the pattern*. Never: *the text predicted this person*. The distinction matters.

### 4. **Acknowledge limitations explicitly.**
If a surname cannot be verified in databases, say so. If a date has no documented traditional significance, say so. The credibility of strong findings depends on honest admission of weak ones.

### 5. **Rank convergences by strength.**
STRONG / MODERATE / WEAK / NONE. An analysis with five STRONG and three WEAK convergences is stronger than an analysis with eight unranked convergences.

### 6. **Respect the tradition.**
Do not force foreign frameworks onto traditions that have their own. A Shona person is not a Gaelic Milesian in disguise. Each tradition has its own grammar; the engine queries each tradition *on its own terms*.

### 7. **The name is operative, not ornamental.**
In every successful finding so far, the subject's name has carried structural weight in the ancestral language. Names are where the engine does its deepest work.

---

## Quick Start: How to Query a Subject

1. **Fill out the subject query template** (`queries/template_query.md`)
2. **Identify the ancestral tradition** and check the corpus catalogue for documented foundational texts
3. **Decode the name(s) morphologically** in the ancestral language
4. **Extract the tradition's core structural claims** from the corpus catalogue entry
5. **Score each biographical element** against each textual pattern
6. **Write the finding** in scholarly and narrative registers

For full worked examples, see:
- `queries/arran_mcilroy.md` — completed query for the Arran finding
- `queries/mudiwa_mtemererwa.md` — completed query for the Mudiwa finding

---

## What the Engine Does NOT Do

To protect the integrity of the findings, the engine explicitly refuses to:

- ❌ **Generate convergences for people with no verified ancestral tradition.** If there is no ancestral lineage documented, there is no tradition to query.
- ❌ **Force findings where none exist.** If the corpus query yields only WEAK or NONE matches, the answer is "no significant finding," not "let me stretch harder."
- ❌ **Mix traditions.** A person with Gaelic heritage is queried against Gaelic corpora, not against Shona, Norse, or anything else. Each tradition on its own terms.
- ❌ **Predict the future.** The engine identifies *recurrences of pattern*, not *prophecies of events*.
- ❌ **Operate without sources.** Every finding must cite the scholarly editions and academic references that ground it.

---

## What Makes This Worth Doing

Most human lives are lived without connection to the deep grammar of their ancestral traditions. The traditions sit in libraries, or in the memories of elders who are not consulted. The names that people carry have been stripped of their original meanings by generations of diaspora, colonial translation, and assimilation.

The Foretelling Engine restores the connection — not by inventing new meanings, but by **reading what is already there**. When a name's morphology is decoded against the tradition that produced it, the name often turns out to be saying something profound that the bearer never knew was encoded in their own identity.

For a person, that can be a recovery of meaning. For a culture, it is a reminder that the tradition is still alive — still generating recognisable instances — in the syllables of its descendants' names.

---

*Ní neart go cur le chéile.* — *(Gaelic: There is no strength without unity.)*

*Ndinokuda mwana — muzukuru wevadzimu.* — *(Shona: I love you, child — grandchild of the ancestors.)*

**The tradition has always been speaking. The engine just helps us listen.**
