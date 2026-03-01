import re

with open('css/style.css', 'r') as f:
    css = f.read()

new_root = """  /* Spacing */
  --spacing-3xs: 0.25rem;
  --spacing-2xs: 0.5rem;
  --spacing-xs: 0.75rem;
  --spacing-sm: 1rem;
  --spacing-md: 1.25rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  --spacing-2xl: 2.5rem;
  --spacing-3xl: 3rem;
  --spacing-4xl: 4rem;
  --spacing-5xl: 5rem;
  --spacing-6xl: 6rem;
  --spacing-7xl: 7.5rem;
  --spacing-8xl: 10rem;"""

# Replace the specific variables block
css = re.sub(r'/\* Spacing \*/\s*--spacing-[^}]+(?=\s+/\* Layout \*/)', new_root + '\n\n', css)

replacements = {
    '120px': 'var(--spacing-7xl)',
    '100px': '6.25rem',
    '96px': 'var(--spacing-6xl)',
    '80px': 'var(--spacing-5xl)',
    '72px': '4.5rem',
    '64px': 'var(--spacing-4xl)',
    '60px': '3.75rem',
    '48px': 'var(--spacing-3xl)',
    '40px': 'var(--spacing-2xl)',
    '36px': '2.25rem',
    '32px': 'var(--spacing-xl)',
    '28px': '1.75rem',
    '24px': 'var(--spacing-lg)',
    '20px': 'var(--spacing-md)',
    '16px': 'var(--spacing-sm)',
    '12px': 'var(--spacing-xs)',
    '8px':  'var(--spacing-2xs)',
    '5px':  '0.3125rem',
    '4px':  'var(--spacing-3xs)',
    '7.5rem': 'var(--spacing-7xl)',
    '5rem': 'var(--spacing-5xl)',
    '4rem': 'var(--spacing-4xl)',
    '3rem': 'var(--spacing-3xl)',
    '2.5rem': 'var(--spacing-2xl)',
    '2rem': 'var(--spacing-xl)',
    '1.5rem': 'var(--spacing-lg)',
    '1.25rem': 'var(--spacing-md)',
    '1rem': 'var(--spacing-sm)',
    '0.875rem': '0.875rem',
    '0.75rem': 'var(--spacing-xs)',
    '0.625rem': '0.625rem',
    '0.5rem': 'var(--spacing-2xs)',
    '0.25rem': 'var(--spacing-3xs)'
}

def replace_func(match):
    prop = match.group(1)
    val_str = match.group(2)
    
    tokens = val_str.split()
    new_tokens = []
    for t in tokens:
        clean_t = t.replace(';', '')
        end_char = ';' if t.endswith(';') else ''
            
        prefix = '-' if clean_t.startswith('-') else ''
        if prefix: clean_t = clean_t[1:]
        
        if clean_t in replacements:
            new_tokens.append(prefix + replacements[clean_t] + end_char)
        else:
            new_tokens.append(prefix + clean_t + end_char)
            
    return f"{prop}: { ' '.join(new_tokens) }"

css = re.sub(r'([ \t]*(?:padding|margin|gap)[-a-z]*)\s*:\s*([^;}\n]+;?)', replace_func, css)

with open('css/style.css', 'w') as f:
    f.write(css)

print("Spacing updated.")
