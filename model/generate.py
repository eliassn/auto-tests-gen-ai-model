import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

MODEL_DIR = "./model/gpt2-cypress"

def generate_test(prompt, max_length=200):
    tokenizer = GPT2Tokenizer.from_pretrained(MODEL_DIR)
    model = GPT2LMHeadModel.from_pretrained(MODEL_DIR)
    model.eval()

    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated_test = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return generated_test

if __name__ == "__main__":
    prompt = "// Cypress test prompt: describe('My Test', () => {"
    generated = generate_test(prompt)
    print("Generated Cypress Test:\n", generated)
