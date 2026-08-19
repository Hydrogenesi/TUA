# Plate71 Renderer Specification

## 1. Overview

### 1.1 Purpose

Plate71 is the proposed visual plate rendering system for MATRIUN matrices. Its role is to turn matrix data produced by MATRIUN operations into interactive SVG/HTML views that are easy to inspect in terminals, notebooks, static docs, and browser applications.

This specification is:

- A **design guide** for implementers building the renderer
- An **API contract** between matrix-processing code and visualization code
- A **configuration schema** for controlling appearance and interaction
- A **foundation** for future visualization features

This document is intentionally non-prescriptive: it defines required behavior and interfaces, while allowing multiple internal implementation approaches.

### 1.2 Integration with MATRIUN

Plate71 sits after existing MATRIUN matrix operations.

For context, MATRIUN currently provides matrix APIs such as:

- `add_matrices`
- `multiply_matrices`
- `transpose_matrix`
- `scale_matrix`
- `apply_wildcard_mask`

See:

- [Project README](../README.md)
- [Documentation index](./index.md)
- Core library module: `matriun.py`

Plate71 should accept outputs from these operations without requiring MATRIUN core behavior changes.

### 1.3 Use Cases and Benefits

Primary use cases:

1. Visual debugging of matrix transformations
2. Educational views for matrix operations
3. Reporting snapshots embedded in markdown/html
4. Interactive data inspection (hover, click, zoom)
5. Comparing masked/unmasked matrix states

---

## 2. Architecture

### 2.1 High-Level Data Flow

```text
MATRIUN Matrix Ops
  (add/multiply/transpose/scale/mask)
            |
            v
   Plate71 Input Adapter
  (normalize + metadata attach)
            |
            v
      Layout Engine
 (geometry + coordinates)
            |
            v
      Style Engine
 (theme + states + classes)
            |
            v
       SVG Builder
 (semantic groups + a11y)
            |
            v
   SVG/HTML Output Artifact
```

### 2.2 Core Components

#### 2.2.1 Renderer Facade

Responsible for one public entry point:

- Input: matrix payload + Plate71 config
- Output: SVG string (or DOM fragment in browser mode)

#### 2.2.2 Layout Engine

Computes:

- Canvas dimensions
- Cell rectangles
- Text anchors
- Optional overlays (selection/highlight)

#### 2.2.3 Style System

Maps data and state to:

- Fill colors
- Stroke styles
- Typography
- Hover/active classes

#### 2.2.4 SVG Builder

Assembles semantic SVG structure with accessibility attributes.

### 2.3 Extensibility Points

Recommended extension hooks:

- **Value formatter**: custom cell text rendering
- **Color mapper**: value/type/state driven palette mapping
- **Interaction adapter**: host-specific event wiring
- **Metadata enrichers**: add domain attributes to cells

Implementations may expose hooks as callbacks, plugin objects, or strategy classes.

---

## 3. Plate Geometry

### 3.1 Canvas and Viewport Model

Required geometry fields:

- `width`, `height` (rendered pixel dimensions)
- `viewBox` dimensions (logical coordinate system)
- `padding` (outer margin)
- Optional `clip` behavior for overflow

Coordinate recommendation:

- Layout in logical units
- Apply final scaling through `viewBox` for responsiveness

### 3.2 Coordinate Systems

Plate71 supports two coordinate modes:

1. **Cartesian mode** (default): row/column orthogonal grid
2. **Plate71 projection mode**: Cartesian base with optional 71° transform layer for visual identity

A practical approach for projection mode:

- Compute base Cartesian positions first
- Apply a group transform to plate/cell layers
- Keep interaction hitboxes in unprojected or transformed coordinates consistently

### 3.3 Cell Rendering Geometry

Each cell should define:

- `x`, `y`
- `width`, `height`
- `row`, `col`
- `centerX`, `centerY` (for text/markers)

Spacing controls:

- `cellGapX`, `cellGapY`
- `platePadding`
- Optional `rowBandGap` / `colBandGap` for grouped layouts

### 3.4 Scaling and Responsive Behavior

