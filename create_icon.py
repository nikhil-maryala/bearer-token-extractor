#!/usr/bin/env python3
"""
Custom icon generator for Bearer Token Extractor
Creates a professional-looking icon with:
- UiPath orange gradient background
- Key symbol (representing token/authentication)
- Code brackets (representing extraction)
- "T" badge (for Token)
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import math
except ImportError:
    print("PIL/Pillow not installed. Installing...")
    import subprocess
    subprocess.check_call(['pip3', 'install', 'pillow'])
    from PIL import Image, ImageDraw, ImageFont
    import math


def create_icon(size):
    """Create icon at specified size"""
    # Create image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Scale factor for different sizes
    scale = size / 128.0

    # Colors
    bg_color1 = (250, 70, 22)  # UiPath orange
    bg_color2 = (255, 107, 53)  # Lighter orange
    key_color = (255, 215, 0)  # Gold
    white = (255, 255, 255, 255)
    green = (76, 175, 80)  # Green for "T" badge

    # Draw rounded rectangle background with gradient simulation
    corner_radius = int(24 * scale)

    # Simple gradient by drawing multiple rectangles
    for i in range(size):
        ratio = i / size
        r = int(bg_color1[0] + (bg_color2[0] - bg_color1[0]) * ratio)
        g = int(bg_color1[1] + (bg_color2[1] - bg_color1[1]) * ratio)
        b = int(bg_color1[2] + (bg_color2[2] - bg_color1[2]) * ratio)

        # Draw horizontal line with rounded corners
        y = i
        x_start = 0
        x_end = size

        # Apply corner rounding
        if i < corner_radius:
            x_offset = int(corner_radius - math.sqrt(corner_radius**2 - (corner_radius - i)**2))
            x_start = x_offset
            x_end = size - x_offset
        elif i >= size - corner_radius:
            dist_from_bottom = size - i
            x_offset = int(corner_radius - math.sqrt(corner_radius**2 - (corner_radius - dist_from_bottom)**2))
            x_start = x_offset
            x_end = size - x_offset

        if x_end > x_start:
            draw.line([(x_start, y), (x_end, y)], fill=(r, g, b, 255), width=1)

    # Draw key icon
    key_center_x = int(50 * scale)
    key_center_y = int(45 * scale)
    key_radius = int(18 * scale)
    key_inner_radius = int(8 * scale)

    # Key circle (head)
    draw.ellipse(
        [key_center_x - key_radius, key_center_y - key_radius,
         key_center_x + key_radius, key_center_y + key_radius],
        fill=key_color, outline=white, width=int(3 * scale)
    )

    # Inner circle
    draw.ellipse(
        [key_center_x - key_inner_radius, key_center_y - key_inner_radius,
         key_center_x + key_inner_radius, key_center_y + key_inner_radius],
        fill=None, outline=white, width=int(3 * scale)
    )

    # Key shaft
    shaft_x = int(56 * scale)
    shaft_y = int(40 * scale)
    shaft_width = int(35 * scale)
    shaft_height = int(10 * scale)

    draw.rounded_rectangle(
        [shaft_x, shaft_y, shaft_x + shaft_width, shaft_y + shaft_height],
        radius=int(2 * scale), fill=key_color, outline=white, width=int(2 * scale)
    )

    # Key teeth
    tooth1_x = int(75 * scale)
    tooth1_y = int(50 * scale)
    tooth1_w = int(6 * scale)
    tooth1_h = int(8 * scale)

    draw.rounded_rectangle(
        [tooth1_x, tooth1_y, tooth1_x + tooth1_w, tooth1_y + tooth1_h],
        radius=int(1 * scale), fill=key_color, outline=white, width=int(2 * scale)
    )

    tooth2_x = int(83 * scale)
    tooth2_h = int(12 * scale)

    draw.rounded_rectangle(
        [tooth2_x, tooth1_y, tooth2_x + tooth1_w, tooth1_y + tooth2_h],
        radius=int(1 * scale), fill=key_color, outline=white, width=int(2 * scale)
    )

    # Draw code brackets
    bracket_y1 = int(75 * scale)
    bracket_y2 = int(100 * scale)
    bracket_width = int(4 * scale)

    # Left bracket
    left_x1 = int(35 * scale)
    left_x2 = int(25 * scale)
    draw.line([(left_x1, bracket_y1), (left_x2, bracket_y1)], fill=white, width=bracket_width)
    draw.line([(left_x2, bracket_y1), (left_x2, bracket_y2)], fill=white, width=bracket_width)
    draw.line([(left_x2, bracket_y2), (left_x1, bracket_y2)], fill=white, width=bracket_width)

    # Right bracket
    right_x1 = int(93 * scale)
    right_x2 = int(103 * scale)
    draw.line([(right_x1, bracket_y1), (right_x2, bracket_y1)], fill=white, width=bracket_width)
    draw.line([(right_x2, bracket_y1), (right_x2, bracket_y2)], fill=white, width=bracket_width)
    draw.line([(right_x2, bracket_y2), (right_x1, bracket_y2)], fill=white, width=bracket_width)

    # Token dots
    dot_y = int(87 * scale)
    dot_radius = int(3 * scale)

    for dot_x in [int(50 * scale), int(64 * scale), int(78 * scale)]:
        draw.ellipse(
            [dot_x - dot_radius, dot_y - dot_radius,
             dot_x + dot_radius, dot_y + dot_radius],
            fill=white
        )

    # "T" badge
    badge_x = int(100 * scale)
    badge_y = int(28 * scale)
    badge_radius = int(16 * scale)

    draw.ellipse(
        [badge_x - badge_radius, badge_y - badge_radius,
         badge_x + badge_radius, badge_y + badge_radius],
        fill=green, outline=white, width=int(2 * scale)
    )

    # Draw "T" manually as strokes (more reliable than text rendering)
    # Horizontal top bar
    t_top_y = badge_y - int(8 * scale)
    t_top_x1 = badge_x - int(7 * scale)
    t_top_x2 = badge_x + int(7 * scale)
    t_top_height = int(3 * scale)

    draw.rectangle(
        [t_top_x1, t_top_y, t_top_x2, t_top_y + t_top_height],
        fill=white
    )

    # Vertical stem
    t_stem_x = badge_x - int(2 * scale)
    t_stem_y = t_top_y
    t_stem_width = int(4 * scale)
    t_stem_height = int(12 * scale)

    draw.rectangle(
        [t_stem_x, t_stem_y, t_stem_x + t_stem_width, t_stem_y + t_stem_height],
        fill=white
    )

    return img


def main():
    """Generate all required icon sizes"""
    sizes = [128, 48, 16]

    for size in sizes:
        print(f"Creating icon{size}.png...")
        icon = create_icon(size)
        icon.save(f'icon{size}.png', 'PNG')
        print(f"✓ Created icon{size}.png")

    print("\n✅ All icons created successfully!")


if __name__ == '__main__':
    main()
