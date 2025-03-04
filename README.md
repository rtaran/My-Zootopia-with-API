# 🦊 Zootopia - Animal Encyclopedia with API

Zootopia is an interactive animal encyclopedia that dynamically fetches animal data using the **API Ninja's Animals API**. 🐾

## 🚀 Features
- 🔍 **Search for any animal** by entering its name.
- 📜 Displays **scientific classification, habitat, diet, type, skin type, and more**.
- 🎨 **Beautiful UI** with structured CSS styling.
- 🌍 **Real-time data** from an external API instead of a static JSON file.
- ✅ **Shows all matching animals**, not just the first result.

---

## 📥 Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/zootopia-with-api-and-github.git
cd zootopia-with-api-and-github
```

### **2️⃣ Install Dependencies**
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up API Key**
Create a `.env` file and add your API key:
```env
API_KEY=your_actual_api_key_here
```

### **4️⃣ Run the Web Generator**
To generate the animal encyclopedia website, run:
```bash
python animals_web_generator.py
```
💡 **Enter an animal name** when prompted (e.g., `Fox`).

💡 The generated website will be saved as `animals.html`.

## 🐍 Project Structure
📂 `zootopia-with-api-and-github`
 ├── 📄 `.gitignore`
 ├── 📄 `.env`                # Stores API key (ignored in Git)
 ├── 📄 `README.md`           # Project documentation
 ├── 📄 `requirements.txt`    # List of dependencies
 ├── 📄 `animals.html`        # Generated website
 ├── 📄 `animals_template.html`  # HTML template
 ├── 📄 `style.css`           # 🎨 New CSS file added
 ├── 🐍 `animals_web_generator.py`  # Generates the website dynamically from API
 ├── 🐍 `data_fetcher.py`     # Fetches all matching animals from API

## 🎨 Screenshots
(Screenshots attached)

## 🤝 Contributing
Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest improvements
- ✨ Submit pull requests

## ⚖️ License
This project is open-source and available under the MIT License.

## ⭐ Acknowledgments
Special thanks to API Ninja for providing the free animal API! 🦁🐯🐻