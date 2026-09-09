# PaperWorkflow evidence package

- Workflow ID: 4f732622cea1f062
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
| retrieval | 66 | review |
| quantities | 100 | ready |
| dependencies | 100 | ready |

### Audit warnings

- [extraction/low] core_sections_missing: Several common paper sections were not identified: abstract, methods, results, conclusion.
- [structure/medium] mixed_scientific_streams_in_chunks: Chunks combine body, figure-caption and/or image streams: E002, E003.
- [retrieval/medium] evidence_coverage_incomplete: Precision or facet coverage is incomplete for: limitations.

## Semantic outline

| Chunk | Raw heading | Semantic owner | Kind | Lines | Figure parent(s) |
|---|---|---|---|---:|---|
| E001 | Failure Mechanisms of Graphene under Tension | Failure Mechanisms of Graphene under Tension | semantic | 1-16 |  |
| E002 | Failure Mechanisms of Graphene under Tension | Failure Mechanisms of Graphene under Tension | semantic | 18-28 |  |
| E003 | Failure Mechanisms of Graphene under Tension | Failure Mechanisms of Graphene under Tension | semantic | 30-48 |  |
| E004 | Failure Mechanisms of Graphene under Tension | Failure Mechanisms of Graphene under Tension | semantic | 50-102 |  |

## Query-to-evidence map

### Research objective (objective)

- Intent: objective
- Status: **acceptable**
- Evidence: EV0001, EV0002, EV0003, EV0004, EV0005

### Methods and conditions (methods)

- Intent: methods
- Status: **acceptable**
- Evidence: EV0006, EV0007, EV0008, EV0009, EV0010

### Results and conclusions (results)

- Intent: key_results
- Status: **acceptable**
- Evidence: EV0010, EV0011, EV0012, EV0013, EV0014, EV0015, EV0016, EV0002
- Coverage: 60.0%; missing: scale_or_throughput, optical_tunability

### Limitations and uncertainty (limitations)

- Intent: limitations
- Status: **weak**
- Evidence: EV0017, EV0018, EV0019, EV0020, EV0021
- Coverage: 0.0%; missing: illumination_geometry, observation_geometry, background_or_substrate, evidence_dependency

## Evidence Registry

Evidence text appears only here; queries above reference these stable IDs.

### EV0001 · S0020 · E001

- Source lines: 14-14
- Source chars: 1997-2107
- Modality / support: body_text / direct_observation
- Used by: objective
- Text: This experiment reinvigorates the fundamental question of how and why a material fails under ideal conditions.

### EV0002 · S0032 · E001

- Source lines: 16-16
- Source chars: 4004-4166
- Modality / support: body_text / direct_observation
- Used by: objective, results
- Text: In this work, we demonstrate that a soft mode is responsible for a phase transition and the resulting mechanical failure of graphene in certain states of tension.

### EV0003 · S0008 · E001

- Source lines: 8-8
- Source chars: 347-492
- Modality / support: body_text / direct_observation
- Used by: objective
- Text: Recent experiments established pure graphene as the strongest material known to mankind, further invigorating the question of how graphene fails.

### EV0004 · S0101 · E003

- Source lines: 35-35
- Source chars: 12112-12266
- Modality / support: body_text / direct_observation
- Used by: objective
- Text: Therefore, the question arises as to when the elastic instability is the failure mode versus the $K_{1}$ -mode instability for a generic state of tension.

### EV0005 · S0117 · E003

- Source lines: 46-46
- Source chars: 13973-14186
- Modality / support: body_text / direct_observation
- Used by: objective
- Text: This analysis is not yet exhaustive due to the fact that graphene is anisotropic, and therefore shear strain would have to be included in the present coordinate system to enumerate every possible state of tension.

### EV0006 · S0018 · E001

- Source lines: 14-14
- Source chars: 1758-1871
- Modality / support: body_text / measurement
- Used by: methods
- Text: Recently, the measurement of ideal strength has been achieved in the case of graphene [2], a monolayer of carbon.

### EV0007 · S0041 · E002

- Source lines: 18-18
- Source chars: 5466-5560
- Modality / support: body_text / simulation
- Used by: methods
- Text: All DFT calculations were performed using the Vienna ab initio simulation program (VASP) [18].

