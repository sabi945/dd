#include <SFML/Graphics.hpp>
#include <iostream>
#include <string>

using namespace std;

int main() {
    sf::RenderWindow window(sf::VideoMode(400, 500), "Kalkulator");

    sf::Font font;
    if (!font.loadFromFile("arial.ttf")) {
        cout << "Gagal memuat font\n";
        return 1;
    }

    sf::Text text("", font, 50);
    text.setFillColor(sf::Color::Black);

    string input;

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();

            if (event.type == sf::Event::TextEntered) {
                if (event.text.unicode == 8 && input.size() > 0) { // Handle backspace
                    input.pop_back();
                } else if (event.text.unicode >= 48 && event.text.unicode <= 57) { // Handle numbers
                    input += static_cast<char>(event.text.unicode);
                } else if (event.text.unicode == '+' || event.text.unicode == '-' || event.text.unicode == '*' || event.text.unicode == '/') { // Handle operators
                    input += static_cast<char>(event.text.unicode);
                } else if (event.text.unicode == 13) { // Handle Enter
                    try {
                        float result = eval(input); // Function to evaluate expression
                        input = to_string(result);
                    } catch (...) {
                        input = "Error";
                    }
                }
            }
        }

        text.setString(input);
        window.clear(sf::Color::White);
        window.draw(text);
        window.display();
    }

    return 0;
}