Responsive strategy:

- Keep intrinsic geometry in viewBox units
- Use `preserveAspectRatio` policy
- Scale typography with optional min/max constraints

Suggested behavior:

- Small viewport: hide non-essential labels first
- Medium/Large viewport: progressively restore full labels and overlays

---

## 4. Data Model

### 4.1 Rendering Context

Renderer input should normalize into a rendering context:

```json
{
  "matrix": [[1, 2], [3, 4]],
  "rows": 2,
  "cols": 2,
  "source": {
    "operation": "multiply_matrices",
    "timestamp": "2026-08-19T00:00:00Z"
  },
  "cells": []
}
```

`cells` may be generated internally from `matrix`, but exposing this shape helps plugins.

### 4.2 Cell Metadata

Each cell metadata object should support:

```json
{
  "row": 0,
  "col": 1,
  "value": 2,
  "valueType": "number",
  "state": ["default"],
  "masked": false,
  "label": "r0c1",
  "tags": ["derived"],
  "styleKey": "scale-neutral"
}
```

### 4.3 Wildcard Masking Representation

For `apply_wildcard_mask` results, masked cells should be represented with explicit state, not inferred from display text alone.

Required concepts:

- `masked: true|false`
- `maskToken` (example: `"*"`)
- Distinct semantic class (example: `plate71-cell--masked`)

Visual recommendations for masked cells:

- Reduced saturation or patterned fill
- Optional symbol overlay
- Accessible textual description (e.g., "masked cell")

### 4.4 Cell Styling Model

Cell styling should resolve from layered sources:

1. Base theme defaults
2. Value/type mapping
3. State mapping (hover/selected/masked/error)
4. Per-cell overrides

Resolution order should be deterministic.

---

## 5. Rendering Process

### 5.1 Inputs

Minimum inputs:

- Matrix data from MATRIUN operation output
- Renderer configuration object

Optional inputs:

- Cell metadata enrichments
- Interaction state model
- Previous render snapshot (for diff-based refresh)

### 5.2 Layout Phase

Layout phase responsibilities:

1. Validate matrix rectangularity
2. Resolve dimensions and scaling
3. Compute each cell box
4. Place text anchors and optional overlays

Pseudo-flow:

```text
normalize -> validate -> compute grid -> assign cell boxes -> derive text anchors
```

### 5.3 Style Phase

Style phase responsibilities:

1. Resolve active theme
2. Map values to color scale (optional)
3. Apply state classes and inline/style refs
4. Compute typography fallback chain

### 5.4 Output Phase

Output should be semantic SVG with grouped structure:

- Root plate group
- Grid layer
- Cell layer
- Label/text layer
- Optional interaction overlay layer

### 5.5 Caching and Refresh Strategy

Possible caching keys:

- Matrix hash
- Effective config hash
- Theme hash

Refresh modes:

- **Full rerender** (simple baseline)
- **Patch update** for changed cells only
- **State-only update** (hover/selection classes)

---

## 6. Configuration Schema

### 6.1 Top-Level Shape

```json
{
  "geometry": {},
  "theme": {},
  "typography": {},
  "borders": {},
  "interaction": {},
  "accessibility": {},
  "performance": {}
}
```

### 6.2 Geometry Configuration

```json
{
  "geometry": {
    "mode": "cartesian",
    "projection": {
      "enabled": false,
      "angleDeg": 71
    },
    "width": 640,
    "height": 480,
    "padding": 16,
    "cell": {
      "width": 40,
      "height": 40,
      "gapX": 4,
      "gapY": 4,
      "minSize": 18,
      "maxSize": 72
    },
    "responsive": {
      "enabled": true,
      "preserveAspectRatio": "xMidYMid meet"
    }
  }
}
```

### 6.3 Theme and Color Mapping

```json
{
  "theme": {
    "name": "matriun-default",
    "background": "#0b1020",
    "grid": "#1f2a44",
    "text": "#e8ecff",
    "states": {
      "masked": "#5f6b85",
      "hover": "#89b4ff",
      "selected": "#f9c74f"
    },
    "valueScale": {
      "enabled": true,
      "domain": [-10, 10],
      "range": ["#2d3250", "#7aa2f7"]
    }
  }
}
```

