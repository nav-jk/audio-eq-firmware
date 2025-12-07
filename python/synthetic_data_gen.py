import numpy as np
from scipy.io.wavfile import write

# ---------- CONFIG ----------
FS = 48000          # sampling rate (Hz)
DURATION_SEC = 2.0  # length of signal in seconds
OUTPUT_WAV = "test_signal.wav"
OUTPUT_HEADER = "audio_data.h"

# Tone frequencies for testing EQ (Hz)
F_BASS   = 100.0     # should react to your low band
F_MID    = 1000.0    # should react to your mid band
F_TREBLE = 8000.0    # should react to your high band

# Relative amplitudes
A_BASS   = 0.7
A_MID    = 0.5
A_TREBLE = 0.4
A_NOISE  = 0.2       # white noise level


def main():
    num_samples = int(FS * DURATION_SEC)
    t = np.arange(num_samples, dtype=np.float32) / FS

    # --- Build test signal: bass + mid + treble + noise ---
    bass   = A_BASS   * np.sin(2.0 * np.pi * F_BASS   * t)
    mid    = A_MID    * np.sin(2.0 * np.pi * F_MID    * t)
    treble = A_TREBLE * np.sin(2.0 * np.pi * F_TREBLE * t)
    noise  = A_NOISE  * np.random.randn(num_samples).astype(np.float32)

    x = bass + mid + treble + noise

    # Normalize to -1..1 to be safe
    max_abs = np.max(np.abs(x))
    if max_abs > 0:
        x = x / max_abs

    print(f"Generated {num_samples} samples at {FS} Hz")
    print("Peak amplitude after normalization:", np.max(np.abs(x)))

    # --- Save WAV for listening on laptop ---
    pcm16 = np.int16(np.clip(x, -1.0, 1.0) * 32767)
    write(OUTPUT_WAV, FS, pcm16)
    print("Wrote WAV:", OUTPUT_WAV)

    # --- Generate audio_data.h for ESP32 ---
    with open(OUTPUT_HEADER, "w") as f:
        f.write("#pragma once\n\n")
        f.write(f"#define AUDIO_NUM_SAMPLES {num_samples}\n\n")
        f.write("static const float audio_data[AUDIO_NUM_SAMPLES] = {\n")

        # Write samples in rows for readability
        per_line = 8
        for i, s in enumerate(x):
            if i % per_line == 0:
                f.write("    ")
            f.write(f"{s:.6f}f")
            if i != num_samples - 1:
                f.write(", ")
            if (i + 1) % per_line == 0:
                f.write("\n")

        if num_samples % per_line != 0:
            f.write("\n")

        f.write("};\n")

    print("Wrote header:", OUTPUT_HEADER)
    print("Include this in your ESP32 project and use audio_data[] as input.")


if __name__ == "__main__":
    main()
