
# iPro-Wael Model Evaluation

### Model Overview
The **iPro-Wael** model is primarily designed and trained for **protein sequences**. The model was tested on **promoter sequences** to evaluate its performance outside its intended use case. Below are the results and observations from the tests performed on the **promoter sequences**.

### Mandatory Information
- **Model Objective**: iPro-Wael is built to predict properties from protein sequences.
- **Tested Sequence**: Promoter sequences were used for testing, but the model's original training was on protein sequences. The results should be viewed with caution as the model was not specifically trained for promoter sequences.

### Model Testing Results

1. **Dataset Information**:
   - **B. subtilis** dataset: Total sequences analyzed.
   - **E. coli** dataset: Total sequences analyzed.

2. **Model Performance Comparison**:
   - The **iPro-Wael model** was evaluated using two machine learning models:
     - **CNN (Convolutional Neural Network)**
     - **Random Forest (RF)**

   The results include predictions for each dataset (B. subtilis, E. coli) showing the number of positive and negative predictions, as well as the mean and standard deviation of probabilities.

   #### CNN Model Results
   ```
   Organism      Pos_Pred    Neg_Pred    Mean_Prob    Std_Prob
   -------------------------------------------------------------
   B. subtilis   225         511         0.4874       0.0290
   E. coli       6389        11663       0.4907       0.0294
   ```

   #### Random Forest Model Results
   ```
   Organism      Pos_Pred    Neg_Pred    Mean_Prob    Std_Prob
   -------------------------------------------------------------
   B. subtilis   225         511         0.4874       0.0290
   E. coli       6389        11663       0.4907       0.0294
   ```

3. **Promoter Region Classification**:
   - The **CNN model** classified a sequence as a **promoter region** if the prediction value (CNN_Class) equals **1**, and as a **non-promoter region** if the prediction value equals **0**.

4. **Results Summary**:
   - The model did not perform significantly better or worse on **promoter sequences** compared to its performance on the **protein sequences**. However, since the model was not trained for promoters, the results should be interpreted with caution.

5. **Conclusion**:
   - While the iPro-Wael model performed reasonably well, it is clear that its accuracy and reliability are likely lower when applied to sequences outside its original training scope. Additional fine-tuning or retraining with promoter-specific data may improve performance.

### Instructions for Use
1. **Dependencies**:
   - Keras
   - PyTorch
   - NumPy
   - Joblib
   - TensorFlow
   - Custom dataset files: `index_promoters.txt`, `word2vec_promoters.txt`

2. **Running the Model**:
   - Follow the steps in the notebook to load the pre-trained models and input your own datasets for testing.
   - Use the provided functions to load and test promoter sequences using both the CNN and Random Forest models.
