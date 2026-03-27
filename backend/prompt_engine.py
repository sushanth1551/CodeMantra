def improve_prompt(prompt):
    return f"""
    Generate a COMPLETE working project.

    Requirements:
    - Include all necessary files (HTML, CSS, JS, Backend)
    - Output each file separately
    - Provide full working code
    - No explanations

    Task: {prompt}
    """