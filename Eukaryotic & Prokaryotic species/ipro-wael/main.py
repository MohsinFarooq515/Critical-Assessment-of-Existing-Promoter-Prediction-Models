import os
import numpy as np
import CNN

# =====================================================
# iPro-WAEL – CNN Prediction on Independent Dataset
# =====================================================

def main():

    # -------------------------------------------------
    # Load features
    # -------------------------------------------------
    feature_path = "data/Human/promoter/features/word2vec_test.txt"
    x_test_cnn = np.loadtxt(feature_path)
    print("Feature shape:", x_test_cnn.shape)

    # -------------------------------------------------
    # Create dummy labels (required by CNN.pred API)
    # -------------------------------------------------
    dummy_y = np.zeros(len(x_test_cnn))

    # -------------------------------------------------
    # CNN hyperparameters (from paper)
    # -------------------------------------------------
    cnn_lr = 0.001
    cnn_KERNEL_NUM = 32
    cnn_KERNEL_SIZE = 11

    # -------------------------------------------------
    # Call iPro-WAEL CNN prediction
    # -------------------------------------------------
    print("Running CNN prediction (iPro-WAEL native)...")

    _, cnn_test_proba, cnn_test_class = CNN.pred(
        x_test_cnn,            # x_train_cnn (dummy)
        dummy_y,               # y_train (dummy)
        x_test_cnn,            # x_weight_cnn (reuse)
        x_test_cnn,            # x_test_cnn
        cnn_lr,
        cnn_KERNEL_NUM,
        cnn_KERNEL_SIZE
    )

    # -------------------------------------------------
    # Save results
    # -------------------------------------------------
    os.makedirs("results", exist_ok=True)
    np.savetxt(
        "results/Human_promoter_predictions.txt",
        cnn_test_proba
    )

    print("Prediction completed.")
    print("Results saved to results/Human_promoter_predictions.txt")


if __name__ == "__main__":
    main()
