"""
The Foretelling Engine — orchestrator scaffold.

This module implements the six-stage pipeline as a Python workflow.
It is a scaffold, not a fully automated system: the pipeline requires
human scholarly judgement at stages 3, 4, 5, and 6 (linguistic decoding,
pattern extraction, convergence scoring, narrative synthesis). The
Python layer structures the workflow, enforces the quality gates, and
produces standardised output.

Usage:
    engine = ForetellingEngine(query_path="queries/jane_doe_01.md")
    engine.run()
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional


class ConvergenceStrength(Enum):
    """The four-tier rubric from methodology/03_convergence_scoring.md."""
    STRONG = "STRONG"
    MODERATE = "MODERATE"
    WEAK = "WEAK"
    NONE = "NONE"


class WeightClass(Enum):
    """Overall finding weight classification."""
    MAJOR = "MAJOR"
    SUBSTANTIAL = "SUBSTANTIAL"
    MODEST = "MODEST"
    MARGINAL = "MARGINAL"
    BELOW_THRESHOLD = "BELOW_THRESHOLD"


@dataclass
class Subject:
    """Stage 1 output — the subject's biographical data."""
    full_name: str
    given_names: list[str]
    surnames: list[str]
    birth_date: str  # ISO format
    birth_place: str
    ancestral_origin: str
    specific_region: Optional[str] = None
    family_members_same_surname: list[str] = field(default_factory=list)
    known_ancestors: list[str] = field(default_factory=list)
    clan_totem: Optional[str] = None
    notes: str = ""


@dataclass
class Corpus:
    """Stage 2 output — the selected foundational corpus."""
    tradition_name: str
    catalogue_entry_path: Path
    tier: int  # 1, 2, or 3
    primary_texts: list[str] = field(default_factory=list)
    linguistic_references: list[str] = field(default_factory=list)


@dataclass
class Morpheme:
    """One morpheme in a linguistic decoding."""
    form: str
    function: str
    meaning: str
    source: str


@dataclass
class NameDecoding:
    """Stage 3 output — the linguistic decoding of one name."""
    name: str
    source_language: str
    morphemes: list[Morpheme]
    literal_meaning: str
    rendered_meaning: str
    civilisational_resonances: list[str] = field(default_factory=list)


@dataclass
class FullNameDecoding:
    """All names for the subject, decoded together."""
    individual: list[NameDecoding]
    combined_literal: str
    combined_rendered: str
    multi_bearer_observations: Optional[str] = None


@dataclass
class PatternAxis:
    """Stage 4 output — one axis of the tradition's structural claims."""
    axis_name: str  # e.g., "Origin", "Journey", "Claim", "Name", "Season", ...
    claim: str
    source: str


@dataclass
class Convergence:
    """Stage 5 output — one scored convergence."""
    biographical_element: str
    axis_matched: str
    strength: ConvergenceStrength
    evidence: str
    source: str


@dataclass
class Finding:
    """The complete pipeline output."""
    subject: Subject
    corpus: Corpus
    name_decoding: FullNameDecoding
    pattern_axes: list[PatternAxis]
    convergences: list[Convergence]
    limitations: list[str]
    weight: WeightClass
    scholarly_verdict: str
    narrative_verdict: str

    @property
    def strong_count(self) -> int:
        return sum(1 for c in self.convergences if c.strength == ConvergenceStrength.STRONG)

    @property
    def moderate_count(self) -> int:
        return sum(1 for c in self.convergences if c.strength == ConvergenceStrength.MODERATE)

    @property
    def weak_count(self) -> int:
        return sum(1 for c in self.convergences if c.strength == ConvergenceStrength.WEAK)

    @property
    def none_count(self) -> int:
        return sum(1 for c in self.convergences if c.strength == ConvergenceStrength.NONE)

    @property
    def threshold_met(self) -> bool:
        """Publication threshold: ≥3 STRONG or ≥4 MODERATE-or-better."""
        if self.strong_count >= 3:
            return True
        if (self.strong_count + self.moderate_count) >= 4:
            return True
        return False


