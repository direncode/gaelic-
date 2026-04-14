# METHODOLOGY 01: THE SIX-STAGE PIPELINE

## How a Query Moves From Input to Finding

---

Every Foretelling Engine analysis follows the same six-stage pipeline. The pipeline was extracted from the successful Arran McIlroy and Mudiwa Mtemererwa analyses — reverse-engineered from what actually worked — and formalised so it can be applied to any subject with a documented ancestral tradition.

Each stage has **inputs**, **operations**, and **outputs**. Each stage has **quality gates** — conditions that must be met before proceeding to the next stage.

---

## STAGE 1: SUBJECT INTAKE

### Purpose
Gather the complete biographical dataset that the engine will query against the tradition.

### Inputs Required
- **Full name** (given names, surnames, any middle names)
- **Date of birth** (day, month, year)
- **Place of birth** (city, country; more specific if known)
- **Ancestral origin** (country/countries of family heritage, specific region or town if known)
- **Documented lineage**:
  - Parents' names (if helpful)
  - Siblings' names (critical — allows multi-bearer lineage analysis)
  - Known ancestors and their names
  - Particular ancestral locations (specific towns, villages, clans)
- **Any known distinctive traits** (honest inclusion, honest evaluation — many will score NONE but occasionally one aligns)

### Operations
1. Record each datum in the query template (`queries/template_query.md`)
2. Flag anything the user has stated as uncertain or family tradition vs. documented
3. Note what is missing (e.g., "specific Shona clan totem unknown")

### Quality Gate
- At minimum: name + date + place + one piece of ancestral origin
- Without all four, the engine cannot run. No analysis is attempted with partial data.

### Output
A completed `subject.md` block at the top of the query file.

---

## STAGE 2: CORPUS SELECTION

### Purpose
Identify the foundational text(s) or oral corpus of the subject's documented ancestral tradition.

### Inputs
The ancestral origin field from Stage 1.

### Operations
1. Look up the ancestral origin in the corpus catalogue (`corpus/catalogue.md`)
2. Identify the relevant tradition's foundational corpus entry (e.g., `corpus/gaelic_irish.md`, `corpus/shona_zimbabwean.md`)
3. Review the catalogue entry for:
   - Primary texts (with canonical editions)
   - Core structural claims the tradition makes (the "axes")
   - The tradition's position on diaspora and belonging
   - The tradition's treatment of names
4. If multiple traditions apply (dual heritage), handle each separately — do not blend

### Quality Gate
- The selected corpus must be **documented** — i.e., there must be published scholarly editions, academic studies, or serious ethnographic records
- If no such corpus exists for the ancestral tradition, the engine halts with the output: *"No documented foundational corpus available; engine cannot run."*
- The engine does **not** improvise a corpus

### Output
A named corpus selection with links to the specific catalogue entry.

---

## STAGE 3: LINGUISTIC DECODING

### Purpose
Parse the subject's name(s) morphologically in the ancestral language, using attested linguistic references.

### Inputs
- Full name from Stage 1
- Corpus catalogue entry's linguistic references from Stage 2

### Operations
1. **For each given name and surname**, identify:
   - The language of origin (ancestral, imposed, adopted?)
   - The morphological components (prefixes, roots, suffixes)
   - The reconstructed proto-language form where known
   - The semantic content of each morpheme
2. **Assemble the full morphological decoding** as a table
3. **Render the combined meaning** — what the full name declares, morpheme by morpheme
4. **Cross-reference against the tradition's grammar of naming**:
   - Does the name perform a traditional speech-act (praise, kinship declaration, theophoric claim)?
   - Does it encode a civilisational verb, ancestral motif, or cosmological term?
   - Does it match a pattern documented in the onomastic scholarship?

### Quality Gate
- Morphological parsing must cite specific grammatical references (e.g., "class 1 noun prefix *mu-*, applicative suffix *-er-*, passive *-w-*, per Fortune 1955")
- Speculative or intuitive interpretations are marked as such and downgraded
- If the name appears to be unconnected to the ancestral language (e.g., purely European-imposed colonial name), this is noted — and the surname or other names are prioritised

