from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My DevOps Project</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
                color: #333;
            }
            header {
                background-color: #2c3e50;
                color: white;
                padding: 20px;
                text-align: center;
            }
            nav {
                display: flex;
                justify-content: center;
                background-color: #34495e;
            }
            nav a {
                color: white;
                padding: 14px 20px;
                text-decoration: none;
                text-align: center;
            }
            nav a:hover {
                background-color: #2c3e50;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            .hero {
                background-color: #3498db;
                color: white;
                padding: 40px 20px;
                text-align: center;
            }
            .hero h1 {
                font-size: 2.5em;
                margin: 0;
            }
            .section {
                padding: 40px 20px;
                text-align: center;
            }
            .section h2 {
                font-size: 2em;
                margin-bottom: 20px;
            }
            .section p {
                font-size: 1.2em;
                color: #555;
            }
            footer {
                background-color: #2c3e50;
                color: white;
                padding: 10px;
                text-align: center;
                position: fixed;
                width: 100%;
                bottom: 0;
            }
        </style>
    </head>
    <body>

        <header>
            <h1>Welcome DevOps Project</h1>
            <p>Running with Flask, Docker, and Kubernetes</p>
        </header>

        <nav>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#contact">Contact</a>
        </nav>

        <div class="container">
            <div class="hero" id="home">
                <h1>🚀 Launch Your DevOps Journey</h1>
                <p>We're taking DevOps to the next level with Flask, Docker, and Kubernetes!</p>
            </div>

            <div class="section" id="about">
                <h2>About Us</h2>
                <p>We are a team of developers working to streamline your DevOps pipeline using the latest technologies and best practices. From development to deployment, we automate it all!</p>
            </div>

            <div class="section" id="services">
                <h2>Our Services</h2>
                <p>We provide DevOps solutions for automation, continuous integration, and deployment using Docker and Kubernetes. Our goal is to help you scale your infrastructure efficiently!</p>
            </div>

            <div class="section" id="contact">
                <h2>Contact Us</h2>
                <p>If you have any questions or need assistance with your DevOps setup, feel free to reach out to us. We're here to help!</p>
            </div>
        </div>

        <footer>
            <p>&copy; 2025 My DevOps Project. All rights reserved.</p>
        </footer>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)