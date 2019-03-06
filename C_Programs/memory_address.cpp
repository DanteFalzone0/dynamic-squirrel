#include <iostream>

int your_number;

int main(void) {
    std::cout << "Type in any number\n";
    std::cin >> your_number;
    std::cout << "That number is now stored at memory address ";
    std::cout << &your_number << ", which is a block of transistors somewhere in Dante's computer.\n";
    return 0;
}
