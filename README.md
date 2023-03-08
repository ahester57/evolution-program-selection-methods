# A Simple Genetic Algorithm

## Objective

Solve the following optimization of a simple function using a genetic algorithm (GA):

$$\underset{\vec{x}}{\arg\min} f(\vec{x}) = x_1^2 + x_2^2 + x_3^2$$

With bounds $$-7.0 \leq x_i \leq 4.0, i = 1, 2, 3$$

----

## Details of Genetic Algorithm

### GA Properties

* Chromosomes (input vector $\vec{x}$) made up of real, floating-point values, e.g. $(2.3, -0.05, 2.71)$
* Proportional selection, i.e. probability of advancement equal to fitness values over sum of all fitness values.
* Single-point crossover, i.e. from two parents, choose a cut-point and swap sides of each parent to create two children.
* Gene-wise mutation, i.e. each gene ($x_i$) has equal but indenpendent chance ($p_m$) to mutate a small amount.

### Parameters

* Dimensions (of $\vec{x}$), $d = 3$
* Population Size, $N = 30$
* Crossover probability, $p_c = 0.8$
* Mutation probability, $p_m = 0.1$

### Termination Condition

* Terminate simulation after $t_{max}$ generations, $t_{max} = 50$

----
