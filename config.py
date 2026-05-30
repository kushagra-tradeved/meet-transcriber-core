import os
import torch

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RECORDINGS_DIR = os.path.join(BASE_DIR, "recordings")

# Model Configuration for Ultimate Accuracy
# We use full 'large-v3' (not turbo) for deepest contextual understanding of diverse accents.
MODEL_SIZE = "large-v3"

# Hardware Ingestion Configuration
if torch.cuda.is_available():
    DEVICE = "cuda"
    COMPUTE_TYPE = "float16"  # Uses GPU Tensor cores without sacrificing accuracy
else:
    DEVICE = "cpu"
    COMPUTE_TYPE = "int8"     # Fallback optimization for system processors

# Ingestion Parameters
BEAM_SIZE = 5                 # Evaluates top 5 linguistic paths simultaneously to catch edge words
TEMPERATURE_FALLBACK = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0] # Recalculates if phrase confidence drops