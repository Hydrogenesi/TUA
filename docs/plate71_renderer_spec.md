# Plate71 Renderer Specification

## Overview

**Plate71** is a visualization system for rendering MATRIUN matrices as interactive SVG/HTML visual plates. It transforms numeric matrix data into a structured, visually rich canvas where each cell is rendered as a discrete unit with configurable styling, layout, and interactivity.

### Purpose

- **Bridge** pure matrix operations to visual representation
- **Enable** interactive exploration of matrix data
- **Provide** foundation for future visualization features (animation, multi-plate layouts, export)
- **Maintain** performance and accessibility standards

### Design Philosophy

- **Data-driven:** SVG is generated from configuration + matrix data, never mutated
- **Semantic:** HTML structure is meaningful; accessibility is built-in
- **Extensible:** Configuration schema supports future enhancements
- **Pure:** No external rendering library required; works anywhere SVG is supported

---

## Architecture

### Data Flow

```
MATRIUN Matrix
    ↓
[matrix: [[1, 2], [3, 4]], config: {...}]
    ↓
Renderer Engine
    ├─ Layout Phase
    ├─ Style Phase
    └─ Render Phase
    ↓
SVG Markup (with semantic structure)
    ↓
HTML Display / Export / Cache
```

### Core Components

1. **Matrix Data Model** — Numeric data + metadata (types, states, masks)
2. **Layout Engine** — Computes cell positions, sizes, alignment
3. **Style System** — Maps data values to visual attributes (colors, borders, text)
4. **Renderer** — Generates SVG elements with semantic markup
5. **Configuration** — Geometry, colors, typography, interactions

---

## Plate Geometry

### Canvas Model

A **plate** is a rectangular canvas that displays a matrix as a grid of cells.

```
┌─────────────────────────────────────────┐
│  margin_top                             │
│  ┌──────────────────────────────────┐   │
│  │  Grid (rows × cols)              │   │
│  │  ┌────┐ ┌────┐ ┌────┐          │   │
│  │  │ 0,0│ │ 0,1│ │ 0,2│          │   │
│  │  ├────┤ ├────┤ ├────┤          │   │
│  │  │ 1,0│ │ 1,1│ │ 1,2│          │   │
│  │  └────┘ └────┘ └────┘          │   │
│  └──────────────────────────────────┘   │
│  margin_bottom                          │
└─────────────────────────────────────────┘
```

### Coordinate Systems

#### Cartesian (Default)

- **Origin:** top-left corner (0, 0)
- **X-axis:** increases left-to-right
- **Y-axis:** increases top-to-bottom
- **Example:** Cell at row 1, col 2 is at screen position (x₀ + 2 × cell_width, y₀ + 1 × cell_height)

#### Polar (Future)

- **Origin:** center
- **Angle:** radial position
- **Radius:** distance from center
- **Use case:** Circular/radial matrix layouts

### Cell Rendering

Each cell is rendered as a rectangular region with optional borders, padding, and text.

**Cell Dimensions:**
- `cell_width` — width of a single cell (pixels)
- `cell_height` — height of a single cell (pixels)
- `cell_padding` — internal padding around text (pixels)
- `cell_border_width` — thickness of cell border (pixels)
- `cell_gap` — space between cells (pixels)

**Example (3×3 matrix):**
```
cell_width = 40px
cell_height = 40px
cell_gap = 2px
cell_padding = 2px

Grid dimensions = 3 × 40 + 2 × 2 = 124px (width)
```

---

## Data Model

### Matrix Representation

Matrices are passed as standard Python lists-of-lists:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### Cell Metadata

Each cell may carry additional information:

```python
cell_data = {
    "value": 42,           # Numeric value
    "type": "number",      # Type hint: number, text, boolean, null
    "state": "normal",     # Visual state: normal, masked, selected, error
    "format": ".2f"        # Format specifier for display
}
```

### Masked Values

Cells with `state: "masked"` (from `apply_wildcard_mask()`) are visually distinct:

```python
masked_matrix = [[1, None, 3], [None, 5, None]]
# None values render as empty cells or with a special glyph
```

### Type-Based Styling

Cells can be styled based on their type:

- **number:** Renders right-aligned with numeric formatting
- **text:** Renders left-aligned
- **boolean:** Renders with a symbol (✓/✗) or colored background
- **null:** Renders as empty or with a placeholder glyph

---

## Rendering Process

### Phase 1: Input Validation

- Verify matrix dimensions are valid (non-empty)
- Check configuration schema compliance
- Handle edge cases (empty matrix, single cell, very large matrix)

### Phase 2: Layout Computation

