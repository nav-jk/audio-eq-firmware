import numpy as np
from scipy.io.wavfile import write
from tqdm import tqdm

INPUT_TEXT_FILE = "filtered_raw.txt"
OUTPUT_WAV_FILE = "filtered.wav"
FS = 48000  # must match your ESP fs

def extract_samples(path):
    samples = []
    with open(path, "r", errors="ignore") as f:
        for line in tqdm(f, desc="Parsing"):
            line = line.strip()
            # only care about lines like: "S 0.5623977"
            if not line.startswith("S "):
                continue
            parts = line.split()
            if len(parts) != 2:
                continue
            try:
                val = float(parts[1])
            except ValueError:
                continue
            samples.append(val)
    return np.array(samples, dtype=np.float32)

def main():
    data = extract_samples(INPUT_TEXT_FILE)
    print("\nLoaded", len(data), "samples")

    if len(data) == 0:
        print("No samples found — check your log file or prefix.")
        return

    # Optional: normalize to avoid clipping
    max_abs = np.max(np.abs(data))
    print("Peak amplitude:", max_abs)
    if max_abs > 1.0:
        print("Normalizing...")
        data = data / max_abs

    # Convert to 16-bit PCM
    pcm = np.int16(np.clip(data, -1.0, 1.0) * 32767)

    write(OUTPUT_WAV_FILE, FS, pcm)
    print("Wrote:", OUTPUT_WAV_FILE)

if __name__ == "__main__":
    main()