### 6.4 Typography

```json
{
  "typography": {
    "fontFamily": "Inter, Segoe UI, Roboto, sans-serif",
    "fontSize": 12,
    "fontWeight": 500,
    "lineHeight": 1.2,
    "autoScale": true,
    "minFontSize": 9,
    "maxFontSize": 16,
    "format": {
      "numberPrecision": 3,
      "trimTrailingZeros": true
    }
  }
}
```

### 6.5 Borders and Spacing

```json
{
  "borders": {
    "cellStrokeWidth": 1,
    "cellRadius": 4,
    "plateStrokeWidth": 1,
    "showOuterFrame": true
  }
}
```

### 6.6 Interaction Configuration

```json
{
  "interaction": {
    "hover": true,
    "click": true,
    "zoom": {
      "enabled": true,
      "min": 0.5,
      "max": 4.0,
      "wheelStep": 0.1
    },
    "tooltip": {
      "enabled": true,
      "template": "({row}, {col}) = {value}"
    },
    "selection": {
      "mode": "single"
    }
  }
}
```

### 6.7 Accessibility and Performance Configuration

```json
{
  "accessibility": {
    "role": "img",
    "title": "Matrix Plate",
    "description": "Visual rendering of MATRIUN matrix output",
    "includeCellAria": true
  },
  "performance": {
    "useClipPaths": true,
    "groupByRow": true,
    "deferTextForLargeMatrices": true,
    "largeMatrixThreshold": 2500
  }
}
```

---

## 7. SVG Output Specification

### 7.1 Element Hierarchy

Recommended structure:

```text
<svg class="plate71 plate71--theme-matriun-default">
  <title/>
  <desc/>
  <g class="plate71__viewport">
    <g class="plate71__grid"/>
    <g class="plate71__cells">
      <g class="plate71__row" data-row="0">...</g>
    </g>
    <g class="plate71__labels"/>
    <g class="plate71__overlay"/>
  </g>
</svg>
```

### 7.2 Required Semantic Classes

Suggested class contract:

- `plate71`
- `plate71__viewport`
- `plate71__grid`
- `plate71__cells`
- `plate71__cell`
- `plate71__cell-text`
- `plate71-cell--masked`
- `plate71-cell--hover`
- `plate71-cell--selected`

### 7.3 Data Attributes

Each cell group should expose machine-readable attributes:

- `data-row`
- `data-col`
- `data-value`
- `data-masked`
- `data-state`

This enables host-level event delegation and testing.

### 7.4 Accessibility Requirements

At minimum:

- Root `<svg>` with `role="img"` and accessible title/description
- Per-cell accessible name when interaction is enabled
- Masked state voiced in labels where relevant

Convention: `data-row`/`data-col` remain zero-based for machine use, while human-facing `aria-label` text should use one-based indexing.

Example:

```svg
<g class="plate71__cell plate71-cell--masked"
   data-row="1" data-col="2" data-value="*" data-masked="true"
   aria-label="Cell row 2 column 3, masked">
  <rect x="96" y="48" width="40" height="40" rx="4" />
  <text x="116" y="72" text-anchor="middle">*</text>
</g>
```

### 7.5 Performance Considerations

For larger matrices:

- Group by row or tile for DOM locality
- Avoid excessive per-cell filters/shadows
- Prefer transform-based pan/zoom over recomputing geometry
- Defer or simplify text for dense views

---

## 8. Examples

### 8.1 Example A: Simple 3x3 Matrix

Input matrix:

