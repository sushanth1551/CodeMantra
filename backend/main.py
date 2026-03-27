from fastapi import FastAPI
from backend.llm import generate_response
from backend.prompt_engine import improve_prompt
from backend.safety_filter import is_safe
from backend.context_manager import add_to_history, get_context

app = FastAPI()

@app.post("/chat")
async def chat(prompt: str):
    try:
        
        if not is_safe(prompt):
            return {"error": "Unsafe prompt detected"}

        
        improved = improve_prompt(prompt)

        
        context = get_context()

        final_prompt = context + "\n" + improved

        
        response = generate_response(final_prompt)

       
        add_to_history(prompt, response)

        return {
            
            "response": response
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}