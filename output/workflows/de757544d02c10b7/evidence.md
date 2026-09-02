# PaperWorkflow evidence package

- Workflow ID: 7dde3945b421c1a6
- Input: /home/simcrq/0_Project/paperworkflow/INput/Li.pdf
- Markdown: /home/simcrq/0_Project/paperworkflow/temp_markdowns/de757544d02c10b7/Li.md
- Text-capture fidelity: **ready** (100/100)
- Scientific-synthesis readiness: **review** (69/100)
- Mechanism completeness: **partial**

## Readiness gates

| Gate | Status | Meaning |
|---|---|---|
| text_capture_fidelity | pass | Raw OCR/Markdown text must be usable. |
| reading_order_integrity | review | Scientific prose must not be silently reordered by layout streams. |
| support_span_exposure | pass | Every retrieved item must expose an exact sentence/span and offsets. |
| evidence_coverage | pass | Required workflow facets must be covered, not merely represented in top-k. |
| supplementary_dependencies | review | Required supplementary evidence must be locally available for a complete mechanism audit. |
| quantity_and_symbol_consistency | review | Linked quantities and symbol definitions require contextual consistency. |

## Quality dimensions

| Dimension | Score | Readiness |
|---|---:|---|
| extraction | 100 | ready |
| structure | 54 | review |
| reading_order | 54 | review |
| semantic_structure | 53 | review |
| chunk_coherence | 55 | review |
| retrieval | 97 | ready |
| quantities | 40 | review |
| dependencies | 52 | review |

### Audit warnings

- [structure/medium] layout_headings_not_semantic: 7 layout/boilerplate headings were detached from semantic ownership.
- [structure/medium] empty_heading_nodes: Heading-only nodes were retained as containers, not scientific evidence: E012, E013.
- [structure/high] sentence_interrupted_by_layout_heading: Detected 1 sentence continuation(s) split by a layout heading.
- [structure/high] body_text_interrupted_by_media_stream: Detected 1 likely body continuation(s) displaced by images/captions.
- [structure/medium] mixed_scientific_streams_in_chunks: Chunks combine body, figure-caption and/or image streams: E004, E005, E006, E032, E033.
- [quantities/medium] multiple_temperature_ranges: Multiple temperature ranges occur in different contexts; preserve each source location.
- [quantities/medium] multiple_operating_temperature_regimes: Laboratory drying, synthesis and R2R curing temperatures form distinct operating regimes; do not merge them.
- [quantities/high] potential_relational_inconsistency: Printing speed (2 mm/s) and synchronized winding speed (3 mm/s) differ at line 290; verify the intended relationship.
- [quantities/high] symbol_definition_drift: D_n is associated with both photonic lattice constant and nanoparticle size; downstream claims must preserve the source wording.
- [dependencies/high] required_supplementary_sources_unavailable: The paper relies on supplementary evidence that is referenced but not present locally: supplementary_information, supplementary_discussions, supplementary_figures, supplementary_materials.

## Semantic outline

