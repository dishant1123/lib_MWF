# decision tree :
data = {
    "Hours_Studied": [2, 3, 4, 5, 6, 1, 7, 2, 8, 3,
                      5, 6, 1, 4, 7, 8, 2, 3, 6, 5],

    "Attendance": [60, 65, 70, 75, 80, 50, 85, 55, 90, 60,
                   78, 82, 52, 72, 88, 92, 58, 63, 84, 76],

    "Result": ["Fail", "Fail", "Pass", "Pass", "Pass",
               "Fail", "Pass", "Fail", "Pass", "Fail",
               "Pass", "Pass", "Fail", "Pass", "Pass",
               "Pass", "Fail", "Fail", "Pass", "Pass"]
}

# step :1 df 
# step :2 split 
# step :3 scaler
# step :4 model 
"""
from sklearn.tree import DecisionTreeClassifier
    1. crearea ----> geini ,entropy ,log_loss
    2. max_depth ---->    for loop  
    3. ranodm_state ---->  random forest

"""
# step :5 fit  , predict 
# step :6 accuracy score
# step : 7 new  data   ----> 5.5 , 78 


