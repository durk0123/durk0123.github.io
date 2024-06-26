from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    try:
        profile_url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
        profile_response = requests.get(profile_url)
        if profile_response.status_code != 200:
            return jsonify({"error": "User not found"}), 404
        profile_data = profile_response.json()
        
        uuid = profile_data['id']
        username = profile_data['name']
        
        return jsonify({"username": username, "uuid": uuid})
                
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