| Chunk | Raw heading | Semantic owner | Kind | Lines | Figure parent(s) |
|---|---|---|---|---:|---|
| E001 | Printable meta-assemblies enable synergetic colouration | Printable meta-assemblies enable synergetic colouration | semantic | 1-21 |  |
| E002 | Article | Printable meta-assemblies enable synergetic colouration | boilerplate | 23-29 |  |
| E003 | Principles for scalable R2R-ANP | Principles for scalable R2R-ANP | semantic | 31-35 |  |
| E004 | Optical synergies in meta-assembly systems | Optical synergies in meta-assembly systems | semantic | 37-58 | Fig. 1 |
| E005 | Article | Optical synergies in meta-assembly systems | boilerplate | 60-111 | Fig. 2, Fig. 3 |
| E006 | Article | Optical synergies in meta-assembly systems | boilerplate | 113-124 | Fig. 4, Fig. 5 |
| E007 | Rich colour tunability of the meta-assembly | Rich colour tunability of the meta-assembly | semantic | 126-130 |  |
| E008 | Macroscopic synergetic colouration | Macroscopic synergetic colouration | semantic | 132-136 |  |
| E009 | Conclusions | Conclusions | semantic | 138-140 |  |
| E010 | Online content | Online content | semantic | 142-230 |  |
| E011 | Online content | Online content | semantic | 232-242 |  |
| E012 | Article | Online content | boilerplate | 244-244 |  |
| E013 | Methods | Methods | semantic_container | 246-246 |  |
| E014 | Materials | Materials | semantic | 248-250 |  |
| E015 | Preparing monodispersed core-shell PS nanoparticles | Preparing monodispersed core-shell PS nanoparticles | semantic | 252-258 |  |
| E016 | Fabricating hydrophobic and low-adhesion substrates | Fabricating hydrophobic and low-adhesion substrates | semantic | 260-262 |  |
| E017 | Fabricating heterogeneous wettability substrates | Fabricating heterogeneous wettability substrates | semantic | 264-266 |  |
| E018 | Fabricating black background | Fabricating black background | semantic | 268-270 |  |
| E019 | Printing DCPCs | Printing DCPCs | semantic | 272-274 |  |
| E020 | Coating PDMS polymer matrix | Coating PDMS polymer matrix | semantic | 276-278 |  |
| E021 | Curing the PDMS prepolymer | Curing the PDMS prepolymer | semantic | 280-282 |  |
| E022 | Peeling off the cured PDMS | Peeling off the cured PDMS | semantic | 284-286 |  |
| E023 | Experimental details during R2R processing | Experimental details during R2R processing | semantic | 288-290 |  |
| E024 | Microscopic optical intensity test and normalization | Microscopic optical intensity test and normalization | semantic | 292-294 |  |
| E025 | Macroscopic optical performance test | Macroscopic optical performance test | semantic | 296-298 |  |
| E026 | Mechanical performance test | Mechanical performance test | semantic | 300-302 |  |
| E027 | Stability tests | Stability tests | semantic | 304-306 |  |
| E028 | Numerical simulation of meta-assemblies | Numerical simulation of meta-assemblies | semantic | 308-310 |  |
| E029 | Characterizations | Characterizations | semantic | 312-314 |  |
| E030 | Data availability | Data availability | semantic | 316-324 |  |
| E031 | Additional information | Additional information | semantic | 326-334 |  |
| E032 | Article | Additional information | boilerplate | 336-376 | Extended Data Fig. 1, Extended Data Fig. 2 |
| E033 | Article | Additional information | boilerplate | 378-459 | Extended Data Fig. 3, Extended Data Fig. 4, Extended Data Fig. 5 |
| E034 | Article | Extended Data Fig. 6 | boilerplate | 461-461 | Extended Data Fig. 6 |

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
- Evidence: EV0011, EV0012, EV0013, EV0014, EV0015, EV0016, EV0017, EV0001
- Coverage: 100.0%; missing: (none)

### Limitations and uncertainty (limitations)

- Intent: limitations
- Status: **acceptable**
- Evidence: EV0018, EV0019, EV0020, EV0021, EV0022
- Coverage: 100.0%; missing: (none)

### Custom question 1 (custom-01)

- Intent: sample_preparation
- Status: **acceptable**
- Evidence: EV0023, EV0007, EV0024, EV0025, EV0009, EV0026, EV0027, EV0028, EV0008, EV0029, EV0030, EV0010
- Coverage: 100.0%; missing: (none)

### Custom question 2 (custom-02)

- Intent: physical_mechanism
- Status: **acceptable**
- Evidence: EV0031, EV0032, EV0033, EV0034, EV0035, EV0036, EV0037, EV0038, EV0039
- Coverage: 100.0%; missing: (none)

### Custom question 3 (custom-03)

- Intent: key_results; canonical: results
- Status: **acceptable**
- Evidence: EV0011, EV0012, EV0013, EV0014, EV0015, EV0016, EV0017, EV0001
- Coverage: 100.0%; missing: (none)

### Custom question 4 (custom-04)

- Intent: limitations; canonical: limitations
- Status: **acceptable**
- Evidence: EV0018, EV0019, EV0020, EV0021, EV0022
- Coverage: 100.0%; missing: (none)

## Evidence Registry

Evidence text appears only here; queries above reference these stable IDs.

### EV0001 · S0199 · E009

- Source lines: 140-140
- Source chars: 32945-33136
- Modality / support: body_text / direct_observation
- Used by: objective, results, custom-03
- Text: Collectively, this printable meta-assembly strategy resolves the trade-off between optical functionality and engineering performance, providing key insights for multiscale photonics research.

### EV0002 · S0017 · E001

- Source lines: 15-15
- Source chars: 2117-2254
- Modality / support: body_text / direct_observation
- Used by: objective
- Text: This work provides a versatile methodology for biologically inspired metamaterial construction by means of multiscale photonics research.

### EV0003 · S0012 · E001

- Source lines: 15-15
- Source chars: 1079-1260
- Modality / support: body_text / method_protocol
- Used by: objective
- Text: Here we present a printable meta-assembly strategy that enables the fabrication of multiscale hierarchical optical architectures through continuous roll-to-roll (R2R) manufacturing.

