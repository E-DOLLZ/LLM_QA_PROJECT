from flask import Flask, render_template, request
from LLM_QA_CLI import preprocess, ask_cohere
import markdown2
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    processed_question = None
    answer_html = None

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if question:
            processed_question = preprocess(question)
            try:
                raw_answer = ask_cohere(processed_question)
                # Convert Markdown to HTML
                answer_html = markdown2.markdown(raw_answer)
            except Exception as e:
                answer_html = f"<p style='color:red;'>Error: {e}</p>"

    return render_template(
        "index.html",
        processed_question=processed_question,
        answer_html=answer_html
    )

if __name__ == "__main__":
    # Render sets the PORT environment variable for production
    port = int(os.environ.get("PORT", 5000))
    # Debug mode is False by default on Render
    debug = os.environ.get("FLASK_DEBUG", "False") == "True"
    app.run(host="0.0.0.0", port=port, debug=debug)
