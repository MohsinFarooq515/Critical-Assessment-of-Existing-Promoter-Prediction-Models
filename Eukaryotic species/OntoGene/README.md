When testing this model on an independent dataset, we observe that all sequences are being classified as promoter sequences. This result suggests that there may be an issue with how the model is making predictions on the new data. Here's a detailed breakdown of what might be happening:

Model Output:
The model generates logits for each sequence, which represent the raw, unnormalized scores for each class (in this case, "promoter" and "non-promoter"). These logits are then passed through a softmax function, which converts them into probabilities that sum to 1. A higher value in the promoter class probability (promoter_prob) compared to the non-promoter class probability (non_promoter_prob) indicates that the model has classified the sequence as a promoter.

Problem with Prediction:
The fact that all sequences are being classified as promoters indicates that the model might have learned to overfit to predicting the "promoter" class, or it might have been trained on imbalanced data where the promoter class was dominant. As a result, the softmax probabilities for the promoter class are likely higher than the non-promoter class for every sequence, causing the model to label all instances as promoters.

Possible Causes:

Imbalanced Training Data: If the model was trained on a dataset where the majority of the sequences were promoters, it could have developed a bias towards predicting the "promoter" class more often. This imbalance can lead to the model outputting very high probabilities for the promoter class, regardless of the input sequence.

Improper Model Calibration: The model might not have been properly calibrated during training, meaning that even if the actual probabilities are low, they might be skewed towards one class due to improper weight initialization, overfitting, or other issues during fine-tuning.

Inference Issues: The model might be producing logits where the difference between the two classes (promoter vs non-promoter) is minimal. When passed through the softmax function, even small differences can lead to higher probabilities for one class over the other. This could be due to the model's architecture or the training process, which may not have been fully optimized for the independent dataset.

Inspection of Raw Logits:
Upon inspecting the raw logits before the softmax function, if the values for both classes are very close to each other, it suggests that the model has difficulty distinguishing between the two classes. This could be a sign of an ineffective decision boundary, where both classes are treated almost equally by the model, but due to slight biases, the promoter class gets the higher probability after applying softmax.