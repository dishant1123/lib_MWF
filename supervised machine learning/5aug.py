"""

1. data set : salary 
2. feature selection 
3. train split 
4. feature scale  :fit_transform(),transform()
5. linear model : linear model , model.fit() .model.predict,r2score = r2(y_test,predict)
6. ridge : ridge model(alpha=1) , model.fit() .model.predict,r2score = r2(y_test,predict)\
7. lasso : lasso model(alpha=100) , model.fit() .model.predict,r2score = r2(y_test,predict)\
8. elasticnet :elasticnet model(alpha=100,l1_ratio=.5) , model.fit() .model.predict,r2score = r2(y_test,predict)

| Alpha | Effect                                        |
| ----- | --------------------------------------------- |
| 0     | No regularization (same as Linear Regression) |
| 0.001 | Very little regularization                    |
| 0.01  | Small regularization                          |
| 0.1   | Mild regularization                           |
| 1     | Default in most examples                      |
| 10    | Strong regularization                         |
| 100   | Very strong regularization                    |
| 1000  | May cause underfitting                        |

The alpha and l1_ratio values are hyperparameters, meaning there is no fixed value. They are usually chosen by cross-validation


| Model      | Recommended Value         |
| ---------- | ------------------------- |
| Ridge      | alpha=1                 	 |
| Lasso      | alpha=0.1 or alpha=1 	 |
| ElasticNet | alpha=1, l1_ratio=0.5 	 |
"""