### EV0004 · S0028 · E001

- Source lines: 21-21
- Source chars: 4532-4728
- Modality / support: body_text / method_protocol
- Used by: objective
- Text: In this work, we present a printable meta-assembly strategy that enables the scalable fabrication of multiscale hierarchical optical architectures with distinct synergetic colouration performance.

### EV0005 · S0025 · E001

- Source lines: 19-19
- Source chars: 4013-4243
- Modality / support: body_text / author_inference
- Used by: objective
- Text: Present artificial colouration systems struggle to predict multiscale synergetic interactions or unify disparate chromogenic mechanisms $^{38-40}$ , thus failing to guide the rational design of hierarchical colouration structures.

### EV0006 · S0562 · E028

- Source lines: 310-310
- Source chars: 51185-51255
- Modality / support: body_text / simulation
- Used by: methods
- Text: More simulation details are summarized in the Supplementary Materials.

### EV0007 · S0482 · E015

- Source lines: 254-254
- Source chars: 40986-41091
- Modality / support: body_text / method_protocol
- Used by: methods, custom-01
- Text: PS nanospheres with core–shell structure were synthesized by the one-step emulsion polymerization method.

### EV0008 · S0527 · E023

- Source lines: 290-290
- Source chars: 46711-47027
- Modality / support: body_text / method_protocol
- Used by: methods, custom-01
- Text: To enable high-efficiency R2R printing, the following details should be noted, including: preheating of the set-up to ensure rapid solvent evaporation and PDMS curing; presetting the module speeds to ensure coordination among various processing sections; overall cleanliness of the set-up to prevent optical defects.

### EV0009 · S0526 · E023

- Source lines: 290-290
- Source chars: 46125-46710
- Modality / support: body_text / method_protocol
- Used by: methods, custom-01
- Text: Inkjet printing: nozzle diameter (25 $\mu$ m), inter-nozzle spacing (100 $\mu$ m), droplet volume (10 pl), printing speed (2 mm s $^{-1}$ ), jetting frequency (0.5–20.0 Hz), droplet drying temperature (70 °C); PDMS blading: blade gap (0.5 mm), blade height (1.5 mm), blading speed (2 mm s $^{-1}$ ); thermal curing: curing temperature (180 °C), curing time per unit length (5 s cm $^{-1}$ ); peeling: peeling angle (45°), peeling speed (2 mm s $^{-1}$ ), applied pressure (0.1 MPa); rolling: winding tension (5 N), winding speed (synchronized with the printing speed, 3 mm s $^{-1}$ ).

### EV0010 · S0107 · E005

- Source lines: 71-71
- Source chars: 16427-16773
- Modality / support: figure_caption / figure_caption
- Used by: methods, custom-01
- Text: Fig. 2 | Principles for scalable meta-assembly printing. a, Schematic illustrations of the fabrication details, including inkjet printing of DCPC structures (1), PDMS prepolymer blade coating (2), thermal curing (3) and the cured PDMS peeling off (4). b, Top, rim intensity variations with the change of receding contact angle ( $\theta_{Rec}$ ).

### EV0011 · S0075 · E003

- Source lines: 35-35
- Source chars: 11728-11965
- Modality / support: body_text / method_protocol
- Used by: results, custom-03
- Text: Experimentally, we fabricate a metre-scale film containing more than 40 million meta-assemblies, with the total number of nanoparticles exceeding $7 \times 10^{13}$ , which effectively validates the scalability of our strategy (Fig. 2e).

### EV0012 · S0015 · E001

- Source lines: 15-15
- Source chars: 1691-1899
- Modality / support: body_text / method_protocol
- Used by: results, custom-03
- Text: Overcoming scalability constraints, metre-scale meta-assembly prints with single-pixel customization can be rapidly fabricated from the nanoscale building blocks, spanning seven orders of magnitude in length.

### EV0013 · S0174 · E007

- Source lines: 130-130
- Source chars: 28400-28541
- Modality / support: body_text / direct_observation
- Used by: results, custom-03
- Text: Second, meta-assemblies with different $D_{n}$ and $D_{m}$ can be integrated and printed to achieve the predefined macroscopic colour mixing.

### EV0014 · S0198 · E009

- Source lines: 140-140
- Source chars: 32653-32944
- Modality / support: body_text / author_inference
- Used by: results, custom-03
- Text: Moreover, the meta-assembly prints enable a more straightforward realization of synergistic optical performance while featuring excellent stability, thus offering substantial application potential for practical colouration scenarios ranging from information security to intelligent displays.

### EV0015 · S0541 · E026

