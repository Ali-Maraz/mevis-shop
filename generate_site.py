import os

# Создаем директории, если они не существуют
os.makedirs('templates', exist_ok=True)
os.makedirs('static', exist_ok=True)

def generate_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mevis</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <header>
            <div class="header-image-container">
                <img src="/static/header-bg.jpg" alt="Furniture Image" class="header-image">
                <div class="overlay">
                    <div class="logo-container">
                        <img src="/static/logo.jpg" alt="Mevis Logo" class="logo">
                    </div>
                    <p class="description">Mevis с 2020 года обеспечивает клиентов по всей России качественной мебелью, придающей интерьеру особенный характер. У нас более 10 000 довольных клиентов. Наше производство находится в городе Ижевск. С нами ваш дом наполнится стилем и комфортом.</p>
                </div>
            </div>
        </header>
        <section class="social-buttons">
            <a href="https://t.me/your_telegram" class="button telegram">Телеграм</a>
            <a href="https://vk.com/your_vk" class="button vkontakte">ВКонтакте</a>
            <a href="https://instagram.com/your_instagram" class="button instagram">Инстаграм</a>
        </section>
        <section class="contact-info">
            <p>Телефон: +7 904 247 06 75</p>
            <p>Email: alierik0404@gmail.com</p>
        </section>
        <section class="contact-form">
            <form action="submit_form" method="POST">
                <input type="text" name="name" placeholder="Имя" required>
                <input type="email" name="email" placeholder="Email" required>
                <textarea name="message" rows="5" placeholder="Сообщение" required></textarea>
                <button type="submit">Отправить</button>
            </form>
        </section>
    </body>
    </html>
    """
    with open('templates/home.html', 'w') as file:
        file.write(html_content)

def generate_css():
    css_content = """
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f4f4f4;
    }
    .header-image-container {
        position: relative;
        width: 100%;
        height: 300px;
        overflow: hidden;
    }
    .header-image {
        width: 100%;
        height: auto;
    }
    .overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: rgba(0, 0, 0, 0.5);
        color: #fff;
    }
    .logo-container {
        padding: 20px 0;
    }
    .logo {
        max-width: 300px;
        height: auto;
    }
    .description {
        max-width: 800px;
        margin: 1em auto;
        font-size: 1.2em;
        text-align: center;
    }
    .social-buttons {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    .social-buttons .button {
        margin: 0 10px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        display: inline-block;
        text-decoration: none;
        color: #fff;
        border-radius: 5px;
        transition: background 0.3s ease;
    }
    .telegram { background: #0088cc; }
    .vkontakte { background: #4c75a3; }
    .instagram { background: #e4405f; }
    .contact-info {
        text-align: center;
        margin: 20px 0;
    }
    .contact-form {
        max-width: 500px;
        margin: 0 auto;
        padding: 20px;
        background: #fff;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        border-radius: 5px;
    }
    .contact-form input,
    .contact-form textarea {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .contact-form button {
        width: 100%;
        padding: 10px;
        border: none;
        background: #333;
        color: #fff;
        border-radius: 5px;
        cursor: pointer;
        transition: background 0.3s ease;
    }
    .contact-form button:hover {
        background: #555;
    }
    """
    with open('static/style.css', 'w') as file:
        file.write(css_content)

generate_html()
generate_css()
