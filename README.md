# Root-Growth-Simulation-Experiment

An experimental study investigating the mechanical behavior of flexible fibers penetrating granular media, simulating plant root growth under various environmental conditions.

## Project Overview

This project explores the bending behavior of plastic fibers pushed through different granular media configurations, serving as a simplified model for understanding how plant roots navigate through soil with varying density and composition. The research combines mechanical engineering principles with materials science to characterize critical transition points between stable and unstable fiber motion.

## Scientific Background

Plant roots face mechanical challenges when growing through soil, particularly when encountering high-density regions or obstacles. This study uses controlled laboratory conditions to investigate:

- **Mechanical stability**: Critical length thresholds for fiber bending
- **Media effects**: How particle size distribution affects penetration resistance  
- **Force balance**: Competition between friction forces and bending moments

## Experimental Setup

### Equipment
- **Stepper Motor**: Precise fiber advancement control
- **Pulley System**: Force transmission mechanism
- **Brass Cylinders**: Granular media containers (3 types)
  - Radius: 0.3 cm, 0.35 cm, 0.4 cm
- **Plastic Fiber**: Test specimen (various lengths: 2.5-6 cm)
- **High-Speed Camera**: Motion capture for analysis

### Media Configurations
1. **Single-type grains**: Uniform particle size
2. **Two-type mixture**: Binary size distribution
3. **Three-type mixture**: Polydisperse system

### Key Parameters
- **Packing Fraction (φ)**: 60-90% density range
- **Fiber Length (L)**: 2.5-6.0 cm
- **Critical Packing Fraction (φⱼ)**: 
  - 1-type: 81-89%
  - 2-type: 84%
  - 3-type: 81%

## Theoretical Framework

### Force Analysis
The system exhibits two competing forces:

**Friction Force**:
```
F_f = μ × W_grains = (μρgL²/2) × φh_grains
```

**Bending Force**:
```
F_b = (8EIπ²)/(L³) × deflection
```

### Critical Length Calculation
From force balance (F_f = F_b):
```
L_c = K × (φ - φⱼ)^(-1/3)
```

Where:
- K: Material-dependent constant
- φⱼ: Jamming packing fraction
- E: Young's modulus (1.16 × 10⁹ Pa)
- I: Second moment of inertia

### Motion Regimes

1. **Jiggling** (L < L_c): Small oscillations around equilibrium
2. **Critical Transition** (L ≈ L_c): Onset of instability
3. **Exponential Bending** (L > L_c): Rapid deflection growth

## Analysis Methods

### Video Processing Pipeline
1. **Time-lapse Recording**: High-resolution motion capture
2. **Image Processing**: 8-bit conversion and threshold adjustment
3. **Feature Tracking**: Automated fiber tip and pulley position detection
4. **Data Extraction**: Position vs. time analysis using Fiji ImageJ

### Statistical Analysis
- **Exponential Fitting**: δ = A×e^(-L/s) for bending curves
- **Critical Point Detection**: Transition boundary identification
- **Uncertainty Quantification**: Error propagation in measurements

## Key Experimental Results

### Packing Fraction Effects
- **Higher density → easier bending**: Increased friction force
- **Critical transitions**:
  - R=0.3cm: φⱼ = 81%
  - R=0.35cm: φⱼ = 89%  
  - R=0.4cm: φⱼ = 81%

### Fiber Length Scaling
- **Exponential regime**: δ = 1678.2 × e^(-L/3.2) + constant
- **Critical length**: L_c ≈ 5.8 cm (typical conditions)
- **Length correction**: Adjusted for jiggling-independent behavior

### Media Composition Impact
- **Polydisperse systems**: Enhanced bending tendency
- **Size distribution effects**: 3-type > 2-type > 1-type (bending ease)
- **Jamming fraction variation**: φⱼ decreases with polydispersity

### Bending Classification
1. **Exponential Bending**: Standard power-law deflection
2. **Critical Length Behavior**: Transition region dynamics
3. **High Packing Fraction**: Modified response curves

## Engineering Applications

### Geotechnical Engineering
- **Foundation Design**: Understanding soil-structure interaction
- **Drilling Operations**: Optimizing penetration strategies
- **Slope Stability**: Fiber reinforcement mechanisms

### Agricultural Technology
- **Precision Agriculture**: Root growth optimization
- **Soil Modification**: Density control for crop enhancement  
- **Irrigation Systems**: Subsurface installation techniques

### Biomedical Devices
- **Catheter Design**: Flexible insertion mechanisms
- **Minimally Invasive Surgery**: Navigation through tissue
- **Drug Delivery**: Micro-needle penetration dynamics

## Technical Specifications

### Material Properties
- **Fiber Material**: Plastic (E = 1.16 × 10⁹ Pa)
- **Cross-section**: Rectangular (1.5 cm × 0.5 mm)
- **Poisson's Ratio**: ν = 0.28
- **Density**: Variable based on granular media

### Measurement Precision
- **Position Accuracy**: ±0.05 cm
- **Force Resolution**: 0-50g range
- **Temporal Resolution**: High-speed video capture
- **Statistical Confidence**: Multiple trial averaging

## Data Analysis Workflow

```
Raw Video Data
    ↓
Image Processing (Fiji)
    ↓
Feature Extraction
    ↓
Position Tracking
    ↓
Curve Fitting & Analysis
    ↓
Statistical Validation
    ↓
Physical Interpretation
```



## Key Findings Summary

1. **Scaling Relationship**: Critical length follows L_c ∝ (φ - φⱼ)^(-1/3)
2. **Material Effect**: Higher density media reduces stability threshold
3. **Geometric Influence**: Polydisperse systems enhance bending tendency
4. **Transition Dynamics**: Three distinct bending regimes identified
5. **Predictive Model**: Successful force balance validation

## Laboratory Skills Demonstrated

### Experimental Design
- Multi-parameter study planning
- Control variable isolation
- Systematic data collection protocols

### Technical Proficiencies  
- Precision mechanical setup
- High-speed imaging techniques
- Automated data processing pipelines
- Statistical analysis and curve fitting

### Problem-Solving Abilities
- Complex system characterization
- Multi-scale analysis (microscopic forces → macroscopic behavior)
- Theoretical model validation through experiment

## Files
- `Final_Report.pdf` – Final presentation/report of the project  
- `analysis_codes/` – Example data and code for analysis and fitting
- `Ref_paper.pdf` – Reference Paper of the project
