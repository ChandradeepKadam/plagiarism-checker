from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# Tokenize code (remove symbols, keep words)
def tokenize(text):
    return re.findall(r'\w+', text.lower())

# Jaccard similarity
def similarity(tokens1, tokens2):
    set1, set2 = set(tokens1), set(tokens2)
    if not set1 or not set2:
        return 0
    return len(set1 & set2) / len(set1 | set2)

@app.route('/')
def home():
    return "✅ Plagiarism Checker Backend Running"

@app.route('/compare', methods=['POST'])
def compare():
    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    if not file1 or not file2:
        return jsonify({"error": "Files missing"}), 400

    code1 = file1.read().decode('utf-8').split('\n')
    code2 = file2.read().decode('utf-8').split('\n')

    matches = []
    total_score = 0
    count = 0

    for i, line1 in enumerate(code1):
        tokens1 = tokenize(line1)
        best_score = 0
        best_line = ""
        best_index = -1

        for j, line2 in enumerate(code2):
            tokens2 = tokenize(line2)
            score = similarity(tokens1, tokens2)

            if score > best_score:
                best_score = score
                best_line = line2
                best_index = j

        if best_score > 0.5:
            common = list(set(tokens1) & set(tokenize(best_line)))

            matches.append({
                "line1_num": i + 1,
                "line2_num": best_index + 1,
                "line1": line1,
                "line2": best_line,
                "similarity": round(best_score * 100, 2),
                "common_words": common
            })

        total_score += best_score
        count += 1

    overall = round((total_score / count) * 100, 2) if count else 0

    return jsonify({
        "overall_similarity": overall,
        "matches": matches
    })

if __name__ == '__main__':
    app.run(debug=True)