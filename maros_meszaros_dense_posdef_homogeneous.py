#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2023-2024 Inria

"""Dense subset with positive definite P of the Maros-Meszaros test set - homogeneous reformulation"""

import os
from typing import Iterator

import qpbenchmark
from qpbenchmark.benchmark import main
from qpbenchmark import Problem

from maros_meszaros_dense import MarosMeszarosDense


class MarosMeszarosDensePosdefHomogeneous(MarosMeszarosDense):
    """Subset of Maros-Meszaros restricted to smaller dense problems - homogeneous reformulation"""


    @property
    def description(self) -> str:
        """Description of the test set."""
        return (
            "Subset of the Maros-Meszaros test set "
            "restricted to smaller dense problems "
            "with positive definite Hessian matrix"
            "in homogeneous reformulation."
        )

    @property
    def title(self) -> str:
        """Test set title."""
        return "Maros-Meszaros dense positive definite subset - homogeneous reformulation"

    @property
    def sparse_only(self) -> bool:
        """Test set is dense."""
        return False


    def __init__(self):
        """Initialize test set."""
        super().__init__()
        self.data_dir += "_homogeneous"


    def __iter__(self) -> Iterator[qpbenchmark.Problem]:
        """Iterate over test set problems."""
        for fname in os.listdir(self.data_dir):
            if fname.endswith(".npz"):
                npz_path = os.path.join(self.data_dir, fname)
                problem = Problem.load(npz_path)
                yield problem


if __name__ == "__main__":
    main(test_set_path=os.path.abspath(__file__))
