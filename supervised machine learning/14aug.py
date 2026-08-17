"""
step:1 read csv 
step:2 features engineering   x = df['Study_Hours','Attendance'] y=df['Result']
        replace : pass 1 fail 0
        map : pass 1 fail 0
step :3 split : 80% train 20% test 
step :4 scale : scaler = StandardScaler() --->  fit ,transform 
step :5 model :  from  skelarn.neighbors import KNeighborsClassifier 
        knn = KNeighborsClassifier(n_neighbors=3)
        
step:6 fit : knn.fit(scale)
step:7 predict : knn.predict(scale)
step:8 accuracy : accuracy_score(y_test,y_pred)
"""