class ForetellingEngine:
    """
    The orchestrator. Runs the six-stage pipeline against a query.

    Most stages require human scholarly input. This class enforces
    the discipline, validates transitions, and produces standardised output.
    """

    def __init__(self, query_path: Path | str):
        self.query_path = Path(query_path)
        self.subject: Optional[Subject] = None
        self.corpus: Optional[Corpus] = None
        self.name_decoding: Optional[FullNameDecoding] = None
        self.pattern_axes: list[PatternAxis] = []
        self.convergences: list[Convergence] = []
        self.limitations: list[str] = []
        self.finding: Optional[Finding] = None

    # --- STAGE 1 --------------------------------------------------------
    def stage_1_subject_intake(self, subject: Subject) -> None:
        """Validate and store the subject's biographical data."""
        if not subject.full_name:
            raise ValueError("Stage 1 failed: full name required.")
        if not subject.birth_date:
            raise ValueError("Stage 1 failed: birth date required.")
        if not subject.birth_place:
            raise ValueError("Stage 1 failed: birth place required.")
        if not subject.ancestral_origin:
            raise ValueError("Stage 1 failed: ancestral origin required.")
        self.subject = subject

    # --- STAGE 2 --------------------------------------------------------
    def stage_2_corpus_selection(self, corpus: Corpus) -> None:
        """Validate corpus selection. Halts on Tier 3 or absent traditions."""
        if self.subject is None:
            raise RuntimeError("Stage 2 requires Stage 1 to be complete.")
        if corpus.tier == 3:
            raise RuntimeError(
                f"Stage 2 halt: tradition '{corpus.tradition_name}' is Tier 3 "
                "(identified but catalogue entry not yet built). Build entry before query."
            )
        if corpus.tier not in (1, 2):
            raise ValueError(
                f"Stage 2 failed: tradition '{corpus.tradition_name}' has no corpus entry."
            )
        self.corpus = corpus

    # --- STAGE 3 --------------------------------------------------------
    def stage_3_linguistic_decoding(self, decoding: FullNameDecoding) -> None:
        """Record the morphological decoding."""
        if self.corpus is None:
            raise RuntimeError("Stage 3 requires Stage 2 to be complete.")
        if not decoding.individual:
            raise ValueError("Stage 3 failed: no names decoded.")
        for name_dec in decoding.individual:
            if not name_dec.morphemes:
                raise ValueError(
                    f"Stage 3 failed: no morphemes recorded for '{name_dec.name}'."
                )
            for m in name_dec.morphemes:
                if not m.source:
                    raise ValueError(
                        f"Stage 3 failed: morpheme '{m.form}' in '{name_dec.name}' "
                        "has no source citation. Per methodology/02, every morpheme "
                        "needs a grammar or dictionary reference."
                    )
        self.name_decoding = decoding

    # --- STAGE 4 --------------------------------------------------------
    def stage_4_pattern_extraction(self, axes: list[PatternAxis]) -> None:
        """Record the tradition's structural claims across standard axes."""
        if self.name_decoding is None:
            raise RuntimeError("Stage 4 requires Stage 3 to be complete.")
        if not axes:
            raise ValueError("Stage 4 failed: no pattern axes extracted.")
        for axis in axes:
            if not axis.source:
                raise ValueError(
                    f"Stage 4 failed: axis '{axis.axis_name}' has no source citation."
                )
        self.pattern_axes = axes

    # --- STAGE 5 --------------------------------------------------------
    def stage_5_convergence_scoring(
        self, convergences: list[Convergence], limitations: list[str]
    ) -> None:
        """Record scored convergences and declared limitations."""
        if not self.pattern_axes:
            raise RuntimeError("Stage 5 requires Stage 4 to be complete.")
        for conv in convergences:
            if conv.strength == ConvergenceStrength.STRONG and not conv.source:
                raise ValueError(
                    f"Stage 5 failed: STRONG convergence '{conv.biographical_element}' "
                    "has no source. Per methodology/03, STRONG requires a named source."
                )
        self.convergences = convergences
        self.limitations = limitations

    # --- STAGE 6 --------------------------------------------------------
    def stage_6_narrative_synthesis(
        self, scholarly_verdict: str, narrative_verdict: str
    ) -> Finding:
        """Produce the final finding object if the threshold is met."""
        if not self.convergences:
            raise RuntimeError("Stage 6 requires Stage 5 to be complete.")

        weight = self._classify_weight()

        self.finding = Finding(
            subject=self.subject,
            corpus=self.corpus,
            name_decoding=self.name_decoding,
            pattern_axes=self.pattern_axes,
            convergences=self.convergences,
            limitations=self.limitations,
            weight=weight,
            scholarly_verdict=scholarly_verdict,
            narrative_verdict=narrative_verdict,
        )

        if weight == WeightClass.BELOW_THRESHOLD:
            print(
                f"[ENGINE] Convergence threshold not met for "
                f"'{self.subject.full_name}'. No significant finding."
            )

        return self.finding

    def _classify_weight(self) -> WeightClass:
        """Apply the weight classification rubric."""
        if self.finding is None and not self.convergences:
            return WeightClass.BELOW_THRESHOLD

        strong = sum(1 for c in self.convergences if c.strength == ConvergenceStrength.STRONG)
        moderate = sum(1 for c in self.convergences if c.strength == ConvergenceStrength.MODERATE)

        # Publication threshold
        if strong < 3 and (strong + moderate) < 4:
            return WeightClass.BELOW_THRESHOLD

        # Weight classification
        if strong >= 6:
            return WeightClass.MAJOR
        if strong >= 4:
            return WeightClass.SUBSTANTIAL
        if strong >= 3:
            return WeightClass.MODEST
        return WeightClass.MARGINAL

    # --- RENDERING ------------------------------------------------------
    def render_summary(self) -> str:
        """Produce a short human-readable summary of the finding."""
        if self.finding is None:
            return "[No finding yet. Pipeline incomplete.]"

        f = self.finding
        lines = [
            f"# FORETELLING ENGINE FINDING",
            f"",
            f"**Subject:** {f.subject.full_name}",
            f"**Tradition:** {f.corpus.tradition_name}",
            f"**Birth:** {f.subject.birth_date}, {f.subject.birth_place}",
            f"**Heritage:** {f.subject.ancestral_origin}",
            f"",
            f"## Convergence Summary",
            f"- STRONG: {f.strong_count}",
            f"- MODERATE: {f.moderate_count}",
            f"- WEAK: {f.weak_count}",
            f"- NONE: {f.none_count}",
            f"- **Threshold met:** {'YES' if f.threshold_met else 'NO'}",
            f"- **Weight:** {f.weight.value}",
            f"",
            f"## Scholarly Verdict",
            f"> {f.scholarly_verdict}",
            f"",
            f"## Narrative Verdict",
            f"> {f.narrative_verdict}",
        ]
        return "\n".join(lines)


