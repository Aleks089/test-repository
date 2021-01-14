#copied from course material 12.5
#https://krspiced.pythonanywhere.com/chapters/project_software_engineering/continuous_integration/continuous_integration.html
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
import pandas as pd




def train_model(X,y):
    m = DecisionTreeClassifier(max_depth=5)
    m.fit(X,y)    
    return m

if __name__ == '__main__':
    d = load_wine()
    print(d['DESCR'])
    df = pd.DataFrame(d['data'], columns=d['feature_names'])
    y = d['target']  # cultivator