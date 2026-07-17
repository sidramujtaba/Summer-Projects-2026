# Sonic Courtyards

An interactive digital experience exploring the relationship between **traditional architecture, motion, and sound**.

Sonic Courtyards transforms cultural architectural elements into an immersive web-based environment where users interact with hanging character strings inspired by traditional structures from **China, Japan, and Uzbekistan**. Cursor movement creates physical motion and generates unique sound responses, turning architecture into a playable sonic experience.

---

## Project Concept

Traditional courtyards, temples, and silk-road architectures often use hanging ornaments, wind chimes, and layered structures to create a connection between space, movement, and sound.

This project reimagines those ideas digitally by creating:

- Architectural forms as interactive environments
- Hanging strings as responsive sound instruments
- Cultural writing systems as visual elements
- Cursor movement as a form of interaction

The goal is to explore how digital experiences can preserve cultural aesthetics while creating new forms of interaction.

---

# Features

## Interactive String Physics

- Real-time cursor-based interaction
- Responsive string movement
- Natural swinging and vibration behaviour
- Dynamic visual feedback when strings are activated

## Generative Sound System

Built using the **Web Audio API**.

Each location has its own sound identity:

### China
- Warm silk-like resonance
- Soft traditional plucked tones
- Longer harmonic decay

### Japan
- Bright koto-inspired tones
- Clearer higher-frequency response
- Shorter musical articulation

### Uzbekistan
- Deeper Silk Road inspired resonance
- Glass-like harmonic layers
- Richer echo characteristics

---

## Cultural Visual Systems

Each environment uses its own writing style:

### China

Chinese characters are used as hanging elements:
風 音 雲 山 月 天 水 心

### Japan

Japanese characters create the string patterns:
あ い う え お か さ な

### Uzbekistan

Uzbek-inspired lettering represents the Silk Road environment:
OʻZBEKISTON

---

# Technologies Used

- HTML5
- CSS3
- JavaScript
- Canvas API
- Web Audio API
- SVG Graphics
- Responsive Web Design

---

# Technical Implementation

## Canvas Rendering

The visual system uses HTML Canvas for:

- Drawing architectural elements
- Rendering hanging strings
- Animating movement
- Creating smooth transitions

## Physics Simulation

Strings use a lightweight spring-based physics model:

- Velocity
- Tension
- Damping
- Cursor interaction forces

This allows realistic movement while maintaining performance.

## Audio Generation

The project uses procedural sound generation instead of pre-recorded audio.

Sound parameters are controlled through:

- Frequency
- Harmonics
- Envelope decay
- Resonance profiles

---

# Performance Optimizations

The project includes:

- Adaptive rendering quality
- Optimized Canvas calculations
- Limited audio polyphony
- Reduced unnecessary physics calculations
- Efficient animation loops

---
