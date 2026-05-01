# ECC3479-SMProject
# Research Question Draft

## What is your research question?

“Among young adults/students, is heavier use of short-form social media platforms associated with worse self-reported academic performance and cognitive ability?”

## Why is it economically relevant?

Platforms such as TikTok, Instagram and Youtube encourage the production of short, fast-paced and visually stimulating content that maximises user retention through a personalised algorithm. Short-form content has been suggested to impair cognitive performance by nurturing our preference for quick dopamine hits, which reduces our attention span, weakens our short-term memory and reduces our capacity for extensive learning. This form of content is now comparatively more desirable to longer videos. Rapid dopamine sources are highly stimulating, and prolonged scrolling through short videos can strain cognitive function, desensitising the brain to tasks that require more effort and a larger attention span, creating addictive patterns of immediate gratification. 

This is economically relevant as cognitive function is directly correlated to our educational attainment, as a higher cognitive ability is associated with better academic performance, faster skill acquisition as well as more complex problem solving. These factors directly translate to developing more highly skilled individuals for the labour market. As economies continue to develop and advance, a society’s cognitive skill becomes increasingly important in educational attainment, employability and wage determination. There have been an increasing number of studies conducted pertaining to the role of cognitive ability to educational outcome, implying that cognitive ability may be utilised as a useful tool when predicting economic outcomes, both on a national (GDP levels) and individual level (employment & earnings). 

## Why do you need to use empirical methods to answer your question?

Empirical methods are necessary to answer this question because they rely on observable evidence to test hypotheses and draw conclusions. By collecting and analysing real data, empirical analysis would allow me to determine whether there is a relationship between exposure to short-form content and cognitive ability, and whether this may influence employment outcomes. This can be examined by measuring changes in average exposure to short-form content and comparing them with changes in cognitive performance metrics. Subsequently, it would become easier to identify patterns and assess whether increased exposure is associated with differences in cognitive functioning and workplace productive capacities.

I will be utilising OLS regression to answer my research question. OLS regression isolates the relationship between short-form social media consumption and cognitive performance after holding other relevant factors constant, producing a more credible estimate. The model will regress cognitive test scores on average daily short-form content consumption, controlling for age, education level and income.

## What kind of data will you use/collect to address your research question?

To address this research question, I would collect data on both cognitive ability and short-form social media exposure and subsequently employment levels. Cognitive processes cannot be directly observed, so they are typically measured using indicators that infer cognitive ability based on established psychological theories. These indicators are often obtained through standardised metrics, such as general intelligence or cognitive performance tests like the Wechsler Intelligence Scale, or other measures of attention, memory, and processing speed. I plan to utilise datasets from Kaggle, containing information on students’ social media usage (e.g screentime), platform preferences, and self-reported academic performance, focusing on time spent on short-form content platforms such as TikTok and Instagram. By comparing measures of cognitive performance with levels of exposure to these platforms, it would be possible to analyse whether higher levels of short-form content consumption are associated with differences in cognitive functioning and potential employment-related outcomes such as productivity or attention.


# REPOSITORY STRUCTURE

My repository is structured into four main folders - data, SRC, output and docs - alongside my README.md file. The data folder is divided into two key components, raw and clean. The raw data is the original, unmodified dataset, while the clean data consists of processed data that has been refined through code to correct errors, resolve inconsistencies and standardise variables for analysis. The SRC folder contains the Python scripts used for data cleaning. The output folder stores any figures or tables generated from the data, and the docs folder holds project related notes and documentation. Finally, the README.md file includes project instructions as well as a draft of my research question.

```
ECC3479-SMProject/
├── code/
│   └── clean_data.py              ← script to clean raw dataset
├── data/
│   ├── raw/
│   │   └── Students Social Media Addiction.csv
│   └── clean/
│       └── cleaned_social_media.csv
├── outputs/
│   └── placeholder.txt
├── docs/
│   └── placeholder.txt
├── requirements.txt
└── README.md
```
# HOW TO RUN PROJECT FROM SCRATCH:

## Manual Steps Outside of the Code

The following steps must be completed manually before running the project:

1. Download the dataset from Kaggle: https://www.kaggle.com/datasets/zahranusratt/student-social-media-addiction-analysis-dataset
2. Extract the dataset from the downloaded ZIP file.
3. Place the CSV file into your own directory

