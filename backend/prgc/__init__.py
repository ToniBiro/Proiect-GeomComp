"""Geometry library.

This module provides simple geometric primitives and supports performing
operations on them.
"""

from .primitive import Vector2D, right_turn
from .dcel import DCEL
from .intersect import Segment, intersect_segments, intersect_polygons
