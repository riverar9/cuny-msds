- Taking a look at lazy learners
    - Called a lazy learner because it's not "learning" anything. There's no training data and no training of the model. We're just creating a state space and then measuring distance.
    - KNN - look at a new piece of data and categorize it based on it's neighbors. Simple, powerful, and commonly used.
        - Netflix uses it to create a starting point of what to recommend you based on rudimentary info (geo, time, etc).
        - Very useful for the "cold start" problem where you don't have any training data
        - Always use an odd number for k so there's always a tie
        - When chosing k, use the sqrt(N) where N = number of data points.
            - When K is too small, it's sensitive to noise
            - When K is too large, the "neighborhood" in search is too high
        - The calculation is computationally expensive as you must use the entire dataset to calculate which are the nearest K learners
    - When computing distance 

## Principal Component Analysis (PCA)
    - A dimension reduction technique based on maximum variance in data
    - We're looking for the axis where the greatest variance is across the space of the data
    - Then we will pick an orthogonal axis which also maximizes variance across the data
        - IE, in a 3d space we find a 2d space which has the highest variance
    - PCA is useful to help visualize data

## Linear Discriminant Analysis (LDA)
    - A slightly different approach of dimensionality reduction
    - useful for classification
    - LDA looks at the greatest variance for each class.
        - LDA wants to look at the means in a class and maximize the distance between the means of the two classes.
        - LDA also wants to mimize the variation (spread) within each class
    - "PCA doesn't care about the classes, LDA cares"

## PCA vs LDA

| | PCA | LDA |
| :--- | :--- | :--- |
| **Transformation** | Linear | Linear |
| **Supervised vs Unsupervised** | Un-supervised | Supervised |
| **Objective** | Capture variability by finding principal components | Separate classes by identifying a lower dimension which has better discriminatory power |
| **Type** | Component: maximize the variance in the data | Discriminant: maximize the separation between classes |
| **Compute requirements** | Low | High |
| **Use-cases** | Visualization (and classification) | Any classification |

---

### **PCA: component axes that maximize the variance**

### **LDA: maximizing the component axes for class-separation**

## The Curse of Dimensionality
- "As dimensions increase, the data we need to generalize grows exponentially"
- It's an issue as the amount of data needed for good coverage (to avoid sparse data) increases exponentially
    - If we need 5 datapoints per feature, then 3 features will need 5^3=125 total datapoints.
    - Data need grows at an exponential rate
    - feature reduction and feature engineering helps reduce the number of features to simplify the model and increase coverage
- Remove columns, perform dimensionality reduction, do what you can to remove extra data

- For assignment 1, we want to dedupe, investigate, and potentially perform dimensionality reduction