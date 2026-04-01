**Independent Test Dataset = output.fasta**

**Processing**

This presents an end-to-end pipeline for bacterial promoter classification using a trained deep learning model. 
It processes DNA sequences from FASTA files, converts them into numerical representations, and feeds them into a CNN-based 
architecture to predict promoter classes. The workflow supports multi-class classification across several sigma factors 
and non-promoter sequences. Predictions are systematically evaluated against true labels using robust statistical metrics,
including accuracy, sensitivity, specificity, MCC, confusion matrices, and ROC analysis. Overall, the file bridges raw 
genomic data and biological interpretation by delivering reliable promoter identification with transparent and 
comprehensive performance validation.

**Results Analysis**

The results of the pre-trained model, as published, show excellent performance across various metrics, with accuracy ranging from 92.1% to 98.9%, sensitivity (Sn) from 84.6% to 94.9%, specificity (Sp) from 87.9% to 99.6%, and MCC from 0.836 to 0.885. However, when the same model was tested on an independent dataset, the results diverged significantly, indicating potential overfitting or lack of generalization to new data.

For *SIGMA24*, the accuracy dropped from 96.8% (published) to 95.5% (tested), which is a minor decrease. However, the sensitivity dropped substantially from 88.5% to 82.5%, suggesting the model struggled more to correctly identify true positives on the new dataset. The specificity remained high at 96.2%, indicating that the model was still good at identifying non-promoters, but the lower sensitivity indicates a loss in its ability to detect promoters accurately.

In *SIGMA28*, the accuracy showed an increase from 98.9% to 98.8%, which is quite consistent. However, sensitivity decreased sharply from 84.6% to 62.3%, indicating a reduction in the model's ability to identify true positives. The specificity was still impressive, rising to 99.3%, but the decreased sensitivity suggests the model may have become biased towards predicting non-promoters. The MCC also dropped from 0.875 to 0.594, showing a decline in the model's overall balanced performance.

For *SIGMA32*, the accuracy decreased from 97.9% to 96.9%, but the most concerning issue was the drastic drop in sensitivity from 87.7% to just 23.5%. This sharp decline indicates that the model failed to correctly classify a significant portion of true positives on the independent data, despite maintaining a high specificity of 99.3%. The MCC also saw a considerable drop from 0.881 to 0.339, reflecting a poor balance between precision and recall.

In *SIGMA38*, the accuracy slightly decreased from 96.5% to 96.6%, but sensitivity plummeted from 87.2% to a mere 3.7%. This drastic drop suggests the model struggled significantly to identify promoters in this class, while still maintaining a relatively high specificity of 98.3%. The MCC dropped drastically from 0.882 to 0.020, indicating that the model's performance in identifying promoters was extremely poor despite a reasonable level of specificity.

For *SIGMA70*, the accuracy dropped from 92.1% to 83.8%, and sensitivity decreased slightly from 94.9% to 82.3%. The model maintained a relatively low specificity of 84.2%, which could explain the sensitivity decline, as it may have become biased toward predicting non-promoters. The MCC decreased from 0.836 to 0.578, showing a decline in balanced performance.

Finally, *SIGMA54*, which wasn't included in the original published results, shows a concerning performance with 96.2% accuracy, 0% sensitivity, and 96.2% specificity. This indicates that the model failed to identify any true positives, resulting in poor sensitivity despite a high specificity. The MCC also being 0.000 further confirms the model's failure to generalize.

**Conclusion**

The performance on the independent dataset shows significant degradation, especially in terms of sensitivity across most sigma factors. This suggests that the model may have been overfitted to the original dataset, as it performed well in the controlled environment but struggled with the diversity and complexity of independent data. Additionally, the high specificity in some cases indicates that the model was conservative in predicting promoters, focusing on avoiding false positives but sacrificing the ability to identify true promoters. This highlights the importance of testing models on diverse, independent datasets to assess their true generalizability and robustness.

