# PaperWorkflow evidence package

- Workflow ID: 9d52b167e5da5cdf
- Input: /home/simcrq/0_Project/paperworkflow/INput/Fail.pdf
- Markdown: /home/simcrq/0_Project/paperworkflow/temp_markdowns/29f92e3a9869f609/Fail.md
- Text-capture fidelity: **ready** (90/100)
- Scientific-synthesis readiness: **review** (87/100)
- Mechanism completeness: **complete_with_available_sources**

## Readiness gates

| Gate | Status | Meaning |
|---|---|---|
| text_capture_fidelity | pass | Raw OCR/Markdown text must be usable. |
| reading_order_integrity | pass | Scientific prose must not be silently reordered by layout streams. |
| support_span_exposure | pass | Every retrieved item must expose an exact sentence/span and offsets. |
| evidence_coverage | review | Required workflow facets must be covered, not merely represented in top-k. |
| supplementary_dependencies | pass | Required supplementary evidence must be locally available for a complete mechanism audit. |
| quantity_and_symbol_consistency | pass | Linked quantities and symbol definitions require contextual consistency. |

## Quality dimensions

| Dimension | Score | Readiness |
|---|---:|---|
| extraction | 90 | ready |
| structure | 78 | review |
| reading_order | 100 | ready |
| semantic_structure | 55 | review |
| chunk_coherence | 82 | review |
| retrieval | 65 | review |
| quantities | 100 | ready |
| dependencies | 100 | ready |

### Audit warnings

- [extraction/low] core_sections_missing: Several common paper sections were not identified: abstract, methods, results, conclusion.
- [structure/medium] mixed_scientific_streams_in_chunks: Chunks combine body, figure-caption and/or image streams: E002, E003.
- [retrieval/medium] evidence_coverage_incomplete: Precision or facet coverage is incomplete for: custom-04, custom-07.

## Semantic outline

| Chunk | Raw heading | Semantic owner | Kind | Lines | Figure parent(s) |
|---|---|---|---|---:|---|
| E001 | Failure Mechanisms of Graphene under Tension | Failure Mechanisms of Graphene under Tension | semantic | 1-16 |  |
| E002 | Failure Mechanisms of Graphene under Tension | Failure Mechanisms of Graphene under Tension | semantic | 18-28 |  |
| E003 | Failure Mechanisms of Graphene under Tension | Failure Mechanisms of Graphene under Tension | semantic | 30-48 |  |
| E004 | Failure Mechanisms of Graphene under Tension | Failure Mechanisms of Graphene under Tension | semantic | 50-102 |  |

## Query-to-evidence map

### Custom question 1 (custom-01)

- Intent: general
- Status: **acceptable**
- Evidence: EV0001, EV0002, EV0003, EV0004, EV0005

### Custom question 2 (custom-02)

- Intent: general
- Status: **acceptable**
- Evidence: EV0006, EV0004, EV0005, EV0007, EV0002

### Custom question 3 (custom-03)

- Intent: general
- Status: **acceptable**
- Evidence: EV0002, EV0008, EV0009, EV0010, EV0011

### Custom question 4 (custom-04)

- Intent: physical_mechanism
- Status: **weak**
- Evidence: EV0002, EV0012, EV0013, EV0014, EV0015, EV0016, EV0017, EV0018, EV0019
- Coverage: 50.0%; missing: multiscale_structure, photonic_bandgap, total_internal_reflection

### Custom question 5 (custom-05)

- Intent: general
- Status: **acceptable**
- Evidence: EV0003, EV0016, EV0011, EV0020, EV0021

### Custom question 6 (custom-06)

- Intent: general
- Status: **acceptable**
- Evidence: EV0022, EV0006, EV0004, EV0005, EV0007

### Custom question 7 (custom-07)

- Intent: limitations
- Status: **weak**
- Evidence: EV0023, EV0024, EV0025, EV0026, EV0027
- Coverage: 0.0%; missing: illumination_geometry, observation_geometry, background_or_substrate, evidence_dependency

## Evidence Registry

Evidence text appears only here; queries above reference these stable IDs.

### EV0001 · S0101 · E003

