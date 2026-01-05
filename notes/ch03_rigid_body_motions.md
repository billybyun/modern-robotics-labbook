# Chapter 3 — Rigid-Body Motions (WHY-first notes)

## Why this chapter exists
Robotics needs a *language* for 3D pose and motion:
- **Pose**: orientation + position
- **Motion**: angular + linear velocity
- **Composition**: chaining transforms across joints/links

## Key ideas (intuition)
### 1) Orientation is not a 3D vector
A single direction vector loses **roll** (many orientations share the same forward direction).

### 2) Rotations live on SO(3)
Rotations don’t add like vectors. Composition is multiplication.

### 3) Rigid transforms live on SE(3)
Pose combines rotation and translation into one object.

### 4) Twists are the velocity version
Twist is a 6D object describing instantaneous rigid-body motion.

## Diagrams / mental models
- (Add your sketches or screenshots here)
- (Add GIFs from notebooks in `assets/` and embed them here)

## Self-quiz
1. Give a real example where two poses share the same forward vector but are different.
2. Why does naive "vector addition" fail for composing rotations?
3. What does a twist represent physically?
