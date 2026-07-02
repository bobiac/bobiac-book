# Spatial Statistics

In the following 3 notebooks, we will learn how to assess spatial relationships between objects. Our focus will be on **clustering** and **co-localisation**.

### Notebook Lessons
Each notebook will focus on a question:
* **Notebook 1:** Does a protein cluster?
* **Notebook 2:** Do two different protein clusters co-localize?
* **Notebook 3:** Does a protein localize to a cellular compartment?

To answer these questions, we will introduce the following concepts:
| Concept | Purpose |
|---------|---------|
| `complete spatial randomness` method | A null distribution where all object locations are randomly distributed |
| `KD-tree` | A data structure for efficient nearest neighbor search |
| `nearest neighbor` relationship | A formalism to establish spatial relationships between objects |
| `nearest neighbor distance` | A metric to quantify spatial realtionships between objects |
| `Clark-Evans index` | An index that reports whether a distribution of objects is randomly distributed |
| `Ripleys L` | A method to assess the length scale of clustering / dispersion |

### Dataset
Our data consists of fluorescence images with five channels:
| Channel | Staining | Staining Description |
|---------|---------|----------------|
| 0 | Hoechst | Nuclear stain |
| 1 | Phalloidin | F-actin stain; whole cell marker |
| 2 | Protein A | Spot pattern |
| 3 | Protein B | Spot pattern |
| 4 | Protein C | Spot pattern |



