import pandas as pd

# Create weather dataset inline (since the CSV file is missing)
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast',
                'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
                    'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal',
                 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong',
             'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes',
             'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Load into DataFrame
df = pd.DataFrame(data)

# Test instance to predict
test_instance = ['Sunny', 'Cool', 'High', 'Strong']

# Step 1: Separate data by class
def separate_by_class(data):
    separated = {}
    for _, row in data.iterrows():
        class_label = row['Play']
        features = row.drop('Play').tolist()
        if class_label not in separated:
            separated[class_label] = []
        separated[class_label].append(features)
    return separated

# Step 2: Calculate prior probabilities
def prior_prob(separated):
    total = sum(len(rows) for rows in separated.values())
    return {cls: len(rows) / total for cls, rows in separated.items()}

# Step 3: Calculate likelihood
def likelihood(feature_index, value, class_rows):
    count = sum(1 for row in class_rows if row[feature_index] == value)
    return count / len(class_rows) if len(class_rows) > 0 else 0

# Step 4: Prediction using Naive Bayes
def predict(test_instance, data):
    separated = separate_by_class(data)
    priors = prior_prob(separated)
    posteriors = {}
    for cls, rows in separated.items():
        prob = priors[cls]
        for i in range(len(test_instance)):
            prob *= likelihood(i, test_instance[i], rows)
        posteriors[cls] = prob
    prediction = max(posteriors, key=posteriors.get)
    return prediction, posteriors

# Run the prediction
prediction, probs = predict(test_instance, df)

# Output results
print("Test Instance:", test_instance)
print("Posterior Probabilities:", probs)
print("Predicted Class:", prediction)
