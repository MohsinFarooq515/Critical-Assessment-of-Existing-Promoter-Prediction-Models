The Promote-Predictor model was considered for testing on an independent dataset. However, the model relies on a fixed set of 727 handcrafted features that cannot be generated from raw FASTA sequences without reproducing the exact feature extraction pipeline used by the authors.

In the provided implementation, the extractor.jar is tightly coupled to the original dataset through hard-coded headers, and the feature extraction methodology is not sufficiently documented. Additionally, the Java implementation lacks modularity and does not support direct processing of raw FASTA sequences.

Consequently, without reconstructing the complete feature extraction pipeline, any attempt to generate predictions would be scientifically unreliable. This represents a critical reproducibility limitation, significantly restricting the model’s applicability for independent validation and comparative analysis.

**This is a fundamental reproducibility limitation, not merely an implementation issue.**
