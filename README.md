# **Cantilever Retaining Wall Analysis**

This project demonstrates the structural analysis of a **Cantilever Retaining Wall** using the **OpenSeesPy** library. The script defines a 2D plane strain model with triangular elements, simulates static loads, and outputs the displacements for the nodes.

## **Project Overview**

This script models and analyzes a cantilever retaining wall under specific load conditions. The key steps include:

1. **Model Initialization**:

   - Clearing previous models and defining a 2D space with two degrees of freedom (DOF) per node.

2. **Node and Element Definitions**:

   - Nodes and triangular elements (`Tri31`) are defined for the plane strain model.

3. **Boundary Conditions**:

   - Supports are set to restrict translational motion based on the design.

4. **Material Properties**:

   - An **elastic isotropic material** with defined modulus of elasticity and Poisson’s ratio.

5. **Loading Conditions**:

   - Static loads are applied at specific nodes to simulate external forces.

6. **Static Analysis**:
   - A linear static analysis is performed, and nodal displacements are extracted.

## **Files and Requirements**

### **Files**

- **`main.py`**: Python script containing the OpenSeesPy model.

## How to Run the Script

### **Step 1: Install Dependencies**

Ensure you have Python installed and the necessary libraries

```bash
pip install openseespy openseespy.postprocessing
```

### **Step 2: Execute the Script**

Run the script using Python:

```bash
python main.py
```

## Outputs

### **1. Node Displacements:**

The script prints the displacements (x and y directions) for each node after the analysis.

**Sample Output:**

```bash
1 numaralı düğüm x= 0.0 m  -  y= 0.0 m
2 numaralı düğüm x= 0.0 m  -  y= -0.001 m
...
16 numaralı düğüm x= -0.0025 m  -  y= -0.0020 m
```

### **2. Model Visualization:**

The model with nodes and elements is plotted using the plot_model function:

- Nodes are labeled.
- Elements are visualized for verification.
