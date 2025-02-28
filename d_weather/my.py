from jinja2 import Template

def generate_weather_svg(city, temperature, condition, time, wind_speed, sunrise, sunset):
    svg_template = Template('''
    <svg width="500" height="300" viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="100%" fill="{{ background_color }}" rx="20"/>
        
        <text x="20" y="40" font-size="24" fill="white">{{ city }}</text>
        <text x="20" y="80" font-size="20" fill="white">{{ time }}</text>
        
        <text x="400" y="40" font-size="24" fill="white" text-anchor="end">{{ temperature }}°C</text>
        <text x="400" y="80" font-size="20" fill="white" text-anchor="end">{{ condition }}</text>
        
        <text x="20" y="200" font-size="16" fill="white">Wind: {{ wind_speed }} mph</text>
        <text x="20" y="230" font-size="16" fill="white">Sunrise: {{ sunrise }}</text>
        <text x="20" y="260" font-size="16" fill="white">Sunset: {{ sunset }}</text>
        
        {{ icon_svg }}
    </svg>
    ''')
    
    icons = {
        'Clear': '<circle cx="250" cy="100" r="40" fill="yellow"/>',
        'Clouds': '<ellipse cx="250" cy="100" rx="50" ry="30" fill="gray"/>',
        'Rain': '<ellipse cx="250" cy="90" rx="50" ry="30" fill="gray"/><line x1="230" y1="120" x2="230" y2="140" stroke="blue" stroke-width="4"/><line x1="270" y1="120" x2="270" y2="140" stroke="blue" stroke-width="4"/>',
        'Snow': '<ellipse cx="250" cy="90" rx="50" ry="30" fill="white"/><circle cx="230" cy="130" r="5" fill="white"/><circle cx="270" cy="130" r="5" fill="white"/>',
        'Sunset': '<circle cx="250" cy="120" r="30" fill="orange"/>'
    }
    
    background_colors = {
        'Clear': '#1E90FF',  # Blue sky
        'Clouds': '#708090',  # Grayish
        'Rain': '#4682B4',  # Dark blue
        'Snow': '#B0E0E6',  # Light cyan
        'Sunset': '#FF4500'  # Orange
    }
    
    svg_output = svg_template.render(
        city=city,
        temperature=temperature,
        condition=condition,
        time=time,
        wind_speed=wind_speed,
        sunrise=sunrise,
        sunset=sunset,
        icon_svg=icons.get(condition, ''),
        background_color=background_colors.get(condition, '#000000')
    )
    
    return svg_output

# Example usage:
svg_content = generate_weather_svg("New York", 33, "Rain", "7:42 AM", "5 mph", "5:55 AM", "6:35 PM")
with open("weather_widget.svg", "w") as f:
    f.write(svg_content)
