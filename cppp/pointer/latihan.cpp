#include <iostream>
#include <memory>

// Node dari linked list
struct Node {
    int data;
    std::unique_ptr<Node> next;

    Node(int value) : data(value), next(nullptr) {}
};

// Linked list
class LinkedList {
private:
    std::unique_ptr<Node> head;

public:
    // Fungsi untuk menambahkan node baru ke linked list
    void addNode(int value) {
        std::unique_ptr<Node> newNode = std::make_unique<Node>(value);
        if (!head) {
            head = std::move(newNode);
        } else {
            Node* current = head.get();
            while (current->next) {
                current = current->next.get();
            }
            current->next = std::move(newNode);
        }
    }

    // Fungsi untuk mencetak isi linked list
    void printList() {
        Node* current = head.get();
        while (current) {
            std::cout << current->data << " ";
            current = current->next.get();
        }
        std::cout << std::endl;
    }
};

int main() {
    // Membuat linked list
    LinkedList list;

    // Menambahkan beberapa node ke linked list
    list.addNode(10);
    list.addNode(20);
    list.addNode(30);

    // Mencetak isi linked list
    list.printList();

    return 0;
}
    