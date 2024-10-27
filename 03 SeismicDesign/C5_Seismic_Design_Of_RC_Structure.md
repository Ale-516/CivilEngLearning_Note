# Seismic Design of RC Structure
```mermaid
graph LR
A[introduction]-->B[damage]-->C[systems]
-->D[calculation]-->E[details]-->F[examples]
```

## Introduction
* The primary purpose of all structures used for building is to support gravity loads. However, building may also be subjected lateral forces due to wind or earthquake.
```mermaid
graph LR
A[systems]-->B[pure systems]
A-->C[dual systems]
B-->D1[frame structure]
B-->D2[shear wall structures]
C-->E1[frame-shear structure]
C-->E2[tube-in-tube structure]
C-->E3[bundled tube sturcture]
```
* **Frame Structure**
    * Frame structures make the building flexible in plane design and are commonly used in multistory RC building
    * Beams, columns, and supporting floors are continuous and meet at nodes, often called "rigid" point
* **Shear Wall Sturcture**
* **Dual Systems**
    * When RC frames interacting with RC or masonry wall together provide the necessary resistance to lateral forces, while each system carries its appropriate share of the gravity load, these types of structure sre variously known as dual, hybrid or wall-frame structures.

```mermaid
graph TB
A[structure scheme and configuration]-->B[preliminary selection of member cross sections and material]-->C[loads and representive value of gravity loads of each story]-->D[structural stiffness]-->E[natural vibration periods and modes]-->F[seismic action of minor earthquake]-->G[lateral displacement under minor earthquake]-->H[internal forces under seismic action]-->I[internal forces under vertiacal load]
G-->W[adjustment of structural scheme]-->C

```