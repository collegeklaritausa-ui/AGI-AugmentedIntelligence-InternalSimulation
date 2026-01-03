# Simulated MIDI and Rhythmic Data: Ecos de la Noche Eterna

This document provides the core rhythmic and melodic data structures for the 20 tracks of the "Ecos de la Noche Eterna" album, a simulated output from the Manus 1.7 AGI entity. All data is presented in a technical format suitable for direct input into a Digital Audio Workstation (DAW).

## 1. Core Rhythmic Patterns (4-Bar Loops)

The rhythmic foundation is built on the interplay between the standard 4/4 kick and the syncopated Latin percussion.

| Track # | BPM | Kick Pattern | Hi-Hat/Shaker Pattern | Latin Percussion (Key Hits) | Clave/Groove Type |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 120 | None (Drone) | 1/4 Note Shaker (Filtered) | Bongo hit on 2.4.3, Conga on 4.1.3 | Ambient/Sub-Rhythmic |
| **5** | 122 | 4/4 (House Kick) | 1/8 Note Closed Hat (Swung) | Conga on 1.4, Bongo on 3.2 | Deep House 3-2 Clave |
| **10** | 126 | 4/4 (Techno Kick) | 1/8 Note Closed Hat (Straight) | Timbales Roll on 4.4, Cowbell on 2.2 | Peak-Time Driving |
| **15** | 125 | 4/4 (Hybrid Kick) | 1/16 Note Open Hat (Layered) | Conga on 1.1.3, 2.1.3, 3.1.3, 4.1.3 | Salsa/Triumphant |
| **16** | 124 | 4/4 (Dry Kick) | 1/4 Note Metallic Shaker | Bongo on 1.2, Conga on 2.4, Tumbao on 3.3 | Tribal/Raw |

***

## 2. Melodic and Harmonic MIDI Data

Melodic data is presented as a 4-bar MIDI sequence, detailing the note, octave, and velocity.

### Track 5: El Viaje Interior (The Inner Journey) - 122 BPM, E minor