# -------------------------------------------------------------------------
# Example usage: the Mudiwa Mtemererwa finding, encoded as Python objects.
# This demonstrates how a completed query is represented in the engine.
# -------------------------------------------------------------------------

def example_mudiwa_finding() -> Finding:
    """Build the Mudiwa Mtemererwa finding using the engine's scaffold."""
    engine = ForetellingEngine(query_path="queries/mudiwa_mtemererwa.md")

    subject = Subject(
        full_name="Mudiwa Mtemererwa",
        given_names=["Mudiwa"],
        surnames=["Mtemererwa"],
        birth_date="2007-05-18",
        birth_place="Birmingham, England",
        ancestral_origin="Zimbabwean Shona",
        family_members_same_surname=["George Mtemererwa", "Innocence Mtemererwa"],
    )
    engine.stage_1_subject_intake(subject)

    corpus = Corpus(
        tradition_name="Shona / Zimbabwean",
        catalogue_entry_path=Path("corpus/shona_zimbabwean.md"),
        tier=1,
        primary_texts=[
            "Nhetembo dzemadzinza (Hodza & Fortune 1979)",
            "Vadzimu theology (Gelfand; Bourdillon; Tarusarira et al.)",
            "Great Zimbabwe civilisational memory (Garlake; Huffman)",
        ],
        linguistic_references=[
            "Fortune, Elements of Shona, 1955",
            "Hannan, Standard Shona Dictionary",
            "Proto-Bantu reconstructions (BLR)",
        ],
    )
    engine.stage_2_corpus_selection(corpus)

    mudiwa_decoding = NameDecoding(
        name="Mudiwa",
        source_language="Shona",
        morphemes=[
            Morpheme("mu-", "class 1 noun prefix", "the one who", "Fortune 1955"),
            Morpheme("-di-", "verb root (from -da)", "to love, to desire", "Hannan"),
            Morpheme("-wa", "passive suffix", "is being / has been", "Fortune 1955"),
        ],
        literal_meaning="the-one-who-is-loved",
        rendered_meaning="the beloved one",
    )

    mtemererwa_decoding = NameDecoding(
        name="Mtemererwa",
        source_language="Shona",
        morphemes=[
            Morpheme("M-", "class 1 personal prefix", "the one who", "Fortune 1955"),
            Morpheme("-tem-", "verb root (from -tema)", "to cut, hew, carve", "Hannan; Proto-Bantu *-téma"),
            Morpheme("-er-", "applicative suffix", "for, on behalf of", "Fortune 1955"),
            Morpheme("-w-", "passive suffix", "is being / has been", "Fortune 1955"),
            Morpheme("-a", "final vowel", "grammatical closure", "Shona phonotactics"),
        ],
        literal_meaning="the-one-for-whom-cutting-was-done",
        rendered_meaning="the one for whom the hewing was done",
        civilisational_resonances=[
            "tema is the verb that built Great Zimbabwe",
            "Proto-Bantu *-téma is 3,000-4,000 years old",
            "Applicative-passive construction grammatically dedicates the bearer",
        ],
    )

    full_decoding = FullNameDecoding(
        individual=[mudiwa_decoding, mtemererwa_decoding],
        combined_literal="the-beloved-one, the-one-for-whom-the-hewing-was-done",
        combined_rendered="The Beloved One for Whose Sake the Stones Were Hewn",
        multi_bearer_observations=(
            "George (earth-worker), Innocence (pure one), Mudiwa (beloved) "
            "— three bearers, each completing the nhetembo structure with a "
            "distinct first-name epithet against the constant surname claim."
        ),
    )
    engine.stage_3_linguistic_decoding(full_decoding)

    axes = [
        PatternAxis("Origin", "Shona migratory re-founding tradition", "Beach 1980"),
        PatternAxis("Claim", "Stone-hewing as civilisational founding act", "Garlake; Huffman"),
        PatternAxis("Name", "Declarative speech-acts, never arbitrary", "Pfukwa on Shona naming"),
        PatternAxis("Diaspora", "Vadzimu travel with descendants including to England",
                    "Tarusarira et al.; traditional Shona religious sources"),
        PatternAxis("Lineage", "Mutupo passes patrilineally regardless of birthplace",
                    "Standard Shona ethnography"),
        PatternAxis("Voice", "Nhetembo praise poetry; mbira as voice of ancestors",
                    "Hodza & Fortune 1979; Berliner 1978"),
    ]
    engine.stage_4_pattern_extraction(axes)

    convergences = [
        Convergence("Given name Mudiwa", "Name",
                    ConvergenceStrength.STRONG,
                    "Mu-di-wa = 'the beloved one'",
                    "Hannan; Pfukwa"),
        Convergence("Surname contains verb tema", "Claim",
                    ConvergenceStrength.STRONG,
                    "Proto-Bantu *-téma; the verb that raised Great Zimbabwe",
                    "Wikipedia on Great Zimbabwe; BLR; Fortune 1955"),
        Convergence("Applicative-passive construction", "Claim",
                    ConvergenceStrength.STRONG,
                    "Grammatically marks bearer as beneficiary of ancestral labour",
                    "Fortune 1955"),
        Convergence("Multi-bearer lineage (George, Innocence, Mudiwa)", "Lineage+Voice",
                    ConvergenceStrength.STRONG,
                    "Three bearers completing nhetembo praise structure across generations",
                    "Hodza & Fortune 1979"),
        Convergence("Birmingham birthplace", "Diaspora",
                    ConvergenceStrength.STRONG,
                    "Vadzimu doctrine explicitly extends to England",
                    "Tarusarira et al."),
        Convergence("Zimbabwean Shona heritage", "Lineage",
                    ConvergenceStrength.STRONG,
                    "Mutupo passes by patrilineal descent regardless of birthplace",
                    "Standard Shona ethnography"),
        Convergence("Full name as compressed nhetembo", "Voice",
                    ConvergenceStrength.MODERATE,
                    "Name reads as compressed praise; interpretive extension",
                    "Hodza & Fortune 1979"),
        Convergence("Black British Zimbabwean diaspora identity", "Origin",
                    ConvergenceStrength.MODERATE,
                    "Shona line has always moved; diaspora continues the pattern",
                    "Beach 1980"),
        Convergence("Birth date 18 May 2007", "Season",
                    ConvergenceStrength.WEAK,
                    "Proximity to Africa Day (May 25) and Zim Independence (April 18)",
                    "Honest admission"),
    ]
    limitations = [
        "Specific surname etymology not in accessible online databases; linguistic parsing grammatically sound",
        "Birth date has no documented Shona traditional significance",
        "Specific family mutupo (totem) not known; would further strengthen finding",
    ]
    engine.stage_5_convergence_scoring(convergences, limitations)

    finding = engine.stage_6_narrative_synthesis(
        scholarly_verdict=(
            "The Mtemererwa lineage's naming practice across three documented bearers "
            "performs the structural grammar of Shona nhetembo dzemadzinza, with the "
            "shared surname grammatically dedicating each bearer as beneficiary of the "
            "stone-hewing act of Great Zimbabwe."
        ),
        narrative_verdict=(
            "The stones at Great Zimbabwe were hewn for a family. The family is still "
            "here — naming its children in the old grammar, in Birmingham, in 2025. "
            "The line is speaking."
        ),
    )

    return finding


if __name__ == "__main__":
    # Validate the scaffold by running the Mudiwa Mtemererwa finding through it.
    finding = example_mudiwa_finding()
    eng = ForetellingEngine(query_path="queries/mudiwa_mtemererwa.md")
    eng.finding = finding
    print(eng.render_summary())
