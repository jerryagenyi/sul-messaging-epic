#!/usr/bin/env python3
"""
Convert Figma SVG files to PNG baselines
Prepares your Figma designs for visual testing
"""
import os
import sys
from pathlib import Path
import subprocess

class FigmaSVGConverter:
    """Convert SVG files to PNG for visual testing"""
    
    def __init__(self):
        self.figma_dir = Path("messaging-epic-figma-svg")
        self.baselines_dir = Path("design-specs/baselines")
        self.baselines_dir.mkdir(parents=True, exist_ok=True)
    
    def convert_all_svgs(self):
        """Convert all SVG files to PNG baselines"""
        
        if not self.figma_dir.exists():
            print(f"Error: {self.figma_dir} not found")
            return False
        
        svg_files = list(self.figma_dir.glob("*.svg"))
        
        if not svg_files:
            print(f"No SVG files found in {self.figma_dir}")
            return False
        
        print(f"Found {len(svg_files)} SVG files to convert:")
        
        for svg_file in svg_files:
            print(f"  - {svg_file.name}")
            
            # Create baseline name
            baseline_name = self._create_baseline_name(svg_file.name)
            baseline_path = self.baselines_dir / f"{baseline_name}.png"
            
            # Convert SVG to PNG
            success = self._convert_svg_to_png(svg_file, baseline_path)
            
            if success:
                print(f"    ✅ → {baseline_path}")
            else:
                print(f"    ❌ Conversion failed")
        
        return True
    
    def _create_baseline_name(self, svg_filename):
        """Create standardized baseline name from SVG filename"""
        
        # Remove .svg extension
        name = svg_filename.replace('.svg', '')
        
        # Convert to lowercase and replace spaces/hyphens with underscores
        name = name.lower().replace(' ', '_').replace('-', '_')
        
        # Map specific files to standard names
        name_mapping = {
            'company_dashboard___message': 'company_dashboard',
            'company_dashboard___message_1': 'company_dashboard_variant_1',
            'company_dashboard___message_2': 'company_dashboard_variant_2',
            'volunteer_dashboard___message': 'volunteer_dashboard',
            'volunteer_dashboard___message_1': 'volunteer_dashboard_variant_1',
        }
        
        return name_mapping.get(name, name)
    
    def _convert_svg_to_png(self, svg_path, png_path):
        """Convert single SVG file to PNG"""
        
        # Method 1: Try using cairosvg (Python library)
        try:
            import cairosvg
            cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=1440)
            return True
        except ImportError:
            print("    cairosvg not available, trying alternative methods...")
        except Exception as e:
            print(f"    cairosvg failed: {e}")
        
        # Method 2: Try using Inkscape command line
        try:
            result = subprocess.run([
                'inkscape',
                '--export-type=png',
                '--export-width=1440',
                f'--export-filename={png_path}',
                str(svg_path)
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0 and png_path.exists():
                return True
            else:
                print(f"    Inkscape failed: {result.stderr}")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            print("    Inkscape not available")
        except Exception as e:
            print(f"    Inkscape error: {e}")
        
        # Method 3: Try using rsvg-convert
        try:
            result = subprocess.run([
                'rsvg-convert',
                '-w', '1440',
                '-f', 'png',
                '-o', str(png_path),
                str(svg_path)
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0 and png_path.exists():
                return True
            else:
                print(f"    rsvg-convert failed: {result.stderr}")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            print("    rsvg-convert not available")
        except Exception as e:
            print(f"    rsvg-convert error: {e}")
        
        # Method 4: Create placeholder PNG with instructions
        return self._create_placeholder_png(svg_path, png_path)
    
    def _create_placeholder_png(self, svg_path, png_path):
        """Create placeholder PNG with conversion instructions"""
        
        try:
            from PIL import Image, ImageDraw, ImageFont
            
            # Create placeholder image
            img = Image.new('RGB', (1440, 900), 'white')
            draw = ImageDraw.Draw(img)
            
            try:
                title_font = ImageFont.truetype("arial.ttf", 32)
                body_font = ImageFont.truetype("arial.ttf", 18)
            except:
                title_font = ImageFont.load_default()
                body_font = ImageFont.load_default()
            
            # Add text
            title = f"Manual Conversion Required"
            subtitle = f"SVG: {svg_path.name}"
            instructions = [
                "To create this baseline:",
                "1. Open the SVG file in a browser or design tool",
                "2. Take a screenshot at 1440px width",
                "3. Save as PNG and replace this placeholder",
                "",
                "Or install conversion tools:",
                "pip install cairosvg",
                "# or install Inkscape/rsvg-convert"
            ]
            
            # Draw title
            draw.text((50, 50), title, fill='red', font=title_font)
            draw.text((50, 100), subtitle, fill='black', font=body_font)
            
            # Draw instructions
            y_pos = 150
            for instruction in instructions:
                draw.text((50, y_pos), instruction, fill='black', font=body_font)
                y_pos += 25
            
            # Add border
            draw.rectangle([(10, 10), (1430, 890)], outline='red', width=3)
            
            img.save(png_path)
            return True
            
        except Exception as e:
            print(f"    Failed to create placeholder: {e}")
            return False
    
    def create_conversion_guide(self):
        """Create guide for manual SVG conversion"""
        
        guide_content = """# Figma SVG to PNG Conversion Guide

## Automatic Conversion

Run the conversion script:
```bash
python tools/convert_figma_svgs.py
```

## Manual Conversion (if automatic fails)

### Method 1: Browser Screenshot
1. Open SVG file in Chrome/Firefox
2. Set browser width to 1440px
3. Take full-page screenshot
4. Save as PNG in `design-specs/baselines/`

### Method 2: Design Tools
1. Open SVG in Figma/Sketch/Adobe XD
2. Export as PNG at 1440px width
3. Save in `design-specs/baselines/`

### Method 3: Command Line Tools

Install cairosvg:
```bash
pip install cairosvg
python -c "import cairosvg; cairosvg.svg2png(url='input.svg', write_to='output.png', output_width=1440)"
```

Install Inkscape:
```bash
inkscape --export-type=png --export-width=1440 --export-filename=output.png input.svg
```

## File Naming Convention

Your SVG files should be converted to:
- `Company Dashboard - Message.svg` → `company_dashboard.png`
- `Volunteer Dashboard - Message.svg` → `volunteer_dashboard.png`
- `Company Dashboard - Message-1.svg` → `company_dashboard_variant_1.png`

## Using Baselines in Tests

Once converted, your tests will use these baselines:
```python
def test_company_dashboard_visual():
    screenshot = take_screenshot()
    baseline = "design-specs/baselines/company_dashboard.png"
    similarity = compare_images(screenshot, baseline)
    assert similarity > 0.85
```
"""
        
        guide_path = Path("FIGMA_CONVERSION_GUIDE.md")
        with open(guide_path, 'w') as f:
            f.write(guide_content)
        
        return guide_path

def main():
    converter = FigmaSVGConverter()
    
    print("🎨 Figma SVG to PNG Converter")
    print("=" * 40)
    
    # Create conversion guide
    guide_path = converter.create_conversion_guide()
    print(f"📖 Created conversion guide: {guide_path}")
    
    # Convert SVG files
    success = converter.convert_all_svgs()
    
    if success:
        print("\n✅ Conversion process completed!")
        print(f"📁 Check {converter.baselines_dir} for results")
        print("\nNext steps:")
        print("1. Review generated PNG files")
        print("2. Replace any placeholder images with proper conversions")
        print("3. Run visual tests: python run_tests.py --visual")
    else:
        print("\n❌ Conversion failed")
        print(f"📖 See {guide_path} for manual conversion instructions")

if __name__ == "__main__":
    main()
