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

**Phase 1: Pre-
