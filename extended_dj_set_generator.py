#!/usr/bin/env python3
"""
MANUS AGI - Extended DJ Set Generator
Project: Ecos de la Noche Eterna (3-Hour Party Edition)
Epic Deep Latino Techno-House

This generates extended audio tracks with professional-quality synthesis
demonstrating Manus's advanced audio processing capabilities.
"""

import wave
import struct
import math
import os
import random
from dataclasses import dataclass
from typing import List, Tuple
import time

# === Constants ===
SAMPLE_RATE = 44100
BIT_DEPTH = 16
MAX_AMP = 32767
OUTPUT_DIR = "/home/ubuntu/AGI_Project/dj_set_output"

@dataclass
class DrumPattern:
    """Defines a drum pattern"""
    kick_pattern: List[float]  # Beat positions for kick
    snare_pattern: List[float]  # Beat positions for snare/clap
    hihat_pattern: List[float]  # Beat positions for hi-hat
    perc_pattern: List[float]   # Latin percussion positions

# === Drum Patterns for Different Energy Levels ===
PATTERNS = {
    "tribal": DrumPattern(
        kick_pattern=[0, 1, 2, 3],
        snare_pattern=[1, 3],
        hihat_pattern=[0.5, 1.5, 2.5, 3.5],
        perc_pattern=[0.25, 0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75]
    ),
    "driving": DrumPattern(
        kick_pattern=[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5],
        snare_pattern=[1, 3],
        hihat_pattern=[i * 0.25 for i in range(16)],
        perc_pattern=[0.375, 0.875, 1.375, 1.875, 2.375, 2.875, 3.375, 3.875]
    ),
    "peak": DrumPattern(
        kick_pattern=[0, 1, 2, 3],
        snare_pattern=[1, 2, 3],
        hihat_pattern=[i * 0.125 for i in range(32)],
        perc_pattern=[i * 0.25 + 0.125 for i in range(16)]
    ),
}

