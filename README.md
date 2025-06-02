# LinkedIn Post Generator

## 📌 Overview
The LinkedIn Post Generator is an end-to-end Generative AI project designed to help LinkedIn influencers create engaging posts tailored to their unique style. By leveraging advanced AI technologies, this tool generates high-quality LinkedIn posts based on a dataset provided for a specific individual.

For this project, the dataset has been created using posts made by Raj Vikramaditya (https://www.linkedin.com/in/rajstriver/), ensuring that the generated content aligns with his writing style, tone, and subject matter.

## 🚀 Tech Stack
- **Llama 3.2 Open Source Model** – For text generation
- **LangChain Framework** – For integrating and managing the LLM pipeline
- **Streamlit** – For building an interactive web-based UI
- **Groq Cloud** – For scalable and efficient cloud-based processing
- **Docker** – For containerization and seamless deployment

## 🛠 Features
- Generates LinkedIn posts based on an individual's writing style and past content
- Ensures consistency in tone, structure, and topic relevance
- Simple and interactive UI using Streamlit
- Cloud-based processing for scalability
- Dockerized for easy deployment and portability

## 🏗 How to Run the Project with Docker

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/<your-username>/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2️⃣ Build the Docker Image
```sh
docker build -t linkedin-post-generator .
```

### 3️⃣ Run the Docker Container
```sh
docker run -p 8501:8501 linkedin-post-generator
```

### 4️⃣ Access the App
Once the container is running, open your browser and go to:
👉 **http://localhost:8501**

## 🛠 Environment Variables
Create a `.env` file in the root directory to store API keys and configurations:
```
GROQ_API_KEY=your_groq_api_key
OTHER_ENV_VAR=your_value
```

## 🤝 Contributing
Feel free to fork this repository and submit pull requests to improve the project!
