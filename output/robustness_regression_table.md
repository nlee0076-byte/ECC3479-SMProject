# Table 1: Robustness Check - Main Explanatory Variable

Logistic regression (1-5, 7-8) and OLS (6). Dependent variable: affects_academic_performance (binary).

| Specification | Coefficient | Std. Error | N |
|---|---|---|---|
| (1) Main | 1.7653*** | (0.2344) | 705 |
| (2) No Controls | 2.4466*** | (0.1987) | 705 |
| (3) Age+Sleep | 1.8825*** | (0.2352) | 705 |
| (4) No Outliers | 1.7651*** | (0.2345) | 702 |
| (5) Undergrad | 0.9414*** | (0.3406) | 353 |
| (6) LPM | 0.1632*** | (0.0173) | 705 |
| (7) Log(Usage) | 7.5449*** | (1.0400) | 705 |
| (8) Quadratic | -0.7883 | (1.6428) | 705 |

**Notes:**
- (1) Main specification with all controls (age, sleep, gender, academic level)
- (2) Usage hours only, no controls
- (3) Usage + demographic controls (age, sleep)
- (4) Main specification excluding outliers (IQR method, removed 3 obs)
- (5) Restricted to undergraduate students only
- (6) Linear probability model (OLS)
- (7) Usage entered in log form (semi-log specification)
- (8) Usage and usage-squared terms (quadratic)

Significance: *** p<0.01, ** p<0.05, * p<0.10