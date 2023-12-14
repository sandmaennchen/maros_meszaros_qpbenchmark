# Maros-Meszaros dense subset

| Number of problems | 62       |
|:-------------------|:--------------------|
| Benchmark version  | 2.1.0rc1 |
| Date               | 2023-12-14 14:36:22.782397+00:00              |
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

Subset of the Maros-Meszaros test set restricted to smaller dense problems.

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
| `hz_actual_friendly` | 4.1681 GHz |
| `hz_advertised_friendly` | 4.1681 GHz |
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
| proxqp   | ``check_duality_gap``            | -         | True            | True           | True           |
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
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                    58.2 |                                 1.0 |
| cvxopt   |                                66.1 |                               4763.9 |                                 328484412.0 |                                355759.0 |                               408.7 |
| daqp     |                                51.6 |                              15838.5 |                                1186948529.5 |                                651320.4 |                               625.0 |
| ecos     |                                17.7 |                              83360.9 |                                1053926549.3 |                               1183238.4 |                               330.7 |
| highs    |                                66.1 |                               3802.8 |                                 286980656.5 |                                347338.0 |                               688.3 |
| osqp     |                                51.6 |                               1165.7 |                                6771430245.4 |                               4756504.0 |                             48876.1 |
| piqp     |                                93.5 |                                520.5 |                                  60976981.9 |                                 66047.0 |                                25.9 |
| proxqp   |                                96.8 |                                 27.8 |                                      1865.7 |                                     1.0 |                                83.9 |
| qpalm    |                                59.7 |                                163.2 |                                1086516212.4 |                                532254.3 |                             13083.1 |
| qpoases  |                                24.2 |                              14694.1 |                                9014689633.3 |                              30880392.5 |                               181.5 |
| quadprog |                                33.9 |                              41656.0 |                                 858192806.5 |                                929441.8 |                               268.4 |
| scs      |                                72.6 |                                350.6 |                                3167816782.8 |                                489682.7 |                              5843.6 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                75.8 |                                  1.3 |                                         1.0 |                                     4.6 |                                 2.9 |
| cvxopt   |                                 3.2 |                                 10.5 |                                         5.5 |                                   667.7 |                        1402672804.6 |
| daqp     |                                27.4 |                                 36.5 |                                     69996.2 |                                     2.1 |                           1387836.0 |
| ecos     |                                 0.0 |                                149.7 |                                         9.2 |                              23751199.8 |                           1026027.9 |
| highs    |                                 0.0 |                                  6.8 |                                         5.0 |                              99347179.1 |                        2752783762.1 |
| osqp     |                                41.9 |                                 30.9 |                                         6.4 |                                     2.3 |                                 3.1 |
| piqp     |                                82.3 |                                  3.0 |                                         1.7 |                                     1.0 |                                 2.9 |
| proxqp   |                                80.6 |                                  1.0 |                                         1.7 |                                     1.7 |                                 2.8 |
| qpalm    |                                43.5 |                                 12.7 |                                         4.8 |                                     1.7 |                               212.7 |
| qpoases  |                                19.4 |                                 28.7 |                               68926667491.6 |                           79815543813.2 |                                 1.5 |
| quadprog |                                25.8 |                                 74.8 |                                        14.2 |                                    10.9 |                                10.0 |
| scs      |                                62.9 |                                 16.9 |                                         4.7 |                                     1.9 |                                 1.0 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                98.4 |                                  1.0 |                                         1.0 |                                     8.3 |                                 1.0 |
| cvxopt   |                                53.2 |                               4585.8 |                                      9304.3 |                                    25.2 |                              5546.4 |
| daqp     |                                33.9 |                               6909.5 |                                 395098024.4 |                                    30.2 |                             22345.6 |
| ecos     |                                14.5 |                             104016.5 |                                     32255.5 |                                    93.9 |                                 6.5 |
| highs    |                                50.0 |                               4070.4 |                                      8683.9 |                                  2484.6 |                             10880.8 |
| osqp     |                                37.1 |                              11003.5 |                                     18197.1 |                                    52.8 |                              1045.2 |
| piqp     |                                93.5 |                                772.9 |                                      2604.6 |                                    16.8 |                                 2.1 |
| proxqp   |                                96.8 |                                 32.2 |                                      1974.0 |                                     1.0 |                                70.0 |
| qpalm    |                                54.8 |                                174.3 |                                      7365.9 |                                     9.7 |                             14105.0 |
| qpoases  |                                19.4 |                              18476.7 |                                 153650741.8 |                               1339210.7 |                                 3.7 |
| quadprog |                                33.9 |                              44638.1 |                                     25432.0 |                                    65.1 |                                 5.1 |
| scs      |                                79.0 |                               3639.8 |                                     11939.4 |                                    28.3 |                                 2.8 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel |                                93.5 |                                  5.1 |                                         1.0 |                                  1302.7 |                                 2.1 |
| cvxopt   |                                35.5 |                                135.7 |                                        14.7 |                                   244.3 |                           3139844.5 |
| daqp     |                                27.4 |                                502.4 |                                  25541547.1 |                                    19.5 |                           4394356.8 |
| ecos     |                                 3.2 |                               2643.3 |                                        48.5 |                              21469971.5 |                            722348.3 |
| highs    |                                29.0 |                                120.4 |                                        13.6 |                               1045055.1 |                           6160728.8 |
| osqp     |                                41.9 |                                423.4 |                                        29.0 |                                    23.7 |                                 9.0 |
| piqp     |                                93.5 |                                 22.9 |                                         4.0 |                                     4.7 |                                 1.0 |
| proxqp   |                               100.0 |                                  1.0 |                                         3.7 |                                     1.0 |                                 1.0 |
| qpalm    |                                53.2 |                                 37.0 |                                        14.3 |                                     6.8 |                             66744.7 |
| qpoases  |                                19.4 |                                427.9 |                                 810345223.3 |                             841108695.7 |                                 3.2 |
| quadprog |                                33.9 |                               1320.9 |                                        39.8 |                                    27.7 |                                 2.9 |
| scs      |                                74.2 |                                150.8 |                                        18.5 |                                    14.0 |                                 1.7 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |              76 |             98 |             94 |
| cvxopt   |        66 |               3 |             53 |             35 |
| daqp     |        52 |              27 |             34 |             27 |
| ecos     |        18 |               0 |             15 |              3 |
| highs    |        66 |               0 |             50 |             29 |
| osqp     |        52 |              42 |             37 |             42 |
| piqp     |        94 |              82 |             94 |             94 |
| proxqp   |        97 |              81 |             97 |            100 |
| qpalm    |        60 |              44 |             55 |             53 |
| qpoases  |        24 |              19 |             19 |             19 |
| quadprog |        34 |              26 |             34 |             34 |
| scs      |        73 |              63 |             79 |             74 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       100 |              82 |             98 |             95 |
| cvxopt   |        92 |              32 |             77 |             60 |
| daqp     |        98 |              79 |             65 |             74 |
| ecos     |        98 |              81 |             98 |             84 |
| highs    |        89 |              23 |             73 |             52 |
| osqp     |        61 |              90 |             76 |             85 |
| piqp     |        98 |              95 |            100 |            100 |
| proxqp   |        97 |              85 |             97 |            100 |
| qpalm    |        61 |              76 |             56 |             63 |
| qpoases  |        69 |              65 |             68 |             63 |
| quadprog |       100 |              92 |            100 |            100 |
| scs      |        76 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             1.3 |            1.0 |            5.1 |
| cvxopt   |    4763.9 |            10.5 |         4585.8 |          135.7 |
| daqp     |   15838.5 |            36.5 |         6909.5 |          502.4 |
| ecos     |   83360.9 |           149.7 |       104016.5 |         2643.3 |
| highs    |    3802.8 |             6.8 |         4070.4 |          120.4 |
| osqp     |    1165.7 |            30.9 |        11003.5 |          423.4 |
| piqp     |     520.5 |             3.0 |          772.9 |           22.9 |
| proxqp   |      27.8 |             1.0 |           32.2 |            1.0 |
| qpalm    |     163.2 |            12.7 |          174.3 |           37.0 |
| qpoases  |   14694.1 |            28.7 |        18476.7 |          427.9 |
| quadprog |   41656.0 |            74.8 |        44638.1 |         1320.9 |
| scs      |     350.6 |            16.9 |         3639.8 |          150.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |      default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|-------------:|----------------:|---------------:|---------------:|
| clarabel |          1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt   |  328484412.0 |             5.5 |         9304.3 |           14.7 |
| daqp     | 1186948529.5 |         69996.2 |    395098024.4 |     25541547.1 |
| ecos     | 1053926549.3 |             9.2 |        32255.5 |           48.5 |
| highs    |  286980656.5 |             5.0 |         8683.9 |           13.6 |
| osqp     | 6771430245.4 |             6.4 |        18197.1 |           29.0 |
| piqp     |   60976981.9 |             1.7 |         2604.6 |            4.0 |
| proxqp   |       1865.7 |             1.7 |         1974.0 |            3.7 |
| qpalm    | 1086516212.4 |             4.8 |         7365.9 |           14.3 |
| qpoases  | 9014689633.3 |   68926667491.6 |    153650741.8 |    810345223.3 |
| quadprog |  858192806.5 |            14.2 |        25432.0 |           39.8 |
| scs      | 3167816782.8 |             4.7 |        11939.4 |           18.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |    default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|-----------:|----------------:|---------------:|---------------:|
| clarabel |       58.2 |             4.6 |            8.3 |         1302.7 |
| cvxopt   |   355759.0 |           667.7 |           25.2 |          244.3 |
| daqp     |   651320.4 |             2.1 |           30.2 |           19.5 |
| ecos     |  1183238.4 |      23751199.8 |           93.9 |     21469971.5 |
| highs    |   347338.0 |      99347179.1 |         2484.6 |      1045055.1 |
| osqp     |  4756504.0 |             2.3 |           52.8 |           23.7 |
| piqp     |    66047.0 |             1.0 |           16.8 |            4.7 |
| proxqp   |        1.0 |             1.7 |            1.0 |            1.0 |
| qpalm    |   532254.3 |             1.7 |            9.7 |            6.8 |
| qpoases  | 30880392.5 |   79815543813.2 |      1339210.7 |    841108695.7 |
| quadprog |   929441.8 |            10.9 |           65.1 |           27.7 |
| scs      |   489682.7 |             1.9 |           28.3 |           14.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |             2.9 |            1.0 |            2.1 |
| cvxopt   |     408.7 |    1402672804.6 |         5546.4 |      3139844.5 |
| daqp     |     625.0 |       1387836.0 |        22345.6 |      4394356.8 |
| ecos     |     330.7 |       1026027.9 |            6.5 |       722348.3 |
| highs    |     688.3 |    2752783762.1 |        10880.8 |      6160728.8 |
| osqp     |   48876.1 |             3.1 |         1045.2 |            9.0 |
| piqp     |      25.9 |             2.9 |            2.1 |            1.0 |
| proxqp   |      83.9 |             2.8 |           70.0 |            1.0 |
| qpalm    |   13083.1 |           212.7 |        14105.0 |        66744.7 |
| qpoases  |     181.5 |             1.5 |            3.7 |            3.2 |
| quadprog |     268.4 |            10.0 |            5.1 |            2.9 |
| scs      |    5843.6 |             1.0 |            2.8 |            1.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).