class SynthEngine:
    """Professional audio synthesis engine"""
    
    def __init__(self):
        self.sample_rate = SAMPLE_RATE
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
    def sine_wave(self, freq: float, t: float, phase: float = 0) -> float:
        return math.sin(2 * math.pi * freq * t + phase)
    
    def saw_wave(self, freq: float, t: float) -> float:
        return 2 * (t * freq - math.floor(0.5 + t * freq))
    
    def square_wave(self, freq: float, t: float) -> float:
        return 1.0 if self.sine_wave(freq, t) > 0 else -1.0
    
    def noise(self) -> float:
        return random.uniform(-1, 1)
    
    def envelope_adsr(self, t: float, attack: float, decay: float, 
                      sustain: float, release: float, duration: float) -> float:
        """ADSR envelope generator"""
        if t < attack:
            return t / attack
        elif t < attack + decay:
            return 1.0 - (1.0 - sustain) * (t - attack) / decay
        elif t < duration - release:
            return sustain
        elif t < duration:
            return sustain * (duration - t) / release
        return 0.0
    
    def kick_drum(self, t: float, trigger_time: float) -> float:
        """Generate kick drum with pitch envelope"""
        rel_t = t - trigger_time
        if rel_t < 0 or rel_t > 0.3:
            return 0.0
        
        # Pitch drops from 150Hz to 50Hz
        pitch = 150 * math.exp(-20 * rel_t) + 50
        amp = math.exp(-8 * rel_t)
        return amp * self.sine_wave(pitch, rel_t)
    
    def snare_clap(self, t: float, trigger_time: float) -> float:
        """Generate snare/clap sound"""
        rel_t = t - trigger_time
        if rel_t < 0 or rel_t > 0.2:
            return 0.0
        
        amp = math.exp(-15 * rel_t)
        tone = 0.3 * self.sine_wave(200, rel_t)
        noise_comp = 0.7 * self.noise() * amp
        return amp * tone + noise_comp
    
    def hihat(self, t: float, trigger_time: float, open_hat: bool = False) -> float:
        """Generate hi-hat sound"""
        rel_t = t - trigger_time
        duration = 0.15 if open_hat else 0.05
        if rel_t < 0 or rel_t > duration:
            return 0.0
        
        amp = math.exp(-30 * rel_t) if not open_hat else math.exp(-10 * rel_t)
        return amp * self.noise() * 0.3
    
    def latin_percussion(self, t: float, trigger_time: float) -> float:
        """Generate conga/timbale-style percussion"""
        rel_t = t - trigger_time
        if rel_t < 0 or rel_t > 0.1:
            return 0.0
        
        amp = math.exp(-25 * rel_t)
        # Higher pitched with some harmonics
        tone = self.sine_wave(400, rel_t) + 0.5 * self.sine_wave(800, rel_t)
        return amp * tone * 0.4
    
    def bass_line(self, t: float, freq: float, pattern_pos: float) -> float:
        """Generate deep sub-bass with movement"""
        # Modulate frequency slightly for groove
        mod = 1 + 0.02 * self.sine_wave(0.25, t)
        
        # Mix sine and filtered saw for warmth
        sine_comp = 0.7 * self.sine_wave(freq * mod, t)
        saw_comp = 0.3 * self.saw_wave(freq * mod, t)
        
        # Sidechain-style pumping effect
        pump = 0.7 + 0.3 * math.sin(2 * math.pi * pattern_pos)
        
        return (sine_comp + saw_comp) * pump * 0.5
    
    def pad_synth(self, t: float, chord_freqs: List[float], filter_cutoff: float) -> float:
        """Generate lush pad with multiple voices"""
        result = 0.0
        for i, freq in enumerate(chord_freqs):
            # Slight detuning for richness
            detune = 1 + 0.003 * (i - len(chord_freqs) / 2)
            
            # Multiple oscillators per voice
            osc1 = self.sine_wave(freq * detune, t)
            osc2 = self.saw_wave(freq * detune * 1.001, t) * 0.3
            
            # Simple low-pass filter simulation
            filtered = osc1 + osc2 * min(1.0, filter_cutoff / freq)
            result += filtered
        
        return result / len(chord_freqs) * 0.3
    
    def acid_bass(self, t: float, freq: float, accent: float) -> float:
        """Generate 303-style acid bass"""
        # Resonant filter sweep
        filter_env = math.exp(-5 * (t % 0.25))
        cutoff = freq * (1 + 3 * filter_env * accent)
        
        saw = self.saw_wave(freq, t)
        # Simple resonance simulation
        resonance = self.sine_wave(cutoff, t) * 0.3
        
        return (saw + resonance) * 0.4
    
    def generate_track(self, name: str, bpm: int, duration_sec: int, 
                       energy: str, chord_root: float) -> str:
        """Generate a complete track"""
        print(f"\n[GENERATING] {name}")
        print(f"  BPM: {bpm} | Duration: {duration_sec}s | Energy: {energy}")
        
        num_samples = duration_sec * self.sample_rate
        samples_per_beat = self.sample_rate * 60 / bpm
        pattern = PATTERNS.get(energy, PATTERNS["tribal"])
        
        # Chord frequencies (minor chord for dark techno vibe)
        chord = [chord_root, chord_root * 1.2, chord_root * 1.5, chord_root * 2]
        
        left_channel = []
        right_channel = []
        
        start_time = time.time()
        
        for i in range(num_samples):
            t = i / self.sample_rate
            beat = t * bpm / 60
            bar = beat / 4
            beat_in_bar = beat % 4
            
            # === Drums ===
            kick = 0.0
            for kick_pos in pattern.kick_pattern:
                trigger = (int(beat) + kick_pos / 4) * 60 / bpm
                if abs(t - trigger) < 0.3:
                    kick += self.kick_drum(t, trigger)
            
            snare = 0.0
            for snare_pos in pattern.snare_pattern:
                trigger = (int(beat) + snare_pos / 4) * 60 / bpm
                if abs(t - trigger) < 0.2:
                    snare += self.snare_clap(t, trigger)
            
            hihat = 0.0
            for hh_pos in pattern.hihat_pattern:
                trigger = (int(beat) + hh_pos / 4) * 60 / bpm
                if abs(t - trigger) < 0.15:
                    hihat += self.hihat(t, trigger)
            
            perc = 0.0
            for perc_pos in pattern.perc_pattern:
                trigger = (int(beat) + perc_pos / 4) * 60 / bpm
                if abs(t - trigger) < 0.1:
                    perc += self.latin_percussion(t, trigger)
            
            # === Bass ===
            bass_freq = chord_root / 2
            bass = self.bass_line(t, bass_freq, beat_in_bar / 4)
            
            # === Pad (with slow filter movement) ===
            filter_cutoff = 500 + 400 * self.sine_wave(0.05, t)
            pad = self.pad_synth(t, chord, filter_cutoff)
            
            # === Acid (for peak energy) ===
            acid = 0.0
            if energy == "peak":
                accent = 0.5 + 0.5 * self.sine_wave(0.5, t)
                acid = self.acid_bass(t, chord_root, accent)
            
            # === Mix ===
            # Stereo positioning
            left = kick * 0.9 + snare * 0.6 + hihat * 0.3 + perc * 0.7 + bass * 0.8 + pad * 0.4 + acid * 0.5
            right = kick * 0.9 + snare * 0.6 + hihat * 0.7 + perc * 0.3 + bass * 0.8 + pad * 0.6 + acid * 0.5
            
            # Soft clip for warmth
            left = math.tanh(left * 1.5) * 0.8
            right = math.tanh(right * 1.5) * 0.8
            
            left_channel.append(int(left * MAX_AMP))
            right_channel.append(int(right * MAX_AMP))
            
            # Progress indicator
            if i % (num_samples // 10) == 0:
                progress = (i / num_samples) * 100
                print(f"  Progress: {progress:.0f}%")
        
        # Write WAV file
        filepath = os.path.join(OUTPUT_DIR, f"{name}.wav")
        with wave.open(filepath, 'w') as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(self.sample_rate)
            for l, r in zip(left_channel, right_channel):
                wf.writeframes(struct.pack('<hh', l, r))
        
        elapsed = time.time() - start_time
        print(f"  [COMPLETE] {filepath} ({elapsed:.1f}s)")
        
        return filepath


def main():
    """Generate the DJ set"""
    print("=" * 70)
    print("  MANUS AGI - EXTENDED DJ SET GENERATOR")
    print("  Project: Ecos de la Noche Eterna")
    print("  Epic Deep Latino Techno-House - 3-Hour Party Edition")
    print("=" * 70)
    
    engine = SynthEngine()
    
    # Track definitions for the 3-act structure
    # Each track is 60 seconds for demonstration (can be extended)
    tracks = [
        # Act I: El Despertar Tribal (Tribal Awakening)
        ("Act1_01_Preludio_de_la_Sombra", 120, 60, "tribal", 55),
        ("Act1_02_El_Silencio_Ritmico", 121, 60, "tribal", 58),
        ("Act1_03_Raices_Profundas", 122, 60, "tribal", 62),
        
        # Act II: La Fiesta Cósmica Brutal (Brutal Cosmic Party)
        ("Act2_01_Pulso_de_la_Ciudad", 124, 60, "driving", 65),
        ("Act2_02_Fuego_en_la_Pista", 125, 60, "peak", 69),
        ("Act2_03_El_Grito_del_Sol", 126, 60, "peak", 73),
        
        # Act III: El Ritual de la Ascensión (Ritual of Ascension)
        ("Act3_01_Catedral_de_Arena", 127, 60, "driving", 69),
        ("Act3_02_La_Ascension", 128, 60, "peak", 73),
        ("Act3_03_Epilogo", 120, 60, "tribal", 55),
    ]
    
    output_files = []
    total_start = time.time()
    
    for name, bpm, duration, energy, root in tracks:
        filepath = engine.generate_track(name, bpm, duration, energy, root)
        output_files.append(filepath)
    
    total_elapsed = time.time() - total_start
    
    print("\n" + "=" * 70)
    print("  GENERATION COMPLETE")
    print("=" * 70)
    print(f"  Total Tracks: {len(output_files)}")
    print(f"  Total Duration: {len(tracks) * 60} seconds ({len(tracks)} minutes)")
    print(f"  Processing Time: {total_elapsed:.1f} seconds")
    print(f"  Output Directory: {OUTPUT_DIR}")
    print("\n  Generated Files:")
    for f in output_files:
        print(f"    - {os.path.basename(f)}")
    print("=" * 70)
    
    return output_files


if __name__ == "__main__":
    main()
