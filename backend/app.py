from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust the allowed origins as necessary
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TransformationInput(BaseModel):
    text: str

def clean_and_uppercase(text):
    return ''.join([char.upper() for char in text if char.isalpha()])

def group_and_pad_to_matrix_with_transformations(text):
    # Helper to convert characters to indices and back to characters
    alpha_numeric = {chr(i): i - 65 for i in range(65, 91)}
    numeric_alpha = {i - 65: chr(i) for i in range(65, 91)}

    # Initial running total setup
    running_total = [0, 0, 0, 0]
    detailed_steps = []

    # Prepare text by removing non-alpha characters and splitting into chunks
    filtered_text = clean_and_uppercase(text)
    chunks = [filtered_text[i:i+16] for i in range(0, len(filtered_text), 16)]
    padded_chunks = [chunk + 'A' * (16 - len(chunk)) for chunk in chunks]

    # Process each chunk
    for chunk in padded_chunks:
        # Convert chunk to matrix
        matrix = [[alpha_numeric.get(chunk[i+j*4], 0) for i in range(4)] for j in range(4)]
        alph_matrix = [[chunk[i+j*4] if i+j*4 < len(chunk) else 'A' for i in range(4)] for j in range(4)]

        # Record initial matrices and running total
        step_details = {
            'original_alpha_matrix': [row[:] for row in alph_matrix],
            'original_numeric_matrix': [row[:] for row in matrix],
            'running_total_initial': running_total[:]
        }

        # Step 1: Sum columns and update running total
        column_sums_initial = [sum(matrix[i][j] for i in range(4)) % 26 for j in range(4)]
        running_total = [(rt + cs) % 26 for rt, cs in zip(running_total, column_sums_initial)]

        # Update step details with running total after initial matrix
        step_details['running_total_after_initial'] = running_total[:]

        # Apply transformations
        for i in range(4):
            if i < 3:
                matrix[i] = matrix[i][i+1:] + matrix[i][:i+1]
                alph_matrix[i] = alph_matrix[i][i+1:] + alph_matrix[i][:i+1]
            else:
                matrix[i].reverse()
                alph_matrix[i].reverse()

        # Record transformed matrices
        step_details.update({
            'transformed_alpha_matrix': [row[:] for row in alph_matrix],
            'transformed_numeric_matrix': [row[:] for row in matrix],
        })

        # Step 2: Sum columns again and update running total
        column_sums_transformed = [sum(matrix[i][j] for i in range(4)) % 26 for j in range(4)]
        running_total = [(rt + cs) % 26 for rt, cs in zip(running_total, column_sums_transformed)]

        # Update step details with final running total after transformation
        step_details['running_total_after_transformation'] = running_total[:]

        detailed_steps.append(step_details)

    running_total_alpha = ''.join([numeric_alpha[rt] for rt in running_total])
    return detailed_steps, running_total_alpha

@app.post("/transform/")
async def transform_text(input: TransformationInput):
    steps, final_alpha_running_total = group_and_pad_to_matrix_with_transformations(input.text)
    return {
        "steps": steps,
        "final_running_total": final_alpha_running_total
    }
