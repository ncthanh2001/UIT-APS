# APS Optimization Algorithms — Full Analysis (README)

> **Author:** BA  
> **Purpose:** Deep comparison of 4 optimization algorithms used for APS/MRP systems  
> **Date:** 2025-11-09  

---

## 🔍 Overview

APS (Advanced Planning & Scheduling) systems can use multiple optimization techniques to plan and schedule effectively.  
This README analyzes **4 core algorithms** used in BA’s MRP Optimization layer:

1. **Genetic Algorithm (GA)**  
2. **Simulated Annealing (SA)**  
3. **Particle Swarm Optimization (PSO)**  
4. **Linear Programming (LP / MILP)**  

---

## 1️⃣ Genetic Algorithm (GA) ⭐⭐⭐⭐⭐

**Purpose:**  
> “Bio-inspired metaheuristic — Tiến hóa tự nhiên”

**Mechanism:**
```
Population of solutions
 → Selection (natural selection)
 → Crossover (recombination)
 → Mutation (random changes)
 → Repeat (evolution over generations)
```

**Advantages:**
✅ Excellent for **multi-objective** problems  
✅ Handles **complex constraints** well  
✅ Robust (avoids local optima)  
✅ Scalable for **large search space**  
✅ Flexible customization  

**Disadvantages:**
⚠️ Slow convergence (many generations)  
⚠️ Many hyperparameters (population, rates)  
⚠️ Computationally expensive  
⚠️ No guaranteed optimum  

**Suitability for MRP:** ⭐⭐⭐⭐⭐ **EXCELLENT**  
**Use Cases:**
- Multi-objective MRP (cost, lead time, service)
- Supplier selection + lot sizing
- Large datasets (100+ items)

**Example (Chromosome representation):**
```
Chromosome = [Supplier, Qty, Date, Lot]
Gene[0]: NCC_A  → Supplier
Gene[1]: 2000   → Order qty
Gene[2]: Dec-16 → Order date
Gene[3]: 1000   → Lot size
```

---

## 2️⃣ Simulated Annealing (SA) ⭐⭐⭐⭐

**Purpose:**  
> “Physics-inspired — Quá trình tôi luyện kim loại”

**Mechanism:**
```
Start with random solution
 → Generate neighbor
 → Accept if better, or worse with probability
 → Gradually cool down (reduce temperature)
```

**Advantages:**
✅ Simple implementation  
✅ Escapes local optima  
✅ Low memory (single solution)  
✅ Fewer parameters  
✅ Good speed for small-medium problems  

**Disadvantages:**
⚠️ Single-objective preferred  
⚠️ Sensitive to cooling schedule  
⚠️ Noisy convergence  
⚠️ Less robust than GA  

**Suitability for MRP:** ⭐⭐⭐⭐ **GOOD**  
**Use Cases:**
- Single-objective MRP (minimize cost)
- Medium complexity
- Need fast prototype or simple heuristic  

**Example (MRP transition):**
```
Current: [NCC_A, 2000, Dec-16]
Neighbor: [NCC_B, 2000, Dec-16]
ΔC = cost_diff
Accept if better OR with probability e^(-ΔC/T)
```

---

## 3️⃣ Particle Swarm Optimization (PSO) ⭐⭐⭐⭐

**Purpose:**  
> “Swarm Intelligence — Đàn chim bay tìm thức ăn”

**Mechanism:**
```
Swarm of particles (solutions)
 → Each has position & velocity
 → Move toward personal & global best
 → Update velocity & position iteratively
```

**Advantages:**
✅ Fast convergence  
✅ Population-based like GA  
✅ Few parameters  
✅ Works well for continuous problems  
✅ Parallelizable  

**Disadvantages:**
⚠️ Originally for **continuous** domains  
⚠️ MRP is **discrete** → needs Binary/Discrete PSO  
⚠️ May converge prematurely  
⚠️ Requires tuning inertia & coefficients  

**Suitability for MRP:** ⭐⭐⭐⭐ **GOOD (with modifications)**  
**Use Cases:**
- Continuous lot sizing
- Real-time re-planning
- Medium-scale APS systems  

**Example (adapted for discrete MRP):**
```
Particle = solution
Position = [supplier_score, quantity, date_offset]
Velocity = direction/speed of change
position += velocity  → Discretize before evaluation
```

---

## 4️⃣ Linear Programming (LP / MILP) ⭐⭐⭐⭐⭐

**Purpose:**  
> “Mathematical optimization — Exact method”

**Mechanism:**
```
Formulate problem → Define objective + constraints
 → Solve using Simplex or Interior Point
 → Return optimal (or near-optimal) solution
```

**Advantages:**
✅ Guaranteed **optimal**  
✅ Fast with modern solvers (Gurobi, OR-Tools)  
✅ Mature & proven  
✅ Deterministic results  
✅ Handles constraints elegantly  

**Disadvantages:**
⚠️ Requires **linear** formulation  
⚠️ Integer variables need **MILP**  
⚠️ Formulation effort  
⚠️ May scale poorly for >1000 variables  