| Element | Chord Progression (4-Bar Loop) | Bassline (Root Notes & Rhythm) | Melodic Motif (Trumpet) |
| :--- | :--- | :--- | :--- |
| **MIDI Data** | **Em7** (E3, G3, B3, D4) - **Am7** (A3, C4, E4, G4) - **D7** (D3, F#3, A3, C4) - **Gmaj7** (G3, B3, D4, F#4) | **Bar 1:** E2 (1.1, Vel 100), E2 (1.3, Vel 90) **Bar 2:** A2 (2.1.3, Vel 110), A2 (2.4, Vel 95) **Bar 3:** D2 (3.1, Vel 100), D2 (3.3, Vel 90) **Bar 4:** G2 (4.1, Vel 110), G2 (4.3.3, Vel 95) | **Bar 16:** C5 (1.1, Vel 120, Duration 1/2), B4 (1.3, Dur 1/4), A4 (1.4, Dur 1/4) **Bar 17:** G4 (2.1, Dur 1/2), F#4 (2.3, Dur 1/4), E4 (2.4, Dur 1/4) |
| **Notes** | Classic Deep House progression, played with a long release on the Pad/Rhodes. | Syncopated pattern to create a "rolling" feel, side-chained to the kick. | Melancholic, reverbed motif that appears every 16 bars. |

### Track 10: El Grito del Sol (The Sun's Cry) - 126 BPM, F# minor

| Element | Acid Bassline (TB-303 Style) | Techno Stab (Rhythmic) | Brass Section (Breakdown - 4 Bar Phrase) |
| :--- | :--- | :--- | :--- |
| **MIDI Data** | **Bar 1:** F#2 (1.1, Accented, Slide to G#2 on 1.3) **Bar 2:** C#3 (2.1, Accented, Decay Mod) **Bar 3:** B2 (3.1, Slide to A2 on 3.3) **Bar 4:** F#2 (4.1, Accent) | **Bar 1:** F#4 (1.2, Vel 127, Dur 1/16) **Bar 2:** F#4 (2.2, Vel 127, Dur 1/16) **Bar 3:** F#4 (3.2, Vel 127, Dur 1/16) **Bar 4:** F#4 (4.2, Vel 127, Dur 1/16) | **Bar 1:** F#4 (1.1, Dur 1), C#5 (2.1, Dur 1) **Bar 2:** B4 (3.1, Dur 1), A4 (4.1, Dur 1) **Bar 3:** G#4 (1.1, Dur 1), F#4 (2.1, Dur 1) **Bar 4:** E4 (3.1, Dur 1), F#4 (4.1, Dur 1) |
| **Notes** | Aggressive filter envelope, high resonance, heavy distortion. | Used as a rhythmic marker, heavily filtered and delayed. | Triumphant, heroic motif, played with a full, layered brass sound. |

### Track 15: La Ascensión (The Ascension) - 125 BPM, C major

| Element | Chord Progression (Layered Pads) | Lead Synth (Supersaw) | Choir Sample (Riser) |
| :--- | :--- | :--- | :--- |
| **MIDI Data** | **Cmaj9** (C3, E3, G3, B3, D4) - **G/B** (B2, G3, D4) - **Am7** (A2, C3, E3, G3) - **Fmaj7** (F2, A2, C3, E3) | **Bar 1:** G4 (1.1, Dur 1/2), A4 (1.3, Dur 1/2) **Bar 2:** B4 (2.1, Dur 1), G4 (3.1, Dur 1) **Bar 3:** F4 (1.1, Dur 1/2), E4 (1.3, Dur 1/2) **Bar 4:** D4 (2.1, Dur 1), C4 (3.1, Dur 1) | **Bar 64 (Build):** C3 (Sustained, Velocity 100-127 over 8 bars) |
| **Notes** | Wide, open voicings for an "Epic" feel. | Triumphant, soaring motif, introduced only at the final drop. | Used as a continuous, filtered riser over the final 64-bar build. |

***

## 3. Rhythmic Data for Remaining Tracks (Summary)

| Track # | Key Rhythmic Feature | Key Melodic Feature |
| :---: | :--- | :--- |
| **2** | Subtle 1/16th note shaker on the off-beats (2.2, 4.2). | Jazzy Rhodes chords (e.g., F#m7b5). |
| **3** | Filtered Conga loop with heavy emphasis on the 1.4. | Simple, repetitive sub-bass pattern (1/4 notes). |
| **4** | Arpeggio pattern: 1/16th notes, up-down sequence, 4 octaves. | Melancholic Trumpet motif (e.g., D5, C#5, B4). |
| **6** | Sharp, short Cowbell on every 1/4 note. | Simple, rhythmic bass pulse (1/8th notes). |
| **7** | Call-and-response: High Bongo on 1.2, Low Conga on 3.2. | Aggressive 303 line with high resonance. |
| **8** | Fast Timbales roll on the 4th beat of every bar. | Short, filtered square wave stab on the 1.1. |
| **9** | Continuous white noise riser (automation) over 8 bars. | Repetitive, hypnotic synth loop (e.g., G3, A3, B3). |
| **11** | Slow, evolving pad (Dmaj) with a 60-second attack time. | Main melodic lead is a clean, sustained synth with heavy reverb. |
| **12** | Nylon-string guitar riff (sampled) playing a simple, syncopated 1/8th note pattern. | Emotional Spanish female vocal sample (clean, upfront). |
| **13** | Complex, minor-key chord progression (e.g., Cm9, Gm7, Fmaj7). | Heavy use of ping-pong delay and shimmer reverb on all melodic elements. |
| **14** | Subtle industrial metallic hit on the 2 and 4. | Darker, more melancholic melody (e.g., D#4, C4, A#3). |
| **17** | Deep, dub-style sub-bass (1/4 notes). | Filtered vocal chants (male, low-pitched). |
| **18** | Organic percussion (shaker, wood block) with a simple, repetitive, grounding melody (flute). | Natural sound effects (waves, wind) layered into the background. |
| **19** | Groove slowly breaks down, elements drop out every 8 bars. | Focus on a single, sustained pad. Final, fading trumpet note. |
| **20** | Pure ambient outro, final echo of the sub-bass. | White noise fades to silence. |
