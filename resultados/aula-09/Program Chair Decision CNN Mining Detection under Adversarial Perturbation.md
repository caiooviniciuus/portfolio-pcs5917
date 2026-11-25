# Program Chair Decision: CNN Mining Detection under Adversarial Perturbation

Nov 24, 2026 · @Pietro

> **Note:** This assessment is based on the four reviews only; the manuscript itself was not available. All reviewers scored each criterion on a 0–2 scale.

## Reviewer scores

| Criterion | Arthur (human) | LLM 1 | LLM 2 | LLM 3 |
| --- | --- | --- | --- | --- |
| C1 Relevance | 2 | 2 | 2 | 2 |
| C2 Contribution / related work | 2 | 2 | 2 | 2 |
| C3 Clarity | 1 | 2 | 2 | 1 |
| C4 Scope of conclusions | 1 | 1 | 2 | 2 |
| E1 Evaluation design | 1 | 1 | 1 | 1 |
| E2 Verifiability | 2 | 2 | 1 | 2 |
| **Total (/12)** | **9** | **10** | **10** | **10** |

All four agree on relevance and contribution, and all four give evaluation design a 1, pointing to one weakness everyone saw. They split on how much the clarity problems and the scope of the conclusions should count. The human reviewer found concrete, checkable errors (typos, a truncated sentence in the abstract, fog/occlusion missing from Table 1) that most LLM reviewers missed; only LLM 3 flagged the related 0.5% vs. 0.01 mismatch. Those observations get extra weight.

## 1) Is the paper related to the conference topics? — Score: 9/10

Yes, clearly. The core is adversarial robustness of a CNN classifier (FGSM, PGD, noise and brightness perturbations), which falls under **Security and privacy in machine learning: ML and AI in security**. The paper also frames the classifier as an attack surface in an environmental enforcement pipeline — an attacker could flood analysts with false positives or hide real mines — tying into **Application security** and, through enforcement, **Auditing and risk analysis**. It loses a point only because the main object of study is the robustness of a remote-sensing model rather than a security system as such.

## 2) Is the methodology clear and coherent, and do the authors follow it? — Score: 6/10

**Strengths**

- The protocol is coherent: random noise vs. low-pass noise with the **same budget and same mean shift** (a frequency-matched control) cleanly separates high-frequency texture dependence from plain sensitivity to perturbation magnitude.
- Directional metrics separate false positives (forest → mining) from evasion (mining → forest), matching the threat model.
- Strip-based split limits spatial leakage; fixed seed, deterministic cuDNN, public dataset and notebook.
- By the reviewers' accounts, the authors follow the stated protocol.

**Weaknesses**

- Seven perturbations are claimed, but fog and occlusion appear only in the text, not in Table 1 (Arthur).
- Text gives 0.5% for low-pass noise; the table gives 0.01 (LLM 3).
- Key parameters missing from the paper: patch size, exact preprocessing, low-pass filter construction, full FGSM/PGD and fog/occlusion settings (LLM 2, LLM 3).
- Typos and a truncated sentence in the abstract.

The design is good, but these reporting gaps keep a reader from checking the paper on its own terms.

## 3) What biases does the paper have, and do they affect the conclusions? — Score: 4/10 (how well biases are controlled)