**Suitability for MRP:** ⭐⭐⭐⭐⭐ **EXCELLENT (Industry Standard)**  
**Use Cases:**
- Budget-critical planning  
- Need guaranteed optimal  
- Enterprise-grade APS (SAP, Oracle, etc.)

**Example (MILP Model):**
```
Decision variables:
  x[i,s,t] = quantity of item i from supplier s at time t

Objective:
  Minimize Σ(cost[s]*x[i,s,t] + setup[s]*y[i,s,t])

Constraints:
  Σ(x[i,s,t]) ≥ demand[i,t]
  x[i,s,t] ≤ capacity[s]*y[i,s,t]
  Σ(cost[s]*x[i,s,t]) ≤ budget
  x[i,s,t] ≥ 0; integer
  y[i,s,t] ∈ {0,1}
```

---

## 📊 Comparison Summary

| Criteria | GA | SA | PSO | LP/MILP |
|-----------|----|----|-----|---------|
| **Optimality** | ⭐⭐⭐ Near-opt | ⭐⭐⭐ Near-opt | ⭐⭐⭐ Near-opt | ⭐⭐⭐⭐⭐ Optimal |
| **Speed** | ⭐⭐ Slow | ⭐⭐⭐ Medium | ⭐⭐⭐⭐ Fast | ⭐⭐⭐⭐ Fast |
| **Multi-objective** | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐ OK | ⭐⭐⭐⭐ Good | ⭐⭐ Limited |
| **Constraints Handling** | ⭐⭐⭐⭐ Good | ⭐⭐⭐ OK | ⭐⭐⭐ OK | ⭐⭐⭐⭐⭐ Excellent |
| **Complexity** | ⭐⭐⭐ Medium | ⭐⭐ Simple | ⭐⭐⭐ Medium | ⭐⭐⭐⭐ High |
| **Implementation** | ⭐⭐⭐ Medium | ⭐⭐⭐⭐ Easy | ⭐⭐⭐ Medium | ⭐⭐ Hard |
| **Scalability** | ⭐⭐⭐ Good | ⭐⭐ OK | ⭐⭐⭐⭐ Good | ⭐⭐ Medium |
| **Robustness** | ⭐⭐⭐⭐ Strong | ⭐⭐ Fair | ⭐⭐ Fair | ⭐⭐⭐⭐ Deterministic |
| **Industry Use** | ⭐⭐⭐⭐ Common | ⭐⭐ Rare | ⭐⭐ Research | ⭐⭐⭐⭐⭐ Standard |
| **For MRP** | ⭐⭐⭐⭐⭐ Perfect | ⭐⭐⭐⭐ Good | ⭐⭐⭐⭐ Good* | ⭐⭐⭐⭐⭐ Best |

> *PSO needs discrete adaptation for supplier & date decisions.

---

## 🎯 Recommendations

### **Scenario-based Guidance**

**1️⃣ Enterprise / Industry System**
✅ **Use:** Linear Programming (MILP)  
→ Need optimal, repeatable, and constrained solution  
→ Use solver: **PuLP, OR-Tools, Gurobi, Pyomo**

---

**2️⃣ Multi-Objective / Research Focus**
✅ **Use:** Genetic Algorithm  
→ Trade-off between cost, service level, and inventory  
→ Generate Pareto front (non-dominated solutions)  
→ Libraries: **DEAP**, **pymoo**

---

**3️⃣ Quick MVP / Simple Prototype**
✅ **Use:** Simulated Annealing  
→ Fast to code, low dependency  
→ Good for single objective (min cost)  
→ Ideal for early testing

---

**4️⃣ Real-Time or Adaptive Planning**
✅ **Use:** Particle Swarm Optimization  
→ Faster convergence  
→ Real-time heuristic re-optimization  
→ Adapt discrete PSO for supplier/date decision variables

---

## 🧭 Recommended Roadmap for BA Project

### **Phase 1 — MVP (Stable & Optimal)**
Algorithm: **Linear Programming (MILP)**  
Libraries: `PuLP`, `OR-Tools`  
Objective: `Minimize total purchase cost`

### **Phase 2 — Advanced (Multi-objective)**
Algorithm: **Genetic Algorithm (GA)**  
Libraries: `DEAP`, `pymoo`  
Objective: `Minimize cost & inventory, maximize service`

### **Phase 3 — Benchmarking**
Algorithms: `SA`, `PSO`  
Purpose: Comparison & user customization (choose algorithm per scenario)

---

## ✅ Conclusion

| Algorithm | Strength | Best Use Case |
|------------|-----------|----------------|
| **Genetic Algorithm** | Excellent for multi-objective and complex MRP | Advanced APS |
| **Simulated Annealing** | Simple and quick | MVP / single-objective |
| **Particle Swarm Optimization** | Fast and adaptable | Real-time planning |
| **Linear Programming** | Exact optimal and stable | Enterprise solution |

> ✅ **Final Recommendation:**  
> - **Phase 1:** Linear Programming (MILP)  
> - **Phase 2:** Genetic Algorithm (GA)  
> - **Optional:** Add SA & PSO for user comparison later.

---
