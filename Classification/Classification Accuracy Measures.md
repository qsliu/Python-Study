# Classification Accuracy Measures

**Precision**: the proportion of data points that the model correctly find "relevant cases"
$$
\text{Precision} = \frac{\#(\text{True Positive})}{\#(\text{True Positive}) + \#(\textbf{False Positive})}
$$




**Recall**: the ability to find all the relevant cases within a dataset. 
$$
\text{Recall} = \frac{\#(\text{True Positive})}{\#(\text{True Positive}) + \#(\textbf{False Negative})}
$$

* **True Positive**:  data points that model identify as positive that are actually positive.
* **False Negative**: data points that model identify as negative that are actually positive.
  * doctor declare that a patient does not have the disease, but actually he does have the disease. (this situation is not good for the patients, they may miss the best time to treat.)
* **False Positive**: data points that model identify as positive that are actually negative.
  * doctor identify a patient with some disease, but actually he does not has the disease. (the normal people may get the wrong treat of disease and cause un-necessary worries to the patients)
* **True Negative**: data points that model identify as negative that are actually negative.



For example, in preliminary disease screening of patients for follow-up examinations, we would probably want a recall near 1.0 — we want to find all patients who actually have the disease — and we can accept a low precision if the cost of the follow-up examination is not significant. 



**F1 Score**: <u>harmonic mean</u> of precision and recall.
$$
\text{F1 Score} = 2 * \frac{\text{Precision $*$ Recall}}{\text{Precision $+$ Recall}}
$$


**Fowlkes–Mallows Index**: the geometric mean of precision and recall
$$
\text{Fowlkes–Mallows Index} = \sqrt{\text{Precision $*$ Recall}}
$$


**confusion matrix**

|             |          | Actual         | Actual         |
| ----------- | -------- | -------------- | -------------- |
|             |          | Positive       | Negative       |
| **predict** | Positive | True Positive  | False Positive |
| **predict** | Negative | False Negative | True Negative  |



**Receiver Operating Characteristic (ROC) curve**



* true positive rate = $\frac{\text{true positive}}{\text{true positive + false negative}}$



- **Area under the curve (AUC):** metric to calculate the overall performance of a classification model based on area under the ROC curve
- 

A typical ROC curve is shown below:



![img](https://cdn-images-1.medium.com/max/1200/0*2iHR8dFXev5GWo_f.png)

Receiver Operating Characteristic Curve ([Source](http://www.statisticshowto.com/c-statistic/))

The black diagonal line indicates a random classifier and the red and blue curves show two different classification models. For a given model, we can only stay on one curve, but we can move along the curve by adjusting our threshold for classifying a positive case. Generally, as we decrease the threshold, we move to the right and upwards along the curve. With a threshold of 1.0, we would be in the lower left of the graph because we identify no data points as positives leading to no *true positives* and no *false positives* (TPR = FPR = 0). As we decrease the threshold, we identify more data points as positive, leading to more true positives, but also more false positives (the TPR and FPR increase). Eventually, at a threshold of 0.0 we identify all data points as positive and find ourselves in the upper right corner of the ROC curve (TPR = FPR = 1.0).

Finally, we can quantify a model’s ROC curve by calculating the total [Area Under the Curve (AUC)](https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve), a metric which falls between 0 and 1 with a higher number indicating better classification performance. In the graph above, the AUC for the blue curve will be greater than that for the red curve, meaning the blue model is better at achieving a blend of precision and recall. A random classifier (the black line) achieves an AUC of 0.5.





----

Reference

https://towardsdatascience.com/beyond-accuracy-precision-and-recall-3da06bea9f6c

