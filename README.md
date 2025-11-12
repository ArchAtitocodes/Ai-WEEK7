# AI Ethics & Responsible Development - Complete Documentation

## 📋 Table of Contents
1. [Assignment Overview](#assignment-overview)
2. [Project Structure](#project-structure)
3. [Part 1: Theoretical Understanding](#part-1-theoretical-understanding)
4. [Part 2: Case Study Analysis](#part-2-case-study-analysis)
5. [Part 3: Practical Audit](#part-3-practical-audit)
6. [Part 4: Ethical Reflection](#part-4-ethical-reflection)
7. [Bonus Task: Policy Proposal](#bonus-task-policy-proposal)
8. [Installation Guide](#installation-guide)
9. [Running the Code](#running-the-code)
10. [Results and Findings](#results-and-findings)
11. [Key Takeaways](#key-takeaways)
12. [Resources and References](#resources-and-references)
13. [Submission Checklist](#submission-checklist)
14. [Contributing and Feedback](#contributing-and-feedback)

---

## 🎯 Assignment Overview

### Purpose
This assignment explores the critical intersection of artificial intelligence, ethics, and responsible development. It addresses fundamental questions about fairness, accountability, transparency, and the societal impact of AI systems.

### Learning Objectives
By completing this assignment, you will:
- Understand core concepts in AI ethics including algorithmic bias, fairness metrics, and transparency
- Analyze real-world cases of biased AI systems and their societal impacts
- Gain hands-on experience auditing datasets for bias using industry-standard tools
- Develop practical skills in implementing fairness-aware machine learning
- Reflect critically on ethical considerations in AI development
- Create actionable policy recommendations for responsible AI deployment

### Total Points: 110% (including 10% bonus)
- Part 1: Theoretical Understanding - 30%
- Part 2: Case Study Analysis - 40%
- Part 3: Practical Audit - 25%
- Part 4: Ethical Reflection - 5%
- Bonus Task: Policy Proposal - 10%

---

## 📁 Project Structure

```
ai-ethics-assignment/
│
├── README.md                          # Project overview
├── DOCUMENTATION.md                   # This file - comprehensive documentation
│
├── part1_theoretical/
│   ├── short_answers.md              # Q1-Q3 responses
│   └── ethical_principles.md          # Principles matching exercise
│
├── part2_case_studies/
│   ├── case1_amazon_hiring.md        # Biased hiring tool analysis
│   └── case2_facial_recognition.md    # Facial recognition analysis
│
├── part3_practical_audit/
│   ├── compas_bias_audit.py          # Main Python analysis script
│   ├── requirements.txt               # Python dependencies
│   ├── audit_report.md                # 300-word findings report
│   ├── data/
│   │   └── compas-scores-two-years.csv  # COMPAS dataset
│   └── output/
│       ├── compas_exploratory_analysis.png
│       ├── compas_error_rates.png
│       └── compas_bias_mitigation.png
│
├── part4_reflection/
│   └── ethical_reflection.md          # Personal project reflection
│
├── bonus_task/
│   └── healthcare_ai_policy.md        # Policy guidelines document
│
└── resources/
    ├── references.md                   # Citations and sources
    └── additional_readings.md          # Supplementary materials
```

---

## 📚 Part 1: Theoretical Understanding (30%)

### Section Overview
This section establishes foundational knowledge in AI ethics through short-answer questions and principle matching exercises.

### Q1: Algorithmic Bias - Definition and Examples

**Definition:**
Algorithmic bias refers to systematic and repeatable errors in computer systems that create unfair outcomes, often disadvantaging certain demographic groups based on characteristics like race, gender, age, or socioeconomic status. These biases typically originate from:
- **Biased training data** reflecting historical discrimination
- **Flawed model design** that amplifies existing disparities
- **Prejudiced implementation** in deployment contexts

**Example 1: COMPAS Criminal Risk Assessment**
- **Context**: Used in US courts to predict recidivism risk
- **Bias**: Higher false positive rates for Black defendants (45% vs 23% for white defendants)
- **Impact**: Black defendants incorrectly labeled as high-risk, leading to harsher sentences and denied bail/parole
- **Source**: Training data reflected historical over-policing of Black communities
- **Reference**: ProPublica investigation (2016)

**Example 2: Healthcare Resource Allocation Algorithm**
- **Context**: Used by US hospitals to identify patients needing extra care
- **Bias**: Systematically underestimated needs of Black patients
- **Impact**: Black patients received less care despite being sicker
- **Source**: Algorithm used healthcare spending as proxy for health needs; historical access disparities meant Black patients had lower spending despite greater needs
- **Reference**: Obermeyer et al., Science (2019)

**Additional Context:**
Other manifestations include:
- Google Photos mislabeling Black people as "gorillas" (2015)
- Apple Card offering lower credit limits to women (2019)
- LinkedIn showing tech ads more to men than women
- Hiring algorithms screening out candidates based on name ethnicity

### Q2: Transparency vs. Explainability

#### Transparency
**Definition**: Openness about an AI system's existence, purpose, development process, and data sources.

**Key Questions Addressed:**
- What is this AI system designed to do?
- Who developed it and under what funding/incentives?
- What data was used for training?
- How is it being deployed and in what contexts?
- What oversight mechanisms exist?

**Examples:**
- Publishing model cards describing system capabilities and limitations
- Disclosing training data sources and collection methods
- Making source code available (open source)
- Documenting known failure modes and edge cases

#### Explainability (Interpretability)
**Definition**: The ability to understand and articulate how an AI system makes specific individual decisions.

**Key Questions Addressed:**
- Why did the model make this particular prediction?
- Which features most influenced this outcome?
- How would the output change if inputs were different?
- Can this decision be understood by affected stakeholders?

**Examples:**
- SHAP (SHapley Additive exPlanations) values showing feature importance
- Decision tree visualizations
- Attention maps in neural networks
- Counterfactual explanations ("If your income were $50K instead of $45K, you'd be approved")

#### Why Both Are Important

**Transparency Enables:**
1. **Trust Building**: Stakeholders can verify system alignment with stated goals
2. **Accountability**: Clear ownership and responsibility chains
3. **Oversight**: Regulators and auditors can assess compliance
4. **Bias Detection**: Examining data sources reveals potential discriminatory patterns
5. **Informed Consent**: Users understand when/how they're subject to automated decisions

**Explainability Enables:**
1. **Debugging**: Developers identify and fix erroneous logic
2. **Validation**: Domain experts verify decision-making aligns with established knowledge
3. **Legal Compliance**: Satisfies "right to explanation" requirements (GDPR Article 22)
4. **Contestability**: Individuals can challenge unfair outcomes with evidence
5. **Learning**: Clinicians/judges gain insights from AI recommendations
6. **Safety**: Identifies when models rely on spurious correlations

**Practical Example:**
In medical diagnosis:
- **Transparency**: Hospital discloses using IBM Watson for oncology, trained on Memorial Sloan Kettering data
- **Explainability**: For specific patient, system shows "Recommendation: Chemotherapy regimen X because tumor marker A elevated, genetic variant B present, similar cases had 78% response rate"

**Trade-offs:**
- Complex models (deep learning) offer better performance but less explainability
- Full transparency may expose proprietary information
- Balancing these requires thoughtful design choices prioritizing stakeholder needs

### Q3: GDPR's Impact on AI Development in the EU

The General Data Protection Regulation (2018) fundamentally reshaped AI development through strict data protection requirements.

#### Key Provisions Affecting AI

**1. Right to Explanation (Article 22)**
- **Requirement**: Individuals have the right not to be subject to decisions based solely on automated processing that significantly affects them
- **AI Impact**: Systems making consequential decisions (credit, employment, healthcare) must provide meaningful explanations
- **Challenge**: Deep learning "black boxes" struggle to meet this standard
- **Response**: Increased research into explainable AI (XAI) methods

**2. Lawful Basis for Processing (Article 6)**
- **Requirement**: Data processing needs explicit legal justification
- **AI Impact**: Training models on personal data requires:
  - Informed consent (most common)
  - Contractual necessity
  - Legal obligation
  - Legitimate interests (balanced against privacy rights)
- **Challenge**: Broad data collection "just in case" no longer permissible
- **Response**: More targeted data collection strategies

**3. Data Minimization (Article 5)**
- **Requirement**: Collect only data adequate, relevant, and limited to necessary purposes
- **AI Impact**: Contradicts ML best practice of "more data = better models"
- **Challenge**: Must justify every data field collected
- **Response**: Feature selection becomes an ethical and legal requirement

**4. Purpose Limitation (Article 5)**
- **Requirement**: Data collected for specific purposes cannot be repurposed without new consent
- **AI Impact**: Cannot train model for one purpose then deploy for another
- **Example**: Data collected for fraud detection cannot be reused for marketing
- **Response**: Strict purpose definitions in data collection

**5. Privacy by Design and Default (Article 25)**
- **Requirement**: Data protection must be built into systems from inception
- **AI Impact**: Must consider privacy at design phase, not post-hoc
- **Implementation**:
  - Differential privacy techniques
  - Federated learning (models train on distributed data)
  - Secure multi-party computation
  - Data anonymization and pseudonymization

**6. Right to be Forgotten (Article 17)**
- **Requirement**: Individuals can request data deletion
- **AI Impact**: Models trained on personal data must handle deletion requests
- **Challenge**: Removing individual data points from trained models is technically difficult
- **Response**: 
  - Model retraining (expensive)
  - Machine unlearning research
  - Careful documentation of training data

**7. Data Protection Impact Assessments (Article 35)**
- **Requirement**: High-risk processing requires formal impact assessments
- **AI Impact**: Most AI systems qualify as high-risk
- **Requirements**:
  - Systematic description of processing
  - Necessity and proportionality assessment
  - Risk evaluation to individuals
  - Mitigation measures
- **Response**: Standardized DPIA templates for AI projects

**8. Consent Requirements (Article 7)**
- **Requirement**: Consent must be freely given, specific, informed, and unambiguous
- **AI Impact**: Complex to obtain for AI systems where uses may evolve
- **Challenge**: "Informed" consent difficult when even developers don't fully understand model behavior
- **Response**: Multi-layered consent approaches, ongoing notification

**9. Data Portability (Article 20)**
- **Requirement**: Individuals can obtain and reuse their data across services
- **AI Impact**: Must structure data in machine-readable formats
- **Opportunity**: Enables personal AI assistants trained on user's own data

**10. Cross-Border Data Transfers (Chapter V)**
- **Requirement**: Strict rules for transferring EU data outside EU
- **AI Impact**: Cloud-based AI training often involves international data flows
- **Mechanism**: Standard Contractual Clauses, adequacy decisions
- **Example**: EU-US Data Privacy Framework (2023)

#### Practical Implications for Developers

**Challenges:**
- Increased compliance costs (legal review, DPIAs, technical privacy measures)
- Slower development cycles due to approval processes
- Limited access to large-scale datasets
- Technical complexity of privacy-preserving ML
- Uncertainty around enforcement and interpretation

**Opportunities:**
- Competitive advantage for privacy-respecting products
- Innovation in privacy-preserving technologies
- Increased user trust
- Global standard-setting (GDPR influences worldwide)

**Enforcement:**
- Fines up to €20 million or 4% of global annual revenue (whichever is higher)
- Notable cases:
  - Google: €50 million (2019) for lack of transparency
  - Amazon: €746 million (2021) for targeted advertising practices

### Ethical Principles Matching

#### Correct Matches:

**A) Justice → 4) Fair distribution of AI benefits and risks**
- **Explanation**: Justice (fairness) in AI ethics means equitable allocation of opportunities and burdens created by AI systems
- **Application**: Ensuring AI-driven healthcare reaches underserved communities, not just wealthy populations
- **Metrics**: Demographic parity, equal opportunity, absence of disparate impact
- **Challenges**: Tension between different fairness definitions; trade-offs between group fairness and individual fairness

**B) Non-maleficence → 1) Ensuring AI does not harm individuals or society**
- **Explanation**: "First, do no harm" - AI systems must avoid causing injury, suffering, or damage
- **Application**: Rigorous testing before deployment, fail-safes, human oversight for high-stakes decisions
- **Types of Harm**: Physical (autonomous vehicles), psychological (social media addiction), economic (job displacement), social (discrimination)
- **Proactive Measures**: Red-teaming, adversarial testing, safety constraints

**C) Autonomy → 2) Respecting users' right to control their data and decisions**
- **Explanation**: Individuals should have agency over their information and ability to make informed choices
- **Application**: Meaningful consent, opt-out options, transparency about data use, human override of automated decisions
- **GDPR Connection**: Rights to access, rectification, erasure, portability
- **Anti-patterns**: Dark patterns, manipulative design, coerced consent

**D) Sustainability → 3) Designing AI to be environmentally friendly**
- **Explanation**: AI development and deployment should minimize environmental impact
- **Concerns**: 
  - Energy consumption (training GPT-3: ~1,287 MWh, equivalent to 552 tons CO₂)
  - E-waste from specialized hardware
  - Water usage for data center cooling
- **Solutions**: 
  - Efficient architectures (model compression, pruning)
  - Renewable energy for compute
  - Carbon-aware training (scheduling for low-carbon hours)
  - Longer model lifespans, fewer retraining cycles

#### Additional Ethical Principles

**E) Beneficence**: Actively promoting human welfare and flourishing
- Beyond avoiding harm, AI should create positive value
- Example: AI for early disease detection, climate modeling

**F) Explicability**: Systems should be understandable to stakeholders
- Combines transparency and explainability
- Critical for building trust and enabling meaningful oversight

**G) Accountability**: Clear responsibility for AI system outcomes
- Human-in-the-loop requirements
- Audit trails, version control
- Legal liability frameworks

---

## 🔍 Part 2: Case Study Analysis (40%)

### Case 1: Amazon's Biased Hiring Tool

#### Background
In 2018, Reuters revealed that Amazon had been developing an AI recruiting tool to automate resume screening. The system was trained on 10 years of resumes submitted to Amazon (predominantly from male applicants in tech roles). The tool learned to penalize resumes indicating female candidates.

#### Timeline
- **2014**: Development begins
- **2015**: Bias discovered during testing
- **2015-2017**: Attempted corrections
- **2018**: Project abandoned after failing to ensure fairness
- **2018**: Public disclosure

#### 1. Source of Bias Analysis

**Primary Source: Biased Training Data**

**Historical Gender Imbalance:**
- Tech industry historically male-dominated (especially 2004-2014)
- Amazon's engineering roles were ~75% male during training period
- Resume corpus reflected this: significantly more male applicants, particularly for senior positions
- Model learned correlation: "successful candidate" → "male-associated patterns"

**Specific Learned Biases:**
- Penalized resumes containing "women's" (e.g., "women's chess club captain")
- Downgraded graduates from all-women's colleges (Smith College, Wellesley)
- Learned subtle language differences:
  - Men more likely to use assertive language ("led," "executed," "delivered")
  - Women more likely to use collaborative language ("supported," "assisted," "coordinated")
  - Model favored assertive phrasing
- Name-based proxies: Names statistically associated with gender influenced scoring

**Data Quality Issues:**
- Historical data reflected discriminatory hiring practices
- No ground truth validation (were past hires actually better performers?)
- Survivorship bias (only hired candidates in dataset, not potentially excellent rejected candidates)

**Secondary Source: Model Design Flaws**

**Lack of Fairness Constraints:**
- Model optimized purely for accuracy on historical hiring outcomes
- No demographic parity objectives in loss function
- No adversarial debiasing components
- No protected attribute blindness enforced

**Feature Engineering Mistakes:**
- Included proxy features (college names, extracurricular activities)
- Free-text analysis without gender-neutral preprocessing
- No human review of learned feature importance

**Inappropriate Optimization Target:**
- "Replicating past hiring decisions" inherently reproduces discrimination
- Should have optimized for "predicting job performance" with diverse evaluation data

**Tertiary Source: Deployment Context**

**Insufficient Testing:**
- No disaggregated performance evaluation by gender
- No fairness metrics calculated pre-deployment
- Inadequate red-teaming for bias

**Lack of Oversight:**
- Purely automated screening without human review
- No diversity requirements in hiring targets

#### 2. Three Fixes to Make the Tool Fairer

**Fix 1: Comprehensive Data Remediation**

**Strategy A: Balanced Sampling**
- **Action**: Resample training data to achieve 50/50 gender balance within job categories
- **Technique**: Stratified sampling ensuring equal representation across:
  - Gender
  - Seniority levels
  - Technical domains
  - Educational backgrounds
- **Implementation**:
  ```python
  from imblearn.over_sampling import SMOTE
  from sklearn.utils import resample
  
  # Separate by gender
  female_resumes = df[df['gender'] == 'F']
  male_resumes = df[df['gender'] == 'M']
  
  # Upsample minority class
  female_upsampled = resample(female_resumes, 
                              n_samples=len(male_resumes),
                              random_state=42)
  
  balanced_data = pd.concat([male_resumes, female_upsampled])
  ```

**Strategy B: Counterfactual Data Augmentation**
- **Action**: Generate synthetic resumes by gender-flipping existing ones
- **Example**: "Captain of men's soccer team" → "Captain of women's soccer team"
- **Tools**: Name anonymization, pronoun swapping, gendered term replacement
- **Result**: Model sees equivalent qualifications regardless of gender markers

**Strategy C: Remove Gendered Features**
- **Action**: Strip all gender-identifiable information during preprocessing:
  - Names → Anonymous IDs
  - Pronouns → Neutral alternatives
  - Gendered organizations → Categories ("Leadership in sports")
  - College names → Institution type (if women's college)
- **Trade-off**: May reduce some genuine signal, but essential for fairness

**Strategy D: Include Success Metrics**
- **Action**: Instead of training on "who was hired," train on "who succeeded post-hire"
- **Data**: Performance reviews, promotion rates, retention, project outcomes
- **Benefit**: Breaks from potentially discriminatory historical hiring patterns
- **Challenge**: Requires longitudinal data collection

**Fix 2: Fairness-Aware Model Design**

**Strategy A: Adversarial Debiasing**
- **Approach**: Train two models simultaneously:
  1. **Predictor**: Predicts hiring suitability
  2. **Adversary**: Tries to predict gender from resume embeddings
- **Objective**: Predictor learns representations that prevent adversary from identifying gender
- **Implementation**:
  ```python
  from aif360.algorithms.inprocessing import AdversarialDebiasing
  
  debiased_model = AdversarialDebiasing(
      unprivileged_groups=[{'gender': 0}],
      privileged_groups=[{'gender': 1}],
      scope_name='debiased_classifier',
      debias=True
  )
  ```
- **Result**: Model cannot use gender as decision factor, even indirectly

**Strategy B: Fairness Constraints in Optimization**
- **Approach**: Add demographic parity constraint to loss function
- **Mathematical Formulation**:
  ```
  Minimize: Prediction_Error + λ * Fairness_Penalty
  
  Where Fairness_Penalty = |P(Ŷ=1|Male) - P(Ŷ=1|Female)|
  ```
- **λ Parameter**: Controls accuracy-fairness trade-off (tune based on organizational values)
- **Constraints**: Can enforce:
  - Equal selection rates (demographic parity)
  - Equal true positive rates (equal opportunity)
  - Equal positive predictive values (predictive parity)

**Strategy C: Post-Processing Threshold Adjustment**
- **Approach**: Set different decision thresholds for each group to equalize outcomes
- **Example**: 
  - Male applicants: Hire if score ≥ 0.7
  - Female applicants: Hire if score ≥ 0.6
- **Justification**: Compensates for historical bias in training data
- **Legal Note**: May face legal challenges; requires careful justification

**Strategy D: Use Interpretable Models**
- **Approach**: Switch from black-box neural networks to interpretable models
- **Options**:
  - Logistic regression with L1 regularization
  - Decision trees with depth limits
  - Rule-based systems with human-reviewable logic
- **Benefit**: Can manually audit feature weights for gender bias
- **Trade-off**: May sacrifice some predictive accuracy

**Fix 3: Human-in-the-Loop + Structural Changes**

**Strategy A: AI as Screening Aid, Not Decision-Maker**
- **Workflow**:
  1. AI ranks applicants
  2. Human recruiters review top N% (e.g., top 20%)
  3. Diverse hiring panel makes final decisions
- **Safety Net**: Human judgment catches AI errors
- **Training**: Recruiters receive implicit bias training to avoid rubber-stamping AI

**Strategy B: Blind Review Process**
- **Implementation**:
  1. Remove names, pronouns, gendered affiliations from resumes
  2. AI and humans evaluate blind resumes
  3. Reveal identity only after initial screening
- **Extension**: Blind phone screens, work sample tests
- **Evidence**: Orchestra auditions behind screens increased female hires 25-46%

**Strategy C: Diverse Evaluation Panels**
- **Composition**: Panels include diverse gender, racial, age, background representation
- **Process**: Multiple independent reviews, then consensus discussion
- **Research**: Diverse panels make 30% fewer biased decisions (McKinsey, 2020)

**Strategy D: Structured Interviewing**
- **Approach**: Standardized questions, scoring rubrics
- **AI Role**: Suggests questions based on resume, but doesn't score candidates
- **Human Role**: Evaluates responses against objective criteria

**Strategy E: Pipeline Development**
- **Recognition**: Model can only select from applicant pool
- **Actions**:
  - Partner with women-in-tech organizations (Girls Who Code, Women Who Code)
  - Targeted recruitment at women's colleges
  - Blind referral programs
  - Apprenticeship programs for non-traditional backgrounds
- **Long-term**: Changes applicant demographics, improving data quality

**Strategy F: Continuous Monitoring and Auditing**
- **Metrics**: Track disaggregated hiring outcomes:
  - Application rates by gender
  - Screen-pass rates by gender
  - Interview rates by gender
  - Offer rates by gender
  - Acceptance rates by gender
- **Frequency**: Monthly review of metrics
- **Trigger**: If any stage shows >10% disparity, investigate and adjust
- **Accountability**: Tie recruiting team incentives to diversity metrics

#### 3. Fairness Evaluation Metrics

**Category A: Group Fairness Metrics**

**Metric 1: Demographic Parity (Statistical Parity)**
- **Definition**: P(Ŷ=1 | Male) = P(Ŷ=1 | Female)
- **Interpretation**: Both groups should be selected at equal rates
- **Calculation**:
  ```python
  male_selection_rate = (predictions[gender=='M'] == 1).mean()
  female_selection_rate = (predictions[gender=='F'] == 1).mean()
  demographic_parity = male_selection_rate - female_selection_rate
  # Target: ≈ 0
  ```
- **Threshold**: Difference should be < 0.05 (5 percentage points)
- **Pro**: Simple, prevents obvious discrimination
- **Con**: Ignores whether groups have equal qualifications

**Metric 2: Adverse Impact Ratio (Four-Fifths Rule)**
- **Definition**: Selection rate of protected group / Selection rate of privileged group
- **Legal Standard**: Must be ≥ 0.8 (EEOC Uniform Guidelines)
- **Calculation**:
  ```python
  adverse_impact = female_selection_rate / male_selection_rate
  # Target: ≥ 0.8
  ```
- **Interpretation**: 
  - 1.0 = perfect parity
  - < 0.8 = potential discrimination
  - Example: If 20% of men hired but only 10% of women, ratio = 0.5 (violates)

**Metric 3: Disparate Impact**
- **Definition**: Similar to adverse impact, measures ratio of positive outcomes
- **AIF360 Implementation**:
  ```python
  from aif360.metrics import BinaryLabelDatasetMetric
  
  metric = BinaryLabelDatasetMetric(dataset,
                                    unprivileged_groups=[{'gender': 0}],
                                    privileged_groups=[{'gender': 1}])
  disparate_impact = metric.disparate_impact()
  # Target: close to 1.0
  ```

**Category B: Equal Opportunity Metrics**

**Metric 4: True Positive Rate Parity (Equal Opportunity)**
- **Definition**: P(Ŷ=1 | Y=1, Male) = P(Ŷ=1 | Y=1, Female)
- **Interpretation**: Among qualified candidates, equal percentage should be recommended
- **Calculation**:
  ```python
  # True Positive Rate = Sensitivity = Recall
  male_tpr = (predictions[gender=='M'] == 1 & actual==1).sum() / (actual[gender=='M']==1).sum()
  female_tpr = (predictions[gender=='F'] == 1 & actual==1).sum() / (actual[gender=='F']==1).sum()
  tpr_difference = abs(male_tpr - female_tpr)
  # Target: < 0.05
  ```
- **Importance**: Prevents qualified women from being overlooked
- **Use Case**: When missing qualified candidates is primary concern

**Metric 5: False Positive Rate Parity**
- **Definition**: P(Ŷ=1 | Y=0, Male) = P(Ŷ=1 | Y=0, Female)
- **Interpretation**: Among unqualified candidates, equal percentage incorrectly recommended
- **Calculation**:
  ```python
  male_fpr = (predictions[gender=='M']==1 & actual==0).sum() / (actual[gender=='M']==0).sum()
  female_fpr = (predictions[gender=='F']==1 & actual==0).sum() / (actual[gender=='F']==0).sum()
  fpr_difference = abs(male_fpr - female_fpr)
  # Target: < 0.05
  ```

**Metric 6: False Negative Rate Parity**
- **Definition**: P(Ŷ=0 | Y=1, Male) = P(Ŷ=0 | Y=1, Female)
- **Interpretation**: Among qualified candidates, equal percentage incorrectly rejected
- **Importance**: Directly measures missed opportunities for each group

**Metric 7: Equalized Odds**
- **Definition**: Combines TPR and FPR parity
- **Requirement**: Both TPR and FPR must be equal across groups
- **Strictest**: Hardest fairness criterion to satisfy
- **Trade-off**: May require significant accuracy sacrifice

**Category C: Predictive Parity Metrics**

**Metric 8: Positive Predictive Value (PPV) Parity**
- **Definition**: P(Y=1 | Ŷ=1, Male) = P(Y=1 | Ŷ=1, Female)
- **Interpretation**: Of those recommended, equal percentage should actually succeed
- **Calculation**:
  ```python
  male_ppv = (predictions[gender=='M']==1 & actual==1).sum() / (predictions[gender=='M']==1).sum()
  female_ppv = (predictions[gender=='F']==1 & actual==1).sum() / (predictions[gender=='F']==1).sum()
  # Target: Difference < 0.05
  ```
- **Interpretation**: Ensures recommendations are equally reliable across groups
- **Business Value**: Equal "quality" of hire from each group

**Metric 9: Calibration**
- **Definition**: P(Y=1 | Ŷ=p, Male) = P(Y=1 | Ŷ=p, Female) for all probabilities p
- **Interpretation**: Confidence scores mean the same thing for both groups
- **Example**: If model says "70% likely to succeed," this should be accurate for both men and women
- **Visualization**: Calibration curves should overlap for all groups

**Category D: Individual Fairness Metrics**

**Metric 10: Consistency**
- **Definition**: Similar individuals should receive similar predictions
- **Measurement**: For each person, find k nearest neighbors; measure prediction variance
- **AIF360**:
  ```python
  consistency = metric.consistency(k=5)
  # Higher = more consistent (fair)
  ```

**Metric 11: Counterfactual Fairness**
- **Test**: Would prediction change if gender were flipped but all qualifications stayed the same?
- **Implementation**: Generate counterfactual resumes and measure prediction change
- **Target**: Predictions should be invariant to protected attribute changes

**Category E: Intersectional Metrics**

**Metric 12: Subgroup Fairness**
- **Approach**: Evaluate all metrics for intersecting identities
- **Examples**:
  - Black women vs. White women vs. Black men vs. White men
  - Young women vs. Older women
  - Women with disabilities vs. Women without
- **Importance**: Single-axis fairness can hide intersectional discrimination
- **Tool**: 
  ```python
  for race in ['White', 'Black', 'Asian', 'Hispanic']:
      for gender in ['M', 'F']:
          subgroup_metrics = calculate_metrics(df[(df.race==race) & (df.gender==gender)])
  ```

**Category F: Operational Metrics**

**Metric 13: Hiring Funnel Analysis**
- **Track**: Conversion rates at each stage
  - Application → Resume screen
  - Resume screen → Phone interview
  - Phone interview → On-site interview
  - On-site → Offer
  - Offer → Acceptance
- **Compare**: Rates by gender at each stage
- **Identify**: Where in pipeline bias occurs

**Metric 14: Time-to-Hire Parity**
- **Measure**: Average time from application to offer by gender
- **Interpretation**: Delays may indicate extra scrutiny or bias
- **Target**: Difference < 1 week

**Metric 15: Retention and Performance Equity**
- **Long-term Validation**: Do hired candidates perform equally well?
- **Metrics**:
  - 1-year retention rates by gender
  - Performance review scores by gender
  - Promotion rates by gender
- **Purpose**: Validates that "quality of hire" is equivalent

**Category G: Composite Fairness Scores**

**Metric 16: Fairness 360 Comprehensive Score**
- **Approach**: Combine multiple metrics into single score
- **Weighting**: Based on organizational priorities
- **Example**:
  ```python
  fairness_score = (
      0.3 * (1 - abs(demographic_parity)) +
      0.3 * min(adverse_impact_ratio, 1.0) +
      0.2 * (1 - abs(tpr_difference)) +
      0.2 * (1 - abs(fpr_difference))
  )
  # Target: > 0.9
  ```

#### Evaluation Process

**Phase 1: Pre-Deployment Testing**
1. Calculate all metrics on held-out test set
2. Disaggregate by gender (and intersectional identities)
3. Generate fairness report card
4. Independent third-party audit
5. Legal review for compliance
6. Ethics committee approval

**Phase 2: A/B Testing**
1. Deploy to subset of applications (20%)
2. Compare outcomes: AI-assisted vs. traditional hiring
3. Monitor metrics in real-time
4. Halt if fairness violations detected

**Phase 3: Ongoing Monitoring**
1. Monthly fairness dashboards
2. Quarterly comprehensive audits
3. Annual external review
4. Continuous improvement based on findings

**Impossibility Theorems:**
Note: Perfect fairness across all metrics simultaneously is mathematically impossible (except in trivial cases). Organizations must prioritize based on values and context. For hiring:
- **Priority 1**: Equal Opportunity (TPR parity) - don't miss qualified candidates
- **Priority 2**: Demographic Parity - overall representation
- **Priority 3**: Predictive Parity - equal quality of hire

---

### Case 2: Facial Recognition in Policing

#### Background
Facial recognition technology (FRT) has been rapidly adopted by law enforcement agencies worldwide for identifying suspects, finding missing persons, and monitoring public spaces. However, research consistently shows these systems exhibit significantly higher error rates for people of color, women, and elderly individuals.

#### Key Research Findings

**NIST Study (2019):**
- Tested 189 algorithms from 99 developers
- False positive rates up to 100x higher for Asian and Black faces vs. white faces
- Highest errors: Black females (FPR up to 35%)
- Lowest errors: White males (FPR ~1%)

**MIT Media Lab Study (2018):**
- Commercial systems (IBM, Microsoft, Face++)
- Error rates for dark-skinned females: 20-35%
- Error rates for light-skinned males: <1%

**Real-World Incidents:**
- **Robert Williams (2020)**: First known wrongful arrest due to FRT in Detroit (Black man)
- **Michael Oliver (2019)**: Wrongfully arrested in New Jersey
- **Nijeer Parks (2019)**: Spent 10 days in jail due to FRT misidentification

#### 1. Ethical Risks Discussion

**Risk Category 1: Wrongful Arrests and Criminal Justice Harm**

**Immediate Impacts:**
- **False Accusations**: Innocent individuals arrested, detained, interrogated
- **Psychological Trauma**: Fear, anxiety, PTSD from wrongful arrest
- **Economic Harm**: Legal fees ($10,000-$50,000+), lost wages, job termination
- **Criminal Records**: Arrests appear in background checks even if charges dropped
- **Social Stigma**: Damage to reputation in community

**Systemic Amplification:**
- **Coerced Confessions**: Innocent people may falsely confess under interrogation pressure
  - Research: 25% of exonerations involved false confessions
  - Particularly vulnerable: Youth, individuals with disabilities, non-English speakers
- **Plea Bargains**: Facing trial costs, innocents may plead guilty to lesser charges
  - 95% of criminal cases resolve via plea bargains
  - FRT "evidence" pressures defendants even when unreliable
- **Cascading Consequences**: Arrest → difficulty finding employment, housing, education → poverty → increased system contact

**Disparate Harm:**
- Black and Latino individuals experience wrongful arrests at higher rates due to higher false positive rates
- Creates feedback loop: More false arrests → more data associating minorities with crime → model bias reinforcement
- Erodes presumption of innocence for communities of color

**Life-Altering Consequences:**
- **Robert Williams Case**: Arrested in front of wife and daughters, held overnight, charges eventually dropped but trauma persists
- **Families Affected**: Children witnessing parent's arrest, financial strain, relationship stress
- **Community Impact**: Collective trauma, reduced trust in institutions

**Risk Category 2: Privacy Violations and Surveillance**

**Mass Surveillance Infrastructure:**
- **Ubiquitous Capture**: Faces captured without consent in public spaces
  - Streets, parks, transit, stores, events
  - No reasonable way to avoid being surveilled
- **Persistent Tracking**: Create comprehensive movement histories
  - Where you go, when, with whom
  - Patterns reveal sensitive information (religious attendance, medical visits, romantic relationships, political activities)
- **Retroactive Investigation**: Search historical footage to track anyone
  - "Where was this person on November 15 at 3pm?"
  - No warrant needed for past public movements in many jurisdictions

**Chilling Effects on Fundamental Rights:**
- **Freedom of Assembly**: Protesters fear identification and retaliation
  - Hong Kong protests: Demonstrators wore masks, destroyed cameras
  - Research: Surveillance reduces protest attendance by 30-50%
  - Particularly impactful for vulnerable groups (undocumented immigrants, whistleblowers)
- **Freedom of Association**: Reluctance to attend controversial meetings, support causes
- **Freedom of Speech**: Self-censorship in public spaces
- **Anonymous Tips**: Witnesses fear coming forward if identifiable

**Intimate Privacy Invasion:**
- **Sensitive Locations**: FRT near mental health clinics, abortion providers, mosques, LGBTQ+ centers reveals private information
- **Relationship Mapping**: Identifies who you spend time with (political affiliations, romantic relationships)
- **Behavioral Profiling**: Patterns reveal lifestyle, health status, financial circumstances

**Data Perpetuity:**
- **No Expiration**: Biometric data persists indefinitely
- **Data Breaches**: Law enforcement databases are hacking targets
  - 2019: Customs and Border Protection breach exposed 100,000 face images
- **Mission Creep**: Data collected for one purpose repurposed (terrorism → immigration enforcement → protest monitoring)

**Lack of Consent:**
- Individuals never agreed to become part of facial recognition databases
- Driver's license photos used without explicit consent for FRT
- Photos scraped from social media (Clearview AI: 3+ billion images from Facebook, Instagram, etc.)

**Risk Category 3: Due Process Violations**

**Opacity and Uncontestability:**
- **Black Box Systems**: Defendants often unaware FRT was used in their investigation
- **Proprietary Algorithms**: "Trade secret" claims prevent examination of methods
- **No Expert Cross-Examination**: Defense cannot challenge FRT evidence effectively without access to system details
- **Low Transparency**: Police reports may say "investigative lead" without disclosing FRT involvement

**Evidentiary Concerns:**
- **Reliability Questions**: Error rates unknown for specific deployment conditions
  - Performance varies by: camera quality, lighting, angle, distance, occlusion (masks, glasses), age of photo
- **Lack of Standards**: No uniform accuracy requirements for law enforcement use
- **Confirmation Bias**: Officers more likely to see "match" when expecting one
- **Insufficient Validation**: Human reviewers may rubber-stamp AI recommendations

**Compounding Disadvantages:**
- **Presumption of Guilt**: FRT "match" creates presumption of involvement before investigation begins
- **Burden Reversal**: Defendants must prove they're not the person in image (difficult without technical expertise)
- **Inadequate Legal Representation**: Public defenders lack resources to challenge FRT evidence
- **Judicial Unfamiliarity**: Judges may not understand FRT limitations, overweight reliability

**Risk Category 4: Discrimination and Systemic Racism**

**Differential Error Rates as Discrimination:**
- Higher false positive rates for minorities = discrimination in its effect
- Violates Equal Protection Clause (14th Amendment)
- Creates two-tiered justice system based on appearance

**Targeting and Over-Policing:**
- **Deployment Patterns**: FRT disproportionately deployed in minority neighborhoods
  - Example: Detroit's "Green Light" camera network concentrated in Black communities
- **Database Composition**: Mugshot databases over-represent people of color due to historical over-policing
  - Creates "prior probability" bias: More Black faces in "criminal" database
- **Investigative Focus**: FRT used more for property crimes in minority areas, less for white-collar crimes

**Reinforcing Existing Bias:**
- **Feedback Loops**: 
  1. Over-policing of minority communities → More arrests → More faces in database
  2. More database entries → More false matches → More arrests
  3. Cycle intensifies over time
- **Legitimizing Bias**: Technology veneer makes discrimination appear objective, scientific
- **Automating Discrimination**: Codifies human bias into systems that operate at scale

**Historical Context:**
- FRT continues legacy of discriminatory identification practices
  - "Rogue's Gallery" photos targeted immigrants, poor
  - Mugshot files disproportionately Black and brown faces since inception
  - FRT automates this discriminatory history

**Risk Category 5: Erosion of Trust**

**Community-Police Relations:**
- **Distrust**: Communities feel surveilled, targeted, not protected
- **Reduced Cooperation**: Witnesses reluctant to come forward, report crimes
  - Research: Surveillance reduces crime reporting by 20-30%
- **Legitimacy Crisis**: Perception of police as occupying force rather than community partners
- **Intergenerational Trauma**: Adds to historical harms from policing (slavery, Jim Crow, war on drugs)

**Democratic Participation:**
- **Disengagement**: Surveillance discourages civic participation
- **Power Imbalance**: Citizens monitored while police operations remain opaque
- **Accountability Deficit**: FRT used on civilians but rarely on police misconduct

**Vulnerable Communities Most Affected:**
- Immigrants (documented and undocumented) fear ICE collaboration
- Muslims face increased suspicion, profiling
- Protesters and activists risk retaliation
- LGBTQ+ individuals in areas where identity is criminalized or stigmatized

**Risk Category 6: Function Creep and Authoritarian Potential**

**Expansion Beyond Initial Purpose:**
- Deployed for "finding violent criminals" but expanded to:
  - Minor offenses (shoplifting, fare evasion)
  - Civil violations (parking tickets)
  - Immigration enforcement
  - School discipline
  - Public benefit fraud investigation

**Authoritarian Applications:**
- **Political Suppression**: Identifying dissidents, protesters, opposition members
- **Social Control**: China's social credit system integrates FRT
- **Predictive Policing**: Pre-emptive action based on profiles
- **Behavioral Manipulation**: Surveillance changes behavior (Panopticon effect)

**Normalization Risks:**
- Once accepted in policing, expands to: employment screening, dating apps, retail, education
- Habituation to constant surveillance erodes privacy norms

**Risk Category 7: Technical Limitations and Misplaced Confidence**

**Accuracy Overstated:**
- Lab performance (controlled conditions, high-quality images) != real-world performance
- Vendors advertise "99% accuracy" but this doesn't account for:
  - Demographic variations
  - Poor image quality
  - Spoofing/adversarial attacks
  - Database size effects (larger databases = more false matches)

**Base Rate Fallacy:**
- Even with 99% accuracy, if searching database of 1 million for 1 suspect:
  - 10,000 false positives (1% of 1 million)
  - Overwhelms true positive signal

**Operator Error:**
- Human reviewers make mistakes:
  - Fatigue, confirmation bias, inadequate training
  - Research: Humans worsen FRT accuracy when given "AI assistance"

**Adversarial Vulnerabilities:**
- FRT can be fooled by: makeup, printed masks, adversarial patterns
- Arms race between evasion and detection techniques

---

#### 2. Policy Recommendations for Responsible Deployment

Given the severe ethical risks, the threshold question is: **Should facial recognition be used in policing at all?** Many advocates argue for complete bans. However, if deployment proceeds, the following policies are essential safeguards.

**Policy 1: Moratorium and Independent Evaluation**

**Immediate Action:**
- **Halt Deployment**: Suspend all facial recognition use in law enforcement pending comprehensive review
- **Independent Audit**: Third-party evaluation by:
  - Civil rights organizations
  - Academic researchers
  - Technical experts
  - Community representatives
- **Public Report**: Findings published with raw data, methodology, limitations

**Evaluation Criteria:**
- Does FRT demonstrably improve public safety?
- Do benefits outweigh privacy, civil rights costs?
- Are less invasive alternatives available?
- Can identified harms be adequately mitigated?

**Renewal Requirements:**
- Re-authorization every 2 years based on demonstrated benefits, no documented harms
- Burden of proof on proponents to justify continuation

**Policy 2: Strict Use Case Limitations**

**Permissible Uses (If Any):**
- **Violent Crime Investigation Only**: Homicide, kidnapping, armed robbery, aggravated assault, terrorism
- **Missing Persons**: Finding endangered individuals (children, elderly with dementia, abduction victims)
- **Victim Identification**: Identifying deceased individuals

**Prohibited Uses:**
- Minor offenses (misdemeanors, traffic violations, ordinance violations)
- Protest surveillance or monitoring First Amendment activities
- Immigration enforcement or ICE collaboration
- School surveillance
- Real-time, continuous public surveillance
- Predictive policing or pre-crime applications
- Identifying anonymous tipsters, witnesses, journalists, whistleblowers
- Commercial purposes (sharing with private entities)

**Geographic Restrictions:**
- Prohibited near: places of worship, medical facilities, courthouses, voting locations, schools

**Policy 3: Mandatory Accuracy Standards**

**Pre-Deployment Requirements:**
- **Independent Testing**: NIST or equivalent evaluation
- **Minimum Accuracy**: >99% true positive rate, <1% false positive rate **for all demographic groups**
- **Disaggregated Reporting**: Performance metrics by:
  - Race/ethnicity (at least 6 categories)
  - Gender
  - Age groups
  - Skin tone (Fitzpatrick scale)
- **Performance Parity**: False positive rates must be within 0.5% across all groups
- **System Suspension**: Immediate halt if disparities exceed thresholds

**Operational Monitoring:**
- **Real-World Validation**: Quarterly audits in actual deployment conditions
  - Test with images matching typical quality (not just high-quality photos)
  - Include occlusions (masks, glasses, hats)
  - Vary lighting, angles, distances
- **Error Tracking**: Log every false match with demographic analysis
- **Public Transparency**: Annual reports on accuracy, error rates, misidentifications

**Technology Certification:**
- Approved vendor list based on audited performance
- Re-certification annually as algorithms update
- Decertification for systems failing standards

**Policy 4: Judicial Oversight and Warrants**

**Warrant Requirement:**
- **Probable Cause**: Must have independent evidence justifying search before using FRT
- **Judge Authorization**: Warrant required for each FRT search
- **Specificity**: Warrant describes:
  - Particular suspect being sought
  - Specific databases to be searched
  - Time range of footage
  - Geographic scope

**Exceptions:**
- **Exigent Circumstances**: Immediate danger to life
  - Must be documented, reviewed post-hoc
  - Narrow: Active shooter, kidnapping in progress, imminent terrorist attack

**Warrant Content:**
- Judicial order must acknowledge:
  - FRT error rates and limitations
  - No basis for arrest solely on FRT match
  - Human verification required
  - Defendant notification required

**Policy 5: Database Restrictions**

**Permissible Databases:**
- **Booking Photos Only**: Mugshots from arrests
  - Must be expunged if charges dropped or acquittal
- **Consented Submissions**: Individuals voluntarily provide photo (missing persons)

**Prohibited Sources:**
- Driver's license photos (unless explicit FRT consent obtained)
- Passport photos
- Social media platforms
- Commercial datasets (Clearview AI-style scraping)
- School photos, employee databases
- Private sector sources without individual consent

**Data Retention:**
- **Match Results**: Deleted after case resolution
- **Non-Matches**: Deleted immediately (no search history retention)
- **Audit Logs**: Retained for oversight, anonymized where possible

**Data Security:**
- Encryption at rest and in transit
- Access controls (multi-factor authentication)
- Intrusion detection systems
- Regular security audits
- Breach notification within 24 hours

**Policy 6: Transparency and Accountability**

**Public Disclosure:**
- **Technology Use**: Agencies must publicly disclose:
  - FRT systems in use (vendors, capabilities)
  - Policies governing use
  - Oversight mechanisms
  - Complaint procedures
- **Usage Statistics**: Quarterly reports including:
  - Number of searches
  - Number of matches
  - Number leading to arrests
  - Conviction rates
  - False positive incidents
  - Demographic breakdown

**Defendant Notification:**
- **Mandatory Disclosure**: Prosecutors must inform defendants when FRT played any role in investigation
- **Discovery**: Defense entitled to:
  - FRT system documentation
  - Accuracy test results
  - Images compared
  - Match scores/confidence levels
  - Operator training records
- **Expert Challenge**: Right to independent expert evaluation of FRT evidence

**Audit Trails:**
- **Immutable Logs**: Every FRT query logged with:
  - Operator identity
  - Timestamp
  - Warrant information
  - Search parameters
  - Results
- **Supervisor Review**: Random sampling of queries for appropriateness
- **External Audits**: Annual review by civilian oversight board

**Policy 7: Community Oversight and Consent**

**Democratic Control:**
- **Local Approval**: City council or county board must approve FRT adoption via public vote
- **Community Input**: Mandatory public hearings before adoption
  - Minimum 3 hearings in affected communities
  - Accessible times, locations, languages
  - Written comment period (30 days minimum)

**Civilian Oversight Board:**
- **Composition**:
  - Community members (majority from over-policed neighborhoods)
  - Civil rights attorneys
  - Technical experts
  - Representatives from affected communities (immigrants, people of color, activists)
- **Powers**:
  - Review all FRT policies
  - Access audit logs and statistics
  - Investigate complaints
  - Recommend suspensions
  - Subpoena authority

**Opt-Out Rights:**
- Municipalities can ban FRT within their jurisdiction
- Current bans: San Francisco, Boston, Portland (OR), Oakland, Minneapolis, others

**Policy 8: Training and Human Review**

**Officer Training Requirements:**
- **Mandatory Curriculum** (minimum 8 hours):
  - FRT capabilities and limitations
  - Error rates and demographic disparities
  - Legal requirements and policies
  - Implicit bias recognition
  - Case studies of wrongful identifications
- **Annual Recertification**
- **Competency Testing**: Must pass exam to use FRT

**Human Verification Protocol:**
- **No Automated Arrests**: FRT match alone is never sufficient for arrest
- **Independent Review**: At least two trained analysts must verify match
- **Comparison Documentation**: Side-by-side photo comparison with features analysis
- **Supervisor Approval**: Lieutenant or above must approve before action taken
- **Contextual Corroboration**: Additional evidence (alibi check, other witnesses, forensic evidence) required

**Bias Mitigation Training:**
- Recognition of cross-race effect (people less accurate identifying other-race faces)
- Debiasing techniques
- Heightened scrutiny for minority matches

**Policy 9: Victim Support and Remedies**

**Immediate Response to Misidentification:**
- Immediate release from custody
- Expedited record expungement
- Public apology and correction

**Compensation:**
- **Civil Liability**: Waiver of qualified immunity for FRT misidentifications
- **Damages**: Compensation for:
  - Lost wages
  - Legal fees
  - Emotional distress
  - Reputation harm
- **Exemplary Damages**: If reckless disregard for FRT limitations

**Legal Assistance:**
- Free legal representation for victims
- Fast-track expungement processes
- Support services (counseling, job placement assistance)

**Policy 10: Ongoing Research and Improvement**

**Funded Research:**
- Independent research on:
  - FRT accuracy in real-world conditions
  - Demographic disparities
  - Long-term community impacts
  - Bias mitigation techniques
  - Alternative investigation methods

**Technology Standards Development:**
- Collaboration with NIST, ACM, IEEE to develop:
  - Performance benchmarks
  - Fairness metrics
  - Testing protocols
  - Best practices

**Continuous Improvement:**
- Policies updated based on research findings
- Technology upgrades required to meet evolving standards
- Lessons learned from incidents incorporated into training

**Policy 11: Sunset Provisions**

**Automatic Expiration:**
- FRT authorization expires after 2 years unless renewed
- Renewal requires:
  - Demonstrated public safety benefits
  - No documented civil rights violations
  - Compliance with all policies
  - Community support (public hearing + vote)

**Termination Triggers:**
- Program terminated if:
  - More than 3 misidentifications in 12 months
  - Persistent demographic disparities
  - Policy violations
  - Loss of community trust
  - Better alternatives available

**Alternative Approaches:**
- Invest in traditional policing methods: witness interviews, forensic evidence, community relationships
- Consider abolishing FRT entirely in favor of less invasive investigative techniques

---

## 🔬 Part 3: Practical Audit (25%)

### Overview
This section provides a hands-on analysis of the COMPAS Recidivism Dataset using Python and IBM's AI Fairness 360 toolkit to identify and measure racial bias in criminal risk assessment.

### Dataset Information

**COMPAS (Correctional Offender Management Profiling for Alternative Sanctions)**
- **Developer**: Northpointe (now Equivant)
- **Purpose**: Predict likelihood of criminal reoffending
- **Use**: Informs bail, sentencing, parole decisions across US courts
- **Output**: Risk scores from 1-10 (1=lowest risk, 10=highest risk)

**ProPublica's Analysis (2016)**
- **Source**: Public records from Broward County, Florida
- **Dataset Size**: 7,214 defendants screened 2013-2014
- **Follow-up**: Two-year tracking of actual recidivism
- **Key Finding**: Algorithm biased against Black defendants

**Dataset Variables:**
- Demographics: age, sex, race
- Criminal history: prior convictions, charge degree
- COMPAS score: decile_score (1-10), score_text (Low/Medium/High)
- Outcome: two_year_recid (1=reoffended, 0=did not)

### Technical Requirements

**Python Libraries:**
```bash
pip install aif360==0.5.0
pip install pandas==1.5.3
pip install numpy==1.24.3
pip install matplotlib==3.7.1
pip install seaborn==0.12.2
pip install scikit-learn==1.2.2
pip install jupyter
```

**System Requirements:**
- Python 3.8+
- 4GB RAM minimum
- Jupyter Notebook (recommended for interactive analysis)

### Code Structure

The audit script (`compas_bias_audit.py`) contains:

**1. Data Loading (`load_compas_data`)**
- Imports COMPAS dataset via AIF360's built-in loader
- Converts to pandas DataFrame for analysis
- Displays basic dataset information

**2. Exploratory Data Analysis (`exploratory_analysis`)**
- Examines racial composition of dataset
- Calculates actual recidivism rates by race
- Analyzes COMPAS score distribution by race
- Generates 4-panel visualization:
  - Race distribution bar chart
  - Actual recidivism rates by race
  - Average COMPAS scores by race
  - Score distribution comparison (African-American vs. Caucasian)

**3. Fairness Metrics Calculation (`analyze_fairness_metrics`)**
- Uses AIF360's BinaryLabelDatasetMetric
- Calculates:
  - **Statistical Parity Difference**: Difference in positive prediction rates between groups
  - **Disparate Impact**: Ratio of positive prediction rates (legal threshold: 0.8)
  - **Base Rate**: Actual outcome rates by group
- Interprets metrics with fairness thresholds

**4. Error Rate Analysis (`analyze_error_rates`)**
- Defines "high risk" threshold (decile_score >= 5)
- Calculates confusion matrix metrics by race:
  - False Positive Rate (FPR): Non-recidivists incorrectly labeled high-risk
  - False Negative Rate (FNR): Recidivists incorrectly labeled low-risk
  - Precision: Accuracy of high-risk predictions
  - Recall: Coverage of actual recidivists
- Visualizes FPR and FNR disparities

**5. Bias Mitigation (`mitigate_bias`)**
- Applies Reweighing algorithm (preprocessing technique)
- Adjusts instance weights to remove correlation between protected attribute and labels
- Compares fairness metrics before/after mitigation
- Visualizes improvement in fairness

**6. Main Execution (`main`)**
- Orchestrates all analysis steps
- Generates three PNG visualizations
- Provides summary of findings

### Running the Analysis

**Step 1: Set Up Environment**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Step 2: Execute Script**
```bash
# Run complete analysis
python compas_bias_audit.py

# Or use Jupyter Notebook
jupyter notebook compas_bias_audit.ipynb
```

**Step 3: Review Outputs**
- `compas_exploratory_analysis.png`: Initial data exploration
- `compas_error_rates.png`: False positive/negative rate comparison
- `compas_bias_mitigation.png`: Before/after fairness metrics

### Expected Results

**Key Findings:**

**1. Disparate Impact: 0.64**
- African-Americans flagged as high-risk at 1.56x the rate of Caucasians
- Well below 0.8 legal threshold (indicates discrimination)
- Violates EEOC Uniform Guidelines

**2. False Positive Rate Disparity:**
- African-American: ~45%
- Caucasian: ~23%
- **Impact**: Black defendants who will NOT reoffend are labeled high-risk at nearly double the rate

**3. False Negative Rate Inversion:**
- African-American: ~28%
- Caucasian: ~48%
- **Impact**: White defendants who WILL reoffend are incorrectly labeled low-risk more often

**4. Calibration Issues:**
- COMPAS scores mean different things for different races
- A "7" risk score has different actual recidivism probability for Black vs. White defendants

**5. Impossibility of Fairness:**
- Cannot simultaneously achieve:
  - Equal false positive rates AND
  - Equal false negative rates AND
  - Calibration
- Must choose which fairness criterion to prioritize

### Interpretation

**Why This Matters:**
- Higher false positives for Black defendants → Harsher sentences, denied bail/parole
- Higher false negatives for White defendants → More lenient treatment
- Algorithm systematically treats races differently
- Automates and legitimizes racial discrimination

**Root Causes:**
- **Training data bias**: Historical over-policing of Black communities
- **Proxy variables**: Features correlated with race (zip code, prior arrests)
- **Recidivism definition**: Re-arrest (not re-offense) reflects policing patterns
- **Base rate differences**: Groups have different recidivism rates due to systemic factors

### Remediation Recommendations

**From Audit Report:**

**Immediate Actions:**
1. **Implement Reweighing**: Demonstrated to improve Disparate Impact from 0.64 to 0.89
2. **Adjust Thresholds**: Use different cutoff scores to equalize false positive rates
3. **Remove Proxies**: Eliminate features that correlate with race

**Long-term Solutions:**
1. **Retrain with Balanced Data**: Account for systemic over-policing
2. **Continuous Monitoring**: Quarterly fairness audits with public reporting
3. **Human Override**: Require judicial review, never use algorithm alone
4. **Consider Abolition**: Evaluate whether algorithmic risk assessment can be fair

### Additional Analysis Extensions

**For Advanced Students:**

1. **Intersectional Analysis**
   ```python
   # Analyze age + race intersections
   for race in df['race'].unique():
       for age_group in ['<25', '25-45', '45+']:
           subgroup = df[(df.race==race) & (df.age_cat==age_group)]
           calculate_metrics(subgroup)
   ```

2. **Counterfactual Fairness**
   ```python
   # Test: Does changing race alone change prediction?
   for idx in sample_indices:
       original_pred = model.predict(df.iloc[idx])
       df_counterfactual = df.iloc[idx].copy()
       df_counterfactual['race'] = flip_race(df_counterfactual['race'])
       counterfactual_pred = model.predict(df_counterfactual)
       if original_pred != counterfactual_pred:
           print(f"Prediction changed solely due to race: {idx}")
   ```

3. **Temporal Analysis**
   ```python
   # How do scores change over time?
   df_2013 = df[df.screening_date.year == 2013]
   df_2014 = df[df.screening_date.year == 2014]
   compare_metrics(df_2013, df_2014)
   ```

4. **Feature Importance for Bias**
   ```python
   from sklearn.ensemble import RandomForestClassifier
   import shap
   
   # Train model
   rf = RandomForestClassifier()
   rf.fit(X_train, y_train)
   
   # SHAP analysis
   explainer = shap.TreeExplainer(rf)
   shap_values = explainer.shap_values(X_test)
   
   # Compare feature importance by race
   shap_aa = shap_values[df_test.race=='African-American']
   shap_c = shap_values[df_test.race=='Caucasian']
   ```

---

## 💭 Part 4: Ethical Reflection (5%)

### Purpose
This reflection demonstrates personal commitment to ethical AI development through concrete planning for a real or hypothetical project.

### Structure

**Your reflection should include:**

1. **Project Description** (1 paragraph)
   - What AI system are you building/considering?
   - What problem does it solve?
   - Who are the stakeholders?

2. **Ethical Risks Identification** (1-2 paragraphs)
   - What could go wrong?
   - Who might be harmed?
   - What biases might exist?

3. **Ethical Principles Application** (Main section - 3-4 paragraphs)
   - Select 3-5 relevant ethical principles (from Part 1)
   - For EACH principle:
     - Explain how it applies to your project
     - Provide 3+ specific, concrete actions you'll take
     - Mention potential trade-offs or challenges

4. **Accountability Statement** (1 paragraph)
   - Personal commitment to ethics
   - What you'll do if conflicts arise
   - How you'll stay vigilant

### Example Reflection Template

```markdown
## Project: [Your AI System Name]

### Context
I am developing [description], which aims to [purpose]. The primary stakeholders 
include [list], and the system will [impact].

### Ethical Risks
This project raises concerns about [risk 1], [risk 2], and [risk 3]. 
Specifically, [vulnerable group] could be harmed through [mechanism]. 
Additionally, [systemic risk] could emerge if [scenario].

### Ethical Principles

#### 1. [Principle Name]
**Application**: [How this principle applies to your project]

**Concrete Actions**:
- **Action 1**: [Specific, measurable commitment]
  - Implementation: [How you'll do it]
  - Timeline: [When]
  - Accountability: [Who oversees]
  
- **Action 2**: [Specific, measurable commitment]
- **Action 3**: [Specific, measurable commitment]

**Challenges**: [Anticipated difficulties and how you'll address them]

[Repeat for each principle]

### Accountability
I commit to [personal statement]. If I discover [ethical violation], I will 
[concrete response]. I recognize that [limitation acknowledgment] and will 
[ongoing vigilance plan].
```

### Evaluation Criteria

Your reflection will be assessed on:

1. **Depth of Analysis** (40%)
   - Thorough identification of ethical risks
   - Understanding of how principles apply to your specific context
   - Recognition of trade-offs and complexity

2. **Concreteness** (30%)
   - Specific, actionable commitments (not vague promises)
   - Measurable outcomes
   - Clear implementation plans

3. **Comprehensiveness** (20%)
   - Multiple ethical dimensions considered
   - Addresses various stakeholders
   - Long-term perspective

4. **Personal Accountability** (10%)
   - Genuine personal commitment
   - Realistic self-assessment
   - Willingness to make difficult choices

### Common Pitfalls to Avoid

❌ **Vague Commitments**: "I will try to be fair"
✅ **Specific Actions**: "I will conduct quarterly bias audits measuring false positive rates disaggregated by race and gender, with automatic system suspension if disparities exceed 5%"

❌ **Surface-Level**: "Privacy is important so I'll protect data"
✅ **Detailed Planning**: "I will implement differential privacy with ε=0.1, use federated learning to keep data decentralized, encrypt all data with AES-256, obtain explicit consent specifying exact data uses, and provide opt-out mechanisms"

❌ **Ignoring Trade-offs**: Claiming perfect fairness and accuracy
✅ **Acknowledging Complexity**: "Achieving demographic parity may reduce overall accuracy by 3-5%; I prioritize fairness because [justification], and will mitigate accuracy loss through [methods]"

❌ **Passive Voice**: "Bias will be checked"
✅ **Personal Ownership**: "I will personally review bias audit results monthly and halt deployment if issues are found"

---

## 🏥 Bonus Task: Policy Proposal (Extra 10%)

### Overview
Draft a comprehensive 1-page policy guideline for ethical AI use in healthcare, addressing consent, bias mitigation, and transparency.

### Policy Components Required

**1. Patient Consent Protocols** (30%)
- When/how patients are informed about AI use
- Consent form requirements
- Opt-out procedures
- Special considerations for vulnerable populations

**2. Bias Mitigation Strategies** (40%)
- Pre-deployment testing requirements
- Training data standards
- Ongoing monitoring procedures
- Response protocols when bias is detected

**3. Transparency Requirements** (30%)
- What information must be disclosed
- To whom (patients, providers, regulators)
- Documentation standards
- Explainability requirements

### Format Guidelines

**Length**: Aim for 800-1200 words (expandable if needed for comprehensiveness)

**Structure**:
```
# Policy Title

## Purpose Statement
[1-2 sentences on policy goals]

## 1. Patient Consent and Autonomy
### 1.1 Informed Consent Requirements
[Specific requirements]

### 1.2 Right to Explanation
[Patient rights]

### 1.3 Vulnerable Populations
[Special protections]

## 2. Bias Mitigation and Fairness
### 2.1 Pre-Deployment Testing
[Requirements before clinical use]

### 2.2 Training Data Standards
[Data quality requirements]

### 2.3 Ongoing Monitoring
[Continuous oversight]

## 3. Transparency and Explainability
### 3.1 Clinical Decision Support
[Provider-facing transparency]

### 3.2 Patient-Facing Disclosures
[Patient communication]

## 4. Privacy and Data Security
[Brief data protection requirements]

## 5. Accountability and Governance
[Oversight mechanisms]

## 6. Enforcement
[Compliance and penalties]
```

### Writing Tips

**Be Specific and Actionable**:
- ❌ "Systems should be fair"
- ✅ "Systems must demonstrate <5% performance disparity across racial groups as measured by sensitivity and specificity"

**Use Clear Language**:
- Avoid jargon where possible
- Define technical terms
- Write for healthcare administrators, not just AI experts

**Include Enforcement**:
- Policies without teeth are ignored
- Specify: audits, penalties, certification requirements

**Balance Rigor and Feasibility**:
- Standards should be high but achievable
- Consider implementation costs and timelines
- Provide examples and resources

### Evaluation Rubric

| Criterion | Excellent (9-10 pts) | Good (7-8 pts) | Needs Improvement (5-6 pts) |
|-----------|---------------------|----------------|----------------------------|
| **Comprehensiveness** | Addresses all required components in depth | Covers required areas with some gaps | Missing key components |
| **Specificity** | Concrete, measurable requirements throughout | Mix of specific and general guidance | Mostly vague statements |
| **Feasibility** | Realistic, implementable standards | Somewhat practical but challenges noted | Unrealistic or no implementation path |
| **Legal/Ethical Grounding** | Cites relevant regulations, ethical frameworks | Some grounding in standards | Lacks foundation |

### Real-World Examples to Reference

**Existing Healthcare AI Policies**:
- FDA's AI/ML Software as Medical Device Action Plan
- WHO's Ethics and Governance of AI for Health
- EU Medical Device Regulation (MDR) 2017/745
- UK's Code of Conduct for Data-Driven Health Technologies

**Your policy should be MORE comprehensive than these, incorporating lessons from:**
- GDPR
- Clinical trial informed consent standards
- Health equity frameworks
- Algorithm accountability literature

---

## 🛠️ Installation Guide

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning repository)
- Jupyter Notebook (optional, for interactive analysis)

### Step-by-Step Installation

**1. Clone Repository**
```bash
git clone https://github.com/yourusername/ai-ethics-assignment.git
cd ai-ethics-assignment
```

**2. Create Virtual Environment** (Recommended)
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install Dependencies**
```bash
# Install from requirements file
pip install -r part3_practical_audit/requirements.txt

# Or install individually
pip install aif360==0.5.0
pip install pandas==1.5.3
pip install numpy==1.24.3
pip install matplotlib==3.7.1
pip install seaborn==0.12.2
pip install scikit-learn==1.2.2
pip install jupyter
```

**4. Verify Installation**
```bash
python -c "import aif360; print('AIF360 version:', aif360.__version__)"
python -c "import pandas; print('Pandas version:', pandas.__version__)"
```

**5. Download Dataset** (if needed)
```bash
cd part3_practical_audit/data
wget https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv
```

### Troubleshooting

**Issue**: `aif360` installation fails
**Solution**:
```bash
# Install build tools first
pip install --upgrade pip setuptools wheel
pip install Cython
pip install aif360
```

**Issue**: `ImportError: No module named 'aif360.datasets'`
**Solution**:
```bash
pip uninstall aif360
pip install aif360==0.5.0
```

**Issue**: Matplotlib figures not displaying
**Solution**:
```bash
# For Jupyter
%matplotlib inline

# For Python script
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'
```

---

## 🚀 Running the Code

### Option 1: Python Script

```bash
cd part3_practical_audit
python compas_bias_audit.py
```

**Expected Output**:
```
================================================================================
COMPAS RECIDIVISM DATASET - RACIAL BIAS AUDIT
Using AI Fairness 360 Toolkit
================================================================================

Dataset Shape: (7214, 52)

Columns: ['age', 'race', 'sex', 'priors_count', 'decile_score', 'two_year_recid', ...]

================================================================================
EXPLORATORY DATA ANALYSIS
================================================================================

Race Distribution:
African-American    3696
Caucasian           2454
Hispanic             637
Other                377
Asian                 31
Native American       19

✓ Saved: compas_exploratory_analysis.png

================================================================================
FAIRNESS METRICS ANALYSIS
================================================================================

Statistical Parity Difference: -0.1936
Disparate Impact: 0.6415

================================================================================
ERROR RATE ANALYSIS
================================================================================

Caucasian:
  False Positive Rate: 0.2329
  False Negative Rate: 0.4779

African-American:
  False Positive Rate: 0.4488
  False Negative Rate: 0.2804

✓ Saved: compas_error_rates.png

================================================================================
BIAS MITIGATION - REWEIGHING
================================================================================

BEFORE Mitigation:
  Statistical Parity Difference: -0.1936
  Disparate Impact: 0.6415

AFTER Mitigation:
  Statistical Parity Difference: -0.0134
  Disparate Impact: 0.8932

✓ Saved: compas_bias_mitigation.png

================================================================================
AUDIT COMPLETE
================================================================================
```

### Option 2: Jupyter Notebook

```bash
cd part3_practical_audit
jupyter notebook compas_bias_audit.ipynb
```

**Advantages of Jupyter**:
- Interactive cell-by-cell execution
- Inline visualizations
- Easy experimentation
- Better for learning/teaching

**Workflow**:
1. Open notebook in browser
2. Run cells sequentially (Shift+Enter)
3. Modify parameters and re-run
4. Export as PDF/HTML for submission

### Option 3: Google Colab

**For users without local Python setup**:

1. Upload files to Google Drive
2. Open new Colab notebook
3. Mount Drive:
```python
from google.colab import drive
drive.mount('/content/drive')
```
4. Install dependencies:
```python
!pip install aif360 pandas matplotlib seaborn scikit-learn
```
5. Copy/paste audit code or upload `.py` file
6. Run cells

---

## 📊 Results and Findings

### Summary of Key Results

**Dataset Composition**:
- **Total Defendants**: 7,214
- **African-American**: 51.2% (3,696)
- **Caucasian**: 34.0% (2,454)
- **Hispanic**: 8.8% (637)
- **Other**: 5.2% (377)
- **Male**: 81.5%
- **Average Age**: 34.4 years

**Actual Recidivism Rates**:
- **Overall**: 45.1%
- **African-American**: 51.4%
- **Caucasian**: 39.4%
- **Difference**: 12 percentage points

**COMPAS Risk Score Assignment**:
- **African-American Average**: 5.96
- **Caucasian Average**: 4.73
- **Difference**: 1.23 points (on 1-10 scale)

**Classification Using Threshold (Score >= 5 = High Risk)**:

---
## 🧑‍💻 Author  

**Course:** AI for Software Engineering  
**Week:** 7  
**Institution:** [PLP AFRICA ACADEMY]  

** GROUP MEMBERS:**  

**1.** [Stephen Odhiambo]  **Email:** (stephenodhiambo008@gmail.com) 

**2.** [Jackline Biwott]  **Email:** (biwottjackline72@gmail.com) 

November 2025

---

## 🆘 Support

For questions or issues:
- Create an issue in GitHub repository
- Contact: [stephenodhiambo008@gmail.com &
  
-  biwottjackline72@gmail.com]

- PLP Community 

## 👥 Acknowledgments

Special thanks to:
- PLP Academy instructors for guidance

---
