import os
import numpy as np
import torch
import torch.nn as nn
from keras.layers.convolutional import Conv2D


def word_embedding(filename, index, word2vec):
    f = open(filename, 'r')
    sequence = []
    for line in f.readlines():
        if line[0] != ' ' and line[0] != '>':
            sequence.append(line.strip('\n'))

    k = 5
    kmer_list = []
    for number in range(len(sequence)):
        seq = []
        for i in range(len(sequence[number]) - k + 1):
            ind = index.index(sequence[number][i:i + k])
            seq.append(ind)
        kmer_list.append(seq)

    feature_word2vec = []
    for number in range(len(kmer_list)):
        feature_seq = []
        for i in range(len(kmer_list[number])):
            kmer_index = kmer_list[number][i]
            for j in word2vec[kmer_index].tolist():
                feature_seq.append(j)

        feature_seq_tensor = torch.Tensor(feature_seq)
        feature_seq_tensor = torch.unsqueeze(feature_seq_tensor, 0)
        feature_seq_tensor = torch.unsqueeze(feature_seq_tensor, 0)
        feature_seq_tensor_avg = nn.AdaptiveAvgPool1d(1000 * 8)(feature_seq_tensor)

        feature_seq_numpy = feature_seq_tensor_avg.numpy()
        feature_seq_numpy = np.squeeze(feature_seq_numpy)
        feature_word2vec.append(feature_seq_numpy.tolist())

    return feature_word2vec


# =====================================================
# CUSTOM INPUT FOR INDEPENDENT DATASET (HUMAN)
# =====================================================

# INPUT FASTA (your generated 300 bp windows)
filename = "iPro-WAEL/data/Human/promoter/test/test.fasta"

# LOAD INDEX + WORD2VEC
with open("index_promoters.txt", "r") as f:
    index = f.read().strip().split(" ")

word2vec = np.loadtxt("word2vec_promoters.txt")

# FEATURE EXTRACTION
feature_word2vec = word_embedding(filename, index, word2vec)
feature_word2vec = np.array(feature_word2vec)

print("Feature shape:", feature_word2vec.shape)

# SAVE FEATURES
os.makedirs("data/Human/promoter/features", exist_ok=True)
np.savetxt(
    "data/Human/promoter/features/word2vec_test.txt",
    feature_word2vec
)