## 1. Install necessary packages. This project utilises Python and Pandas. 
    Python: Go to python.org/downloads and download Python 3.11 or later. 
    VS-Code: Go to code.visualstudio.com and download VS Code for your operating system
    Econometrics Packages: Open VS Code’s integrated terminal and run: “pip install pandas’ 
        Verify with: python -c "import pandas, statsmodels, linearmodels; print('all good')"

## 2. Create project repository in GitHub
    Sign into GitHub, click New button at top-left of screen to create a new repository
    Designate an appropriate project name (E.g ECC3479-Project), select add README file and click create repository.

## 3. Clone the repository to VS Code.
    Open VS Code. Open the Source Control panel (Ctrl+Shift+G) and click Clone Repository.
    Under GitHub, select the green Code button and copy the repository URL. Paste the URL into VS Code and select a local folder. Click open when prompted.

## 4. Create Repository Structure 
    In VS code, select File → Open Folder (from selected local folder)
    In the Explorer panel on the left, by right-clicking your main folder (ECC3479-Project), create the following sub-folders
        data
        code
        output
        docs 
    Right-click the data folder, and create two sub-folders, raw (unmodified data) and clean (processed data refined through code).

## 5. Update the README and commit changes
    In VS Source Control Panel (Ctrl + Shift + G), you will see your changes listed. Stage them by clicking the + next to each file, and enter a short commit message (e.g: establish project structure and README), then click commit.
    An option to sync changes will appear. Click Sync Changes to upload to GitHub. If this does not appear, hover over the bottom left of the screen and select to Push.

## 6. Add the raw data set
    Import dataset from Kaggle: Extract from zipfile (ensure it is a csv file)
    Drag csv file from Desktop into data/raw.
    Open VS Source Control Panel (Ctrl + Shift + G); Stage, commit and sync changes.

## 7. Create a clean version of raw data
    Right-click the code file and select New File. Name it clean_data.py. Our objective is to create a clean version of the raw data. 
    Create a python script that will read raw dataset from data/raw and save the clean output to data/clean without overwriting the file.
        Your script should: Rename any unclear variable names, rectify any obvious data quality issues (e.g: missing values and inconsistent coding) and save the cleaned output without overwriting the raw file.

## 8. Run data cleaning script - Run Order of Script utilised in this file (clean_data.py)
     Run clean_data.py
    

## 9.Locate Cleaned Dataset in data/clean.

## Datasets

| File | Rows | Description |
|------|------|------------|
| Students Social Media Addiction.csv | ~700 | Survey dataset of students’ social media usage and behavioural outcomes. Columns include: student_id, age, gender, academic_level, country, avg_daily_usage_hours, most_used_platform, affects_academic_performance, mental_health_score, sleep_hours. |

The dataset is a survey-based dataset obtained from Kaggle, containing self-reported information on social media usage patterns and academic outcomes among students. 

The cleaned dataset (cleaned_social_media.csv) is generated from the raw dataset using the script in `src/clean_data.py`. The cleaning process standardises variable names, removes missing values, and creates additional variables such as usage_group to categorise daily social media usage.

## RUN REGRESSION

Running `analysis.ipynb` will produce regression results and visualisations used in the analysis.
###  Analysis Overview

The primary analysis is descriptive, not causal. It examines the relationship between social media usage and academic performance.

A logit regression model is estimated where the dependent variable is whether social media affects academic performance. The key explanatory variable is average daily usage hours, with controls for age, sleep, gender, and academic level.

Results indicate that higher social media usage is strongly associated with a greater likelihood of reporting negative academic impacts. However, the results should not be interpreted causally due to potential omitted variables and reverse causality.

### Econometric Specification

The following model is estimated:

affects_academic_performance = β₀ + β₁(usage) + β₂(age) + β₃(sleep) + β₄(gender) + β₅(academic level) + ε

A logit model is used due to the binary dependent variable. Control variables are included to reduce confounding and isolate the association between social media usage and academic outcomes.

### Limitations

The analysis is observational and may suffer from omitted variable bias. Factors such as personality, study habits, or time management are not observed and may influence both social media usage and academic outcomes.

Reverse causality may also be present, where students struggling academically may use social media differently.


