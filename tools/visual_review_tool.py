#!/usr/bin/env python3
"""
Visual Review Tool for First-Time Implementation
Helps QA team review implementation against Figma designs
"""
import os
import sys
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json
from datetime import datetime

class VisualReviewTool:
    """Tool for managing visual review process"""
    
    def __init__(self):
        self.review_dir = Path("visual-review")
        self.baselines_dir = Path("design-specs/baselines")
        self.figma_dir = Path("messaging-epic-figma-svg")
        self.screenshots_dir = Path("screenshots")
        
        # Create directories
        for dir_path in [self.review_dir, self.baselines_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def create_review_comparison(self, component_name, screenshot_path, figma_path):
        """Create side-by-side comparison for manual review"""
        
        try:
            # Load images
            screenshot = Image.open(screenshot_path)
            
            # Handle SVG conversion (simplified - would need proper SVG handling)
            if figma_path.endswith('.svg'):
                print(f"Note: SVG conversion needed for {figma_path}")
                print("Please convert SVG to PNG manually or use svg2png tool")
                figma_image = self._create_placeholder_image("Figma Design\n(Convert SVG to PNG)")
            else:
                figma_image = Image.open(figma_path)
            
            # Resize images to same height for comparison
            max_height = max(screenshot.height, figma_image.height)
            
            screenshot_resized = self._resize_maintain_aspect(screenshot, height=max_height)
            figma_resized = self._resize_maintain_aspect(figma_image, height=max_height)
            
            # Create side-by-side comparison
            total_width = screenshot_resized.width + figma_resized.width + 60  # 60px gap
            comparison = Image.new('RGB', (total_width, max_height + 100), 'white')
            
            # Paste images
            comparison.paste(screenshot_resized, (20, 80))
            comparison.paste(figma_resized, (screenshot_resized.width + 40, 80))
            
            # Add labels
            draw = ImageDraw.Draw(comparison)
            
            try:
                font = ImageFont.truetype("arial.ttf", 24)
                title_font = ImageFont.truetype("arial.ttf", 32)
            except:
                font = ImageFont.load_default()
                title_font = ImageFont.load_default()
            
            # Title
            draw.text((20, 20), f"Visual Review: {component_name}", fill='black', font=title_font)
            
            # Labels
            draw.text((20, 50), "Implementation", fill='black', font=font)
            draw.text((screenshot_resized.width + 40, 50), "Figma Design", fill='black', font=font)
            
            # Save comparison
            comparison_path = self.review_dir / f"{component_name}_comparison.png"
            comparison.save(comparison_path)
            
            return comparison_path
            
        except Exception as e:
            print(f"Error creating comparison: {e}")
            return None
    
    def create_review_checklist(self, component_name, specs=None):
        """Create review checklist for QA team"""
        
        checklist = {
            "component": component_name,
            "review_date": datetime.now().isoformat(),
            "reviewer": "",
            "status": "pending",
            "checks": {
                "layout": {
                    "description": "Overall layout matches Figma design",
                    "status": "pending",
                    "notes": ""
                },
                "colors": {
                    "description": "Colors match design system and Figma",
                    "status": "pending", 
                    "notes": ""
                },
                "typography": {
                    "description": "Fonts, sizes, weights match specifications",
                    "status": "pending",
                    "notes": ""
                },
                "spacing": {
                    "description": "Margins, padding, gaps match design",
                    "status": "pending",
                    "notes": ""
                },
                "interactive_states": {
                    "description": "Hover, focus, active states work correctly",
                    "status": "pending",
                    "notes": ""
                },
                "responsive": {
                    "description": "Component works on mobile/tablet/desktop",
                    "status": "pending",
                    "notes": ""
                }
            }
        }
        
        # Add component-specific checks if specs provided
        if specs:
            for spec_name, spec_value in specs.items():
                checklist["checks"][spec_name] = {
                    "description": f"Verify {spec_name}: {spec_value}",
                    "status": "pending",
                    "notes": ""
                }
        
        # Save checklist
        checklist_path = self.review_dir / f"{component_name}_checklist.json"
        with open(checklist_path, 'w') as f:
            json.dump(checklist, f, indent=2)
        
        return checklist_path
    
    def generate_review_report(self, component_name):
        """Generate HTML review report"""
        
        comparison_path = self.review_dir / f"{component_name}_comparison.png"
        checklist_path = self.review_dir / f"{component_name}_checklist.json"
        
        # Load checklist if exists
        checklist = {}
        if checklist_path.exists():
            with open(checklist_path, 'r') as f:
                checklist = json.load(f)
        
        # Generate HTML report
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Visual Review: {component_name}</title>
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 40px; }}
                .header {{ background: #f6f8fa; padding: 20px; border-radius: 8px; margin-bottom: 30px; }}
                .comparison {{ text-align: center; margin: 30px 0; }}
                .comparison img {{ max-width: 100%; border: 1px solid #d1d9e0; border-radius: 8px; }}
                .checklist {{ background: white; border: 1px solid #d1d9e0; border-radius: 8px; padding: 20px; }}
                .check-item {{ margin: 15px 0; padding: 15px; border-left: 4px solid #e5e7eb; }}
                .check-pending {{ border-left-color: #f59e0b; }}
                .check-pass {{ border-left-color: #10b981; }}
                .check-fail {{ border-left-color: #ef4444; }}
                .actions {{ margin-top: 30px; text-align: center; }}
                .btn {{ padding: 12px 24px; margin: 0 10px; border: none; border-radius: 6px; cursor: pointer; }}
                .btn-approve {{ background: #10b981; color: white; }}
                .btn-reject {{ background: #ef4444; color: white; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🎨 Visual Review: {component_name}</h1>
                <p>Review implementation against Figma design and design system standards</p>
                <p><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
            </div>
            
            <div class="comparison">
                <h2>Visual Comparison</h2>
                <img src="{component_name}_comparison.png" alt="Visual comparison">
            </div>
            
            <div class="checklist">
                <h2>Review Checklist</h2>
        """
        
        # Add checklist items
        if checklist.get('checks'):
            for check_name, check_data in checklist['checks'].items():
                status_class = f"check-{check_data.get('status', 'pending')}"
                html_content += f"""
                <div class="check-item {status_class}">
                    <h3>{check_name.replace('_', ' ').title()}</h3>
                    <p>{check_data.get('description', '')}</p>
                    <p><strong>Status:</strong> {check_data.get('status', 'pending')}</p>
                    <p><strong>Notes:</strong> {check_data.get('notes', 'No notes')}</p>
                </div>
                """
        
        html_content += f"""
            </div>
            
            <div class="actions">
                <h2>Review Actions</h2>
                <p>After reviewing the comparison and checklist:</p>
                <button class="btn btn-approve" onclick="approveImplementation()">✅ Approve & Create Baseline</button>
                <button class="btn btn-reject" onclick="rejectImplementation()">❌ Reject & Request Changes</button>
            </div>
            
            <script>
                function approveImplementation() {{
                    alert('Run: python tools/visual_review_tool.py --approve {component_name}');
                }}
                
                function rejectImplementation() {{
                    alert('Run: python tools/visual_review_tool.py --reject {component_name} --feedback "Your feedback here"');
                }}
            </script>
        </body>
        </html>
        """
        
        # Save HTML report
        report_path = self.review_dir / f"{component_name}_review.html"
        with open(report_path, 'w') as f:
            f.write(html_content)
        
        return report_path
    
    def approve_implementation(self, component_name):
        """Approve implementation and create baseline"""
        
        # Find latest screenshot
        screenshot_files = list(self.screenshots_dir.glob(f"*{component_name}*.png"))
        if not screenshot_files:
            print(f"No screenshots found for {component_name}")
            return False
        
        latest_screenshot = max(screenshot_files, key=os.path.getctime)
        
        # Create baseline
        baseline_path = self.baselines_dir / f"{component_name}_baseline.png"
        
        # Copy screenshot as baseline
        import shutil
        shutil.copy2(latest_screenshot, baseline_path)
        
        # Update checklist status
        checklist_path = self.review_dir / f"{component_name}_checklist.json"
        if checklist_path.exists():
            with open(checklist_path, 'r') as f:
                checklist = json.load(f)
            
            checklist['status'] = 'approved'
            checklist['approval_date'] = datetime.now().isoformat()
            
            with open(checklist_path, 'w') as f:
                json.dump(checklist, f, indent=2)
        
        print(f"✅ {component_name} approved!")
        print(f"📸 Baseline created: {baseline_path}")
        print(f"🧪 Future tests will compare against this baseline")
        
        return True
    
    def reject_implementation(self, component_name, feedback):
        """Reject implementation with feedback"""
        
        # Update checklist status
        checklist_path = self.review_dir / f"{component_name}_checklist.json"
        if checklist_path.exists():
            with open(checklist_path, 'r') as f:
                checklist = json.load(f)
            
            checklist['status'] = 'rejected'
            checklist['rejection_date'] = datetime.now().isoformat()
            checklist['feedback'] = feedback
            
            with open(checklist_path, 'w') as f:
                json.dump(checklist, f, indent=2)
        
        print(f"❌ {component_name} rejected")
        print(f"📝 Feedback: {feedback}")
        print(f"🔄 Developer should address feedback and resubmit")
        
        return True
    
    def _resize_maintain_aspect(self, image, height):
        """Resize image maintaining aspect ratio"""
        aspect_ratio = image.width / image.height
        new_width = int(height * aspect_ratio)
        return image.resize((new_width, height), Image.Resampling.LANCZOS)
    
    def _create_placeholder_image(self, text):
        """Create placeholder image with text"""
        img = Image.new('RGB', (400, 300), 'lightgray')
        draw = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()
        
        # Center text
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (400 - text_width) // 2
        y = (300 - text_height) // 2
        
        draw.text((x, y), text, fill='black', font=font)
        
        return img

def main():
    parser = argparse.ArgumentParser(description="Visual Review Tool")
    parser.add_argument('--component', required=True, help='Component name to review')
    parser.add_argument('--screenshot', help='Path to implementation screenshot')
    parser.add_argument('--figma', help='Path to Figma design file')
    parser.add_argument('--approve', action='store_true', help='Approve implementation')
    parser.add_argument('--reject', action='store_true', help='Reject implementation')
    parser.add_argument('--feedback', help='Rejection feedback')
    
    args = parser.parse_args()
    
    tool = VisualReviewTool()
    
    if args.approve:
        tool.approve_implementation(args.component)
    elif args.reject:
        if not args.feedback:
            print("Error: --feedback required when rejecting")
            sys.exit(1)
        tool.reject_implementation(args.component, args.feedback)
    else:
        # Create review
        if not args.screenshot or not args.figma:
            print("Error: --screenshot and --figma required for review creation")
            sys.exit(1)
        
        # Create comparison
        comparison_path = tool.create_review_comparison(
            args.component, args.screenshot, args.figma
        )
        
        # Create checklist
        checklist_path = tool.create_review_checklist(args.component)
        
        # Generate report
        report_path = tool.generate_review_report(args.component)
        
        print(f"📋 Review created for {args.component}")
        print(f"🖼️  Comparison: {comparison_path}")
        print(f"✅ Checklist: {checklist_path}")
        print(f"📄 Report: {report_path}")
        print(f"🌐 Open {report_path} in browser to review")

if __name__ == "__main__":
    main()