- Source lines: 302-302
- Source chars: 48729-48874
- Modality / support: body_text / measurement
- Used by: results, custom-03
- Text: Similarly, the cycles-to-failure behaviours of the meta-assembly were tested at a constant rate of $30 \, mm s^{-1}$ with cycle number of 10,000.

### EV0016 · S0162 · E007

- Source lines: 128-128
- Source chars: 26246-26349
- Modality / support: body_text / direct_observation
- Used by: results, custom-03
- Text: Subsequently, the colour tunability corresponding to structural changes is systematically demonstrated.

### EV0017 · S0681 · E034

- Source lines: 461-461
- Source chars: 63741-63910
- Modality / support: figure_caption / figure_caption
- Used by: results, custom-03
- Text: With the temperature ranging from -18 to 240 °C, the meta-assembly retains its optical performance, illustrating its wide thermal stability. d, Solvent resistance tests.

### EV0018 · S0536 · E025

- Source lines: 298-298
- Source chars: 47913-48342
- Modality / support: body_text / measurement
- Used by: limitations, custom-04
- Text: For uniform colouration, the following viewing conditions are recommended: (1) ensure collimated incident light; (2) maintain a sufficiently small distance between the observation point and the light source (typically <2 cm); (3) ensure that the observer maintains a proper distance from the sample; (4) mount the sample on a black substrate to eliminate background reflection, absorb scattered light and enhance colour contrast.

### EV0019 · S0181 · E008

- Source lines: 134-134
- Source chars: 29701-30007
- Modality / support: body_text / direct_observation
- Used by: limitations, custom-04
- Text: This illumination-controlled reflection and retroreflection afford the macroscopic meta-assembly colouration with enhanced tunability, for which the colour output can be precisely modulated by tailoring the Bragg angle ( $\theta$ , reflection mode) and the light-viewing distance (D, retroreflection mode).

### EV0020 · S0534 · E025

- Source lines: 298-298
- Source chars: 47720-47794
- Modality / support: body_text / measurement
- Used by: limitations, custom-04
- Text: Macroscopic images were taken by placing the sample on a black background.

### EV0021 · S0033 · E002

- Source lines: 25-25
- Source chars: 5213-5261
- Modality / support: body_text / direct_observation
- Used by: limitations, custom-04
- Text: 1–3; see Supplementary Discussions for details).

### EV0022 · S0020 · E001

- Source lines: 17-17
- Source chars: 2690-2877
- Modality / support: body_text / direct_observation
- Used by: limitations, custom-04
- Text: Although chemical dyes have dominated applications for millennia, the limitations of toxic chemical pollution $^{19-22}$ and colour fading $^{23,24}$ still persist as pressing challenges.

### EV0023 · S0483 · E015

- Source lines: 254-254
- Source chars: 41092-41206
- Modality / support: body_text / method_protocol
- Used by: custom-01
- Text: Briefly, styrene (38.0 g), acrylic acid (2.0 g) and methyl methacrylate (2.0 g) were dispersed in 160 ml of water.

### EV0024 · S0493 · E015

- Source lines: 258-258
- Source chars: 42370-42522
- Modality / support: body_text / method_protocol
- Used by: custom-01
- Text: The nanoparticle ink exhibits suitable printing parameters (such as viscosity: 3.84 mPa s, surface tension: 57.31 mN m $^{-1}$ , boiling point: 210 °C).

### EV0025 · S0496 · E016

- Source lines: 262-262
- Source chars: 42730-42866
- Modality / support: body_text / method_protocol
- Used by: custom-01
- Text: To increase the surface energy, the substrates were treated with air plasma (DT02S, OPS Plasma Technology Co., Ltd.) at 200 W for 200 s.

### EV0026 · S0514 · E020

- Source lines: 278-278
- Source chars: 45012-45206
- Modality / support: body_text / method_protocol
- Used by: custom-01
- Text: Prepolymer of PDMS (SYLGARD 184 silicone elastomer kit, Dow) was prepared by mixing the monomers with the curing agent (with a mass ratio of 10:1) and stirred by a mechanical stirrer for 10 min.

### EV0027 · S0520 · E021

- Source lines: 282-282
- Source chars: 45681-45808
- Modality / support: body_text / method_protocol
- Used by: custom-01
- Text: With the polymerization of PDMS, the nano-assemblies would automatically form a robust composite unit with the polymer network.

### EV0028 · S0522 · E022

- Source lines: 286-286
- Source chars: 45841-45899
- Modality / support: body_text / method_protocol
- Used by: custom-01
- Text: The cured PDMS was directly peeled off from the substrate.

### EV0029 · S0476 · E014