- Source lines: 35-35
- Source chars: 12112-12266
- Modality / support: body_text / direct_observation
- Used by: custom-01
- Text: Therefore, the question arises as to when the elastic instability is the failure mode versus the $K_{1}$ -mode instability for a generic state of tension.

### EV0002 · S0032 · E001

- Source lines: 16-16
- Source chars: 4004-4166
- Modality / support: body_text / direct_observation
- Used by: custom-01, custom-02, custom-03, custom-04
- Text: In this work, we demonstrate that a soft mode is responsible for a phase transition and the resulting mechanical failure of graphene in certain states of tension.

### EV0003 · S0035 · E001

- Source lines: 16-16
- Source chars: 4630-4779
- Modality / support: body_text / direct_observation
- Used by: custom-01, custom-05
- Text: Furthermore, our results on graphene yield an optical phonon instability, as opposed to the acoustic instability observed previously in bulk systems.

### EV0004 · S0059 · E002

- Source lines: 23-23
- Source chars: 7369-7533
- Modality / support: body_text / author_inference
- Used by: custom-01, custom-02, custom-06
- Text: An additional phonon calculation at a strain of $\epsilon_{A} = 0.212$ (not pictured) indicates that the $K_{1}$ mode has become imaginary resulting in a soft mode.

### EV0005 · S0125 · E003

- Source lines: 48-48
- Source chars: 15199-15338
- Modality / support: body_text / measurement
- Used by: custom-01, custom-02, custom-06
- Text: Our prediction of the soft $K_{1}$ mode may be directly verified experimentally by measuring the phonon dispersion as a function of strain.

### EV0006 · S0080 · E002

- Source lines: 28-28
- Source chars: 9535-9685
- Modality / support: body_text / direct_observation
- Used by: custom-02, custom-06
- Text: As the strain is increased, the mode continually becomes softer and eventually the curvature at zero amplitude goes to zero and the mode becomes soft.

### EV0007 · S0081 · E002

- Source lines: 28-28
- Source chars: 9686-9865
- Modality / support: body_text / direct_observation
- Used by: custom-02, custom-06
- Text: This analysis predicts the soft mode to occur at $\epsilon_{A}=0.213$ , independently confirming the results of our phonons which yield a soft mode at $\epsilon_{A}=0.205-0.212$ .

### EV0008 · S0031 · E001

- Source lines: 16-16
- Source chars: 3759-4003
- Modality / support: body_text / direct_observation
- Used by: custom-03
- Text: There are numerous structural phase transitions in which the two phases are directly connected by a soft mode, and the concept of the soft mode gained prominence in the context of elucidating the ferroelectric transition in $BaTiO_{3}$ [11,12].

### EV0009 · S0093 · E003

- Source lines: 30-30
- Source chars: 11353-11539
- Modality / support: body_text / author_inference
- Used by: custom-03
- Text: As a result, the soft $K_{1}$ mode can be seen not only as the precursor to a phase transition as in soft-mode theory, but also as a soft-mode which leads directly to mechanical failure.

### EV0010 · S0060 · E002

- Source lines: 23-23
- Source chars: 7534-7659
- Modality / support: body_text / direct_observation
- Used by: custom-03
- Text: This implies that the structure has become unstable and will undergo a phase transition by distorting along the $K_{1}$ mode.

### EV0011 · S0010 · E001

- Source lines: 8-8
- Source chars: 644-867
- Modality / support: body_text / direct_observation
- Used by: custom-03, custom-05
- Text: One failure mechanism is a novel soft-mode phonon instability of the $K_{1}$ mode, whereby the graphene sheet undergoes a phase transition and is driven towards isolated hexagonal rings resulting in a reduction of strength.

### EV0012 · S0041 · E002

- Source lines: 18-18
- Source chars: 5466-5560
- Modality / support: body_text / simulation
- Used by: custom-04
- Text: All DFT calculations were performed using the Vienna ab initio simulation program (VASP) [18].

### EV0013 · S0020 · E001

- Source lines: 14-14
- Source chars: 1997-2107
- Modality / support: body_text / direct_observation
- Used by: custom-04
- Text: This experiment reinvigorates the fundamental question of how and why a material fails under ideal conditions.