1. **Selection bias in the negative class (critical).** All 1,300 negative patches come from preserved forest, making the task nearly trivial ("intact canopy vs. anything else"). This bears directly on the findings:
   - The **clean results**, including zero false positives, are a dataset artifact, as the authors admit.
   - The **high-frequency texture dependence** may be a shortcut this dataset invites rather than a property of mining detectors in general (consistent with Arthur's overfitting concern).
   - The **asymmetry** (forest → mining is easier than the reverse) may also stem from this design. A negative class with pasture, regrowth, urban areas or sediment-laden rivers could change or even reverse it.
2. **Single architecture, single seed.** Cannot show whether the effect belongs to CNNs, to this architecture, or to this training run.
3. **Small test set per strip** (LLM 3), making per-group estimates noisy.
4. **Prescriptive overreach.** "The next step is dataset redesign, not defense" is plausible but untested (LLM 1).

The authors acknowledge the dataset limitation, but only in the discussion, after the fact. Acknowledging a bias is not controlling for it. The diagnostic claim ("this model uses a texture shortcut") survives; any wider reading does not.

## 4) Are the results statistically significant, and do they suggest generalization? — Score: 3/10

No reviewer mentions confidence intervals, variance across seeds, or significance tests. The flip rates are large (up to \~45% of forest patches for random noise vs. \~0.5% or 0.01 for low-pass noise), so the gap is probably not noise — but "probably" isn't enough for publication. Authors should report binomial or bootstrap CIs on flip rates and results over several seeds.

On generalization: no, and the authors more or less say so. One dataset (trivially separable by their own admission), one architecture, one region. The findings describe this model on this data and show that the diagnostic protocol works; they do not show that mining detectors in general are fragile in this way.

## 5) Does the paper discuss related work, and is the discussion well argued? — Score: 6/10

All four reviewers gave 2/2. The paper positions itself against Camalan et al. 2022 (CNN mining detection), Goodfellow et al. 2015 (adversarial examples), Xu & Ghamisi 2022 (adversarial attacks in remote sensing) and Geirhos et al. 2019 (texture bias). The right areas are covered and the texture-bias link is well argued.

Reasons for caution: the list looks short (the paper appears to be \~3 pages), and no reviewer mentions the **frequency-domain robustness literature** (e.g., Yin et al. 2019, *A Fourier Perspective on Model Robustness*; Wang et al. 2020 on high-frequency components). If uncited, the novelty of the frequency-matched control is overstated.

## 6) What does the paper contribute to the state of the art? — Score: 6/10

- **Method:** adversarial and frequency-controlled perturbations used as a *diagnostic* of what a model learned, not just a robustness benchmark. The matched-budget, matched-mean-shift control is simple and convincing.
- **Domain:** illegal mining detection in the Legal Amazon — high-stakes, under-studied, with outputs feeding enforcement.
- **Threat model:** separating false-positive flooding (wearing analysts down) from evasion (hiding mines) is a practical, useful framing.
- **Reproducibility:** dataset on Zenodo and a notebook reproducing numbers and figures.

Relevance is high; methodological novelty is moderate, since the frequency view of shortcut learning already exists. A solid, focused contribution, not a breakthrough.

## 7) What are the main conclusions, and are they relevant? — Score: 7/10

1. The CNN depends on high-frequency texture (a shortcut) rather than mining-related structure.
2. Fragility is asymmetric: false positives are induced far more easily than evasion — operationally, the realistic attack is exhausting analysts, not hiding a mine.
3. The dataset (mainly its negative class) is the limiting factor and should be redesigned before adversarial defenses are tried.

These matter: high clean accuracy in remote-sensing enforcement can hide brittle shortcuts, and the asymmetry has direct operational value. Conclusions 1 and 2 are well supported *within this setup*. Conclusion 3 is a reasonable recommendation stated as established fact; it should be framed as a hypothesis.

## Decision: Conditional Accept

The paper is on topic, methodologically sound, and makes a clear, reproducible diagnostic contribution in a high-impact area; reviewers rate it 9–10 out of 12. Its weaknesses concern reporting, statistical support and the breadth of claims — all fixable, none invalidating the main finding. A new dataset is not required, because the properly scoped claim does not depend on one.

**Required for acceptance**

1. Fix typos and the truncated abstract sentence; add fog and occlusion to Table 1; reconcile 0.5% vs. 0.01.
2. Report missing parameters in the paper: patch size, preprocessing, low-pass filter construction, ε, steps and step size for FGSM/PGD, fog/occlusion settings.
3. Add uncertainty estimates: CIs on flip rates and results over at least a few seeds.
4. Justify the negative-class choice in Methods, not only Discussion; state plainly that conclusions apply to this model and dataset.
5. Recast "dataset redesign before defense" as a hypothesis or recommendation.
6. Discuss frequency-domain robustness work (e.g., Yin et al. 2019) and state what the matched control adds beyond it.

**Strongly encouraged (not required):** a small set of harder negatives (pasture, regrowth, turbid rivers) or a second architecture, to test whether the texture dependence and asymmetry hold up.