- Source lines: 250-250
- Source chars: 40176-40461
- Modality / support: body_text / method_protocol
- Used by: custom-01
- Text: Styrene (99.0%), acrylic acid (98.0%), methyl methacrylate (99.9%), sodium dodecyl benzene sulfonate (95.0%), ammonium bicarbonate (99.0%), ammonium peroxodisulfate (APS, 99.0%), caustic soda (NaOH, 96.0%), acetic acid (98.0%) and hexadecane (98.0%) were purchased from J&K Scientific.

### EV0030 · S0511 · E019

- Source lines: 274-274
- Source chars: 44553-44777
- Modality / support: body_text / method_protocol
- Used by: custom-01
- Text: Controlled by the digital designed pattern, the colloidal ink was printed on the hydrophobic and low-adhesion substrate with the inkjet printing technology (independent R&D and customization) to form the domed microdroplets.

### EV0031 · S0032 · E002

- Source lines: 25-25
- Source chars: 4926-5212
- Modality / support: body_text / direct_observation
- Used by: custom-02
- Text: The nanolattice first defines a wavelength-selective photonic bandgap (PBG) $^{9}$ and the curved interface with refractive index contrast subsequently endows the meta-assembly with light localization capability by means of total internal reflections (TIRs) $^{10}$ (Supplementary Figs.

### EV0032 · S0143 · E005

- Source lines: 109-109
- Source chars: 21328-21704
- Modality / support: figure_caption / figure_caption
- Used by: custom-02
- Text: When the wavelength of incident light falls within the PBG range, the field intensity at the rim region can be greatly suppressed, owing to the interplay of different-scaled optical effects. g, h, The first Brillouin zone of the hexagonal close-packed photonic crystal with a lattice constant of 215 nm (g) and the calculated band diagram (h), demonstrating the incomplete PBG

### EV0033 · S0117 · E005

- Source lines: 77-77
- Source chars: 18629-18837
- Modality / support: body_text / author_inference
- Used by: custom-02
- Text: Rim dispersion originates from the pronounced optical path difference during TIR-confined propagation when light impinges on the rim regions, thereby inducing the mutual interference of electromagnetic waves.

### EV0034 · S0084 · E004

- Source lines: 39-39
- Source chars: 13301-13495
- Modality / support: body_text / direct_observation
- Used by: custom-02
- Text: Notably, at this wavelength, the field near the central boundary deflects leftward, whereas the rim field deflects rightward, exhibiting distinct interference cancellation in the overlap region.

### EV0035 · S0080 · E004

- Source lines: 39-39
- Source chars: 12612-12788
- Modality / support: body_text / direct_observation
- Used by: custom-02
- Text: Unlike the predictable optical effects of single-scale structures, the meta-assembly enables non-trivial modulation of electromagnetic field distribution and light propagation.

### EV0036 · S0049 · E002

- Source lines: 29-29
- Source chars: 7704-7884
- Modality / support: body_text / direct_observation
- Used by: custom-02
- Text: Meanwhile, the concave optical interface confines the incident light to propagate along the curved trajectories, guiding multibounce interference and colouration at the rim region.

### EV0037 · S0123 · E005

- Source lines: 77-77
- Source chars: 19478-19639
- Modality / support: body_text / direct_observation
- Used by: custom-02
- Text: Consequently, the optical field distribution becomes stably established, with the specific wavelength components exhibiting a more uniform propagation direction.

### EV0038 · S0085 · E004

- Source lines: 39-39
- Source chars: 13496-13572
- Modality / support: body_text / author_inference
- Used by: custom-02
- Text: As a result, ray propagation is suppressed, inducing field valley (Fig. 3e),

### EV0039 · S0551 · E028

- Source lines: 310-310
- Source chars: 49964-50118
- Modality / support: body_text / simulation
- Used by: custom-02
- Text: The finite-difference time-domain simulation technique was performed to understand the near-field coupling between the incident light and meta-assemblies.

## Referenced source dependencies

- supplementary_information: **unavailable**; 3 reference(s); examples: supplementary information, Supplementary Information, Supplementary information
- supplementary_discussions: **unavailable**; 1 reference(s); examples: Supplementary Discussions
- supplementary_figures: **unavailable**; 19 reference(s); examples: Supplementary Figs. 1–3, Supplementary Fig. 4, Supplementary Fig. 5, Supplementary Figs. 6
- supplementary_materials: **unavailable**; 2 reference(s); examples: Supplementary Materials, supplementary material

## Claim ledger contract

Use EV#### plus S####/E###, raw line range and character offsets for every major claim and number.
Treat supplementary-dependent mechanism claims as partial until the referenced files are available.