### EV0008 · S0040 · E002

- Source lines: 18-18
- Source chars: 5326-5465
- Modality / support: body_text / direct_observation
- Used by: methods
- Text: We compute the phonons using the displacement method [17], where the forces are generated using DFT within the local density approximation.

### EV0009 · S0045 · E002

- Source lines: 18-18
- Source chars: 6004-6172
- Modality / support: body_text / direct_observation
- Used by: methods
- Text: Previous work has established that the displacement method is accurate for unstrained graphene [20] when using a $8 \times 8$ supercell to generate the force constants.

### EV0010 · S0140 · E004

- Source lines: 50-50
- Source chars: 17217-17415
- Modality / support: body_text / direct_observation
- Used by: methods, results
- Text: Given that LDA overpredicts the energy of the $K_{1}$ mode in the unstrained case [6,7], the exact result is likely to yield an even smaller breaking strain even farther from the experimental value.

### EV0011 · S0035 · E001

- Source lines: 16-16
- Source chars: 4630-4779
- Modality / support: body_text / direct_observation
- Used by: results
- Text: Furthermore, our results on graphene yield an optical phonon instability, as opposed to the acoustic instability observed previously in bulk systems.

### EV0012 · S0025 · E001

- Source lines: 14-14
- Source chars: 2866-2932
- Modality / support: body_text / direct_observation
- Used by: results
- Text: In this study, we use DFT to determine the mechanism of mechanical

### EV0013 · S0121 · E003

- Source lines: 46-46
- Source chars: 14642-14813
- Modality / support: body_text / direct_observation
- Used by: results
- Text: Conveniently, all of the results for the different rotations are bounded by the envelope curves created by superimposing the original result and the $15^{\circ}$ rotation.

### EV0014 · S0081 · E002

- Source lines: 28-28
- Source chars: 9686-9865
- Modality / support: body_text / direct_observation
- Used by: results
- Text: This analysis predicts the soft mode to occur at $\epsilon_{A}=0.213$ , independently confirming the results of our phonons which yield a soft mode at $\epsilon_{A}=0.205-0.212$ .

### EV0015 · S0085 · E003

- Source lines: 30-30
- Source chars: 10317-10410
- Modality / support: body_text / direct_observation
- Used by: results
- Text: Therefore, we must explore the strength and stability of this new phase of strained graphene.

### EV0016 · S0145 · E004

- Source lines: 52-52
- Source chars: 18015-18139
- Modality / support: body_text / direct_observation
- Used by: results
- Text: In conclusion, we have determined the failure mechanisms of pure graphene in a generic state of tension at zero temperature.

### EV0017 · S0143 · E004

- Source lines: 50-50
- Source chars: 17758-17834
- Modality / support: body_text / direct_observation
- Used by: limitations
- Text: This issue can be resolved by bridging theory and experiment in future work.

### EV0018 · S0113 · E003

- Source lines: 43-43
- Source chars: 13564-13633
- Modality / support: body_text / direct_observation
- Used by: limitations
- Text: A given direction of strain corresponds to an angle $\theta = 0-90$ .

### EV0019 · S0128 · E003

- Source lines: 48-48
- Source chars: 15605-15713
- Modality / support: body_text / direct_observation
- Used by: limitations
- Text: The challenge in this particular case would be the fact that the graphene would have to be strained in situ.

### EV0020 · S0024 · E001

- Source lines: 14-14
- Source chars: 2660-2865
- Modality / support: body_text / direct_observation
- Used by: limitations
- Text: Although quantitative errors are still to be expected, in the vicinity of $10\%$ for certain phonons of graphene [6,7], one can reliably explore the mechanical properties of graphene from first principles.

### EV0021 · S0054 · E002

- Source lines: 23-23
- Source chars: 6805-6921
- Modality / support: body_text / direct_observation
- Used by: limitations
- Text: In Fig. 1, we reproduce the phonons for unstrained graphene, showing excellent agreement with previous work [15,20].

## Referenced source dependencies

- No external supplementary dependency was detected.

## Claim ledger contract

Use EV#### plus S####/E###, raw line range and character offsets for every major claim and number.
Treat supplementary-dependent mechanism claims as partial until the referenced files are available.
