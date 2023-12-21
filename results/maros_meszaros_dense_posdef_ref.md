# Maros-Meszaros dense positive definite subset

| Number of problems | 19 |
|:-------------------|:--------------------|
| Benchmark version  | 2.1.0 |
| Date               | 2023-12-21 14:07:19.882173+00:00 |
| CPU                | [Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz](#cpu-info) |
| Run by             | [@stephane-caron](https://github.com/stephane-caron/) |

Benchmark reports are copious as we aim to document comparison factors as much as possible. You can also [jump to results](#results-by-settings) directly.

## Contents

* [Description](#description)
* [Solvers](#solvers)
* [Settings](#settings)
* [CPU info](#cpu-info)
* [Known limitations](#known-limitations)
* [Results by settings](#results-by-settings)
    * [Default](#default)
    * [High accuracy](#high-accuracy)
    * [Low accuracy](#low-accuracy)
    * [Mid accuracy](#mid-accuracy)
* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Optimality conditions](#optimality-conditions)
        * [Primal residual](#primal-residual)
        * [Dual residual](#dual-residual)
        * [Duality gap](#duality-gap)

## Description

Subset of the Maros-Meszaros test set restricted to smaller dense problems with positive definite Hessian matrix.

## Solvers

| solver   | version   |
|:---------|:----------|
| clarabel | 0.5.1     |
| cvxopt   | 1.3.1     |
| daqp     | 0.5.1     |
| ecos     | 2.0.12    |
| highs    | 1.5.3     |
| osqp     | 0.6.3     |
| piqp     | 0.2.3     |
| proxqp   | 0.6.1     |
| qpalm    | 1.2.1     |
| qpoases  | 3.2.1     |
| quadprog | 0.1.11    |
| scs      | 3.2.3     |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.1.1.

## CPU info

| Property | Value |
|----------|-------|
| `arch` | X86_64 |
| `arch_string_raw` | x86_64 |
| `bits` | 64 |
| `brand_raw` | 12th Gen Intel(R) Core(TM) i7-12800H |
| `count` | 20 |
| `cpuinfo_version_string` | 9.0.0 |
| `family` | 6 |
| `flags` | `3dnowprefetch`, `abm`, `acpi`, `adx`, `aes`, `aperfmperf`, `apic`, `arat`, `arch_capabilities`, `arch_lbr`, `arch_perfmon`, `art`, `avx`, `avx2`, `avx_vnni`, `bmi1`, `bmi2`, `bts`, `clflush`, `clflushopt`, `clwb`, `cmov`, `constant_tsc`, `cpuid`, `cpuid_fault`, `cx16`, `cx8`, `de`, `ds_cpl`, `dtes64`, `dtherm`, `dts`, `epb`, `ept`, `ept_ad`, `erms`, `est`, `f16c`, `flexpriority`, `flush_l1d`, `fma`, `fpu`, `fsgsbase`, `fsrm`, `fxsr`, `gfni`, `hfi`, `ht`, `hwp`, `hwp_act_window`, `hwp_epp`, `hwp_notify`, `hwp_pkg_req`, `ibpb`, `ibrs`, `ibrs_enhanced`, `ibt`, `ida`, `intel_pt`, `invpcid`, `lahf_lm`, `lm`, `mca`, `mce`, `md_clear`, `mmx`, `monitor`, `movbe`, `movdir64b`, `movdiri`, `msr`, `mtrr`, `nonstop_tsc`, `nopl`, `nx`, `ospke`, `osxsave`, `pae`, `pat`, `pbe`, `pcid`, `pclmulqdq`, `pconfig`, `pdcm`, `pdpe1gb`, `pebs`, `pge`, `pku`, `pln`, `pni`, `popcnt`, `pse`, `pse36`, `pts`, `rdpid`, `rdrand`, `rdrnd`, `rdseed`, `rdtscp`, `rep_good`, `sdbg`, `sep`, `serialize`, `sha`, `sha_ni`, `smap`, `smep`, `smx`, `split_lock_detect`, `ss`, `ssbd`, `sse`, `sse2`, `sse4_1`, `sse4_2`, `ssse3`, `stibp`, `syscall`, `tm`, `tm2`, `tme`, `tpr_shadow`, `tsc`, `tsc_adjust`, `tsc_deadline_timer`, `tsc_known_freq`, `tscdeadline`, `umip`, `vaes`, `vme`, `vmx`, `vnmi`, `vpclmulqdq`, `vpid`, `waitpkg`, `x2apic`, `xgetbv1`, `xsave`, `xsavec`, `xsaveopt`, `xsaves`, `xtopology`, `xtpr` |
| `hz_actual_friendly` | 2.8000 GHz |
| `hz_advertised_friendly` | 2.8000 GHz |
| `l1_data_cache_size` | 557056 |
| `l1_instruction_cache_size` | 720896 |
| `l2_cache_associativity` | 7 |
| `l2_cache_line_size` | 1280 |
| `l2_cache_size` | 11.5 MiB |
| `l3_cache_size` | 25165824 |
| `model` | 154 |
| `python_version` | 3.10.13.final.0 (64 bit) |
| `stepping` | 3 |
| `vendor_id_raw` | GenuineIntel |

## Settings

There are 4 settings: *default*, *high_accuracy*, *low_accuracy* and *mid_accuracy*. They validate solutions using the following tolerances:

| tolerance   |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| ``dual``    |         1 |           1e-09 |          0.001 |          1e-06 |
| ``gap``     |         1 |           1e-09 |          0.001 |          1e-06 |
| ``primal``  |         1 |           1e-09 |          0.001 |          1e-06 |
| ``runtime`` |      1000 |        1000     |       1000     |       1000     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   | high_accuracy   | low_accuracy   | mid_accuracy   |
|:---------|:---------------------------------|:----------|:----------------|:---------------|:---------------|
| clarabel | ``tol_feas``                     | -         | 1e-09           | 0.001          | 1e-06          |
| clarabel | ``tol_gap_abs``                  | -         | 1e-09           | 0.001          | 1e-06          |
| clarabel | ``tol_gap_rel``                  | -         | 0.0             | 0.0            | 0.0            |
| cvxopt   | ``feastol``                      | -         | 1e-09           | 0.001          | 1e-06          |
| daqp     | ``dual_tol``                     | -         | 1e-09           | 0.001          | 1e-06          |
| daqp     | ``primal_tol``                   | -         | 1e-09           | 0.001          | 1e-06          |
| ecos     | ``feastol``                      | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``dual_feasibility_tolerance``   | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``primal_feasibility_tolerance`` | -         | 1e-09           | 0.001          | 1e-06          |
| highs    | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| osqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| osqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| osqp     | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| piqp     | ``check_duality_gap``            | -         | 1.0             | 1.0            | 1.0            |
| piqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| piqp     | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| piqp     | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``check_duality_gap``            | -         | 1.0             | 1.0            | 1.0            |
| proxqp   | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| proxqp   | ``eps_duality_gap_abs``          | -         | 1e-09           | 0.001          | 1e-06          |
| proxqp   | ``eps_duality_gap_rel``          | -         | 0.0             | 0.0            | 0.0            |
| proxqp   | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| qpalm    | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| qpalm    | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| qpalm    | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| qpoases  | ``predefined_options``           | default   | reliable        | fast           | -              |
| qpoases  | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         | 1000.0         |
| scs      | ``eps_abs``                      | -         | 1e-09           | 0.001          | 1e-06          |
| scs      | ``eps_rel``                      | -         | 0.0             | 0.0            | 0.0            |
| scs      | ``time_limit_secs``              | 1000.0    | 1000.0          | 1000.0         | 1000.0         |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                       736.7 |                                   350.0 |                                12.1 |
| cvxopt   |                                84.2 |                               3104.3 |                               90710810719.0 |                             180470935.3 |                             11125.2 |
| daqp     |                               100.0 |                                  1.2 |                                    239825.3 |                                     1.0 |                               145.5 |
| ecos     |                                36.8 |                              38942.0 |                              339387408823.0 |                             758318707.3 |                             41875.6 |
| highs    |                                89.5 |                                804.4 |                               30085386291.3 |                             143531703.1 |                              5506.0 |
| osqp     |                                78.9 |                                  1.1 |                              625477870390.8 |                            3549171039.0 |                           2259852.7 |
| piqp     |                               100.0 |                                  1.8 |                                         1.0 |                                   195.4 |                                 1.0 |
| proxqp   |                                94.7 |                                  5.2 |                                   1049423.1 |                                  1210.2 |                              7855.6 |
| qpalm    |                                63.2 |                                795.8 |                               52838547147.9 |                             553592988.4 |                            563843.5 |
| qpoases  |                                57.9 |                               6848.7 |                              254309453730.6 |                           22980126332.2 |                             18541.1 |
| quadprog |                                89.5 |                               1811.7 |                               60322069328.5 |                             120011813.4 |                              7360.7 |
| scs      |                                89.5 |                                 25.6 |                              628784911049.5 |                              80555459.3 |                            540911.3 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                84.2 |                                  1.0 |                                         1.0 |                                    15.4 |                                 5.8 |
| cvxopt   |                                 5.3 |                               2636.0 |                                        71.9 |                                   404.5 |                           2838534.2 |
| daqp     |                                78.9 |                                676.3 |                                     47753.9 |                                     1.0 |                           7426986.3 |
| ecos     |                                 0.0 |                              33085.8 |                                       264.5 |                             151752595.5 |                           5490109.7 |
| highs    |                                 0.0 |                                679.3 |                                       212.2 |                             644512979.2 |                          93237113.5 |
| osqp     |                                63.2 |                               4034.1 |                                       151.1 |                                     3.2 |                                 2.7 |
| piqp     |                                89.5 |                               1538.3 |                                        48.0 |                                     2.0 |                                 1.1 |
| proxqp   |                                84.2 |                                686.0 |                                        88.5 |                                     8.0 |                                 2.2 |
| qpalm    |                                68.4 |                               4033.7 |                                       159.5 |                                     2.2 |                                 3.1 |
| qpoases  |                                52.6 |                               5821.8 |                               76000557643.0 |                          171204953580.5 |                                 1.0 |
| quadprog |                                78.9 |                               1540.0 |                                        48.2 |                                     5.4 |                                 1.3 |
| scs      |                                84.2 |                               2639.5 |                                        94.6 |                                     2.6 |                                 1.1 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                 32151.4 |                                 1.4 |
| cvxopt   |                                73.7 |                               1989.7 |                                    848880.3 |                                174213.3 |                                 8.3 |
| daqp     |                                84.2 |                                  1.9 |                                   3863737.3 |                                     1.0 |                                18.9 |
| ecos     |                                31.6 |                              55201.8 |                                   5093415.7 |                               1202649.5 |                                 6.5 |
| highs    |                                57.9 |                                874.7 |                                    424442.4 |                              83450009.7 |                               238.1 |
| osqp     |                                52.6 |                               1980.6 |                                   1925973.4 |                                450446.2 |                              4186.5 |
| piqp     |                               100.0 |                                  2.4 |                                        78.5 |                                239961.1 |                                 2.1 |
| proxqp   |                                89.5 |                                  5.7 |                                   1152997.1 |                                 39089.1 |                               279.8 |
| qpalm    |                                68.4 |                                871.0 |                                   1615831.0 |                                146675.8 |                               338.9 |
| qpoases  |                                52.6 |                               7493.7 |                                1347878389.2 |                           22251703189.3 |                                 2.5 |
| quadprog |                                89.5 |                               1983.6 |                                    848880.3 |                                125475.9 |                                 1.0 |
| scs      |                                89.5 |                               1998.1 |                                   1664807.4 |                                181683.8 |                                 2.3 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                    68.0 |                                 3.4 |
| cvxopt   |                                52.6 |                               1854.1 |                                     93911.1 |                                 13767.0 |                              7247.9 |
| daqp     |                                84.2 |                                  2.1 |                                    357647.5 |                                     1.0 |                             18886.6 |
| ecos     |                                 0.0 |                              39696.2 |                                    517033.6 |                            2084125475.5 |                           5230772.6 |
| highs    |                                47.4 |                                814.4 |                                     47324.3 |                              83257667.5 |                            237058.4 |
| osqp     |                                68.4 |                               3160.8 |                                    199587.8 |                                   448.8 |                                 7.7 |
| piqp     |                               100.0 |                                  3.0 |                                         4.1 |                                   108.2 |                                 1.4 |
| proxqp   |                               100.0 |                                  5.8 |                                    121116.1 |                                    76.6 |                                 2.7 |
| qpalm    |                                73.7 |                                811.4 |                                    178502.4 |                                    84.3 |                               330.9 |
| qpoases  |                                52.6 |                               6981.4 |                              148869793526.4 |                           22116102156.3 |                                 2.5 |
| quadprog |                                89.5 |                               1847.7 |                                     93911.7 |                                   125.9 |                                 1.0 |
| scs      |                                84.2 |                               3165.6 |                                    180386.4 |                                   291.0 |                                 2.5 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |              84 |            100 |            100 |
| cvxopt   |        84 |               5 |             74 |             53 |
| daqp     |       100 |              79 |             84 |             84 |
| ecos     |        37 |               0 |             32 |              0 |
| highs    |        89 |               0 |             58 |             47 |
| osqp     |        79 |              63 |             53 |             68 |
| piqp     |       100 |              89 |            100 |            100 |
| proxqp   |        95 |              84 |             89 |            100 |
| qpalm    |        63 |              68 |             68 |             74 |
| qpoases  |        58 |              53 |             53 |             53 |
| quadprog |        89 |              79 |             89 |             89 |
| scs      |        89 |              84 |             89 |             84 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |              84 |            100 |            100 |
| cvxopt   |       100 |              21 |             84 |             63 |
| daqp     |       100 |              84 |             84 |             84 |
| ecos     |        95 |              58 |             95 |             58 |
| highs    |        95 |               5 |             63 |             53 |
| osqp     |        79 |              84 |             63 |             84 |
| piqp     |       100 |             100 |            100 |            100 |
| proxqp   |        95 |              89 |             89 |            100 |
| qpalm    |        68 |              89 |             74 |             79 |
| qpoases  |        84 |              79 |             79 |             79 |
| quadprog |       100 |              89 |            100 |            100 |
| scs      |        89 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt   |    3104.3 |          2636.0 |         1989.7 |         1854.1 |
| daqp     |       1.2 |           676.3 |            1.9 |            2.1 |
| ecos     |   38942.0 |         33085.8 |        55201.8 |        39696.2 |
| highs    |     804.4 |           679.3 |          874.7 |          814.4 |
| osqp     |       1.1 |          4034.1 |         1980.6 |         3160.8 |
| piqp     |       1.8 |          1538.3 |            2.4 |            3.0 |
| proxqp   |       5.2 |           686.0 |            5.7 |            5.8 |
| qpalm    |     795.8 |          4033.7 |          871.0 |          811.4 |
| qpoases  |    6848.7 |          5821.8 |         7493.7 |         6981.4 |
| quadprog |    1811.7 |          1540.0 |         1983.6 |         1847.7 |
| scs      |      25.6 |          2639.5 |         1998.1 |         3165.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |        default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|---------------:|----------------:|---------------:|---------------:|
| clarabel |          736.7 |             1.0 |            1.0 |            1.0 |
| cvxopt   |  90710810719.0 |            71.9 |       848880.3 |        93911.1 |
| daqp     |       239825.3 |         47753.9 |      3863737.3 |       357647.5 |
| ecos     | 339387408823.0 |           264.5 |      5093415.7 |       517033.6 |
| highs    |  30085386291.3 |           212.2 |       424442.4 |        47324.3 |
| osqp     | 625477870390.8 |           151.1 |      1925973.4 |       199587.8 |
| piqp     |            1.0 |            48.0 |           78.5 |            4.1 |
| proxqp   |      1049423.1 |            88.5 |      1152997.1 |       121116.1 |
| qpalm    |  52838547147.9 |           159.5 |      1615831.0 |       178502.4 |
| qpoases  | 254309453730.6 |   76000557643.0 |   1347878389.2 | 148869793526.4 |
| quadprog |  60322069328.5 |            48.2 |       848880.3 |        93911.7 |
| scs      | 628784911049.5 |            94.6 |      1664807.4 |       180386.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |       default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|--------------:|----------------:|---------------:|---------------:|
| clarabel |         350.0 |            15.4 |        32151.4 |           68.0 |
| cvxopt   |   180470935.3 |           404.5 |       174213.3 |        13767.0 |
| daqp     |           1.0 |             1.0 |            1.0 |            1.0 |
| ecos     |   758318707.3 |     151752595.5 |      1202649.5 |   2084125475.5 |
| highs    |   143531703.1 |     644512979.2 |     83450009.7 |     83257667.5 |
| osqp     |  3549171039.0 |             3.2 |       450446.2 |          448.8 |
| piqp     |         195.4 |             2.0 |       239961.1 |          108.2 |
| proxqp   |        1210.2 |             8.0 |        39089.1 |           76.6 |
| qpalm    |   553592988.4 |             2.2 |       146675.8 |           84.3 |
| qpoases  | 22980126332.2 |  171204953580.5 |  22251703189.3 |  22116102156.3 |
| quadprog |   120011813.4 |             5.4 |       125475.9 |          125.9 |
| scs      |    80555459.3 |             2.6 |       181683.8 |          291.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |      12.1 |             5.8 |            1.4 |            3.4 |
| cvxopt   |   11125.2 |       2838534.2 |            8.3 |         7247.9 |
| daqp     |     145.5 |       7426986.3 |           18.9 |        18886.6 |
| ecos     |   41875.6 |       5490109.7 |            6.5 |      5230772.6 |
| highs    |    5506.0 |      93237113.5 |          238.1 |       237058.4 |
| osqp     | 2259852.7 |             2.7 |         4186.5 |            7.7 |
| piqp     |       1.0 |             1.1 |            2.1 |            1.4 |
| proxqp   |    7855.6 |             2.2 |          279.8 |            2.7 |
| qpalm    |  563843.5 |             3.1 |          338.9 |          330.9 |
| qpoases  |   18541.1 |             1.0 |            2.5 |            2.5 |
| quadprog |    7360.7 |             1.3 |            1.0 |            1.0 |
| scs      |  540911.3 |             1.1 |            2.3 |            2.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
