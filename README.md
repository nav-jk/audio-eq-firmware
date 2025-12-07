```markdown
# audio-eq-firmware

## Introduction
`audio-eq-firmware` is a firmware project designed to run a **real-time audio equalizer** on the **ESP32** platform. It provides low, mid, and high-band audio processing with configurable gain curves and **DSP-grade filter design** suitable for embedded audio applications.

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Dependencies](#dependencies)
- [Building / Installation](#building--installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Features
* **Real-time audio equalization** on ESP32 hardware.
* **Low, mid, and high frequency bands** for audio shaping.
* Configurable **gain curves** for custom audio profiles.
* **DSP-quality filter design** optimized for embedded performance.
* Implemented in **C and Assembly** with **CMake-based** build system.

---

## Repository Structure
```

/
├── .vscode/    \# VSCode workspace settings
├── build/      \# Build scripts / output directory
├── esp32/      \# ESP32 firmware source (C, ASM, linker scripts)
├── python/     \# Python utility scripts (optional)
├── LICENSE     \# MIT license
└── README.md   \# Project documentation

````

---

## Dependencies
* **ESP32 toolchain / ESP-IDF** or compatible SDK
* **CMake**
* **GNU Make** or **Ninja**
* Standard compiler toolchain (gcc, ld, etc.)
* **Python** (optional)

---

## Building / Installation

> ⚠️ Ensure you have the **ESP32 toolchain** installed and configured in your environment.

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/nav-jk/audio-eq-firmware.git](https://github.com/nav-jk/audio-eq-firmware.git)
    cd audio-eq-firmware
    ```
2.  **Create a build directory**
    ```bash
    mkdir build
    cd build
    ```
3.  **Run CMake**
    ```bash
    cmake ../esp32
    ```
4.  **Compile the firmware**
    ```bash
    make
    ```
5.  **Flash to ESP32**
    Use your preferred flashing tool (`idf.py`, `esptool.py`, etc.):
    ```bash
    idf.py flash
    ```

---

## Usage
Once flashed, the firmware processes **incoming audio** and outputs **equalized audio** based on the configured filter parameters and gain settings.

Connect the ESP32 to your audio input/output chain and reboot the device to apply the current configuration.

---

## Configuration
* Filter coefficients, gain values, and band settings can be modified in the firmware source located in the `esp32/` directory.
* If the `python/` folder contains coefficient-generation scripts, **run them before building** to update DSP parameters.
* **Adjust gain carefully** to avoid distortion or clipping.

---


---

## License
This project is distributed under the **MIT License**. See `LICENSE` for details.
````