```
For each row i:
  y = plate.margin_top + i × (cell_height + cell_gap)
  
  For each column j:
    x = plate.margin_left + j × (cell_width + cell_gap)
    
    cell_rect = {
      x, y, cell_width, cell_height,
      inner_padding, border_width
    }
```

### Phase 3: Style Mapping

```
For each cell(i, j):
  value = matrix[i][j]
  
  color = color_scheme.map(value)
  text_color = contrast(color)
  border_color = theme.border_default
  
  if cell.state == "masked":
    color = theme.masked_color
    text = "–" (dash)
  else:
    text = format_value(value, cell.format)
```

### Phase 4: SVG Generation

```xml
<svg viewBox="0 0 width height">
  <defs>
    <!-- Gradients, patterns, styles -->
    <style>
      .cell { ... }
      .cell.masked { ... }
      .cell-text { ... }
    </style>
  </defs>
  
  <g id="plate">
    <!-- For each cell -->
    <g class="cell" data-row="i" data-col="j">
      <rect x="x" y="y" width="w" height="h" class="cell-bg"/>
      <text x="x" y="y" class="cell-text">value</text>
    </g>
  </g>
</svg>
```

### Phase 5: Output & Caching

- Serialize SVG to string
- Cache rendered SVG (keyed by matrix hash + config hash)
- Support partial updates (refresh only changed cells)

---

## Configuration Schema

### Plate Geometry Config

```json
{
  "plate": {
    "width": 400,
    "height": 400,
    "margin_top": 10,
    "margin_bottom": 10,
    "margin_left": 10,
    "margin_right": 10,
    "cell_width": 40,
    "cell_height": 40,
    "cell_gap": 2,
    "cell_padding": 2,
    "cell_border_width": 1,
    "projection": "cartesian"
  }
}
```

### Color Scheme Config

```json
{
  "colors": {
    "scheme": "viridis",
    "min_value": 0,
    "max_value": 100,
    "color_map": {
      "0": "#440154",
      "25": "#31688e",
      "50": "#35b779",
      "75": "#fde724",
      "100": "#fde724"
    },
    "contrast_threshold": 127,
    "text_light": "#ffffff",
    "text_dark": "#000000",
    "border_default": "#cccccc",
    "border_selected": "#0066cc",
    "masked_color": "#f0f0f0"
  }
}
```

### Typography Config

```json
{
  "typography": {
    "font_family": "monospace",
    "font_size": 12,
    "font_weight": "normal",
    "text_align": "center",
    "line_height": 1.2,
    "letter_spacing": 0
  }
}
```

### Full Configuration Example

```json
{
  "plate": { ... },
  "colors": { ... },
  "typography": { ... },
  "interactive": {
    "enable_hover": true,
    "enable_select": false,
    "enable_zoom": false
  },
  "accessibility": {
    "enable_aria_labels": true,
    "enable_descriptions": true
  }
}
```

---

## SVG Output Specification

### Element Structure

```xml
<svg 
  class="plate71-renderer"
  viewBox="0 0 width height"
  xmlns="http://www.w3.org/2000/svg"
>
  <defs>
    <style>
      .cell { cursor: pointer; }
      .cell.masked { opacity: 0.5; }
      .cell:hover { stroke-width: 2; }
      .cell-text { 
        font-family: monospace;
        font-size: 12px;
        text-anchor: middle;
      }
    </style>
  </defs>
  
  <g id="plate" role="grid">
    <g 
      class="cell"
      data-row="0"
      data-col="0"
      role="gridcell"
      aria-label="Cell (0,0): value 42"
    >
      <rect class="cell-bg" x="10" y="10" width="40" height="40"/>
      <text class="cell-text" x="30" y="35">42</text>
    </g>
    <!-- More cells... -->
  </g>
</svg>
```

### Semantic Attributes

- **`data-row`, `data-col`** — Cell position
- **`data-value`** — Original numeric value
- **`data-state`** — Cell state (normal, masked, selected)
- **`role="grid"`, `role="gridcell"`** — ARIA roles for accessibility

### Performance Considerations

- **Group clipping:** Use `<clipPath>` to hide cells outside viewport
- **Transforms:** Use CSS transforms for zoom/pan instead of recomputing SVG
- **Caching:** Store rendered SVG; regenerate only on data change
- **Lazy rendering:** For very large matrices, render visible region first

---

## Examples

### Example 1: Simple 3×3 Matrix

