#include <iostream>
#include <chrono>
#include <thread>

using namespace std::this_thread;
using namespace std::chrono;
using namespace std;

void DrawProgressBar(int len, double percent) {
  cout << "\x1B[2K"; // Erase the entire current line.
  cout << "\x1B[0E"; // Move to the beginning of the current line.
  string progress;
  for (int i = 0; i < len; ++i) {
    if (i < static_cast<int>(len * percent)) {
      progress += "=";
    } else {
      progress += " ";
    }
  }
  cout << "[" << progress << "] " << (static_cast<int>(100 * percent)) << "%";
  flush(cout); // Required.
}


int main(void) {
    double amount = 0.0;
    while (1 == 1) {
        if (amount < 100.0) {
            DrawProgressBar(24, amount);
            sleep_for(nanoseconds(500000000));
            amount += 0.07;
        } else {
            cout << endl << "Done." << endl;
        }
    }
    return 0;
}
