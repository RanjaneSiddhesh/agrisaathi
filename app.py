from flask import Flask, render_template, request, jsonify
from chat1 import load_all_pdf_texts_from_folder, initialize_vector_store
from chat2 import ask_rag

app = Flask(__name__)

docs = load_all_pdf_texts_from_folder()
db = initialize_vector_store(docs)





# # MAIN PAGE
@app.route("/")
def home():
    return render_template("1.html")

# CHATBOT PAGE
@app.route("/chatbot")
def chatbot():
    return render_template("index.html")

# MARKETPLACE PAGE
@app.route("/marketplace")
def marketplace():
    return render_template("marketplace.html")

# DISEASE PAGE
@app.route("/disease")
def disease():
    return render_template("disease.html")



# @app.route("/")
# def home():
#     return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("messageText", "").strip()
    lang = request.form.get("language", "mr")

    if not question:
        return jsonify({"answer": "कृपया प्रश्न टाइप करा / Please type a question"})

    language = "Marathi" if lang == "mr" else "English"

    try:
        answer = ask_rag(db, question, language)
        return jsonify({"answer": answer})
    except Exception as e:
        print("❌", e)
        return jsonify({"answer": "❌ Server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
