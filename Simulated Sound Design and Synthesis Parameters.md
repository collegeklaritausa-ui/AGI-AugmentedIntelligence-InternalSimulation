# Simulated Sound Design and Synthesis Parameters

This document details the precise synthesis parameters and sound design patches required to realize the **Epic Deep Latino Techno-House** sound of "Ecos de la Noche Eterna." Parameters are specified for a generic, high-quality virtual analog or wavetable synthesizer (e.g., Serum, Massive, Diva, or similar).

## 1. Deep House / Epic Pads (Tracks 5, 11, 15)

The pads are the primary source of the "Deep" and "Epic" atmosphere, characterized by long, evolving textures and wide stereo fields.

| Parameter | "Neblina Pad" (Track 4) | "Ascension Pad" (Track 15) |
| :--- | :--- | :--- |
| **Oscillator 1** | Saw Wave, Detune +7 cents | Saw Wave, Detune +12 cents, Unison 7 voices |
| **Oscillator 2** | Triangle Wave, -1 Octave | Square Wave, -1 Octave, Detune -12 cents |
| **Filter** | Low-Pass (24dB/oct), Cutoff 1.5 kHz, Resonance 10% | Band-Pass (12dB/oct), Cutoff 800 Hz, Resonance 30% |
| **Filter Envelope** | Attack 1.5s, Decay 5s, Sustain 80%, Release 3s | Attack 2.0s, Decay 8s, Sustain 100%, Release 5s |
| **LFO 1 (Filter)** | Rate 1/4, Depth 20%, modulating Filter Cutoff | Rate 1/8 (Sync), Depth 40%, modulating Filter Cutoff and Pan |
| **Effects Chain** | Chorus (Wide, 50%), Reverb (Hall, Decay 4s, Wet 30%) | Phaser (Slow Rate), Delay (Ping-Pong, 1/4 Sync), Reverb (Shimmer, Decay 6s, Wet 40%) |
| **Purpose** | Melancholic, airy, and evolving texture. | Massive, triumphant, and wide stereo field. |

***

## 2. Techno Basslines (Tracks 6, 7, 10)

The basslines provide the driving force, characterized by sub-frequency focus and aggressive mid-range harmonics.

| Parameter | "Moog Sub Bass" (Track 5) | "Acid 303 Clone" (Track 7) | "Techno Saw Bass" (Track 10) |
| :--- | :--- | :--- | :--- |
| **Oscillator 1** | Sine Wave, -2 Octave | Saw Wave | Saw Wave, -1 Octave, Unison 3 voices |
| **Oscillator 2** | None | Square Wave, +1 Octave, Sync On | Square Wave, -1 Octave, Detune -5 cents |
| **Filter** | Low-Pass (12dB/oct), Cutoff 150 Hz | Low-Pass (18dB/oct), High Resonance (80%) | Low-Pass (24dB/oct), Cutoff 250 Hz |
| **Filter Envelope** | Attack 0ms, Decay 200ms, Sustain 0%, Release 50ms | Attack 0ms, Decay 100ms, Sustain 0%, Release 10ms | Attack 0ms, Decay 300ms, Sustain 0%, Release 50ms |
| **LFO 1 (Filter)** | None | Rate 1/16, Depth 10%, modulating Filter Cutoff | Rate 1/4, Depth 5%, modulating Pitch (Subtle wobble) |
| **Effects Chain** | Subtle Saturation (Tube), Hard Clipper | Distortion (Heavy), Delay (Short, Slapback) | Overdrive (Mid-range focus), Sidechain Compression (Heavy) |
| **Purpose** | Deep, felt sub-frequency anchor. | Aggressive, squelching rhythmic lead. | Punchy, driving, and harmonically rich. |

***

## 3. Melodic Leads and Organic Samples (Tracks 4, 12, 15)

The melodic elements bridge the synthetic and organic worlds, providing the "Latino" flavor and the "Epic" motif.

| Element | "Melancholic Trumpet" (Track 4) | "Supersaw Lead" (Track 15) | "Nylon Guitar Riff" (Track 12) |
| :--- | :--- | :--- | :--- |
| **Source** | Sample (Muted Trumpet) | Virtual Analog Synth | Sample (Nylon String Guitar) |
| **Processing** | **Reverb:** Large Hall, Decay 5s, Pre-Delay 50ms. **EQ:** High-Pass 200 Hz, Boost 3 kHz. | **Unison:** 9 voices, Detune 20 cents. **Filter:** High-Pass 400 Hz. **FX:** Hyper/Dimension (Wide), Delay (1/8 Sync). | **EQ:** Mid-Scoop (500 Hz). **FX:** Short Plate Reverb (Wet 15%), Subtle Chorus. |
| **Envelope** | Volume: Attack 50ms, Release 500ms | Volume: Attack 0ms, Decay 1s, Sustain 50%, Release 500ms | Volume: Attack 0ms, Decay 300ms, Sustain 0%, Release 100ms |
| **Purpose** | Ethereal, distant, and emotional hook. | Triumphant, soaring, and cuts through the mix. | Warm, rhythmic, and authentic Latin texture. |

***

## 4. Percussion Processing (Tracks 1, 10, 16)

The rhythmic complexity is achieved through meticulous layering and processing of the percussion elements.

| Element | Processing Chain | Purpose |
| :--- | :--- | :--- |
| **Kick Drum (Techno)** | **EQ:** Sub-Boost (50 Hz), Mid-Scoop (300 Hz). **Transient Shaper:** High Attack. **Clipper:** Gentle clipping for loudness. | Maximum punch and low-end clarity, minimal tail. |
| **Bongos/Congas (Raw)** | **EQ:** High-Pass 80 Hz. **Compression:** Fast Attack, Medium Release (Ratio 4:1) to control transients. **Reverb:** Short Room (Wet 10%) for space. | To sound raw, woody, and present, mimicking a live recording. |
| **Timbales/Cowbell (Peak)** | **EQ:** Aggressive High-Pass 150 Hz, Boost 5 kHz. **Saturation:** Heavy Tape Saturation for grit. **Delay:** Short 1/16th note delay throw. | To cut through the mix and provide high-frequency rhythmic energy. |
| **Shakers/Hi-Hats** | **EQ:** High-Pass 500 Hz. **Compression:** Parallel Compression (New York style) for density. **Panning:** Automated panning (LFO) for stereo movement. | To create a wide, continuous, and shimmering rhythmic layer. |
