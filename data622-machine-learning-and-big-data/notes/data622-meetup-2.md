- Assignments for the week due Sunday:
    1. Discussion 2
    2. Quiz 2

- Assignment 1:
    - EDA and an essay
    - "Answer the questions in R or Python and write a summary of your findings"
    - THERE'S A RUBRIC
    - If doing in python, put it into github or similar

- showed us a cool tool that lets you visualize 3d data
    - projector.tensorflow.org

- look at the data
    - graph it, check out the distributions, etc

- "As a data scientist, you live or die by the data"

- Statistical Probability vs Machine Learning
    - ML relies heavily on statistics (duh)
    - P(A|B) = (P(B|A)*P(A))/(P(B))
    - We glossed over this one

**The Five Tribes of Machine Learning**:
    - Symbolists
        - Approach: Use symbols, rules, and logic to represent knowledge and draw logical inference.
        - Favored Algorithm: Rules and decision trees.
    - Bayesians
        - Approach: Assess the likelihood of occurrence for probabilistic inference.
        - Favored Algorithm: Naive Bayes or Markov models.
    - Connectionists
        - Approach: Recognize and generalize patterns with weighted neurons.
        - Favored Algorithm: Neural networks.
    - Evolutionaries
        - Approach: Generate variations and assess the fitness of each.
        - Favored Algorithm: Genetic programs.
    - Analogizers
        - Approach: Optimize a function in light of constraints.
        - Favored Algorithm: Support vector machines (SVMs).

**Types of Machine Learning  - Ultimate Goal: What is the ultimate goal?**
1.  Action Selection: leads to Reinforcement learning.
    - The type of learning is Reinforcement Learning.
2.  Grouping: leads to Unsupervised learning.
    - The type of learning is Unsupervised Learning which includes Clustering, Anomaly Detection, and Dimensionality Reduction.
3.  Prediction: Can be Supervised or Semi-supervised.
    - Same output every time?
        - NO: Leads to Supervised learning which includes Generation and Annotation.
        - YES: Leads to a decision based on data labels.
            - YES (to predicting different things for different parts of data input) and NO (to a data label available for all inputs) leads to Semi-supervised learning.
            - What is a data label available for? Leads to a decision based on the source of the labels.
                - SOME INPUTS: leads to Semi-supervised learning.
                - ALL INPUTS: leads to Supervised learning.
                - OTHER DATA POINTS: leads to Self-supervised learning.
            - Type of label?
                - TRUE / FALSE: Leads to Binary classification.
                - ONE OF SEVERAL: Leads to Multi-class classification.
                - A REAL NUMBER: Leads to Regression.
                - MULTIPLE NUMBERS/SEQUENCES/TEXT (RICH FORMAT IMAGE/VIDEO): Leads to Data Transformation / Translation.