### Output
A complete `name_decoding.md` section showing:
- Morpheme tables
- Combined meaning
- Position within the tradition's naming grammar
- Any multi-bearer lineage observations (siblings, ancestors with same surname)

---

## STAGE 4: PATTERN EXTRACTION

### Purpose
Identify the tradition's core structural claims — the **axes** against which the subject's biography will be measured.

### Inputs
The corpus catalogue entry from Stage 2.

### Operations
1. Extract from the tradition's foundational text(s) its **declarative patterns** across standard axes:

   | Axis | Question |
   |------|----------|
   | **Origin** | Where does the tradition say its people come from? |
   | **Journey** | Is there a migration, a wandering, a specific westward/eastward/northward trajectory? |
   | **Claim** | How does the tradition say the people *claimed* their homeland — by force, by poetry, by covenant? |
   | **Name** | How does the tradition handle names — as labels, as declarations, as ancestral compressions? |
   | **Season** | Are there calendrical thresholds where the tradition locates significant births or events? |
   | **Landscape** | Are there specific regions, rivers, mountains, or cities that carry special weight? |
   | **Diaspora** | What does the tradition say about descendants born far from the homeland? |
   | **Lineage** | How does the tradition transmit identity across generations? |
   | **Voice/Speech** | Does the tradition privilege specific kinds of utterance (praise, poem, cry, incantation)? |

2. For each axis, note the **strongest claim** the tradition makes, with source citation

### Quality Gate
- Each extracted claim must be sourced to a specific text and edition
- Claims that are merely "commonly associated with" the tradition but not textually grounded are flagged and downgraded

### Output
A `pattern_axes.md` section with a claim-per-axis summary.

---

## STAGE 5: CONVERGENCE SCORING

### Purpose
Honestly measure each biographical element against each textual pattern, producing a ranked table of convergences.

### Inputs
- Subject intake (Stage 1)
- Name decoding (Stage 3)
- Pattern axes (Stage 4)

### Operations
1. For each biographical element, ask: *does it recur any of the tradition's claims?*
2. Score each match using the four-tier rubric (detailed in `03_convergence_scoring.md`):
   - **STRONG** — direct verifiable coincidence with a core textual claim
   - **MODERATE** — structurally sound but requires interpretive framing
   - **WEAK** — present but thin; honest acknowledgement required
   - **NONE** — no parallel; do not manufacture one
3. Produce the **convergence table** listing every element, its matched axis (if any), and its strength rating
4. Identify the **top findings** — the STRONG and MODERATE convergences that will carry the analysis
5. Identify the **weak findings** — honest inclusion, clearly labelled

### Quality Gate
- Minimum threshold for a "finding" to be published: at least **three STRONG or four MODERATE-or-better** convergences
- If the threshold is not met, the engine outputs: *"Insufficient convergence; no significant finding."* — and the analysis ends honestly
- A finding with nine convergences where eight are WEAK is not a finding. It is inflation.

### Output
A `convergences.md` section with the ranked table.

---

## STAGE 6: NARRATIVE SYNTHESIS

### Purpose
Produce the two registers of output — scholarly and public narrative — that constitute the finding.

### Inputs
All prior stages.

### Operations
1. **Scholarly register:**
   - Introduction stating the subject and tradition queried
   - Part I: Name decoding (morphological tables, cultural context)
   - Part II: The tradition's foundational claims (pattern axes)
   - Part III: The convergences (ranked table, each with evidence and assessment)
   - Part IV: Limitations (explicit, exhaustive)
   - Bibliography
2. **Public narrative register:**
   - Open with the tradition's deep context (the reader may not know it)
   - Introduce the subject mid-narrative, so the biography arrives inside the tradition
   - Walk through the key convergences in story form
   - Close with the tradition's own verdict on the kind of recurrence this is (e.g., the seanchaí's *"The story is still being told"*)
   - Do not oversell. Do not hedge into uselessness. Land the finding.