### EV0014 · S0009 · E001

- Source lines: 8-8
- Source chars: 493-643
- Modality / support: body_text / direct_observation
- Used by: custom-04
- Text: Using density functional theory, we reveal the mechanisms of mechanical failure of pure graphene under a generic state of tension at zero temperature.

### EV0015 · S0145 · E004

- Source lines: 52-52
- Source chars: 18015-18139
- Modality / support: body_text / direct_observation
- Used by: custom-04
- Text: In conclusion, we have determined the failure mechanisms of pure graphene in a generic state of tension at zero temperature.

### EV0016 · S0036 · E002

- Source lines: 18-18
- Source chars: 4781-5008
- Modality / support: body_text / direct_observation
- Used by: custom-04, custom-05
- Text: In the case of graphene, previous phonon calculations have determined that the elastic instability is the mechanism of failure for uniaxial strain in the armchair or zigzag directions [15] [i.e., $x$ and $y$ directions in Figs.

### EV0017 · S0129 · E003

- Source lines: 48-48
- Source chars: 15714-15881
- Modality / support: body_text / measurement
- Used by: custom-04
- Text: Another more indirect probe would be Raman spectroscopy [21], which has already been performed for graphene under uniaxial tension [24] in the regime of small strains.

### EV0018 · S0019 · E001

- Source lines: 14-14
- Source chars: 1872-1996
- Modality / support: body_text / direct_observation
- Used by: custom-04
- Text: Using nanoindentation, Lee et al. strained graphene until failure under conditions which appear to be very nearly ideal [3].

### EV0019 · S0050 · E002

- Source lines: 21-21
- Source chars: 6438-6496
- Modality / support: body_text / direct_observation
- Used by: custom-04
- Text: The in-plane phonons of graphene under equibiaxial strain.

### EV0020 · S0100 · E003

- Source lines: 35-35
- Source chars: 11886-12111
- Modality / support: body_text / direct_observation
- Used by: custom-05
- Text: The above analysis has revealed that for equibiaxial strain the mode of failure of graphene is radically different than the usual elastic instability which is observed for uniaxial strain in the zigzag or armchair directions.

### EV0021 · S0146 · E004

- Source lines: 52-52
- Source chars: 18140-18318
- Modality / support: body_text / direct_observation
- Used by: custom-05
- Text: The usual elastic instability causes failure for strains near uniaxial while a novel soft-mode phonon instability of the $K_{1}$ mode causes failure for strains near equibiaxial.

### EV0022 · S0082 · E002

- Source lines: 28-28
- Source chars: 9866-9984
- Modality / support: body_text / direct_observation
- Used by: custom-06
- Text: Further strain results in a double-well potential, where the well depth and amplitude increase with increasing strain.

### EV0023 · S0128 · E003

- Source lines: 48-48
- Source chars: 15605-15713
- Modality / support: body_text / direct_observation
- Used by: custom-07
- Text: The challenge in this particular case would be the fact that the graphene would have to be strained in situ.

### EV0024 · S0143 · E004

- Source lines: 50-50
- Source chars: 17758-17834
- Modality / support: body_text / direct_observation
- Used by: custom-07
- Text: This issue can be resolved by bridging theory and experiment in future work.

### EV0025 · S0137 · E004

- Source lines: 50-50
- Source chars: 16803-16898
- Modality / support: body_text / direct_observation
- Used by: custom-07
- Text: Any and all of these differences may be linked to the difference between theory and experiment.

### EV0026 · S0113 · E003

- Source lines: 43-43
- Source chars: 13564-13633
- Modality / support: body_text / direct_observation
- Used by: custom-07
- Text: A given direction of strain corresponds to an angle $\theta = 0-90$ .

### EV0027 · S0085 · E003

- Source lines: 30-30
- Source chars: 10317-10410
- Modality / support: body_text / direct_observation
- Used by: custom-07
- Text: Therefore, we must explore the strength and stability of this new phase of strained graphene.

## Referenced source dependencies

- No external supplementary dependency was detected.

## Claim ledger contract

Use EV#### plus S####/E###, raw line range and character offsets for every major claim and number.
Treat supplementary-dependent mechanism claims as partial until the referenced files are available.
