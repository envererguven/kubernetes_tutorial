import os
import markdown
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

BASE_DIR = "/workspace" # In Docker, this will be mapped to c:/PROJECTS/docker_kubernetes

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/api/debug', methods=['GET'])
def debug_fs():
    return jsonify({
        "base_dir": BASE_DIR,
        "exists": os.path.exists(BASE_DIR),
        "contents": os.listdir(BASE_DIR) if os.path.exists(BASE_DIR) else "NOT FOUND",
        "node_mounts_root": os.listdir('/run/desktop/mnt/host') if os.path.exists('/run/desktop/mnt/host') else "NOT FOUND"
    })

@app.route('/api/modules', methods=['GET'])
def get_modules():
    try:
        modules = []
        if not os.path.exists(BASE_DIR):
            return jsonify({"error": f"Path {BASE_DIR} not found inside container"}), 500
            
        for entry in sorted(os.listdir(BASE_DIR)):
            if entry.startswith('module') and os.path.isdir(os.path.join(BASE_DIR, entry)):
                modules.append({
                    "id": entry,
                    "name": entry.replace('_', ' ').title(),
                    "path": entry
                })
        return jsonify(modules)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/modules/<module_id>/files', methods=['GET'])
def get_module_files(module_id):
    path = os.path.join(BASE_DIR, module_id)
    files = []
    for root, dirs, filenames in os.walk(path):
        for f in filenames:
            rel_path = os.path.relpath(os.path.join(root, f), path)
            files.append(rel_path)
    return jsonify(files)

@app.route('/api/content/<path:file_path>', methods=['GET'])
def get_file_content(file_path):
    full_path = os.path.join(BASE_DIR, file_path)
    if not os.path.exists(full_path):
        return jsonify({"error": "File not found"}), 404
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if file_path.endswith('.md'):
        html = markdown.markdown(content, extensions=['fenced_code', 'tables', 'attr_list'])
        return jsonify({"type": "markdown", "raw": content, "html": html})
    else:
        return jsonify({"type": "code", "raw": content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