```json
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

Minimal render config:

```json
{
  "geometry": {"width": 320, "height": 240, "padding": 12, "cell": {"width": 48, "height": 48, "gapX": 4, "gapY": 4}},
  "theme": {"name": "light", "background": "#ffffff", "text": "#222"},
  "interaction": {"hover": true, "click": false}
}
```

Result expectations:

- 9 rendered cells
- Identity diagonal visually emphasized (if valueScale enabled)
- Hover class toggles per cell

### 8.2 Example B: 10x10 Matrix with Color Mapping

Scenario:

- Matrix values range from -5 to 5
- Theme value scale maps low/high values to distinct colors

Expected behavior:

- Layout remains rectangular and readable
- Text may auto-reduce size
- Color scale applied consistently to all numeric cells

### 8.3 Example C: Wildcard Masked Matrix

Input generated from `apply_wildcard_mask`:

```json
[[1, "*", 3], ["*", 5, 6], [7, 8, "*"]]
```

Expected behavior:

- Masked cells include `data-masked="true"`
- Masked style class and accessible labels are present
- Tooltips distinguish literal value vs masked token

### 8.4 Example D: Interactive Hover State

Interaction model:

- On `pointerenter`, add `plate71-cell--hover`
- On `pointerleave`, remove hover class

Optional enhancement:

- Emit host callback payload: `{row, col, value, masked, eventType}`

### 8.5 Example E: Responsive Rendering

Responsive plate rules:

- Parent container controls final display size
- SVG scales through viewBox
- Font autoscaling keeps labels legible

ASCII responsive concept:

```text
Desktop:  [ 10x10 visible, full labels ]
Tablet:   [ 10x10 visible, compact labels ]
Mobile:   [ 10x10 visible, minimal labels + tooltip on hover/tap ]
```

---

## 9. Future Extensions

### 9.1 Animation Support

Potential animation scope:

- Transition between operation outputs
- Cell value morph/fade transitions
- Mask/unmask transitions

Animation should remain optional and disable-able for accessibility/performance.

### 9.2 Interactive Matrix Operations

Future interactions may include:

- Cell/range selection
- Copy selected values
- In-place transformation previews
- Operation playback timeline

### 9.3 Multi-Plate Layouts

Support patterns:

- Side-by-side comparison (before/after)
- Overlay diff plate
- Linked hover/selection across multiple plates

### 9.4 Export Formats

Primary output remains SVG, with optional downstream exporters:

- PNG snapshot
- PDF embedding

### 9.5 Real-Time Synchronization

Future MATRIUN integration may stream operation updates to Plate71:

- Renderer subscribes to matrix operation events
- Incremental cell updates applied in near real time
- Sync model remains transport-agnostic (callback, pub/sub, or state store)

---

## 10. Implementation Notes and Non-Prescriptive Guidance

### 10.1 Compatibility Goals

Implementations should prioritize:

- Stable input/output contracts
- Backward-compatible config evolution
- Predictable accessibility and interaction semantics

### 10.2 Allowed Variation

This spec does **not** require:

- A single rendering library/framework
- A fixed plugin architecture shape
- One event system design

Equivalent implementations are acceptable if they preserve external behavior described here.

### 10.3 API Evolution Strategy

To support future change:

- Version renderer config (`schemaVersion`)
- Treat unknown config keys as non-fatal by default
- Document deprecations before removal

#### 10.3.1 Example Versioned Config Envelope

```json
{
  "schemaVersion": "0.1.0",
  "plate71": {
    "geometry": {"mode": "cartesian"}
  }
}
```

#### 10.3.2 Error Handling Guidance

Renderers should provide structured errors for:

- Non-rectangular matrix input
- Invalid numeric bounds in scales
- Unsupported projection configuration

Error payload example:

```json
{
  "code": "PLATE71_INVALID_MATRIX_SHAPE",
  "message": "Matrix rows have inconsistent lengths",
  "details": {"row": 4, "expected": 10, "actual": 9}
}
```

##### 10.3.2.1 Error Classification

Implementations may classify errors as `validation`, `configuration`, or `runtime` to improve host-side diagnostics and user-facing messaging.

### 10.4 Relationship to Existing MATRIUN Docs

This specification extends current MATRIUN docs by defining visualization contracts while keeping matrix computation concerns in core APIs.

Cross-reference points:

- [Root README](../README.md) for project scope and CLI usage
- [Docs index](./index.md) for navigation
- `matriun.py` for matrix operation behavior

Plate71 is introduced as a feature preview, not a completed runtime feature in current MATRIUN releases.