**Input:**
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
config = default_config()
```

**Output:**
```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┴───┴───┘
```

### Example 2: 5×5 with Color Mapping

Values from 0–25 mapped to color gradient (blue → red).

```
┌──┬──┬──┬──┬──┐
│ 0│ 5│10│15│20│  ← values
├──┼──┼──┼──┼──┤
│ 5│10│15│20│25│
├──┼──┼──┼──┼──┤
│10│15│20│25│10│
├──┼──┼──┼──┼──┤
│15│20│25│10│ 5│
├──┼──┼──┼──┼──┤
│20│25│10│ 5│ 0│
└──┴──┴──┴──┴──┘
```

Cells rendered with background colors interpolated from the gradient.

### Example 3: Masked Matrix

**Input:**
```python
matrix = [[1, None, 3], [None, 5, None], [7, 8, 9]]
```

**Rendering:**
- Cells with `None` have distinct visual treatment (lighter color, placeholder glyph)
- Hover state highlights the mask pattern

---

## Future Extensions

### Animation Support

- **Fade:** Transition between two matrices
- **Pulse:** Highlight changed cells
- **Ripple:** Wave effect from origin point

**API:**
```python
renderer.animate(matrix_before, matrix_after, duration_ms=500)
```

### Interactive Operations

- **Select:** Click to select cells; show selection UI
- **Copy:** Copy selected cells to clipboard (CSV format)
- **Transform:** Apply operations (transpose, scale) interactively

**Events:**
```javascript
plate.on("cell-click", (row, col, value) => { ... })
plate.on("selection-change", (cells) => { ... })
```

### Multi-Plate Layouts

Display multiple matrices side-by-side or overlaid.

```python
layout = MultiPlateLayout([matrix1, matrix2, matrix3])
svg = renderer.render(layout)
```

### Export Formats

- **PNG:** Render to canvas, export as image
- **PDF:** Vector export for documents
- **Data URLs:** Inline SVG for sharing
- **LaTeX:** Tikz export for academic papers

### Real-Time Synchronization

Listen to matrix operations and auto-refresh plate.

```python
renderer = Plate71Renderer(config)
matrix = create_identity_matrix(5)

# Whenever matrix changes, re-render
matrix.on_change(lambda m: renderer.render(m))

result = multiply_matrices(matrix, other)
# Plate auto-updates!
```

---

## Implementation Notes

### For Python Implementation

Use standard library `xml.etree.ElementTree` or `svgwrite` to generate SVG.

```python
from xml.etree import ElementTree as ET

def render_plate(matrix, config):
    svg = ET.Element("svg", {
        "viewBox": f"0 0 {config.width} {config.height}",
        "xmlns": "http://www.w3.org/2000/svg"
    })
    
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            x = config.margin_left + j * (config.cell_width + config.cell_gap)
            y = config.margin_top + i * (config.cell_height + config.cell_gap)
            
            cell_group = ET.SubElement(svg, "g", {
                "class": "cell",
                "data-row": str(i),
                "data-col": str(j)
            })
            
            rect = ET.SubElement(cell_group, "rect", {
                "x": str(x),
                "y": str(y),
                "width": str(config.cell_width),
                "height": str(config.cell_height)
            })
            
            text = ET.SubElement(cell_group, "text", {
                "x": str(x + config.cell_width / 2),
                "y": str(y + config.cell_height / 2)
            })
            text.text = str(value) if value is not None else "–"
    
    return ET.tostring(svg, encoding="unicode")
```

### For JavaScript Implementation

Use DOM APIs or a library like `D3.js` for advanced layouts.

```javascript
function renderPlate(matrix, config) {
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("viewBox", `0 0 ${config.width} ${config.height}`);
  
  matrix.forEach((row, i) => {
    row.forEach((value, j) => {
      const x = config.marginLeft + j * (config.cellWidth + config.cellGap);
      const y = config.marginTop + i * (config.cellHeight + config.cellGap);
      
      const cell = document.createElementNS("http://www.w3.org/2000/svg", "g");
      cell.setAttribute("class", "cell");
      cell.setAttribute("data-row", i);
      cell.setAttribute("data-col", j);
      
      const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
      rect.setAttribute("x", x);
      rect.setAttribute("y", y);
      rect.setAttribute("width", config.cellWidth);
      rect.setAttribute("height", config.cellHeight);
      
      const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
      text.setAttribute("x", x + config.cellWidth / 2);
      text.setAttribute("y", y + config.cellHeight / 2);
      text.textContent = value !== null ? String(value) : "–";
      
      cell.appendChild(rect);
      cell.appendChild(text);
      svg.appendChild(cell);
    });
  });
  
  return svg;
}
```

---

## Conclusion

Plate71 establishes a bridge between MATRIUN's pure matrix operations and interactive visual representation. By defining a clear architecture, configuration schema, and SVG output structure, it enables future visualization features while maintaining simplicity, performance, and accessibility.

**Next Steps:**
1. Create a `plate71.py` module implementing the renderer
2. Add test suite for SVG output correctness
3. Implement caching and performance optimizations
4. Add CLI commands for rendering matrices to SVG
5. Extend with animation and interactivity features