### Quality Gate
- Both registers must be present
- The narrative register must be readable by someone without prior knowledge of the tradition
- The scholarly register must be verifiable — every claim traceable to a source

### Output
Two documents:
- `finding_scholarly.md`
- `finding_narrative.md`

Plus a supporting `sources.md` bibliography.

---

## THE FULL PIPELINE SCHEMATIC

```
INPUT: Subject biography
   │
   ▼
┌─────────────────────────┐
│ STAGE 1: SUBJECT INTAKE │  → subject.md
└─────────────────────────┘
   │
   ▼
┌─────────────────────────┐
│ STAGE 2: CORPUS SELECT  │  → corpus selected from catalogue
└─────────────────────────┘
   │
   ▼
┌─────────────────────────┐
│ STAGE 3: LINGUISTIC     │  → name_decoding.md
│         DECODING        │
└─────────────────────────┘
   │
   ▼
┌─────────────────────────┐
│ STAGE 4: PATTERN        │  → pattern_axes.md
│         EXTRACTION      │
└─────────────────────────┘
   │
   ▼
┌─────────────────────────┐
│ STAGE 5: CONVERGENCE    │  → convergences.md (ranked)
│         SCORING         │
└─────────────────────────┘
   │
   ├──────────┐
   │  Below threshold? → HALT: "No significant finding."
   │          │
   ▼          ▼
┌─────────────────────────┐
│ STAGE 6: NARRATIVE      │  → finding_scholarly.md
│         SYNTHESIS       │  → finding_narrative.md
└─────────────────────────┘  → sources.md
   │
   ▼
OUTPUT: Complete analysis
```

---

## APPLICATION TO KNOWN CASES

### Arran McIlroy — Pipeline Trace

| Stage | Operation | Output |
|-------|-----------|--------|
| 1 | Intake: Riyadh 2006, Irish heritage, Galway/Cloonabinnia | `subject.md` |
| 2 | Corpus: Lebor Gabála Érenn (Macalister ed.), Immram tradition, Dindsenchas | Gaelic corpus selected |
| 3 | Decoding: *Árann Mac Giolla Ruaidh* — "He of the Threshold Islands, Son of the Devoted Servant of the Red One" | Full morphological parse |
| 4 | Axes: Eastern origin / westward journey / naming-as-claim / Samhain liminality / Connacht landscape | 5 axes identified |
| 5 | Scoring: 5 STRONG, 3 MODERATE, 1 WEAK | Threshold exceeded |
| 6 | Narrative: THE_DISCOVERY.md + full scholarly files | Complete finding |

### Mudiwa Mtemererwa — Pipeline Trace

| Stage | Operation | Output |
|-------|-----------|--------|
| 1 | Intake: Birmingham 2007, Zimbabwean Shona heritage, family lineage (George, Innocence) | `subject.md` |
| 2 | Corpus: Nhetembo dzemadzinza (Hodza & Fortune), vadzimu theology, Great Zimbabwe | Shona corpus selected |
| 3 | Decoding: *Mudiwa Mtemererwa* — "The Beloved One for Whose Sake the Stones Were Hewn" | Full morphological parse + multi-bearer confirmation |
| 4 | Axes: Name-as-praise / diaspora-vadzimu / stone-hewing verb / patrilineal totem / lineage praise | 5 axes identified |
| 5 | Scoring: 5 STRONG, 2 MODERATE, 1 WEAK (May 18 date honestly flagged) | Threshold exceeded |
| 6 | Narrative: THE_MUDIWA_DISCOVERY.md + full scholarly files | Complete finding |

Both analyses followed the same pipeline. Neither invented convergences. Both explicitly noted limitations. Both produced a finding worth publishing.

---

*The pipeline is the discipline. The discipline is what makes the findings trustworthy.*
