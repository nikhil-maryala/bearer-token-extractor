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

    # Chrome Web Store requires 16px padding on each side for 128px icons
    # So actual icon content should be 96x96 centered in 128x128
    padding_ratio = 16 / 128.0 if size == 128 else 0
    padding = int(size * padding_ratio)

    # Scale factor for different sizes (based on content area)
    content_size = size - (2 * padding)
    scale = content_size / 96.0  # Base scale on 96x96 content area

    # Colors
    bg_color1 = (250, 70, 22)  # UiPath orange
    bg_color2 = (255, 107, 53)  # Lighter orange
    key_color = (255, 215, 0)  # Gold
    white = (255, 255, 255, 255)
    green = (76, 175, 80)  # Green for "T" badge

    # Draw rounded rectangle background with gradient simulation
    corner_radius = int(24 * scale)

    # Add subtle white outer glow for dark backgrounds (Chrome Web Store guideline)
    glow_width = int(1 * scale)
    if glow_width > 0:
        glow_color = (255, 255, 255, 30)
        draw.rounded_rectangle(
            [padding - glow_width, padding - glow_width,
             size - padding + glow_width, size - padding + glow_width],
            radius=corner_radius + glow_width,
            outline=glow_color,
            width=glow_width
        )

    # Simple gradient by drawing multiple rectangles in content area
    for i in range(content_size):
        ratio = i / content_size
        r = int(bg_color1[0] + (bg_color2[0] - bg_color1[0]) * ratio)
        g = int(bg_color1[1] + (bg_color2[1] - bg_color1[1]) * ratio)
        b = int(bg_color1[2] + (bg_color2[2] - bg_color1[2]) * ratio)

        # Draw horizontal line with rounded corners
        y = padding + i
        x_start = padding
        x_end = size - padding

        # Apply corner rounding
        if i < corner_radius:
            x_offset = int(corner_radius - math.sqrt(corner_radius**2 - (corner_radius - i)**2))
            x_start = padding + x_offset
            x_end = size - padding - x_offset
        elif i >= content_size - corner_radius:
            dist_from_bottom = content_size - i
            x_offset = int(corner_radius - math.sqrt(corner_radius**2 - (corner_radius - dist_from_bottom)**2))
            x_start = padding + x_offset
            x_end = size - padding - x_offset

        if x_end > x_start:
            draw.line([(x_start, y), (x_end, y)], fill=(r, g, b, 255), width=1)

    # All coordinates are now offset by padding
    # Draw key icon
    key_center_x = padding + int(38 * scale)
    key_center_y = padding + int(35 * scale)
    key_radius = int(14 * scale)
    key_inner_radius = int(6 * scale)

    # Key circle (head)
    draw.ellipse(
        [key_center_x - key_radius, key_center_y - key_radius,
         key_center_x + key_radius, key_center_y + key_radius],
        fill=key_color, outline=white, width=int(2 * scale)
    )

    # Inner circle
    draw.ellipse(
        [key_center_x - key_inner_radius, key_center_y - key_inner_radius,
         key_center_x + key_inner_radius, key_center_y + key_inner_radius],
        fill=None, outline=white, width=int(2 * scale)
    )

    # Key shaft
    shaft_x = padding + int(43 * scale)
    shaft_y = padding + int(31 * scale)
    shaft_width = int(28 * scale)
    shaft_height = int(8 * scale)

    draw.rounded_rectangle(
        [shaft_x, shaft_y, shaft_x + shaft_width, shaft_y + shaft_height],
        radius=int(2 * scale), fill=key_color, outline=white, width=int(2 * scale)
    )

    # Key teeth
    tooth1_x = padding + int(58 * scale)
    tooth1_y = padding + int(39 * scale)
    tooth1_w = int(5 * scale)
    tooth1_h = int(6 * scale)

    draw.rounded_rectangle(
        [tooth1_x, tooth1_y, tooth1_x + tooth1_w, tooth1_y + tooth1_h],
        radius=int(1 * scale), fill=key_color, outline=white, width=int(1 * scale)
    )

    tooth2_x = padding + int(65 * scale)
    tooth2_h = int(9 * scale)

    draw.rounded_rectangle(
        [tooth2_x, tooth1_y, tooth2_x + tooth1_w, tooth1_y + tooth2_h],
        radius=int(1 * scale), fill=key_color, outline=white, width=int(1 * scale)
    )

    # Draw code brackets
    bracket_y1 = padding + int(58 * scale)
    bracket_y2 = padding + int(78 * scale)
    bracket_width = int(3 * scale)

    # Left bracket
    left_x1 = padding + int(27 * scale)
    left_x2 = padding + int(19 * scale)
    draw.line([(left_x1, bracket_y1), (left_x2, bracket_y1)], fill=white, width=bracket_width)
    draw.line([(left_x2, bracket_y1), (left_x2, bracket_y2)], fill=white, width=bracket_width)
    draw.line([(left_x2, bracket_y2), (left_x1, bracket_y2)], fill=white, width=bracket_width)

    # Right bracket
    right_x1 = padding + int(72 * scale)
    right_x2 = padding + int(80 * scale)
    draw.line([(right_x1, bracket_y1), (right_x2, bracket_y1)], fill=white, width=bracket_width)
    draw.line([(right_x2, bracket_y1), (right_x2, bracket_y2)], fill=white, width=bracket_width)
    draw.line([(right_x2, bracket_y2), (right_x1, bracket_y2)], fill=white, width=bracket_width)

    # Token dots
    dot_y = padding + int(68 * scale)
    dot_radius = int(2 * scale)

    for dot_x_offset in [38, 50, 62]:
        dot_x = padding + int(dot_x_offset * scale)
        draw.ellipse(
            [dot_x - dot_radius, dot_y - dot_radius,
             dot_x + dot_radius, dot_y + dot_radius],
            fill=white
        )

    # "T" badge
    badge_x = padding + int(78 * scale)
    badge_y = padding + int(22 * scale)
    badge_radius = int(12 * scale)

    draw.ellipse(
        [badge_x - badge_radius, badge_y - badge_radius,
         badge_x + badge_radius, badge_y + badge_radius],
        fill=green, outline=white, width=int(2 * scale)
    )

    # Draw "T" manually as strokes (more reliable than text rendering)
    # Horizontal top bar
    t_top_y = badge_y - int(6 * scale)
    t_top_x1 = badge_x - int(5 * scale)
    t_top_x2 = badge_x + int(5 * scale)
    t_top_height = int(2 * scale)

    draw.rectangle(
        [t_top_x1, t_top_y, t_top_x2, t_top_y + t_top_height],
        fill=white
    )

    # Vertical stem
    t_stem_x = badge_x - int(1.5 * scale)
    t_stem_y = t_top_y
    t_stem_width = int(3 * scale)
    t_stem_height = int(9 * scale)

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
