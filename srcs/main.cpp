#include <fstream>
#include "Data.hpp"

int	main() {
	std::fstream	file;
	file.open("data.csv", std::ios::in);
	std::cout << file.rdbuf();
	file.close();
	return (0);
}
